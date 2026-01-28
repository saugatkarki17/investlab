# Project Structure

```text
investlab/
│
├── README.md                     # Project overview, setup, and usage
├── .env                          # Local environment variables
├── .gitignore                    # Files/folders excluded from git
│
├── backend/                      # Python backend (FastAPI + ML logic)
│   ├── requirements.txt          # Backend Python dependencies
│
│   ├── app/                      # Core backend application
│   │   ├── main.py               # FastAPI entry point
│   │
│   │   ├── api/                  # API route definitions
│   │   │   ├── routes.py         # Central router registration
│   │   │   ├── ai.py             # AI trade execution + explanations
│   │   │   ├── human.py          # Human trade submission endpoints
│   │   │   ├── market.py         # Market data & feature endpoints
│   │   │   ├── portfolio.py      # Portfolio state endpoints
│   │   │   └── leaderboard.py    # Performance comparison endpoints
│   │   │
│   │   ├── core/                 # Global configs and system rules
│   │   │   ├── config.py         # Constants, paths, environment flags
│   │   │   └── contracts.py      # Trading rules & system constraints
│   │   │
│   │   ├── db/                   # Database layer
│   │   │   ├── db.py             # PostgreSQL connection/session
│   │   │   └── schema.sql        # Database schema (AI + Human unified)
│   │   │
│   │   ├── pipelines/            # Data processing pipelines
│   │   │   ├── ingestion.py      # Market + news data ingestion
│   │   │   ├── features.py       # Feature engineering (TA, regimes)
│   │   │   └── sentiment.py      # NLP sentiment pipeline (FinBERT)
│   │   │
│   │   ├── models/               # Machine learning models
│   │   │   ├── train.py          # Model training scripts
│   │   │   ├── predict.py        # Inference logic for signals
│   │   │   └── model.pkl         # Saved trained model artifact
│   │   │
│   │   ├── strategy/             # Trading decision logic
│   │   │   ├── signal_engine.py  # Signal generation from model output
│   │   │   ├── risk_manager.py   # Risk and exposure controls
│   │   │   └── position_sizer.py # Position sizing logic
│   │   │
│   │   ├── execution/            # Trade execution & accounting
│   │   │   ├── execution_engine.py # Order execution at daily close
│   │   │   └── fee_model.py      # Transaction cost model
│   │   │
│   │   ├── explainability/       # AI explainability layer
│   │   │   ├── shap_explainer.py # SHAP value computation
│   │   │   └── rationale.py      # Human-readable trade explanations
│   │   │
│   │   ├── competition/          # Performance tracking & comparison
│   │   │   ├── portfolio.py      # Portfolio state & valuation
│   │   │   ├── metrics.py        # PnL, Sharpe, drawdown calculations
│   │   │   └── leaderboard.py    # AI vs Human ranking logic
│   │   │
│   │   ├── human/                # Human-specific validation logic
│   │   │   └── validator.py      # Enforces same rules as AI
│   │   │
│   │   └── utils/                # Shared helper utilities
│   │       └── time_utils.py     # Date/time alignment helpers
│   │
│   ├── data/                     # Local data storage (replayable)
│   │   ├── raw/                  # Raw market & news data
│   │   ├── features/             # Engineered feature datasets
│   │   └── sentiment/            # Processed sentiment outputs
│   │
│   ├── scripts/                  # Local execution scripts
│   │   ├── run_simulation.py     # End-to-end simulation runner
│   │   ├── replay_history.py     # Historical replay/backtest
│   │   └── reset_db.py           # Database reset utility
│   │
│   └── notebooks/                # Research & experimentation
│       ├── eda.ipynb             # Exploratory data analysis
│       └── model_experiments.ipynb # Model testing & experiments
│
├── frontend/                     # Next.js frontend (UI only)
│   ├── app/                      # Next.js app router pages
│   │   ├── page.tsx              # Home / trading arena
│   │   ├── ai/
│   │   │   └── page.tsx          # AI performance & explanations
│   │   ├── human/
│   │   │   └── page.tsx          # Human trading interface
│   │   ├── leaderboard/
│   │   │   └── page.tsx          # AI vs Human comparison
│   │   └── layout.tsx            # Global layout
│   │
│   ├── components/               # Reusable UI components
│   │   ├── charts/               # Chart visualizations
│   │   │   ├── EquityCurve.tsx   # Portfolio equity curve
│   │   │   └── TradeChart.tsx    # Trade-level visualization
│   │   │
│   │   ├── cards/                # Information cards
│   │   │   ├── TradeExplanation.tsx # AI explanation display
│   │   │   └── MetricsCard.tsx   # Performance metrics display
│   │   │
│   │   └── common/               # Shared UI elements
│   │       └── Header.tsx        # App header/navigation
│   │
│   ├── lib/                      # Frontend helpers
│   │   └── api.ts                # Backend API fetch wrappers
│   │
│   ├── styles/                   # Global and component styles
│   └── tailwind.config.ts        # TailwindCSS configuration
│
└── docs/                         # Project documentation
    ├── system_contract.md        # Trading rules & constraints
    ├── architecture.md           # High-level system architecture
    └── explainability.md         # AI explainability design
