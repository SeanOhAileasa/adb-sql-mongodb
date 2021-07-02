# import package - pymongo
import pymongo

# define function - fMod_Insert
def fMod_Insert(nParCollection,nParID,nParName,nParLevel):
	return nParCollection.insert_one({"_id":nParID,"name":nParName,"level":nParLevel})