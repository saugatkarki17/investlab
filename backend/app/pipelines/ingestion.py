import yfinance as yf
import pandas as pd
from pathlib import Path

DATA_PATH = Path("backend/data/market/raw")
DATA_PATH.mkdir(parents=True, exist_ok=True)

START = "2020-01-01"
END = "2025-01-01"

TICKERS = pd.read_csv(
    "backend/data/universe/top100_us.csv"
)["ticker"].tolist()

def download_5yr_market_data():
    all_data = []

    for ticker in TICKERS:
        df = yf.download(ticker, start=START, end=END, auto_adjust=True)
        df = df.reset_index()
        df["ticker"] = ticker
        all_data.append(df)

    full_df = pd.concat(all_data, ignore_index=True)
    full_df.to_parquet(DATA_PATH / "ohlcv_2020_2025.parquet")

    print("✅ Market data saved locally (one-time)")

if __name__ == "__main__":
    download_5yr_market_data()
# Downloads 5 years of historical market data for top 100 US stocks using yfinance.
# Saves the data as a Parquet file in backend/data/market/raw/ohlcv_2020_2025.parquet.