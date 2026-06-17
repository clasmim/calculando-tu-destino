import pandas as pd
import numpy as np
import random

df = pd.read_csv("example.csv")

dic = {}
for col in df.columns:
    dic[col] = [random.randint(1,10) for i in range(28)]


dv = pd.DataFrame.from_dict(dic)
dv.to_csv("example2.csv")