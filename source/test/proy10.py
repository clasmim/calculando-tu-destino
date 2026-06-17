import pandas as pd

df = pd.read_csv("BetterLife2024_cleaned.csv")

df["Housing"] = (df["Dwellings without basic facilities"] + df["Housing expenditure"] + df["Rooms per person"])/3
df