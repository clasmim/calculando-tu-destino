import sklearn as sk
import pandas as pd
import numpy as np

df = pd.read_csv("BetterLife.csv")
ls = df["Life satisfaction"]

rf = sk.ensemble.RandomForestRegressor(n_estimators = 1000, random_state = 42)
p = ls.values.reshape(-1,1)
meow = rf.fit(np.array(df["Country"].index).reshape(-1,1),p)
print(meow.predict(np.array(df["Country"].index).reshape(-1,1)))