import pandas as pd

qgis=pd.read_csv('sortedqgisadj.csv', sep=',',header=0, index_col=0, dtype=object)
pyshp = pd.read_csv('sortedadj.csv', sep=',',header=0, index_col=0, dtype=object)

for i in range(1, qgis.shape[1]):
	if (qgis[i][0] != pyshp[i][0]):
		print("Horizontal: " + str(i))

for i in range(1, qgis.shape[1]):
	if (qgis[0][i] != pyshp[0][i]):
		print("Vertical: " + str(i))