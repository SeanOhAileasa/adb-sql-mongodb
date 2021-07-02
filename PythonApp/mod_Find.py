# import package - pymongo
import pymongo

# define function - fMod_FindAddress
def fMod_FindAddress(nParCollection,nParAddress):
	return nParCollection.find({"details.address":nParAddress},
		{"_id":1,"details.name":int(1),"details.age":int(1),"qualifications":int(1)})