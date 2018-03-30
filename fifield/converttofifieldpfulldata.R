library(redist)
library(spdep)

intermediateadjlist = scan(file="pfulladjlist.txt", what="string", sep="\n")
intermediateadjlist2 = lapply(intermediateadjlist, strsplit, " ")
intermediateadjlist3 = lapply(intermediateadjlist2, "[[", 1)
adjlist = lapply(intermediateadjlist3, as.numeric)
attr(adjlist, "class") <- "nb"
attr(adjlist, "region.id") <- c("0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                                "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
                                "20", "21", "22", "23", "24")
attr(adjlist, "type") <- "rook"
attr(adjlist, "sym") <- TRUE

pdata = read.csv(file="pfullpdata.csv", sep=",")
dmatintermediate = read.csv(file="dmat2.csv", sep=",", header=FALSE)
dmat = as.matrix(dmat)

initcds <- algdat.pfull$cdmat[,sample(1:ncol(algdat.pfull$cdmat), 1)]

cdmat = algdat.pfull$cdmat
cdmat = cdmat[,1]
cdmatlist = scan(file="cdmat.txt", what=integer(), sep="\n")

myout=redist.mcmc(adjobj = adjlist,
                  popvec = pdata$pop,
                  ndists = 3,
                  ssdmat = dmat,
                  initcds = initcds,
                  nsims = 500)
