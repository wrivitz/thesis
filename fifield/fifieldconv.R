library(redist)
library(spdep)

intermediateadjlist = scan(file="adjlist.txt", what="string", sep="\n")
intermediateadjlist2 = lapply(intermediateadjlist, strsplit, " ")
intermediateadjlist3 = lapply(intermediateadjlist2, "[[", 1)
adjlist = lapply(intermediateadjlist3, as.numeric)
attr(adjlist, "class") <- "nb"
attr(adjlist, "region.id") <- paste(seq(0, length(adjlist)-1))
attr(adjlist, "type") <- "rook"
attr(adjlist, "sym") <- TRUE

pdata = read.csv(file="pdata.csv", sep=",")
dmatintermediate = read.csv(file="dmat.csv", sep=",", header=FALSE)
dmat = as.matrix(dmat)

initcd = scan(file="initdistrict.txt", what=integer(), sep="\n")

myout=redist.mcmc(adjobj = adjlist,
                  popvec = pdata$pop,
                  ndists = 3,
                  ssdmat = dmat,
                  initcd = initcd,
                  nsims = 500)