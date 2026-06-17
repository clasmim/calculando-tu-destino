import pandas as pd

df = pd.read_csv("BetterLife2023.csv")
dv = pd.read_csv("BetterLife.csv")

c = set(df["Country"].values)
p = set(dv["Country"].values)
d = c.symmetric_difference(p)

for thing in d:
    print(df.loc[df["Country"] == thing].index)

df.drop(index=[38,39,29,35,20,7],inplace=True)

df.to_csv("BetterLife2023_clean.csv")