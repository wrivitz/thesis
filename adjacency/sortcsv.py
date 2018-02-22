import pandas as pd

df=pd.read_csv('qgisadjmatrix.csv', sep=',',header=None, dtype=object)

df.sort_values(by=[0], axis=0)
df.sort_values(by=[0], axis=1)

df.to_csv("sortedqgisadj.csv", header=None, index=None)