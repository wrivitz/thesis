import csv
from itertools import islice

with open("adjmatrix.csv", newline="") as csvfile:
	reader = csv.reader(csvfile, delimiter=",")
	for row in reader:
		print(len(row))