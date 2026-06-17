import pandas as pd

df = pd.read_csv("BetterLifeRegions.csv")
df_clean = df.dropna(axis=0,how="any")
df_rm = df_clean.drop("Region",axis="columns")
df_rm.to_csv("BetterLifeRegions_cleaned.csv")