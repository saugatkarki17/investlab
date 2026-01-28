# Investlab

**An Explainable Human vs AI Investment Learning Platform**

Investlab is a token-based investment simulation platform where a **human investor** competes against an **explainable AI trading system**. It uses real quantitative market data and news sentiment analysis. Both participants operate under identical constraints and start with equal capital — enabling fair comparison, hands-on learning, and transparent performance evaluation.

## Core Concept

- **Human** vs **AI** head-to-head simulation
- Real historical/daily market data + news sentiment
- Virtual currency: **ALPHA tokens** (starting balance: 10,000 ALPHA)
- Same rules for both sides: transaction fees, no leverage, daily close execution
- Key metrics: PnL, Sharpe Ratio, Maximum Drawdown
- Strong focus on **AI explainability** (SHAP + natural language rationales)

## System Architecture & Development Roadmap

### 1. Foundation & System Rules
**Tech / Tools:** GitHub · Python · Notion · Markdown

- Asset universe: SPY + selected liquid equities
- Trading frequency: daily close prices
- Internal currency: ALPHA token (10,000 starting balance)
- Identical constraints: transaction fees, no leverage
- Evaluation metrics: PnL, Sharpe Ratio, Maximum Drawdown
- Repository structure and coding standards defined

**Output:** A single, agreed-upon system contract

### 2. Data Ingestion — Raw Layer
**Tech / Sources:** yfinance · Polygon (optional) · Google News RSS · Yahoo Finance News · Python

- Daily OHLCV market data via yfinance
- News headlines from RSS feeds and APIs
- Asset-to-headline mapping
- Timestamp normalization across sources
- Raw data stored immutably (no preprocessing)

**Storage:** PostgreSQL (`market_data`, `news_raw`)

**Output:** Replayable, auditable historical datasets

### 3. Feature Factory — Signal Creation
**Tech / Tools:** Pandas · NumPy · pandas-ta (preferred) / TA-Lib · Scikit-learn

- Quantitative features: returns, momentum, volatility, RSI, MACD, etc.
- Market regime proxies: trend state, volatility clustering
- Lagged features to prevent look-ahead bias
- Feature normalization + asset-level joins

**Output:** Daily feature matrix per asset

### 4. NLP Sentiment Pipeline
**Tech / Models:** HuggingFace · FinBERT (ProsusAI/finbert or modern variants) · spaCy

- Headline cleaning and tokenization
- Sentiment scoring (−1 to +1 scale)
- Confidence-weighted aggregation
- Daily per-asset sentiment
- Sentiment momentum + news volume spike detection

**Storage:** PostgreSQL (`news_features`)

**Output:** Asset-level sentiment feature set

### 5. AI Trading Brain
**Tech / Models:** XGBoost · Logistic Regression · Scikit-learn

- Baseline strategies: rule-based, simple logistic regression
- Primary model: ML classifier predicting direction + probability
- Focus: signal prediction (not direct price forecasting)
- Risk-aware decision layer

### 6. Risk & Position Management
**Tech / Math:** NumPy · SciPy

- Position sizing based on model confidence
- Volatility targeting for return stabilization
- Exposure and concentration limits
- Capital allocation in ALPHA tokens

**Output:** Executable trade orders

### 7. Token Execution Engine
**Tech / Logic:** Python · PostgreSQL

- Trades executed at daily close prices
- Consistent transaction fees
- ALPHA token balance updates
- Daily mark-to-market valuation
- Historical portfolio snapshots

**Storage:** PostgreSQL (`trades`, `portfolios`, `token_balances`)

**Output:** Deterministic portfolio evolution

### 8. Explainability & Decision Logs
**Tech / Libraries:** SHAP · NumPy · Rule-based NLP

- Feature attribution (SHAP values) for every AI trade
- SHAP → human-readable rules
- Natural language trade rationales
- Full metadata stored with each explanation

**Output:** Structured, explainable AI decision logs

### 9. Human Investor Module
**Tech / Stack:** FastAPI · PostgreSQL

- Trade submission interface for humans
- Identical pricing & cost rules
- Instant preview of token impact
- Trades logged in same schema as AI

**Output:** Human portfolio timeline

### 10. Performance & Competition Engine
**Tech / Metrics:** NumPy · Pandas

- Equity curve generation for all participants
- Calculation of Sharpe, drawdown, volatility
- AI vs Human comparison
- Leaderboard snapshots

**Output:** Objective performance metrics

### 11. Backend API Layer
**Tech Stack:** FastAPI · Pydantic · Uvicorn

**Core Endpoints:**
- `/market-data`
- `/ai/trade`
- `/ai/explain`
- `/user/trade`
- `/portfolio`
- `/leaderboard`

**Output:** Production-style REST API

### 12. Frontend — Trading Arena
**Tech Stack:** Next.js · TypeScript · TailwindCSS · Chart.js / Recharts

- Split-screen dashboard: AI vs Human
- ALPHA balances and equity curves
- Trade explanation cards & insights
- Visual mapping: News → Sentiment → Trade
- Replay / learning mode for historical analysis

**Output:** Professional, interactive user interface

### 13. Polish, Deployment & Presentation
**Tech / Tools:** Docker · GitHub Actions · README

- Full system documentation + architecture diagrams
- Demo scenarios and walkthroughs
- Performance & stress testing
- Resume-ready project presentation

**Output:** Portfolio-grade, production-quality system

## Project Status
- Name updated to **Investlab**
- Focus: explainable AI + educational human–AI competition
- Stack emphasizes open-source tools, reproducibility, and transparency

## Getting Started (planned)

```bash
# Clone repo
git clone https://github.com/yourusername/investlab.git

# Install dependencies
pip install -r requirements.txt

# Set up PostgreSQL & env variables
# ...

# Run backend
uvicorn app.main:app --reload

# Run frontend
cd frontend && npm run dev
