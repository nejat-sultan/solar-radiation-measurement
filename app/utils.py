import pandas as pd # type: ignore

def load_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)

# def process_data(data: pd.DataFrame) -> pd.DataFrame:
#     data = data.dropna()
#     return data