#!/usr/bin/python3
'''
a script that lists all cities from the database hbtn_0e_4_usa
'''
import sys
import MySQLdb

if __name__ == "__main__":
    myDb = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])

    myCursor = myDb.cursor()
    myCursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                     JOIN states ON cities.state_id = states.id ORDER by\
                     cities.id")

    cities = myCursor.fetchall()
    for city in cities:
        print(cities)

    myCursor.close()
    myDb.close()
