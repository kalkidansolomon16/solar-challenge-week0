from __future__ import annotations
import os
import pandas as pd
from typing import List, Dict, Optional

COUNTRY_FILES: Dict[str, str] = {
    "Benin": "data/benin_clean.csv",
    "Sierra Leone": "data/sierra_leone_clean.csv",
    "Togo": "data/togo_clean.csv",
}

METRICS = ["GHI", "DNI", "DHI"]


def existing_countries() -> List[str]:
    return [c for c, p in COUNTRY_FILES.items() if os.path.exists(p)] or list(COUNTRY_FILES.keys())


def load_countries(countries: List[str]) -> pd.DataFrame:
    frames = []
    for c in countries:
        path = COUNTRY_FILES.get(c)
        if not path or not os.path.exists(path):
            continue
        df = pd.read_csv(path)
        # Coerce expected metrics to numeric
        for col in METRICS:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")
        df["Country"] = c
        frames.append(df)
    if not frames:
        raise FileNotFoundError(
            "No data loaded. Place cleaned CSVs under data/ as benin_clean.csv, sierra_leone_clean.csv, togo_clean.csv"
        )
    return pd.concat(frames, ignore_index=True)


def infer_region_column(df: pd.DataFrame) -> Optional[str]:
    candidates = [
        "region",
        "Region",
        "admin1",
        "Admin1",
        "province",
        "Province",
        "state",
        "State",
        "ADM1_NAME",
        "NAME_1",
        "area",
        "Area",
    ]
    for c in candidates:
        if c in df.columns:
            return c
    return None


def top_regions(df: pd.DataFrame, metric: str = "GHI", n: int = 10) -> pd.DataFrame:
    if metric not in df.columns:
        raise ValueError(f"Metric {metric} not found in data")
    region_col = infer_region_column(df)
    if not region_col:
        raise ValueError("No region-like column found to compute top regions")
    out = (
        df[[region_col, metric]]
        .groupby(region_col)[metric]
        .mean()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
    )
    out.columns = [region_col, f"avg_{metric}"]
    return out
