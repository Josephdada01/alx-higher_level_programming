#!/usr/bin/pythom3
"""
Once again, write a script that takes in arguments and displays
all values in the states table of hbtn_0e_0_usa where name matches the
argument. But this time, write one that is safe from MySQL injections!

Your script should take 4 arguments: mysql username, mysql password,
database name and state name searched (safe from MySQL injection)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""


import MySQLdb
import sys


def search_state(username, password, database, state_name):
    """take 4 arguments: mysql username, mysql password,
    database name and state name searched
    """
    try:
        con = MySQLdb.connect(host='localhost', port=3306,
                              user=username, passwd=password, db=database)
        cursor = con.cursor()
        query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
        cursor.execute(query, (state_name,))
        """fetching the results"""
        states = cursor.fetchall()
        """displaying the results"""
        for state in states:
            print(state)
        cursor.close()
        con.close()
    except MySQLdb.Error as e:
        print(e)
        sys.exit(1)


if __name__ == '__main__':
    username, password, database, state_name = sys.argv[1], sys.argv[2],
    sys.argv[3], sys.argv[4]
    search_state(username, password, database, state_name)
