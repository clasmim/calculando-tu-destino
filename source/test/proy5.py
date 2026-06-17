import pandas as pd
from libProy import reemplazarGuion

df = pd.read_csv("UniversityRanks.csv")
ds = pd.read_csv("better-life-index-2024.csv")
dv = pd.DataFrame()

lista = [df.columns[i] for i in range(5,len(df.columns)-1)]
lista2 = ["2025 Rank", "2024 Rank","Location"]
for pal in lista2:
    lista.append(pal)

df.drop(axis=1,columns=lista, inplace=True)

mapa = df.map(reemplazarGuion)
mapa.dropna(axis=0,inplace=True,how="any")
mapa.sort_values(by="QS Overall Score",ascending=False)

dic = {}
for list in mapa.values:
    if list[1] not in dic:
        dic[list[1]] = [list[0],list[2]]

lista3 = []
for pal in dic:
    for fil in ds["Country"].values:
        if fil == pal:
            lista3.append(fil)

for pais in dic:
    if pais not in lista3:
        dic[pais] = None

dic2 = {}
for value in dic:
    if dic[value] != None:
        dic2[value] = dic[value]

dic3 = {"Country":[],"Top University":[],"University Score":[]}
for key in dic2:
    dic3["Country"].append(key)
    dic3["Top University"].append(dic2[key][0])
    dic3["University Score"].append(dic2[key][1])

res = dv.from_dict(dic3)

dataset = pd.merge(ds,res,on="Country")
dataset.to_csv("bli2024.csv")