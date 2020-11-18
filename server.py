import socket
import os
import time
import pickle
import pyodbc

class authenticate:
    def __init__(self,username, password):
        self.username = username
        self.password = password

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
port = int(input('Enter desired port --> '))

server_socket.bind((ip,port))

server_socket.listen(100)
BUFFERSIZE = 64000
print('Running on IP: '+ip)
print('Running on port: '+str(port))

# Connecting with database
cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=UKXXX00123,45600;"
            "Database=DB01;"
            "UID=JoeBloggs;"
            "PWD=Password123;")

cnxn = pyodbc.connect(cnxn_str)


def Authenticate(conn,addr):
    print("Authentication....")
    data = conn.recv(BUFFERSIZE)
    credentials = pickle.loads(data)
    print(credentials.username)
    print(credentials.password)
    query = ("SELECT * FROM Users "
         f"WHERE Username = '{date}'")

def NewTweet(msg,conn,addr):
    print("New Tweet")
    
    
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




    conn.shutdown(socket.SHUT_RDWR)
    conn.close()
server_socket.close()
