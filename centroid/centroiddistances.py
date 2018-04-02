import fileinput
import math

centroids = []

for line in fileinput.input():
	points = line.replace("(", "").replace(")", "").split(" ")
	centroids.append([float(points[1]), float(points[2])])

for i in range(0, len(centroids)):
	x1 = centroids[i][0]
	y1 = centroids[i][1]
	for j in range(0, len(centroids)):
		x2 = centroids[j][0]
		y2 = centroids[j][1]
		print(math.sqrt((x2 - x1)**2 + (y2 - y1)**2 ), end="")
		print(",", end="")
	print()