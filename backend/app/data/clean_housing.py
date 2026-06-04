from pathlib import Path

import pandas as pd


def clean_dataset(src: Path, dest: Path) -> pd.DataFrame:
    df = pd.read_csv(src)
    df = df.drop_duplicates()
    df = df.fillna(df.median(numeric_only=True))
    df.to_csv(dest, index=False)
    return df
