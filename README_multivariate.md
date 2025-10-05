# Multivariate Time Series Forecasting

This directory contains notebooks for analyzing multivariate time series datasets with multiple features per time step, focusing on feature engineering and transition-based forecasting.

## Dataset

### Beijing Multi-Site Air-Quality Data
- **Features**: PM2.5, PM10, SO2, NO2, CO, O3, temperature, pressure, dew point, wind speed
- **Time Resolution**: Hourly
- **Sites**: 12 monitoring stations
- **Period**: 2013-2017
- **Target**: PM2.5 concentration
- **Kaggle**: [Beijing Multi-Site Air-Quality Data](https://www.kaggle.com/saurabhshahane/beijing-multisite-airquality-data)

## Notebooks

### 01_multivariate_data_exploration.ipynb
- Load and explore multivariate time series datasets
- Understand multiple features per time step
- Feature relationships and correlations
- Time series characteristics and patterns
- Data quality assessment and preprocessing

### 02_multivariate_feature_engineering.ipynb
- Create comprehensive feature sets
- Lag features for multiple variables
- Rolling statistics across features
- Difference and percentage change features
- Interaction features between variables
- Transition state features
- Advanced time series features

### 03_multivariate_model_training.ipynb
- Traditional time series models (VAR, VARMA, etc.)
- Machine learning models with multiple features
- Deep learning models (LSTM, GRU, Transformer)
- Ensemble methods
- Hyperparameter tuning

### 04_multivariate_model_evaluation.ipynb
- Comprehensive model evaluation
- Feature importance analysis
- Model interpretation
- Performance comparison
- Ensemble methods

## Setup

1. **Download dataset**:
   ```bash
   python data_multivariate/download_multivariate_data.py
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run notebooks in order**:
   - Start with `01_multivariate_data_exploration.ipynb`
   - Follow with feature engineering, model training, and evaluation

## Key Features

### Feature Engineering
- **Lag Features**: Multiple time lags for each variable
- **Rolling Statistics**: Mean, std, min, max, median across windows
- **Difference Features**: First and higher-order differences
- **Percentage Change**: Relative changes over time
- **Interaction Features**: Cross-products between variables
- **Transition State Features**: Momentum, trend strength, volatility regimes

### Model Types
- **Traditional**: VAR, VARMA, State Space models
- **Machine Learning**: Random Forest, XGBoost, LightGBM
- **Deep Learning**: LSTM, GRU, Transformer, CNN-LSTM
- **Ensemble**: Weighted averaging, stacking, boosting

### Evaluation Metrics
- **Point Forecasts**: MAE, RMSE, MAPE, sMAPE
- **Probabilistic**: CRPS, Log-likelihood
- **Feature Importance**: Permutation importance, SHAP values
- **Model Interpretation**: Partial dependence plots, feature interactions

## Benefits of Multivariate Time Series

1. **Richer Information**: Multiple variables provide more context
2. **Cross-Variable Dependencies**: Capture relationships between features
3. **Better Forecasting**: Leverage information from related variables
4. **Feature Engineering**: More opportunities for creating predictive features
5. **Transition States**: Model complex state changes across multiple dimensions

## Use Cases

- **Air Quality Forecasting**: Predict pollution levels using weather and traffic data
- **Energy Consumption**: Forecast power usage using temperature, humidity, and time features
- **Financial Markets**: Predict stock prices using multiple economic indicators
- **Healthcare**: Monitor patient vitals using multiple health metrics
- **Supply Chain**: Forecast demand using multiple business indicators

## Best Practices

1. **Start Simple**: Begin with basic features and gradually add complexity
2. **Feature Selection**: Use correlation analysis and feature importance
3. **Cross-Validation**: Use time series cross-validation for robust evaluation
4. **Model Comparison**: Test multiple model types and ensemble methods
5. **Interpretability**: Understand which features drive predictions
6. **Regular Updates**: Retrain models as new data becomes available

## File Structure

```
notebooks_multivariate/
├── 01_multivariate_data_exploration.ipynb
├── 02_multivariate_feature_engineering.ipynb
├── 03_multivariate_model_training.ipynb
└── 04_multivariate_model_evaluation.ipynb

data_multivariate/
├── download_multivariate_data.py
└── PRSA_Data_*.csv (Beijing Air Quality)
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add your improvements
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
