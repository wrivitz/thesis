attr(adjlistdev, "class") <- NULL
attr(adjlistdev, "region.id") <- NULL
attr(adjlistdev, "call") <- NULL
attr(adjlistdev, "type") <- NULL
attr(adjlistdev, "sym") <- NULL

lapply(adjlistdev, write, "pfulladjlist.txt", append=TRUE, ncolumns=1000)
write.csv(pdata, file="pfullpdata.csv")
write.table(dmatactual, file="dmat2.csv", row.names = FALSE, col.names = FALSE, sep=",")
