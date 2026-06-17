import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("BetterLife.csv")

filtro = df.dropna(axis="rows",subset=["Life satisfaction","University Score"])

filtro["University Ratio"] = filtro["University Score"] / (filtro["Life satisfaction"]*10)

sort = filtro.sort_values(by="University Ratio",axis="rows",ascending=True)

fig,ax=plt.subplots(ncols=2,figsize=(10,10))

ax[0].barh(sort["Country"],sort["University Ratio"])
ax[1].barh(sort["Country"],sort["University Score"])

ax[1].axes.get_yaxis().set_visible(False)

ax[0].set_title("University Ratio")
ax[1].set_title("University Score")

ax[0].grid()
ax[1].grid()

fig.text(s="COMPARISON BETWEEN RATIO AND SCORE",y=1,x=0.3 ,fontdict={"size":15,"color":"red"})
fig.tight_layout()

plt.show()