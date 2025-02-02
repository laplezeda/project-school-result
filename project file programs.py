# Login and connection
import mysql.connector
print("-"*50) 
print("LOGIN  :")
login1 = input("Enter user : ")
login2 = input("enter  password : ")
print("-"*50)

if login1 == "user" and login2 == "password":
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin")
    mycursor = mydb.cursor()

else:
    print("Wrong Username or password")

while login1 == "user" and login2 == "password" :
    
    #takes input if the user is student or teacher
    
    print("-"*50)  
    print("Please Choose from the below")
    print("a.) Teacher")
    print("b.) Student")
    print("c.) Exit ")
    print("-"*50)

    a = input("Enter choice here :")
    if a == "a" :
        
        print("-"*50)
        print("1.) Create database")
        print("2.) Create table ")
        print("3.) Enter Result ")
        print("4.) Update result")
        print("5.) Delete a record in table")
        print("6.) Delete a table ")
        print("7.) View request for Rechecking ")
        print("8.) Display structure of a table  ")
        print("9.) Delete a database")
        print("10.) Display no. of records in a table ")
        print("11.) Display the tables in a database ")
        print("12.) Exit ")
        print("-"*50)

        k = int(input("Enter choice :"))
        
        if k == 1 :
            
            #creates the database
            
            databasename = input("enter database name :")
            mycursor.execute("create database %s ;" %databasename)
            mycursor.execute("use %s  ;" %databasename)
            print("Database created")
            mydb.commit()
        
        elif k == 2:

            #Creates custum tables accordings to the specific needs 
            
            s = input("Enter the database you wish to use ")
            mycursor.execute("use "+ s)
            table_name=input("Enter Table Name:\t")
            column=input("Enter first Column:\t")
            datatype=input("Enter Datatype:\t")
            constraint=input("Enter Constraint:\t")
            mycursor.execute("CREATE TABLE " + table_name + "(" + column +" "+ datatype +" "+ constraint + ")")
            
            while True:
                a = input("do you wish to add more columns y/n")
                
                if a == "y":
                    column=input("Enter  Column Name:\t")
                    datatype=input("Enter Datatype:\t")
                    constraint=input("Enter Constraint:\t")
                    mycursor.execute("alter table " + table_name + " add " + column +" "+ datatype +" "+ constraint)
                elif a=="n":
                    break
            mydb.commit()

        elif k == 3:
            
            #enter the result (for teacher )

            s = input("Enter the database you wish to use ")
            g = input("Enter table name you wish to enter record in : ")
            
            while True :
                e = input("Enter values seperated by comma : ")
                mycursor.execute("use "+ s)
                mycursor.execute("insert into " + g + " values(" + e + " )")
                mydb.commit()
                j = input("do you wish to add more records y/n")
                if j == "n" :
                    break


        elif k == 4:
            #update records (for teacher)
            s = input("Enter the database you wish to use ")
            c = input("Enter class of student ")
            h = input("Enter rollno of student: ")
            f = input("Enter what to update ")
            d = input("Enter new value ")
            
            mycursor.execute("use "+ s)
            mycursor.execute("update class_"+c+ " set "+f +" = "+d+ " where roll_no = "+h )
            mydb.commit()


        elif k == 5 :

            #To delete a record

            s = input("Enter the database you wish to use ")
            c = input("Enter class of student ")
            h = input("Enter rollno of student: ")
            
            mycursor.execute("use " + s)
            mycursor.execute("delete from class_"+ c + " where roll_no = "+h ) 
            mydb.commit()

        elif k == 6 :

            #To delete a Table 

            s = input("Enter the database you wish to use ")
            c = input("Enter the name of table ")

            mycursor.execute("use " + s)
            mycursor.execute("drop table "+ c)
            mydb.commit()

        
        elif k== 7 :
            
            # to view rechecking table 
            mycursor.execute("use rechecking")
            mycursor.execute("Select * from rechecking ")
            rec = mycursor.fetchall()
            for i in rec :
                print(i)
        

        elif k == 8 :
            
            # to view the structure of a table 
            
            s = input("Enter the database you wish to use ")
            q = input("Enter the name of the table :  ")
            mycursor.execute("use "+ s)
            mycursor.execute("describe "+ q)            
            rec = mycursor.fetchall() 
            for i in rec:
                print(i)
        
        elif k == 9 :

            #To delete a database

            s = input("Enter the database you wish to Delete  ")
            mycursor.execute("Drop database " + s)
            mydb.commit()     

        elif k == 10 : 
            
            # To count the no of records in a table 

            s = input("Enter the database you wish to use ")
            c = input("Enter Name of table ")
            
            mycursor.execute("use "+ s)
            mycursor.execute("select count(*) from " + c)
            rec = mycursor.fetchone()
            print(rec[0])

        elif k == 11 : 

            # To display the tables in a database

            s = input("Enter the database you wish to use ")

            mycursor.execute("use "+ s)
            mycursor.execute("show tables ")
            rec = mycursor.fetchall()
            for i in rec:
                print(i)
                
        elif k == 12 : 
            break

        else :
            print("Enter a valid choice ")
    
    elif a == "b":
        print("-"*50)
        print("Please Choose from the below")
        print("1.) Show result ")
        print("2.) Request rechecking ")
        print("4.) Exit")
        print("-"*50)
        student_choice =int(input("Enter choice here : "))
        
        
        if student_choice == 1 :
            
            #shows the result of the concerned student
            mycursor.execute("use student_marks")
            enter_rollno = input("Enter your roll no. : ")
            enter_class = input("Enter your class : ")
            mycursor.execute("select * from class_"+enter_class +" where roll_no = "+enter_rollno)
            rec = mycursor.fetchall()
            for i in rec :
                print(i)
        
        
        elif student_choice == 2 :
            
            #request rechecking (for student)
            
            j = input("Enter rollno and subject seprated by comma : ")
            mycursor.execute("use rechecking")
            mycursor.execute("insert into rechecking values( "+ j+" )")
            mydb.commit()
        
        elif student_choice == 3 :
            break   
        
        else :
            print("Enter a valid choice ")
    
    elif a == "c" :
        break
    
    else :
        print("Enter a valid choice ")
