import pandas as pd

df = pd.read_csv('BetterLife 2023.csv')

df_t = df.set_index('Dimension').transpose()

df_t.reset_index(inplace=True)
df_t = df_t.rename(columns={'index': 'Country'})

df_t.to_csv("BetterLife2023.csv")