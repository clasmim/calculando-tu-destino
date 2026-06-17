import pandas as pd

df = pd.read_csv("../web/csv/CountryCoords.csv")
dv = df.drop(columns=["Numeric code","Alpha-3 code"])
dv.to_csv("../web/csv/CountryCoords.csv")