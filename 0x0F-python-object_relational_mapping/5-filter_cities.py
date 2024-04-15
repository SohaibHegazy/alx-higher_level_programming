#!/usr/bin/python3
'''
a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
'''
import sys
import MySQLdb

if __name__ == "__main__":
    myDb = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])

    myCursor = myDb.cursor()
    myCursor.execute("SELECT cities.name FROM cities INNER JOIN states\
                     ON cities.state_id = states.id WHERE states.name=%s\
                     ORDER by cities.id", (sys.argv[4],))

    cityList = []
    cities = myCursor.fetchall()
    for city in cities:
        cityList.append(city[0])
    print(", ".join(cityList))

    myCursor.close()
    myDb.close()
