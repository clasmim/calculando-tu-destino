import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from libProy import esFaltante

df = pd.read_csv("BetterLife.csv")

faltantes = pd.isna(df)
mapa = faltantes.map(esFaltante)

plt.figure(figsize=(20,20))
sns.heatmap(mapa.corr(), cmap = 'Reds', annot = True)

plt.show()