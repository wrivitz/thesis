import shapefile
import copy

class DistPoint:
	def __init__(self, point, district, distid):
		self.x = point[0]
		self.y = point[1]
		self.district = district
		self.id = distid

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __lt__(self, other):
		return self.x < other.x

	def __repr__(self):
		return ("point = (" + str(self.x) + ", " + str(self.y) + "); district = " + \
			str(self.district) + "; id = " + str(self.id))

class DistPair:
	def __init__(self, d1, d2, d1id, d2id):
		self.d1 = d1
		self.d2 = d2
		self.d1id = d1id
		self.d2id = d2id

	def __eq__(self, other):
		return (self.d1 == other.d1 and self.d2 == other.d2) or \
			(self.d1 == other.d2 and self.d2 == other.d1)

	def __hash__(self):
		return hash(frozenset([self.d1, self.d2]))

	def __repr__(self):
		return ("(" + str(self.d1) + "," + str(self.d1id) + ") (" + \
			str(self.d2) + "," + str(self.d2id) + ")") 

def adjacencySet(points):
	distPairs = set()
	for i in range(0, len(points)-1):
		p1 = points[i]
		p2 = points[i+1]
		if p1 == p2 and p1.district != p2.district:
			distPairs.add(DistPair(p1.district, p2.district, p1.id, p2.id))
	return distPairs

def main():
	sf = shapefile.Reader("pa_final.shp")
	shapeRecs = sf.shapeRecords()

	points = []
	for i in range(0, len(shapeRecs)):
		for point in shapeRecs[i].shape.points:
			points.append(DistPoint(point, i, shapeRecs[i].record[3]))

	points.sort()
	distPairs = adjacencySet(points)

	print(len(shapeRecs))
	for i in range(0, len(shapeRecs)):
		print(str(i) + " " + str(shapeRecs[i].record[3]))
	for i in distPairs:
		print(i)

if __name__ == "__main__": main()