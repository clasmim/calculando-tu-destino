from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import joblib

df = pd.read_csv("BetterLifeRegions_clean.csv")

dic_test = {}
countries = df["Country"].unique()
for c in countries:
    dic_test[c] = 0

features = joblib.load("pkl/model_features.pkl") 
country_profiles = df.groupby("Country")[features].mean()

scaler = StandardScaler()
scaled_profiles = scaler.fit_transform(country_profiles)

nn = NearestNeighbors(n_neighbors=1, metric='euclidean')
nn.fit(scaled_profiles)

for i in range(100):
    user_input = df[features].sample(n=1, random_state=i)
    user_scaled = scaler.transform(user_input)
    _, idx = nn.kneighbors(user_scaled,n_neighbors=3)
    recommended_country = country_profiles.index[idx[0]]
    dic_test[recommended_country[0]] += 1
dic_test