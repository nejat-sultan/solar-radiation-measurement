import pandas as pd # type: ignore
from src.eda import load_data, get_basic_statistics
import tempfile

def test_load_data():
    test_data = pd.DataFrame({
        'values': [1, 2, 3, 4, 5]
    })
  
    with tempfile.NamedTemporaryFile(suffix=".csv") as tmp_file:
        test_data.to_csv(tmp_file.name, index=False)

        # Re-read the file to ensure it's saved correctly
        loaded_data = pd.read_csv(tmp_file.name)
        pd.testing.assert_frame_equal(test_data, loaded_data)

def test_get_basic_statistics():
    data = pd.DataFrame({
        'values': [1, 2, 3, 4, 5]
    })
    stats = get_basic_statistics(data)
    
    assert stats.loc['mean', 'values'] == 3, "Expected mean of 3"
