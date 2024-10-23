import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database = "test"
)

mycursor = mydb.cursor()
