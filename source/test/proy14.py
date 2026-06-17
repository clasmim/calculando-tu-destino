import pandas as pd

df = pd.read_csv("better-life-index-2024.csv")
dv = pd.read_csv("bli2024.csv")

c = set(df["Country"].values)
p = set(dv["Country"].values)
c.symmetric_difference(p)