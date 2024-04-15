#!/usr/bin/python3
'''
a script that lists all states with a name
starting with N (upper N) from the database
hbtn_0e_0_usa
'''
import sys
import MySQLdb

if __name__ == "__main__":
    myDb = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])

    myCursor = myDb.cursor()
    myCursor.execute("SELECT * FROM states WHERE name like binary 'N%'\
                     ORDER BY id")

    states = myCursor.fetchall()
    for state in states:
        print(state)

    myCursor.close()
    myDb.close()
