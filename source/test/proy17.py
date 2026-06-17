import pandas as pd

df = pd.read_csv("UniversityRanks_clean.csv")
dv = pd.read_csv("BetterLifeRegions_finish.csv")

c = set(df["Country"].values)
p = set(dv["Country"].values)
p-c