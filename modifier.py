from dbhandler import ReadDB, WriteDB
import math


def checkOptimality(cropname):
    db = ReadDB("CROPDATA.DB")
    if cropname in db:
        return db[cropname]
    return -1


def isPreexist(cropname):
    db = ReadDB("CROPDATA.DB")
    if cropname in db:
        return 1
    return 0


def addOptimality(cropname, data):
    db = ReadDB("CROPDATA.DB")
    db[cropname] = data
    WriteDB(db, "CROPDATA.DB")


def delCrop(cropname):
    db = ReadDB("CROPDATA.DB")
    del db[cropname]
    WriteDB(db, "CROPDATA.DB")


def getCrops(crop=None):
    if crop == None:
        return ReadDB("CROPDATA.DB")
    return ReadDB("CROPDATA.DB")[crop]


def getOptimalList(data):
    def sort_helper(k):
        return k[1]

    scoretable = []
    d = getCrops()
    for i in d:
        scoretable.append(
            (i, 1e4 / abs(sum([i**2 for i in d[i]]) - sum([i**2 for i in data])))
        )
    scoretable.sort(key=sort_helper, reverse=True)
    return scoretable
