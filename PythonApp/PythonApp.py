import worldDB
import mod_MongoClient
import mod_DB
import mod_MyCollection
import mod_Find
# module - mod_Insert - funcion fMod_Insert - access
from mod_Insert import fMod_Insert

# define function - main
def main():
    while True: # infinite

        # function fDisplayMenu - call
        fDisplayMenu()
        nChoice=input("Choice: ")

        if (nChoice=="1"):
            # function worldDB.fViewPeople - call
            nViewPeople=worldDB.fViewPeople()

            for i in range(0, len(nViewPeople), 2):
                for row in nViewPeople[i:i+2]:
                    print(row["personID"],":",  row["personname"], ":", row["age"])
            #
            #
            # help via 
            # https://stackoverflow.com/questions/61459744/pymysql-cursor-fetch-multiple-rows
            #
            #
                nQuit=input("--Quit <q>--")
                if (nQuit=="q"): 
                    break # exit
        #
        #
        # progress to next round of output via enter key only!
        #   > if possible would like to know how to proceed with any key press 
        #   was going to use something like:- https://pypi.org/project/keyboard/  
        #   assuming this is not what you are looking for?
        #
        #    

        elif (nChoice=="2"):
            # function fGetIndepYear - call
            nIndepYear=fGetIndepYear()
            # function - worldDB.fViewCountriesIndepYear - call
            nViewCountriesIndepYear=worldDB.fViewCountriesIndepYear(nIndepYear)
            print("")
            for nEachRow in nViewCountriesIndepYear:
                # db - rows - columns - Name - Continent - IndepYear
                print(nEachRow["Name"]," ¦ ",
                    nEachRow["Continent"]," ¦ ",
                    nEachRow["IndepYear"] )

        elif (nChoice=="3"):
            print("")
            print("Add New Person")
            print("-"*14)
            # function fGetPersonName - call
            nPersonName=fGetPersonName()
            # function fGetPersonAge - call            
            nPersonAge=fGetPersonAge()
            try:
                # function - worldDB.fAddNewPerson - call
                nAddNewPerson=worldDB.fAddNewPerson(nPersonName,nPersonAge)
            except:
                print("***ERROR***:",nPersonName,"already exists")

        elif (nChoice=="4"):
            # function fGetCountry - call
            nCountry=fGetCountry()
            # function - worldDB.fViewCountryByName - call
            nViewCountryByName=worldDB.fViewCountryByName(nCountry)
            for nEachRow in nViewCountryByName:
            # db - rows - columns - Name - Continent - Population - HeadOfState
                print(nEachRow["Name"]," ¦ ",
                    nEachRow["Continent"]," ¦ ",
                    nEachRow["Population"]," ¦ ",
                    nEachRow["HeadOfState"] )
        #
        #
        # NOTES: option 4 and 5 - OUTSTANDING - NOT SURE!
        #   if possible would like to know how to proceed? 
        #
        #

        elif (nChoice=="5"):
            print("")
            print("Countries By Pop")
            print("-"*16)
            # function fGetComparisonOperator - call
            nComparisonOperator=fGetComparisonOperator()
            while True:
                if (nComparisonOperator=="<" or nComparisonOperator==">" or nComparisonOperator=="="):
                    # function fGetCountryByPopTotal - call
                    nCountryPopTotal=fGetCountryByPopTotal()
                    # function - worldDB.fViewCountryByPop - call
                    nViewCountryByPop=worldDB.fViewCountryByPop(nComparisonOperator,nCountryPopTotal)
                    for nEachRow in nViewCountryByPop:
                    # db - rows - columns - Code - Name - Continent - Population
                        print(nEachRow["Code"]," ¦ ",
                            nEachRow["Name"]," ¦ ",
                            nEachRow["Continent"]," ¦ ",
                            nEachRow["Population"] )
                    break
                else:
                    nComparisonOperator=fGetComparisonOperator()
        #
        #
        # NOTES: option 4 and 5 - OUTSTANDING - NOT SURE!
        #   if possible would like to know how to proceed? 
        #
        #

        elif (nChoice=="6"):
            # function mod_MongoClient.fMod_MongoClient - call
            nMongoD=mod_MongoClient.fMod_MongoClient()
            # function mod_DB.fMod_DB - call
            nDB=mod_DB.fMod_DB(nMongoD)
            nSeekCollection="docs"
            # function mod_MyCollection.fMod_MyCollection - call
            nObtainCollection=mod_MyCollection.fMod_MyCollection(nDB,nSeekCollection)   
            # function fGetAddress - call
            nGetAddress=fGetAddress()
            # function mod_Find.fMod_FindAddress - call
            nDocuments=mod_Find.fMod_FindAddress(nObtainCollection,nGetAddress)
            for nEachDocument in nDocuments:
                try:
                    print(nEachDocument["_id"]," ¦ ",
                    nEachDocument["details"]["name"]," ¦ ",
                    nEachDocument["details"]["age"]," ¦ ",nEachDocument["qualifications"])
                except:
                    print(nEachDocument["_id"]," ¦ ",
                    nEachDocument["details"]["name"]," ¦ ",
                    nEachDocument["details"]["age"])

        elif (nChoice=="7"):
            # function mod_MongoClient.fMod_MongoClient - call
            nMongoD=mod_MongoClient.fMod_MongoClient()
            # function mod_DB.fMod_DB - call
            nDB=mod_DB.fMod_DB(nMongoD)
            nSeekCollection="docs"
            # function mod_MyCollection.fMod_MyCollection - call
            nObtainCollection=mod_MyCollection.fMod_MyCollection(nDB,nSeekCollection)
            # function fGetCourseID - call
            nGetCourseID=fGetCourseID()
            # function fGetCourseName - call
            nGetCourseName=fGetCourseName()
            # function fGetCourseLevel - call
            nGetCourseLevel=fGetCourseLevel()
            try:
                # function fMod_Insert - call
                fMod_Insert(nObtainCollection,nGetCourseID,nGetCourseName,nGetCourseLevel)
            except Exception as nE:
                print("*** ERROR ***: _id",nGetCourseID,"already exists")
        
        if (nChoice=="x"):
            break # exit

