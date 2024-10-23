# note find how to take input of database name???
#connection
import mysql.connector 
login1 = input("Enter user ")
login2 = input("enter  password")
if login1 == "user" and login2 == "password":
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin"
)
elif login2 != "password" :
    print("wrong password")
else:
    print("Wrong Usename")

while True :
    #takes input if the user is student or teacher
    a = input("Please Choose from the below \n a.) Teacher \n b.) Student \n enter choise here :")  
    if a == "a" :
        print("1.) Create Table \n 2.) Enter Result \n 3.) Update result  \n 4.)View request for Rechecking \n 5.) Create database  ")
        k = int(input("Enter choice :"))
        if k == 1:

            #makes tables(for teacher )
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

        elif k == 5 :
            #creates the database
            databasename = input("enter database name :")
            mycursor.execute("create database %s ;" %databasename)
            mycursor.execute("use %s  ;" %databasename)
            print("Database created")

    elif a == "b":
        student_choice =int(input("Please Choose from the below \n 1.) show result  \n 2.) request rechecking \n enter choise here : "))
        if student_choice == 1 :
            #shows the result of the concerned student
            enter_rollno = int(input("Enter your roll no. : "))
            enter_class = input("Enter your class : ")
            mycursor.execute("select * from class"+enter_class + " where roll_no ="+enter_rollno)
            

 


            
    
    #request rechecking (for student)
    #enter the result (for teacher )
    #update grades (for teacher)
    #

