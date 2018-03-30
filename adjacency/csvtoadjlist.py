import pandas as pd

df=pd.read_csv('adjmatrix.csv', sep=',',header=None, dtype=object)

adjlist = {}

rowlen = df.shape[0]

for i in range(1, rowlen):
	print(i)
	adjlist[df[i][0]] = []
	for j in range(1, rowlen):
		if df[i][j] == "1":
			adjlist[df[i][0]].append(df[0][j])

for item in adjlist:
	print(item, end=" ")
	for adj in adjlist[item]:
		print(adj, end=",")
	print()