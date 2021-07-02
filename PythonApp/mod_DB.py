# import package - pymongo
import pymongo

# define function - fMod_DB
def fMod_DB(nParMongoClient):
	# instantiate the object - Database
	nInsObjDB=pymongo.database.Database(nParMongoClient,"proj20DB")
	return nInsObjDB