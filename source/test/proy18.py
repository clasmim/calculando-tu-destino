import pandas as pd

df = pd.read_csv("BetterLifeRegions_cleaned.csv")

def replaceCountry(x):
    if x == "Korea":
        return "South Korea"
    if x == "Slovak Republic":
        return "Slovakia"
    if x == "Türkiye":
        return "Turkey"
    else:
        return x

df["Country"] = df["Country"].map(replaceCountry)

def replace(x):
    if x == "..":
        x = None
    return x

df = df.map(replace)
df_clean = df.dropna(axis=0,how="any")
df_clean.to_csv("BetterLifeRegions_clean.csv")