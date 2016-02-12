from credentials import *
import mysql.connector

cnx = mysql.connector.connect(user=username, password=password, host=hostname)
cnx.start_transaction(isolation_level='SERIALIZABLE')
cursor = cnx.cursor()

num_rows = 30

initial_query = '''
CREATE DATABASE trvmssdb;
'''

cursor.execute(initial_query)
cnx.commit()
cursor.close()
cnx.close()

cnx = mysql.connector.connect(user=username, password=password, host=hostname, database='trvmssdb')
cnx.start_transaction(isolation_level='SERIALIZABLE')
cursor = cnx.cursor()

secondary_query = '''
CREATE TABLE work
(
row_index int,
column_index int,
status nvarchar(255),
best_match_index int
);
'''

cursor.execute(secondary_query)


insertions = (
    "INSERT INTO work (row_index, column_index, status, best_match_index) "
    "VALUES (%s, %s, %s, %s)"
)
for row_index in range(0, num_rows):
    for column_index in range(0, num_rows):
        data = (row_index, column_index, "todo", -1)
        #cur_insertions = insertions + '(' + str(row_index) + ',' + str(column_index) + ',' + '"todo",-1);'
        cursor.execute(insertions, data)

cnx.commit()
cursor.close()
cnx.close()
