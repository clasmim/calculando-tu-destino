import pandas as pd

df = pd.read_csv("../csv/UniversityRanks.csv")
df_rm = df.drop(columns=["2024 Rank","Size","Academic Reputation","Employer Reputation","Faculty Student","Citations per Faculty","International Faculty","International Students","International Research Network"])
df_clean = df_rm.dropna(axis=0,how="any")
df_clean.to_csv("../csv/UniversityRanks_clean.csv")