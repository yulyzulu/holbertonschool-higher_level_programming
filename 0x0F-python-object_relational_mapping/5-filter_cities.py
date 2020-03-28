#!/usr/bin/python3
'''Module to execute functions'''
import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=(sys.argv[1]), port=3306, passwd=(sys.argv[2]), db=(sys.argv[3]))
    c = db.cursor()
    c.execute("SELECT cities.name FROM cities INNER JOIN states ON state_id=states.id WHERE states.name = %s ORDER BY cities.id ASC;", (sys.argv[4],))
    rows = c.fetchall()
    for row in rows:
        print("{}, ".format(row[0]), end="")
    print()
    c.close()
    db.close()
