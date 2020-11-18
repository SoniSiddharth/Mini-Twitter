import socket
import os
from _thread import *
import threading
import pickle

# def Authenticate(username, password):
#     return 0
    
def NewTweet():
    pass
def DeleteFollower():
    pass
def LogOut():
    pass
def SearchPerson():
    pass

username = ""
password = ""

class authenticate:
    def __init__(self, username, password):
        self.username = username
        self.password = password


#opening twitter
print("Opening Twitter ...")
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
target_ip = "127.0.1.1"
target_port = input('Enter port --> ')
client_socket.connect((target_ip,int(target_port)))
BUFFERSIZE = 64000
message = "Hello"
client_socket.send(message.encode('ascii'))
reply_from_server = client_socket.recv(BUFFERSIZE)

if reply_from_server=="":
    print("Could not open application")
else:
    print(str(reply_from_server.decode('ascii')))    


while True:
    print("Enter your username, if want to exit application press -1")
    #new user session
    username = input()
    if username== "-1":
        break
    else:
        print("Enter your password")
        password = input()
        new_user = authenticate(username, password)
        data = pickle.dumps(new_user)
        client_socket.send(data)


        
        if 1==0:
            print("Invalid input")
            continue
        else:
            print("You are logged in successfully")
            print("Enter a for new Tweet")
            print("Enter b for searching a person")
            print("Enter c for deleting follower")
            print("Enter d for log out")
            while True:    
                query = input()
                if query =="a":
                    NewTweet()
                if query =="b":
                    SearchPerson()
                if query =="c":
                    DeleteFollower()
                if query == "d":
                    LogOut()
                else:
                    break

client_socket.close()


            


    
