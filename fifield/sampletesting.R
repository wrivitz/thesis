## Load data
library(redist)
data(algdat.pfull)

## Run the simulations
mcmc.out <- redist.mcmc(adjobj = algdat.pfull$adjlist,
                        popvec = algdat.pfull$precinct.data$pop,
                        nsims = 10000,
                        ndists = 3)

partitions = mcmc.out$partitions
write.table(partitions, file="partitiontable.csv")