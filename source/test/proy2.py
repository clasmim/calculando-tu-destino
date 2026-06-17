import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("BetterLife.csv")

popCountry = df.pop("Country")
popUni = df.pop("Top University")

fig,ax = plt.subplots(figsize=(7,10))
ax.barh(popCountry,df["Life satisfaction"])
ax.set_title("Life satisfaction by Country")

plt.show()