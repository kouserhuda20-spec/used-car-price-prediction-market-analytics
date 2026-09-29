# Project Report

## 1. Problem Statement
Used-car pricing depends on vehicle age, mileage, brand, model, fuel, transmission, ownership history and market/location effects. The goal is to create an analytics workflow that explains these factors and estimates resale prices.

## 2. Objectives
- Clean and validate structured vehicle data.
- Explore market trends.
- Answer business questions with SQL.
- Engineer useful prediction features.
- Compare regression algorithms.
- Tune a tree-based model.
- Expose predictions through a simple application.

## 3. Methodology
1. Data ingestion
2. Cleaning and validation
3. EDA
4. SQL analytics
5. Feature preparation
6. Train/test split
7. Baseline model comparison
8. Hyperparameter tuning
9. Evaluation
10. Streamlit application

## 4. Evaluation
Use MAE, RMSE and R². Lower MAE/RMSE indicates smaller prediction errors; R² describes explained variance on the test set.

## 5. Limitations
The bundled dataset is synthetic. It is intended to demonstrate engineering and analytics workflow, not to make claims about actual Indian used-car prices.

## 6. Future Improvements
- Use a licensed real-world dataset.
- Add location/brand encodings based on historical market data.
- Add price confidence intervals.
- Add explainability with SHAP.
- Add model monitoring and drift checks.
- Deploy with a managed ML/API service.
