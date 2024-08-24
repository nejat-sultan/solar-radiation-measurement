import streamlit as st # type: ignore
import pandas as pd # type: ignore
import numpy as np

st.title("Data Insights Dashboard")

def load_data():
    # Replace with actual data loading code
    data = pd.DataFrame(
        {
            "Timestamp": pd.date_range(start="2021-08-09 00:01", periods=5, freq="T"),
            "GHI": [-1.2, -1.1, -1.1, -1.1, -1.0],
            "DNI": [-0.2, -0.2, -0.2, -0.1, -0.1],
            "DHI": [-1.1, -1.1, -1.1, -1.0, -1.0],
            "ModA": [0.0, 0.0, 0.0, 0.0, 0.0],
            "ModB": [0.0, 0.0, 0.0, 0.0, 0.0],
            "Tamb": [26.2, 26.2, 26.2, 26.2, 26.2],
            "RH": [93.4, 93.6, 93.7, 93.3, 93.3],
            "WS": [0.0, 0.0, 0.3, 0.2, 0.1],
            "WSgust": [0.4, 0.0, 1.1, 0.7, 0.7],
            "WSstdev": [0.1, 0.0, 0.5, 0.4, 0.3],
            "WD": [122.1, 0.0, 124.6, 120.3, 113.2],
            "WDstdev": [0.0, 0.0, 1.5, 1.3, 1.0],
            "BP": [998, 998, 997, 997, 997],
            "Cleaning": [0, 0, 0, 0, 0],
            "Precipitation": [0.0, 0.0, 0.0, 0.0, 0.0],
            "TModA": [26.3, 26.3, 26.4, 26.4, 26.4],
            "TModB": [26.2, 26.2, 26.2, 26.3, 26.3],
            "Comments": [None, None, None, None, None]
        }
    )
    return data

data = load_data()

st.subheader("Dataset Overview")
st.write(data)

st.subheader("Adjust Visualization Range")
range_val = st.slider("Select Range", min_value=0, max_value=len(data), value=5)

st.subheader("Filtered Data")
st.write(data.head(range_val))

st.subheader("Data Visualization")
st.line_chart(data.set_index("Timestamp"))

st.subheader("Data Statistics")
st.write(data.describe())