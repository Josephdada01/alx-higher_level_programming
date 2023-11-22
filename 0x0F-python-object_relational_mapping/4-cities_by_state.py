#!/usr/bin/python3
"""
Write a script that lists all cities from the database
hbtn_0e_4_usa
Your script should take 3 arguments: mysql username,
mysql password and database name
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port
3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""

import MySQLdb
import sys


def list_cities(username, password, hbtn_0e_4_usa):
    try:
        connection = MySQLdb.connect(host='localhost', port=3306,
                                     user=username, passwd=password,
                                     db=hbtn_0e_4_usa)
        cursor = connection.cursor()
        cursor.execute("SELECT cities.id, cities.name AS city_name,\
                states.name AS state_name FROM states INNER JOIN cities\
                ON state_id = states.id ORDER BY cities.id;")
        """Fetching the result"""
        cities = cursor.fetchall()
        for city in cities:
            print(city)
    except MySQLdb.Error as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    username, password, hbtn_0e_4_usa = sys.argv[1], sys.argv[2], sys.argv[3]
    list_cities(username, password, hbtn_0e_4_usa)
