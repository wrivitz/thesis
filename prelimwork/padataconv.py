from dbfread import DBF
import sys
import csv

table = DBF("PA.dbf")
with open("PAData.csv", "w") as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(table.field_names)
	for record in table:
		writer.writerow(list(record.values()))