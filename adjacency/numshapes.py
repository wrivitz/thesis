import shapefile

sf = shapefile.Reader("pa_final.shp")
shapes = sf.shapes()

print(len(shapes))