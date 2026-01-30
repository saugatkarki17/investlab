import pandas as pd
import pandas_ta as ta
from pathlib import Path

RAW_PATH = Path("backend/data/market/raw/ohlcv_2020_2025.parquet")
FEATURE_PATH = Path("backend/data/market/features")
FEATURE_PATH.mkdir(parents=True, exist_ok=True)

# Features to generate
FEATURE_COLUMNS = ["Open", "High", "Low", "Close", "Volume"]

def build_training_features():
  
    # Load raw multi-index Parquet
  
    df = pd.read_parquet(RAW_PATH)

    # Flatten MultiIndex columns if present
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = ["_".join(map(str, c)).strip() for c in df.columns]
    else:
        df.columns = [str(c).strip() for c in df.columns]

    # Identify Date column
    date_col_candidates = [c for c in df.columns if "Date" in c or "date" in c.lower()]
    if not date_col_candidates:
        raise ValueError("Cannot find Date column in raw data")
    date_col = date_col_candidates[0]

# Melt the dataframe to long format

    value_vars = [c for c in df.columns if c != date_col]
    df_long = df.melt(id_vars=[date_col], value_vars=value_vars, var_name="col_ticker", value_name="value")

    # Convert 'value' to numeric now, coerce errors to NaN
    df_long["value"] = pd.to_numeric(df_long["value"], errors="coerce")

    # Split 'col_ticker' into 'feature' and 'ticker'
    df_long[["feature", "ticker"]] = df_long["col_ticker"].str.rsplit("_", n=1, expand=True)
    df_long = df_long.drop(columns=["col_ticker"])

  
    # Pivot to wide format: one row per ticker/date
    
    # Use aggfunc='first' to avoid pandas trying mean on object types
    df = df_long.pivot_table(
        index=[date_col, "ticker"],
        columns="feature",
        values="value",
        aggfunc="first"
    ).reset_index()
    df = df.rename(columns={date_col: "Date"})


  
    # Convert numeric columns
  
    for col in FEATURE_COLUMNS:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Drop rows where Close is NaN (essential for features)
    df = df.dropna(subset=["Close"])

    # Convert Date to datetime
    df["Date"] = pd.to_datetime(df["Date"])

    # Sort by ticker + Date
    df = df.sort_values(["ticker", "Date"]).reset_index(drop=True)

  
    # Feature engineering

    df["return_1d"] = df.groupby("ticker", group_keys=False)["Close"].pct_change().reset_index(drop=True)

    df["volatility_20d"] = (
        df.groupby("ticker", group_keys=False)["return_1d"]
          .rolling(20)
          .std()
          .reset_index(drop=True)
    )

    df["rsi_14"] = (
        df.groupby("ticker", group_keys=False)["Close"]
          .apply(lambda x: ta.rsi(x, length=14))
          .reset_index(drop=True)
    )

    # Target: next-day price up?
    df["target"] = (df.groupby("ticker")["Close"].shift(-1) > df["Close"]).astype(int)

    # Drop any remaining NaNs
    df.dropna(inplace=True)

   
    # Save features
    
    FEATURE_PATH.mkdir(parents=True, exist_ok=True)
    output_path = FEATURE_PATH / "features_2020_2025.parquet"
    df.to_parquet(output_path)
    print(f" Training features frozen → {output_path}")


if __name__ == "__main__":
    build_training_features()
