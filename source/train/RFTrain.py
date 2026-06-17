import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os

data = pd.read_csv(str(os.path.dirname(os.path.abspath(__file__)))+"/csv/BetterLifeRegions_clean.csv")

X = data.drop(columns=['Country'])
y = data['Country']

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)
model = RandomForestClassifier(n_estimators=500,random_state=42)
model.fit(X, y_encoded)

joblib.dump(model, str(os.path.dirname(os.path.abspath(__file__)))+"/pkl/rf_model.pkl")
joblib.dump(label_encoder, str(os.path.dirname(os.path.abspath(__file__)))+"/pkl/label_encoder.pkl")
joblib.dump(X.columns, str(os.path.dirname(os.path.abspath(__file__)))+"/pkl/model_features.pkl")