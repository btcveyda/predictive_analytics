from pathlib import Path

import pandas as pd


def dataset_stats(path: Path) -> dict:
    df = pd.read_csv(path)
    return {
        "rows": int(len(df)),
        "columns": int(len(df.columns)),
        "avg_house_value": float(df["MedHouseVal"].mean()),
        "missing_values": df.isnull().sum().to_dict(),
    }