# define function - fDisplayMenu
def fDisplayMenu():
    print("")
    print("World DB")
    print("-"*8)
    print("")
    print("MENU")
    print("=" * 4)
    print("1 - View People")
    print("2 - View Countries by Independence Year")
    print("3 - Add New Person")
    print("4 - View Countries by name")
    print("5 - View Countries by population")
    print("6 - Find Students by Address")
    print("7 - Add New Course")
    print("x - Exit Application")

# define function - fGetIndepYear
def fGetIndepYear():
    print("")
    print("Countries By Independence Year")
    print("-"*30)
    return int(input("Enter Year : "))
    print("")

# define function - fGetPersonName
def fGetPersonName():
    return input("Name : ")

# define function - fGetPersonAge
def fGetPersonAge():
    return int(input("Age : "))

# define function - fGetCountry
def fGetCountry():
    print("")
    print("Countries By Name")
    print("-"*17)
    return input("Enter Country Name : ")

# define function - fGetCountryByPopOp
def fGetComparisonOperator():
    return input("Enter < > or = : ")

# define function - fGetCountryByPopTotal
def fGetCountryByPopTotal():
    return int(input("Enter population : "))

# define function - fGetAddress
def fGetAddress():
    print("")
    print("Find Students by Address")
    print("-"*24)
    return input("Enter Address : ")

# define function - fGetCourseID
def fGetCourseID():
    print("")
    print("Add New Course")
    print("-"*14)
    return input("_id : ")

# define function - fGetCourseName
def fGetCourseName():
    return input("Name : ")

# define function - fGetCourseLevel
def fGetCourseLevel():
    return int(input("Level : "))

# define function - fCheckConnection
def fCheckConnection():
    try:
        print("<mongod> 1:",mod_MongoClient.fMod_MongoClient())
        # functions mod_MongoClient.fMod_MongoClient, fMod_DB - call
        print("    <db> 2:",fMod_DB(mod_MongoClient.fMod_MongoClient()))
    except Exception as nE:
        print("Error",nE)

# keyword - __name__ - evaluate current module [1]
if __name__=="__main__":
    # function main - call
    main()