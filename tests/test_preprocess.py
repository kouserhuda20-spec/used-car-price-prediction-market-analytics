import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))
import pandas as pd
from preprocess import clean_data

def test_clean_data_recomputes_age():
    df=pd.DataFrame([{"brand":"A","model":"B","year":2020,"age":99,"fuel":"Petrol",
                      "transmission":"Manual","kilometers":10000,"owners":1,"location":"Bangalore","price_lakh":5}])
    out=clean_data(df)
    assert out.iloc[0]["age"] == 6

def test_clean_data_removes_bad_price():
    df=pd.DataFrame([{"brand":"A","model":"B","year":2020,"age":6,"fuel":"Petrol",
                      "transmission":"Manual","kilometers":10000,"owners":1,"location":"Bangalore","price_lakh":-1}])
    assert len(clean_data(df)) == 0
