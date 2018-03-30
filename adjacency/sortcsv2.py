import pandas as pd

df=pd.read_csv('adjmatrix.csv', sep=',',header=0, index_col=0, dtype=object)

df.sort_index(axis=0)
df.sort_index(axis=1)

df.to_csv("sortedadj.csv", header=True, index=True)