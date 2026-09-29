import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(page_title="Used Car Analytics",page_icon="🚗",layout="wide")
st.title("🚗 Used Car Price Prediction & Market Analytics")
st.caption("Portfolio demonstration — dataset is synthetic demo data.")

df=pd.read_csv("data/used_cars_demo.csv")
model_path=Path("models/best_car_price_model.joblib")

tab1,tab2,tab3=st.tabs(["📊 Market Analytics","🔮 Price Predictor","ℹ️ Project"])

with tab1:
    c1,c2,c3,c4=st.columns(4)
    c1.metric("Listings",f"{len(df):,}")
    c2.metric("Average Price",f"₹{df.price_lakh.mean():.2f} L")
    c3.metric("Median Price",f"₹{df.price_lakh.median():.2f} L")
    c4.metric("Avg Mileage",f"{df.kilometers.mean():,.0f} km")
    st.subheader("Average Price by Brand")
    st.bar_chart(df.groupby("brand").price_lakh.mean().sort_values(ascending=False))
    st.subheader("Price vs Vehicle Age")
    st.scatter_chart(df,x="age",y="price_lakh")
    st.subheader("Average Price by Fuel")
    st.bar_chart(df.groupby("fuel").price_lakh.mean().sort_values(ascending=False))

with tab2:
    st.subheader("Estimate Resale Price")
    brands=sorted(df.brand.unique()); models=sorted(df.model.unique())
    b=st.selectbox("Brand",brands)
    m=st.selectbox("Model",models)
    year=st.number_input("Year",min_value=2010,max_value=2026,value=2021)
    fuel=st.selectbox("Fuel",sorted(df.fuel.unique()))
    trans=st.selectbox("Transmission",sorted(df.transmission.unique()))
    km=st.number_input("Kilometers",min_value=0,max_value=250000,value=45000,step=1000)
    owners=st.selectbox("Owners",[1,2,3])
    loc=st.selectbox("Location",sorted(df.location.unique()))
    if st.button("Predict Price"):
        if not model_path.exists():
            st.error("Train the model first: python src/train_model.py")
        else:
            model=joblib.load(model_path)
            x=pd.DataFrame([{"brand":b,"model":m,"year":year,"age":2026-year,"fuel":fuel,
                             "transmission":trans,"kilometers":km,"owners":owners,"location":loc}])
            p=float(model.predict(x)[0])
            st.success(f"Estimated resale price: ₹{p:.2f} lakh")

with tab3:
    st.markdown("""
    **Skills demonstrated:** Python, Pandas, NumPy, SQL, EDA, feature engineering,
    regression, model evaluation, hyperparameter tuning, Streamlit and dashboard analytics.

    **Business questions:** Which brands retain value? How do age and mileage affect prices?
    How do fuel type, transmission and location relate to resale value?

    **Data note:** the bundled dataset is synthetic and for demonstration only.
    """)
