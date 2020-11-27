import socket
import os
from _thread import *
import threading
import pickle

class authenticate:
    def __init__(self, username, password):
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

    
def SignUp(conn, message):
    data = pickle.dumps(message)
    client_socket.send(data)

def NewTweet(conn):
    tweet_msg = input("Enter New tweet: ")
    hashtags = input("Provide the hashtags related to the above tweet (separated by space): ")
    tags = list(hashtags.split())
    
    msg = tweet_info(tweet_msg, tags)
    data = pickle.dumps(message)
    client_socket.send(data)

def DeleteFollower():
    pass
def LogOut():
    pass
def SearchPerson():
    pass

username = ""
password = ""



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

    start = int(input("For new user sign up press 0 and for login press 1"))
    if start==0:
        print("Enter username")
        username = input()
        print("Enter password")
        password = input()
        print("Enter name")
        name = input()
        print("Enter email")
        email = input()
        
        new_signup = signup(username, password, name, email)
        SignUp(client_socket, new_signup)
    
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


            


    
