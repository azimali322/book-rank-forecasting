# Book Rank Forecasting Project

## Overview
This project aims to forecast sales rankings for Kindle and Print Editions using time series analysis on Amazon sales rank data from Kaggle.

## Dataset
- **Source**: [Kaggle - Amazon Sales Rank Data](https://www.kaggle.com/datasets/ucffool/amazon-sales-rank-data-for-print-and-kindle-books)
- **Main file**: `amazon_com_extras.csv`

## Project Structure
```
Book Rank Forecasting/
├── data/                    # Raw and processed datasets
├── notebooks/              # Jupyter notebooks for analysis
├── models/                 # Trained model files
├── results/                # Model evaluation results
├── plots/                  # Generated visualizations
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

## Methodology

### 1. Data Preparation
- Load and explore the Amazon sales rank dataset
- Handle missing values and data quality issues
- Convert data types and create time-based features

### 2. Time Series Split
- **In-time sample**: Historical data for training (e.g., 2018-2023)
- **Out-of-time sample**: Future data for testing (e.g., 2024)

### 3. Time Series Techniques
- **Traditional Methods**:
  - ARIMA/SARIMA models
  - Exponential Smoothing (Holt-Winters)
  
- **Machine Learning Methods**:
  - Random Forest
  - XGBoost/LightGBM
  
- **Deep Learning Methods**:
  - LSTM networks
  - Prophet (Facebook's forecasting tool)
  
- **Ensemble Methods**:
  - Model stacking and blending
  - Weighted averaging

### 4. Evaluation Metrics
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Percentage Error (MAPE)
- Symmetric Mean Absolute Percentage Error (sMAPE)

## Getting Started

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up Kaggle API credentials for data download

3. Run notebooks in sequence:
   - `01_data_exploration.ipynb`
   - `02_time_series_analysis.ipynb`
   - `03_model_training.ipynb`
   - `04_model_evaluation.ipynb`

## Expected Outcomes
- Accurate forecasts of book sales rankings
- Comparison of different time series methods
- Insights into ranking patterns and seasonality
- Production-ready forecasting pipeline
