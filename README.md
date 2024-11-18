# **Solar Radiation Measurement Analysis**

## **Project Overview**

- Welcome to the **Solar Data Analytics** project!
- This repository contains a comprehensive analysis of solar radiation data from three West African countries: **Benin**, **Sierra Leone**, and **Togo**.
- The project is part of a week-long challenge for a 12-week training program in:
  - **Data Engineering (DE)**
  - **Financial Analytics (FA)**
  - **Machine Learning Engineering (MLE)**
- The main objective is to extract meaningful insights for strategic solar farm placements aligned with sustainability goals.

## **Project Objectives**

- **Data Analysis**: Perform Exploratory Data Analysis (EDA) on solar radiation and environmental data.
- **Statistical Insights**: Apply statistical methods to validate findings and provide data-driven recommendations.
- **Dashboard Development**: Create an interactive Streamlit dashboard for data exploration.
- **CI/CD Integration**: Implement Continuous Integration and Continuous Deployment for automated testing and deployment.

## **Key Components**

### 1. **Exploratory Data Analysis (EDA)**

- Analyzed solar and environmental data, including:
  - **Global Horizontal Irradiance (GHI)**
  - **Direct Normal Irradiance (DNI)**
  - **Diffuse Horizontal Irradiance (DHI)**
  - **Ambient Temperature**, **Relative Humidity**, and **Wind Speed**
- Identified trends, patterns, and data quality issues (missing values, outliers).
- Derived insights for optimal solar farm placement.

### 2. **Statistical Analysis**

- Conducted various statistical analyses, including:
  - **Correlation Analysis**: Examined relationships between variables.
  - **Trend Analysis**: Analyzed temporal patterns in solar data.
  - **Hypothesis Testing**: Validated key assumptions for decision-making.

### 3. **Streamlit Dashboard**

- Built an interactive dashboard using **Streamlit**:
  - Features time-series visualizations (GHI, DNI, DHI).
  - Provides filters for date range and location selection.
  - Displays statistical summaries and trend charts for insights.

### 4. **CI/CD Implementation**

- Set up **GitHub Actions** for automated testing and deployment.
- Configured **Pytest** for unit testing to maintain code quality.
- Integrated workflows for streamlined updates and robust development.

## **Technologies Used**

- **Python**: Core language for analysis and dashboard development.
- **Pandas & NumPy**: Data manipulation and statistical analysis.
- **Matplotlib & Seaborn**: Data visualization tools.
- **Streamlit**: Dashboard development framework.
- **GitHub Actions**: CI/CD implementation.
- **Pytest**: Automated testing framework.

## **Installation & Usage Instructions**

### **Prerequisites**

- Ensure the following are installed:
  - Python 3.10 or higher
  - Git
  - Virtual environment (optional but recommended)

### **Setup**

1. **Clone the repository:**
   git clone https://github.com/nejat-sultan/solar-radiation-measurement.git
   cd solar-radiation-measurement

2. **Create a virtual environment (optional but recommended):**
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies:**
   pip install -r requirements.txt

### **Running the Analysis**

- To run the data analysis scripts:
  python analysis.py

### **Launching the Streamlit Dashboard**

- To start the interactive dashboard:
  streamlit run app.py
- Access the dashboard at `http://localhost:8501`.

### **Running Tests**

- To run unit tests with Pytest:
  pytest

## **Project Structure**

- The project is organized as follows:
  solar-radiation-measurement/
  ├── data/                     # Raw and processed data files
  ├── notebooks/                # Jupyter notebooks for EDA
  ├── scripts/                  # Python scripts for data processing
  ├── app.py                    # Streamlit dashboard application
  ├── requirements.txt          # Python dependencies
  ├── README.md                 # Project documentation
  └── tests/                    # Unit tests

## **Future Enhancements**

- Add predictive modeling using machine learning for better solar energy forecasting.
- Improve the statistical analysis with advanced time-series forecasting.
- Expand the CI/CD pipeline with additional stages for testing and deployment.

## **Contributing**

- Contributions are welcome!
- Please create a pull request or open an issue if you have suggestions or improvements.
