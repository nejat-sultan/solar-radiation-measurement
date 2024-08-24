import pandas as pd # type: ignore
from src.eda import load_data, get_basic_statistics

def test_load_data():
    test_data = pd.DataFrame({
        'values': [1, 2, 3, 4, 5]
    })
    test_data.to_csv('C:/Users/nejat/AIM Projects/data/benin-malanville.csv', index=False)
    
    data = load_data('C:/Users/nejat/AIM Projects/data/benin-malanville.csv')
    assert isinstance(data, pd.DataFrame), "Expected data to be a pandas DataFrame"
    assert 'values' in data.columns, "Expected 'values' column in the dataset"

def test_get_basic_statistics():
    data = pd.DataFrame({
        'values': [1, 2, 3, 4, 5]
    })
    stats = get_basic_statistics(data)
    
    assert stats.loc['mean', 'values'] == 3, "Expected mean of 3"
