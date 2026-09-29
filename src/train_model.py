import sys, json
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, ExtraTreesRegressor, RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from preprocess import load_data, clean_data, FEATURES, TARGET, CATEGORICAL, NUMERICAL

df=clean_data(load_data())
X=df[FEATURES]; y=df[TARGET]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.2,random_state=42)

pre=ColumnTransformer([
 ("cat",Pipeline([("imp",SimpleImputer(strategy="most_frequent")),("ohe",OneHotEncoder(handle_unknown="ignore"))]),CATEGORICAL),
 ("num",Pipeline([("imp",SimpleImputer(strategy="median")),("scale",StandardScaler())]),NUMERICAL)
])

candidates={
 "Ridge": Ridge(alpha=10),
 "RandomForest": RandomForestRegressor(n_estimators=350,random_state=42,n_jobs=-1,min_samples_leaf=2),
 "GradientBoosting": GradientBoostingRegressor(n_estimators=300,max_depth=3,learning_rate=.04,random_state=42),
 "ExtraTrees": ExtraTreesRegressor(n_estimators=350,random_state=42,n_jobs=-1,min_samples_leaf=2)
}
results=[]; fitted={}
for name,model in candidates.items():
    pipe=Pipeline([("preprocessor",pre),("model",model)])
    pipe.fit(X_train,y_train)
    pred=pipe.predict(X_test)
    mae=mean_absolute_error(y_test,pred); rmse=mean_squared_error(y_test,pred)**.5; r2=r2_score(y_test,pred)
    results.append({"model":name,"MAE":mae,"RMSE":rmse,"R2":r2})
    fitted[name]=pipe

results_df=pd.DataFrame(results).sort_values("RMSE")
Path("models").mkdir(exist_ok=True)
results_df.to_csv("models/model_comparison.csv",index=False)
best_name=results_df.iloc[0]["model"]
joblib.dump(fitted[best_name],"models/best_car_price_model.joblib")

# Tuned Random Forest (kept as a separate artifact)
rf=Pipeline([("preprocessor",pre),("model",RandomForestRegressor(random_state=42,n_jobs=-1))])
params={"model__n_estimators":[250,400],"model__max_depth":[None,12,20],"model__min_samples_leaf":[1,2,4]}
search=RandomizedSearchCV(rf,params,n_iter=6,scoring="neg_root_mean_squared_error",cv=3,random_state=42,n_jobs=-1)
search.fit(X_train,y_train)
tuned_pred=search.predict(X_test)
tuned={"model":"TunedRandomForest","MAE":mean_absolute_error(y_test,tuned_pred),"RMSE":mean_squared_error(y_test,tuned_pred)**.5,"R2":r2_score(y_test,tuned_pred)}
results_df=pd.concat([results_df,pd.DataFrame([tuned])],ignore_index=True).sort_values("RMSE")
results_df.to_csv("models/model_comparison.csv",index=False)
joblib.dump(search.best_estimator_,"models/tuned_random_forest.joblib")
if tuned["RMSE"] < float(results_df.iloc[1]["RMSE"]) if len(results_df)>1 else True:
    joblib.dump(search.best_estimator_,"models/best_car_price_model.joblib")

Path("models/model_metadata.json").write_text(json.dumps({
 "best_model": str(results_df.iloc[0]["model"]),
 "features": FEATURES,
 "target": TARGET,
 "rows": len(df)
},indent=2))
print(results_df.round(4).to_string(index=False))
