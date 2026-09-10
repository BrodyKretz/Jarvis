from pathlib import Path

import pandas as pd


def load_csv(path: Path) -> pd.DataFrame:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"No such data file: {path}")
    return pd.read_csv(path)
