import mysql.connector

mydb = mysql.connector.connect(
user='root',
password='password',
host='127.0.0.1', 
database='sinialo',
auth_plugin='mysql_native_password')

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)
