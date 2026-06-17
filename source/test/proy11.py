import pandas as pd

dv = pd.read_csv('BetterLife 2020.csv')
df = dv.loc[dv["Inequality"]=="Total"]

df_pivoted = df.pivot(index='Country', columns='Indicator', values='Value').reset_index()

df_pivoted.columns.name = None

dp = df_pivoted.drop(axis="rows",index=29)
dp.to_csv("BetterLife2020.csv")