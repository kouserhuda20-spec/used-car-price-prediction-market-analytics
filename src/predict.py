import joblib, pandas as pd

model=joblib.load("models/best_car_price_model.joblib")
sample=pd.DataFrame([{
 "brand":"Hyundai","model":"Creta","year":2021,"age":5,
 "fuel":"Diesel","transmission":"Automatic","kilometers":45000,
 "owners":1,"location":"Bangalore"
}])
prediction=float(model.predict(sample)[0])
print(f"Estimated used-car price: ₹{prediction:.2f} lakh")
