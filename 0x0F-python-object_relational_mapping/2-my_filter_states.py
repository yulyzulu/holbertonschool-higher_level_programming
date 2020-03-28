#!/usr/bin/python3
'''Module to execute functions'''
import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=(sys.argv[1]), port=3306, passwd=(sys.argv[2]), db=(sys.argv[3]))
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC".format(sys.argv[4]))
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
