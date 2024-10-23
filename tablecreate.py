import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database = "test"
)
mycursor = mydb.cursor()
table_name=input("Enter Table Name:\t")
column=input("Enter first Column:\t")
datatype=input("Enter Datatype:\t")
constraint=input("Enter Constraint:\t")
mycursor.execute("CREATE TABLE " + table_name + "(" + column +" "+ datatype +" "+ constraint + ")")
while True:
    a = int(input("do you wish to add more columns y/n"))
    if a == "y":
        column=input("Enter first Column:\t")
        datatype=input("Enter Datatype:\t")
        constraint=input("Enter Constraint:\t")
        mycursor.execute("alter table " + table_name + "add " + column +" "+ datatype +" "+ constraint)
    elif a=="n":
        break
mycursor.commit()