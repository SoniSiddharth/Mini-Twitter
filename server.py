import socket
import os
import time
import pickle
import mysql.connector
import lepl.apps.rfc3696

class authenticate:
    def __init__(self,username, password):
        self.username = username
        self.password = password

class signup:
    def __init__(self, username, password,name,email):
        self.username = username
        self.password = password
        self.email = email
        self.name = name

class tweet_info():
    def __init__(self, message, hashtags):
        self.message = message
        self.hashtags = hashtags

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
port = int(input('Enter desired port --> '))

server_socket.bind((ip,port))

server_socket.listen(100)
BUFFERSIZE = 64000
print('Running on IP: '+ip)
print('Running on port: '+str(port))

# Connecting with database
mydb = mysql.connector.connect(host="localhost",
                                user="root",
                                password="123456789",
                                database="Minitweet",
                                )

def SignUp(conn, addr):
    data = conn.recv(BUFFERSIZE)
    credentials = pickle.loads(data)
    username = credentials.username
    password = credentials.password
    email = credentials.email
    name = credentials.name
    # emailchecker = lepl.apps.rfc3696.Email()
    # if not emailchecker(email):
    #     return "Invalid email"
    if len(password)<3:
        return "Bad password"
    
    query = "INSERT INTO Users (Username, Password, Email, Name) VALUES (%s, %s, %s, %s)"
    val = (username, password, email, name)
    mycursor = mydb.cursor()
    mycursor.execute(query, val)
    mydb.commit()
    return "Done"

def Authenticate(conn,addr):
    print("Authentication....")
    data = conn.recv(BUFFERSIZE)
    credentials = pickle.loads(data)
    print(credentials.username)
    print(credentials.password)
    # query = ("SELECT * FROM Users )

def NewTweet(conn, addr):
    data = conn.recv(BUFFERSIZE)
    message = pickle.loads(data)
    
    
def DeleteFollower(conn, addr):
    print("Deleting follower")

def Decode(msg,conn,addr):
    if msg[0] =="a":
        Authenticate(conn,addr)
    if msg[0] == "n":
        NewTweet(msg,conn,addr)
    if msg[0] == "d":
        DeleteFollower(conn,addr)
    


while True:
    conn, addr = server_socket.accept()
    print(conn)
    data = conn.recv(BUFFERSIZE)
    received_msg = data.decode('ascii')
    print("message received is ", received_msg)

    Decode(received_msg,conn,addr)
    response = "Welcome to the Mini Twitter"
    data = response.encode('ascii')
    conn.send(data)

    result = SignUp(conn, addr)
    print(result)

    conn.shutdown(socket.SHUT_RDWR)
    conn.close()
server_socket.close()
