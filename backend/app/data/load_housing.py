from pathlib import Path

import pandas as pd
from sklearn.datasets import fetch_california_housing


def load_dataset(dest: Path) -> pd.DataFrame:
    dest.parent.mkdir(parents=True, exist_ok=True)
    housing = fetch_california_housing(as_frame=True)
    df = housing.frame
    df.to_csv(dest, index=False)
    return df
