# Project Structure

```text
investlab/
├── README.md
├── .env
├── .gitignore
│
├── backend/
│   ├── requirements.txt
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   │   ├── routes.py
│   │   │   ├── ai.py
│   │   │   ├── human.py
│   │   │   ├── market.py
│   │   │   ├── portfolio.py
│   │   │   └── leaderboard.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── contracts.py
│   │   ├── db/
│   │   │   ├── db.py
│   │   │   └── schema.sql
│   │   ├── pipelines/
│   │   │   ├── ingestion.py
│   │   │   ├── features.py
│   │   │   └── sentiment.py
│   │   ├── models/
│   │   │   ├── train.py
│   │   │   ├── predict.py
│   │   │   └── model.pkl
│   │   ├── strategy/
│   │   │   ├── signal_engine.py
│   │   │   ├── risk_manager.py
│   │   │   └── position_sizer.py
│   │   ├── execution/
│   │   │   ├── execution_engine.py
│   │   │   └── fee_model.py
│   │   ├── explainability/
│   │   │   ├── shap_explainer.py
│   │   │   └── rationale.py
│   │   ├── competition/
│   │   │   ├── portfolio.py
│   │   │   ├── metrics.py
│   │   │   └── leaderboard.py
│   │   ├── human/
│   │   │   └── validator.py
│   │   └── utils/
│   │       └── time_utils.py
│   ├── data/
│   │   ├── raw/
│   │   ├── features/
│   │   └── sentiment/
│   ├── scripts/
│   │   ├── run_simulation.py
│   │   ├── replay_history.py
│   │   └── reset_db.py
│   └── notebooks/
│       ├── eda.ipynb
│       └── model_experiments.ipynb
│
├── frontend/
│   ├── app/
│   │   ├── page.tsx
│   │   ├── ai/
│   │   │   └── page.tsx
│   │   ├── human/
│   │   │   └── page.tsx
│   │   ├── leaderboard/
│   │   │   └── page.tsx
│   │   └── layout.tsx
│   ├── components/
│   │   ├── charts/
│   │   │   ├── EquityCurve.tsx
│   │   │   └── TradeChart.tsx
│   │   ├── cards/
│   │   │   ├── TradeExplanation.tsx
│   │   │   └── MetricsCard.tsx
│   │   └── common/
│   │       └── Header.tsx
│   ├── lib/
│   │   └── api.ts
│   ├── styles/
│   └── tailwind.config.ts
│
└── docs/
    ├── system_contract.md
    ├── architecture.md
    └── explainability.md
