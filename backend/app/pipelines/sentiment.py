# backend/app/pipelines/sentiment.py

import os
import pandas as pd
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import requests
import time
from dotenv import load_dotenv

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")  # Put your NewsAPI key in .env

# -----------------------------
# Paths
# -----------------------------
SENTIMENT_PATH = Path("backend/data/sentiment/updates")
SENTIMENT_PATH.mkdir(parents=True, exist_ok=True)
DAILY_PATH = SENTIMENT_PATH / "sentiment_daily.parquet"
HISTORY_PATH = SENTIMENT_PATH / "sentiment_history.parquet"

# -----------------------------
# Load FinBERT model
# -----------------------------
MODEL_NAME = "yiyanghkust/finbert-tone"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
finbert_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
print("✅ FinBERT model loaded successfully")

# -----------------------------
# Analyze headlines
# -----------------------------
def analyze_headlines(headlines):
    if not headlines:
        return []
    try:
        results = finbert_pipeline(headlines)
    except Exception as e:
        print(f"⚠️ Error analyzing headlines: {e}")
        return [0.0] * len(headlines)

    scores = []
    for res in results:
        label = res['label'].lower()
        score = res['score']
        if label == "positive":
            scores.append(score)
        elif label == "negative":
            scores.append(-score)
        else:
            scores.append(0.0)
    return scores

# -----------------------------
# Fetch top business headlines
# -----------------------------
def fetch_market_news(
    api_key=NEWSAPI_KEY,
    total_articles=1000,
    page_size=100,
    lookback_days=3,
):
    if not api_key:
        raise ValueError("NEWSAPI_KEY is required for /everything endpoint")

    all_headlines = []
    max_pages = (total_articles + page_size - 1) // page_size
    from_date = (pd.Timestamp.utcnow() - pd.Timedelta(days=lookback_days)).strftime("%Y-%m-%d")

    for page in range(1, max_pages + 1):
        try:
            url = "https://newsapi.org/v2/everything"
            params = {
                "q": "stock OR market OR economy OR earnings OR inflation",
                "language": "en",
                "sortBy": "publishedAt",
                "from": from_date,
                "pageSize": page_size,
                "page": page,
                "apiKey": api_key,
            }

            response = requests.get(url, params=params, timeout=15)
            response.raise_for_status()
            data = response.json()
            articles = data.get("articles", [])

            print(f"📰 Page {page}: {len(articles)} articles")

            for a in articles:
                title = a.get("title")
                published = a.get("publishedAt")
                if title and published:
                    all_headlines.append({
                        "Date": published,
                        "Headline": title
                    })

            if len(articles) < page_size:
                break

            time.sleep(1)  # rate-limit friendly

        except Exception as e:
            print(f"⚠️ Failed on page {page}: {e}")
            break

    return pd.DataFrame(all_headlines)

# -----------------------------
# Build daily sentiment
# -----------------------------
def build_daily_sentiment(api_key=NEWSAPI_KEY):
    df_news = fetch_market_news(api_key=api_key or NEWSAPI_KEY, total_articles=1000, page_size=100)

    if df_news.empty:
        print("⚠️ No news fetched, skipping sentiment analysis")
        return

    # Convert and normalize
    df_news["Date"] = pd.to_datetime(df_news["Date"]).dt.date
    df_news["Ticker"] = "MARKET"
    df_news = df_news.drop_duplicates(subset=["Date", "Headline"])

    # Sentiment scoring
    df_news["sentiment_score"] = analyze_headlines(df_news["Headline"].tolist())

    # Save daily sentiment
    df_news.to_parquet(DAILY_PATH, index=False)
    print(f"✅ Daily sentiment saved → {DAILY_PATH}")
    print(f"Total headlines processed: {len(df_news)}")

    # Update historical sentiment
    if HISTORY_PATH.exists():
        df_history = pd.read_parquet(HISTORY_PATH)
        df_history = pd.concat([df_history, df_news], ignore_index=True)
        df_history = df_history.drop_duplicates(subset=["Date", "Headline"])
    else:
        df_history = df_news.copy()

    df_history.to_parquet(HISTORY_PATH, index=False)
    print(f"📚 Sentiment history updated → {HISTORY_PATH}")

    # -----------------------------
    # Rolling 7-day sentiment
    # -----------------------------
    df_history["Date"] = pd.to_datetime(df_history["Date"])
    rolling_sentiment = (
        df_history.groupby("Ticker")
        .apply(lambda x: x.set_index("Date")["sentiment_score"].rolling(7).mean())
        .reset_index()
    )
    rolling_sentiment.rename(
        columns={"level_1": "Date", "sentiment_score": "rolling_7d_sentiment"}, inplace=True
    )

    # Remove duplicate columns if any
    rolling_sentiment = rolling_sentiment.loc[:, ~rolling_sentiment.columns.duplicated()]

    rolling_path = SENTIMENT_PATH / "sentiment_rolling_7d.parquet"
    rolling_sentiment.to_parquet(rolling_path, index=False)
    print(f"📈 Rolling 7-day sentiment saved → {rolling_path}")


# -----------------------------
# Standalone run
# -----------------------------
if __name__ == "__main__":
    build_daily_sentiment()
# Fetches top business headlines using NewsAPI, analyzes sentiment with FinBERT,
# and saves daily and historical sentiment scores in Parquet files under backend/data/sentiment/raw. 