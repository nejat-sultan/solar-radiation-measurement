import pandas as pd # type: ignore

def load_data(file_path):
    return pd.read_csv(file_path)

def get_basic_statistics(data):
    return data.describe()
