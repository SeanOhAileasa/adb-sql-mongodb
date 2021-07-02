# import package - pymongo
import pymongo

# define connection - mongod
nInsObjMongoDeamon=None

# define function - fMod_MongoClient
def fMod_MongoClient():
	# accessible any function
	global nInsObjMongoDeamon

	# instantiate the object - MongoClient - default
	#nInsObjMongoDeamon=pymongo.mongo_client.MongoClient()

	# instantiate the object - MongoClient - alias
	nInsObjMongoDeamon=pymongo.MongoClient("localhost",port=27017)

	# check connection - mongod
	nInsObjMongoDeamon.admin.command("ismaster")
	return nInsObjMongoDeamon