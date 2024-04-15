#!/usr/bin/python3
'''
a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
'''
import sys
import MySQLdb

if __name__ == "__main__":
    myDb = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])

    myCursor = myDb.cursor()
    myCursor.execute("SELECT * FROM states WHERE binary name=%s\
                     ORDER BY id", (sys.argv[4],))

    states = myCursor.fetchall()
    for state in states:
        print(state)

    myCursor.close()
    myDb.close()
