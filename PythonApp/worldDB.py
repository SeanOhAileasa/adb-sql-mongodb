import pymysql

# define connection - name - conn
conn=None

# define function - fViewPeople
def fViewPeople():

    global conn
    conn=pymysql.connect(
        host="localhost",
        user="*",
        password="*",
        db="world",
        cursorclass=pymysql.cursors.DictCursor)

    nLocQuery="SELECT * FROM person"

    # close when finished
    with conn:
        # create object - cursor on connection
        cursor=conn.cursor()
        # execute sql - nQuery
        cursor.execute(nLocQuery)
        # return - cursor - all rows 
        nRows=cursor.fetchall()
        # return - caller function
        return nRows

# define function - fViewCountriesIndepYear
def fViewCountriesIndepYear(nParYear):

    global conn
    conn=pymysql.connect(
        host="localhost",
        user="*",
        password="*",
        db="world",
        cursorclass=pymysql.cursors.DictCursor)

    nLocQuery="SELECT Name,Continent,IndepYear FROM country WHERE IndepYear=%s"

    # close when finished
    with conn:
        # create object - cursor on connection
        cursor=conn.cursor()
        # execute sql - nQuery
        cursor.execute(nLocQuery,nParYear)
        # return - cursor - all rows 
        nRows=cursor.fetchall()
        # return - caller function
        return nRows

# define function - fAddNewPerson
def fAddNewPerson(nParName,nParAge):

    global conn
    conn=pymysql.connect(
        host="localhost",
        user="*",
        password="*",
        db="world",
        cursorclass=pymysql.cursors.DictCursor)

    # parameter - %s - %s -  nParName - nParAge
    nInsert="INSERT INTO person (personname,age) VALUES(%s,%s)"

    # close when finished
    with conn:
        # create object - cursor on connection
        cursor=conn.cursor()
        # execute sql - nQuery
        cursor.execute(nInsert,(nParName,nParAge))

# define function - fViewCountryByName
def fViewCountryByName(nParName):

    global conn
    conn=pymysql.connect(
        host="localhost",
        user="*",
        password="*",
        db="world",
        cursorclass=pymysql.cursors.DictCursor)

    nLocQuery="SELECT Name,Continent,Population,HeadOfState FROM country WHERE Name LIKE %s"

    # close when finished
    with conn:
        # create object - cursor on connection
        cursor=conn.cursor()
        # execute sql - nQuery
        cursor.execute(nLocQuery,("%"+nParName+"%"))
        # return - cursor - all rows 
        nRows=cursor.fetchall()
        # return - caller function
        return nRows

# define function - fViewCountryByPop
def fViewCountryByPop(nComparisonOperator,nCountryPopTotal):

    global conn
    conn=pymysql.connect(
        host="localhost",
        user="*",
        password="*",
        db="world",
        cursorclass=pymysql.cursors.DictCursor)

    # close when finished
    with conn:
        # create object - cursor on connection
        cursor=conn.cursor()
        cursor.execute("SELECT Code,Name,Continent,Population FROM country WHERE Population {} {}".
            format(nComparisonOperator,nCountryPopTotal))

        # return - cursor - all rows 
        nRows=cursor.fetchall()
        # return - caller function
        return nRows