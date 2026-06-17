import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("lifesatis.xlsx")

ds = df.iloc(axis="rows")[1]
dic = {}
for i in range(len(ds.values)):
    val = ds.values[i]
    if val not in dic:
        dic[val] = []
        dic[val].append(i)
    else:
        dic[val].append(i)

for key in dic:
    dv = df.iloc(axis="columns")[dic[key]].drop(1)
    dv["Country"] = df["Measure"]
    dv.to_csv(f"life{key}.csv")