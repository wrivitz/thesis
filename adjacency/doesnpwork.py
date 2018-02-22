import csv

with open('qgisadjmatrix.csv', 'r') as csvfile:
	rdr = csv.reader(csvfile, delimiter=',')
	i = 0
	for row in rdr:
		for item in row:
			if (item == "1"):
				i += 1

	print("qgis: " + str(i))

with open('adjmatrix.csv', 'r') as csvfile:
	rdr = csv.reader(csvfile, delimiter=',')
	i = 0
	for row in rdr:
		for item in row:
			if (item == "1"):
				i += 1

	print("pyshp: "  + str(i))