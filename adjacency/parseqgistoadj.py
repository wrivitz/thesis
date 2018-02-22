import sys
import numpy as np
import pandas as pd

def buildKeys(data):
	d = {}
	for line in data:
		splitline = line.split(" ")
		d[splitline[0]] = set()

	return d

def populateDict(d, data):
	for line in data:
		currdist = line.split(" ")[0]
		adjdists = line.split(" ")[1].strip().split(",")
		for dist in adjdists:
			d[currdist].add(dist)

def mapDistToNumber(d):
	newdict = {}
	i = 0
	for item in d:
		newdict[item] = i
		i += 1

	return newdict

def fillAdj(adj):
	for i in range(0, adj.shape[0]):
		for j in range(0, adj.shape[1]):
			adj[i][j] = "0"

def setIds(adj, d):
	i = 1
	for item in d:
		adj[i][0] = item
		adj[0][i] = item
		i += 1

def createAdj(adj, adjdict, rowdict):
	for item in adjdict:
		d1 = int(rowdict[item])+1
		for adjitem in adjdict[item]:
			d2 = int(rowdict[adjitem])+1
			adj[d1][d2] = "1"
			adj[d2][d1] = "1"

def main():
	data = sys.stdin.readlines()
	size = len(data)

	#build dictionary's entries
	adjdict = buildKeys(data)

	populateDict(adjdict, data)

	rowdict = mapDistToNumber(adjdict)

	adj = np.empty((size+1, size+1), dtype=object)

	fillAdj(adj)

	setIds(adj, adjdict)

	createAdj(adj, adjdict, rowdict)

	df = pd.DataFrame(adj)
	df.to_csv("qgisadjmatrix.csv", header=None, index=None)

if __name__ == "__main__": main()