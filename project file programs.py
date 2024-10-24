#connection
import mysql.connector 
login1 = input("Enter user ")
login2 = input("enter  password")
if login1 == "user" and login2 == "password":
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin")
    mycursor = mydb.cursor
elif login2 != "password" :
    print("wrong password")
else:
    print("Wrong Usename")

while True :
    #takes input if the user is student or teacher
    a = input("Please Choose from the below \n a.) Teacher \n b.) Student \n enter choise here :")  
    if a == "a" :
        print("1.) Create database  \n 2.) Create table  \n 3.) Enter Result \n 4.) Update result  \n 5.)View request for Rechecking  ")
        k = int(input("Enter choice :"))
        if k == 2:

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
            mydb.commit()

        elif k == 1 :
            #creates the database
            databasename = input("enter database name :")
            mycursor.execute("create database %s ;" %databasename)
            mycursor.execute("use %s  ;" %databasename)
            print("Database created")
        elif k == 3:
            #enter the result (for teacher )
            g = input("enter table name you wish to enter record in : ")


        elif k == 4:
            #update grades (for teacher)
            c = input("enter class of student ")
            h = input("enter rollno of student: ")
            f = input("enter what to update ")
            d = input("enter new value ")
            mycursor.execute("update table class"+c+ " set "+f +" = "+d+ " where rollno = "+h )
            mydb.commit()


        elif k== 5 :
            mycursor.execute("slelect * form rechecking ")
            rec = mycursor.fetchall()
            for i in rec :
                print(i)



    elif a == "b":
        student_choice =int(input("Please Choose from the below \n 1.) show result  \n 2.) request rechecking \n enter choise here : "))
        if student_choice == 1 :
            #shows the result of the concerned student
            enter_rollno = int(input("Enter your roll no. : "))
            enter_class = input("Enter your class : ")
            mycursor.execute("select * from class"+enter_class + " where roll_no ="+enter_rollno)
            rec = mycursor.fetchall()
            for i in rec :
                print(i)
        elif student_choice == 2 :
             #request rechecking (for student)
            j = input("enter rollno : ")
            k = input ("enter subject : ")
            mycursor.execute("insert into rechecking values("+j +","+k+" )")