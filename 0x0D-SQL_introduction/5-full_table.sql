-- script that prints the full description of the table 
--first_table from the database hbtn_0c_0 in your MySQL server.
USE hbtn_0c_0;

SELECT COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'first_table';