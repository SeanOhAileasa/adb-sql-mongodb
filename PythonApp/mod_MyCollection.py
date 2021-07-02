# import package - pymongo
import pymongo

# define function - fMod_MyCollection
def fMod_MyCollection(nParDB,nParCollection):
	# instantiate the object - Collection
	nInsObjCollection=pymongo.collection.Collection(nParDB,nParCollection)
	return nInsObjCollection