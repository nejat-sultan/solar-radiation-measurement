import pandas as pd # type: ignore
from app.utils import load_data

def test_load_data():
    data = load_data('C:/Users/nejat/AIM Projects/data/benin-malanville.csv')
    assert isinstance(data, pd.DataFrame)
