#!/usr/bin/python3
'''Module to execute functions'''
import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=(sys.argv[1]), port=3306, passwd=(sys.argv[2]), db=(sys.argv[3]))
    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON state_id=states.id ORDER BY cities.id ASC;")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
