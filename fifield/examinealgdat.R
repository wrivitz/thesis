library(redist)
data(algdat.pfull)

adjlist = algdat.pfull$adjlist
cdmat = algdat.pfull$cdmat
pdata = algdat.pfull$precinct.data
sindex = algdat.pfull$segregation.index
dmat = algdat.pfull$distancemat

dump("adjlist", file="pfulladjlist")
stripAttributes(adjlist)