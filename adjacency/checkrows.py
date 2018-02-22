import csv

pyshpmatrix = csv.reader(open('adjmatrix.csv'), delimiter=",")
i = 0
for row in pyshpmatrix:
	i += 1

print(i)