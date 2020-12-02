import mysql.connector
import socket

BUFFERSIZE = 64000
mydb = mysql.connector.connect(host="localhost",
                                user="root",
                                password="123456789",
                                database="Minitweet",
                                )

