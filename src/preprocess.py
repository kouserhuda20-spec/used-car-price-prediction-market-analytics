import pandas as pd

FEATURES = ["brand","model","year","age","fuel","transmission","kilometers","owners","location"]
TARGET = "price_lakh"
CATEGORICAL = ["brand","model","fuel","transmission","location"]
NUMERICAL = ["year","age","kilometers","owners"]

def load_data(path="data/used_cars_demo.csv"):
    return pd.read_csv(path)

def clean_data(df):
    df = df.copy().drop_duplicates()
    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df["kilometers"] = pd.to_numeric(df["kilometers"], errors="coerce")
    df["owners"] = pd.to_numeric(df["owners"], errors="coerce")
    df["price_lakh"] = pd.to_numeric(df["price_lakh"], errors="coerce")
    df["age"] = 2026 - df["year"]
    df = df.dropna(subset=FEATURES+[TARGET])
    df = df[(df["kilometers"] >= 0) & (df["price_lakh"] > 0)]
    return df

def prepare_xy(df):
    return df[FEATURES], df[TARGET]
