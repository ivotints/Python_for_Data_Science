import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load a dataset from a CSV file."""
    try:
        if not isinstance(path, str):
            raise TypeError(f"Path '{path}' is not a string")
        if not path.lower().endswith(".csv"):
            raise ValueError(f"File '{path}' does not have .csv extension")
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")
        return dataset
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return None
