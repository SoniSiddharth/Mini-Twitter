import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                                user="root",
                                password="123456789",
                                database="Minitweet",
                                )

query = "SELECT * FROM Users where Username='prasad' and Password='prasad'"
mycursor = mydb.cursor()
mycursor.execute(query)
result = mycursor.fetchall()
print(result)
print(type(result))
