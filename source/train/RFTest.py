import pandas as pd
import joblib

df = pd.read_csv("csv/BetterLifeRegions_clean.csv")
model = joblib.load("pkl/rf_model.pkl")
label_encoder = joblib.load("pkl/label_encoder.pkl")
feature_columns = joblib.load("pkl/model_features.pkl")
dic_test = {}
countries = df["Country"].unique()
for c in countries:
    dic_test[c] = 0
for i in range(100):
    user_input = df[feature_columns].sample(n=1, random_state=i) 
    pred_encoded = model.predict(user_input)[0]
    pred_label = label_encoder.inverse_transform([pred_encoded])[0]
    dic_test[pred_label] += 1
dic_test