# 🚗 Used Car Price Prediction & Market Analytics Platform

## Portfolio Project — Data Analytics + Data Science + Machine Learning

This project analyzes used-car market patterns and predicts resale prices from vehicle attributes.

### What makes this project portfolio-ready
- End-to-end data pipeline
- Exploratory data analysis with generated figures
- SQL business analytics
- Four regression baselines
- Random Forest hyperparameter tuning
- MAE / RMSE / R² model comparison
- Saved production-style preprocessing + model pipeline
- Interactive Streamlit analytics dashboard
- Interactive price prediction interface
- Unit tests
- Project report and dashboard specification

### Tech Stack
**Python:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn  
**SQL:** aggregations, CASE, HAVING, window functions  
**ML:** Ridge, Random Forest, Gradient Boosting, Extra Trees, RandomizedSearchCV  
**App:** Streamlit  
**Workflow:** Jupyter, Git/GitHub

## Quick Start — Windows / VS Code

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python src/train_model.py
python src/eda.py
streamlit run app.py
```

Then open the Streamlit URL shown in the terminal.

### Run tests
```powershell
pytest -q
```

### Run prediction from terminal
```powershell
python src/predict.py
```

## Dataset note
`data/used_cars_demo.csv` is **synthetic demonstration data**, generated for this portfolio project. It is not claimed to represent real market prices. For a public GitHub portfolio, replace it with a properly licensed/public dataset and cite the source.

## Suggested GitHub description
> End-to-end used-car market analytics and resale-price prediction using Python, SQL, machine learning, model tuning, and Streamlit.

## Suggested resume bullets
- Built an end-to-end used-car analytics and price-prediction pipeline using Python, SQL, Pandas and Scikit-learn, covering data cleaning, EDA, feature engineering and model evaluation.
- Compared multiple regression algorithms using MAE, RMSE and R² and tuned a Random Forest model using cross-validation and randomized hyperparameter search.
- Developed a Streamlit dashboard for market KPIs, brand/fuel/location analysis and interactive resale-price prediction.

## Interview topics to prepare
- Why RMSE vs MAE?
- How did you prevent data leakage?
- Why one-hot encoding?
- Why did you compare multiple models?
- What does R² mean?
- How would you improve the model with real market data?
- How would you deploy the model?
- How would you validate predictions for a new city or car model?
