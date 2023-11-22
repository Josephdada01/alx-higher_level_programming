#!/usr/bin/python3 
""" 
Once again, write a script that takes in arguments
and displays all values in the states table of hbtn_0e_0_usa
where name matches the argument. But this time, write
one that is safe from MySQL injections!
Your script should take 4 arguments: mysql username,
mysql password, database name and state name searched
(safe from MySQL injection)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on
localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""
  
  
import MySQLdb 
from sys import argv


if __name__ == "_main_":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name_searched = argv[4]

    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name,
            )
    cursor = connection.cursor()
    query = "SELECT id, name FROM states WHERE BINARY name = %s;"
    cursor.execute(query, (state_name_searched,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()
