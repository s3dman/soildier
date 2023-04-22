from dbhandler import ReadDB, WriteDB


def checkOptimality(cropname):
    db = ReadDB("CROPDATA")
    if cropname in db:
        return db[cropname]
    return -1


def isPreexist(cropname):
    db = ReadDB("CROPDATA")
    if cropname in db:
        return 1
    return 0


def addOptimality(cropname, data):
    db = ReadDB("CROPDATA.DB")
    db[cropname] = data
    WriteDB(db, "CROPDATA.DB")


def delCrop(cropname):
    db = ReadDB("CROPDATA")
    del db[cropname]


def getCrops(crop=None):
    if crop == None:
        return ReadDB("CROPDATA.DB")
    return ReadDB("CROPDATA.DB")[crop]
