import sys
import numpy as np
import pandas as pd 

def setIds(data, adj, size):
	for i in range(1, size+1):
		dist = data[i].split(" ")
		index = int(dist[0])+1
		adj[0][index] = dist[1].strip()
		adj[index][0] = dist[1].strip()

def createAdj(data, adj, size):
	for i in range(size+1, len(data)):
		pair = data[i].split(" ")
		d1 = int(pair[0].split(",")[0].strip("()")) + 1
		d2 = int(pair[1].split(",")[0].strip("()")) + 1
		adj[d1][d2] = "1"
		adj[d2][d1] = "1"

def fillAdj(adj):
	for i in range(0, adj.shape[0]):
		for j in range(0, adj.shape[1]):
			adj[i][j] = "0"

data = sys.stdin.readlines()

size = int(data[0])
adj = np.empty((size+1, size+1), dtype=object)

fillAdj(adj)

setIds(data, adj, size)

createAdj(data, adj, size)

df = pd.DataFrame(adj)
df.to_csv("adjmatrix.csv", header=None, index=None)