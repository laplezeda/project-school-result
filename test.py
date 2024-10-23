import mysql.connector as sqlconnect
con = sqlconnect.connect(username = "root",password = "admin",  host ="local host")
mycursor = con.cursor()

