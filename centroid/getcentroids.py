#from https://gis.stackexchange.com/questions/113799/how-to-read-a-shapefile-in-python/113808
import shapefile
from shapely.geometry import shape

shapeRecords = shapefile.Reader("pa_final.shp").shapeRecords()

for shp in shapeRecords:
	interface = shp.shape.__geo_interface__
	shp_geom = shape(interface)
	print(shp_geom.centroid)