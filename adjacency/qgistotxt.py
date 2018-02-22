import csv
from itertools import islice

with open("pa_nghbr.csv", newline="") as csvfile:
	nghbrs = csv.reader(csvfile, delimiter=',')
	quick = True
	q2 = True
	firstRow = True
	for row in nghbrs:
		#col 3: id; col 161: neighboring ids

		#don't print first row
		if firstRow:
			firstRow = False
		else:
			print(row[3] + " " + row[161])