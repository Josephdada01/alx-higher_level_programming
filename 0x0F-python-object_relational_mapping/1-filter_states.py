#!/usr/bin/python3

import MySQLdb
import sys

"""
Write a script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa:
Your script should take 3 arguments: mysql username,
mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""


def list_states(username, password, hbtn_0e_0_usa):
    try:
        con = MySQLdb.connect(host='localhost', port=3306,
                              user=username, passwd=password,
                              db=hbtn_0e_0_usa)
        cr = con.cursor()
        """ executing query to retrive states that start b N & cr == cursor"""
        cr.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
        """ fetching the rows and displaying the results """
        states = cr.fetchall()
        for state in states:
            print(f"{state[0]}: {state[1]}")
        cr.close()
        con.close()
    except MySQLdb.Error as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    username, password, hbtn_0e_0_usa = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, hbtn_0e_0_usa)
