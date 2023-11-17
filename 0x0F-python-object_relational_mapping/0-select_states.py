#!/usr/bin/python3

"""
a script that lists all states from the database hbtn_0e_0_usa:
Your script should take 3 arguments: mysql username, mysql
password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""
import MySQLdb
import sys


def list_states(username, password, hbtn_0e_0_usa):
    try:
        connection = MySQLdb.connect(host='localhost', port=3306, 
                                     user=username, passwd=password,
                                     db=hbtn_0e_0_usa)
        cursor = connection.cursor()
        """ executing query to retrive states sort by states by state.id"""

        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        """ fetching the rows and displaying the results """
        states = cursor.fetchall()
        for state in states:
            print(state)
        cursor.close()
        connection.close()
    except MySQLdb.Error as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    username, password, hbtn_0e_0_usa = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, hbtn_0e_0_usa)