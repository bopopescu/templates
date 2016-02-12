from credentials import *
import mysql.connector

cnx = mysql.connector.connect(user=username, password=password, host=hostname)
cursor = cnx.cursor()

drop_query = 'DROP DATABASE trvmssdb;'

print(cursor.execute(drop_query))

cursor.close()
cnx.close()
