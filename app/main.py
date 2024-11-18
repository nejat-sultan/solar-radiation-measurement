import streamlit as st  # type: ignore
import pandas as pd  # type: ignore
import matplotlib.pyplot as plt  # type: ignore
import seaborn as sns  # type: ignore
import numpy as np
from utils import load_data  # Importing from utils

st.title("Data Insights Dashboard")

file_upload = st.sidebar.file_uploader("Upload CSV file", type=["csv"])

if file_upload:

    data = load_data(file_upload)
    
    # Allow the user to sample the data
    sample_size = st.sidebar.slider("Select Sample Size", min_value=100, max_value=2000, value=1000)
    sample_data = data.sample(n=sample_size, random_state=42)  

    st.subheader("Dataset Overview (Sampled)")
    st.write(sample_data)

    # Adjust Visualization Range
    st.subheader("Adjust Visualization Range")
    range_val = st.slider("Select Range", min_value=0, max_value=len(sample_data), value=5)

    # Filter and show the selected number of rows
    st.subheader("Filtered Data")
    st.write(sample_data.head(range_val))

    # Data Visualization (Line chart of Timestamp vs other columns)
    st.subheader("Data Visualization - Line Chart")
    st.line_chart(sample_data.set_index("Timestamp"))

    # Data Visualization - Bar Chart (e.g., GHI, DNI, DHI comparison)
    st.subheader("Bar Chart - GHI, DNI, DHI Comparison")
    bar_data = sample_data[['GHI', 'DNI', 'DHI']].mean()
    st.bar_chart(bar_data)

    # Data Visualization - Histogram (distribution of RH)
    st.subheader("Histogram - Distribution of RH")
    st.write("Distribution of Relative Humidity (RH) values")
    fig, ax = plt.subplots()
    ax.hist(sample_data['RH'], bins=10, color='skyblue', edgecolor='black')
    ax.set_title('Histogram of RH')
    ax.set_xlabel('Relative Humidity')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

    # Data Visualization - Scatter Plot (GHI vs DNI)
    st.subheader("Scatter Plot - GHI vs DNI")
    st.write("Scatter plot showing relationship between GHI and DNI")
    fig, ax = plt.subplots()
    ax.scatter(sample_data['GHI'], sample_data['DNI'], color='purple')
    ax.set_title('GHI vs DNI')
    ax.set_xlabel('GHI')
    ax.set_ylabel('DNI')
    st.pyplot(fig)

    # Data Visualization - Heatmap (Correlation Matrix)
    st.subheader("Heatmap - Correlation Matrix")
    # Select only numeric columns for correlation calculation
    numeric_data = sample_data.select_dtypes(include=[np.number])

    # Calculate correlation matrix
    corr = numeric_data.corr()

    # Plot the heatmap
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)


    # Data Statistics (Summary statistics)
    st.subheader("Data Statistics")
    st.write(sample_data.describe())

else:
    st.info("Please upload a CSV file to get started.")
