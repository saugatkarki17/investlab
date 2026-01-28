investlab/
│
├── README.md
├── .env
├── .gitignore
│
├── backend/
│   ├── requirements.txt
│   │
│   ├── app/
│   │   ├── main.py                # FastAPI entry point
│   │   │
│   │   ├── api/
│   │   │   ├── routes.py           # Route registration
│   │   │   ├── ai.py               # AI trade + explain
│   │   │   ├── human.py            # Human trade input
│   │   │   ├── market.py           # Market + features
│   │   │   ├── portfolio.py
│   │   │   └── leaderboard.py
│   │   │
│   │   ├── core/
│   │   │   ├── config.py           # Paths, constants
│   │   │   └── contracts.py        # System rules
│   │   │
│   │   ├── db/
│   │   │   ├── db.py               # PostgreSQL connection
│   │   │   └── schema.sql
│   │   │
│   │   ├── pipelines/
│   │   │   ├── ingestion.py        # yfinance + news
│   │   │   ├── features.py         # TA + regimes
│   │   │   └── sentiment.py        # FinBERT pipeline
│   │   │
│   │   ├── models/
│   │   │   ├── train.py
│   │   │   ├── predict.py
│   │   │   └── model.pkl
│   │   │
│   │   ├── strategy/
│   │   │   ├── signal_engine.py
│   │   │   ├── risk_manager.py
│   │   │   └── position_sizer.py
│   │   │
│   │   ├── execution/
│   │   │   ├── execution_engine.py
│   │   │   └── fee_model.py
│   │   │
│   │   ├── explainability/
│   │   │   ├── shap_explainer.py
│   │   │   └── rationale.py
│   │   │
│   │   ├── competition/
│   │   │   ├── portfolio.py
│   │   │   ├── metrics.py
│   │   │   └── leaderboard.py
│   │   │
│   │   ├── human/
│   │   │   └── validator.py
│   │   │
│   │   └── utils/
│   │       └── time_utils.py
│   │
│   ├── data/
│   │   ├── raw/
│   │   ├── features/
│   │   └── sentiment/
│   │
│   ├── scripts/
│   │   ├── run_simulation.py
│   │   ├── replay_history.py
│   │   └── reset_db.py
│   │
│   └── notebooks/
│       ├── eda.ipynb
│       └── model_experiments.ipynb
│
├── frontend/                     # Next.js (already installed)
│   ├── app/
│   │   ├── page.tsx               # Home / Arena
│   │   ├── ai/
│   │   │   └── page.tsx
│   │   ├── human/
│   │   │   └── page.tsx
│   │   ├── leaderboard/
│   │   │   └── page.tsx
│   │   └── layout.tsx
│   │
│   ├── components/
│   │   ├── charts/
│   │   │   ├── EquityCurve.tsx
│   │   │   └── TradeChart.tsx
│   │   │
│   │   ├── cards/
│   │   │   ├── TradeExplanation.tsx
│   │   │   └── MetricsCard.tsx
│   │   │
│   │   └── common/
│   │       └── Header.tsx
│   │
│   ├── lib/
│   │   └── api.ts                 # fetch() wrappers
│   │
│   ├── styles/
│   └── tailwind.config.ts
│
└── docs/
    ├── system_contract.md
    ├── architecture.md
    └── explainability.md
