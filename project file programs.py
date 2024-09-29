# note find how to take input of database name???
#connection
import mysql.connector
login1 = input("Enter user ")
login2 = input("enter  password")
if login1 == "user" and login2 == "password":
    mydb = mysql.connector.connect(host="localhost",user="user",password="password")
    mycursor = mydb.cursor()
elif login2 != "password" :
    print("wrong password")
else:
    print("Wrong Usename")


#creates the database
databasename = input("enter database name :")
mycursor.execute("create database %s ;" %databasename)
print("Database created") 
"""
while True :
    #takes input if the user is student or teacher
    a = input("Please Choose from the below \n a.) Teacher \n b.) Student \n enter choise here :")  
    if a == "a" :
        print("1.) Create Table \n 2.) Enter Result \n 3.) Update result  \n 4.)View request for Rechecking ")
        k = int(input("Enter choice :"))
        if k == 1:

            #makes tables(for teacher )
            table_name =  input("enter table name")
            mycursor.execute("

        elif k == 2 :
            
    #shows the result of the concerned student
    #request rechecking (for student)
    #enter the result (for teacher )
    #update grades (for teacher)
    #

"""
