import socket
import os
from _thread import *
import threading
import pickle
#Prasad127@
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

    
def SignUp(client_socket, username, password, name, email):
    client_socket.send(bytes("s"))
    new_signup = signup(username, password, name, email)
    data = pickle.dumps(new_signup)
    client_socket.send(data)
    return

def NewTweet(client_socket):
    tweet_msg = input("Enter New tweet: ")
    hashtags = input("Provide the hashtags related to the above tweet (separated by space): ")
    tags = list(hashtags.split())
    
    msg = tweet_info(tweet_msg, tags)
    data = pickle.dumps(msg)
    client_socket.send(data)

def LoginCheck(client_socket, username, password):
    credentials = authenticate(username, password)
    data = pickle.dumps(credentials)
    client_socket.send(data)



def DeleteFollower(client_socket ,follower):
    client_socket.send(bytes(follower))

def LogOut():
    pass
def SearchPerson():
    pass

#opening twitter
print("Opening Twitter ...")
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
target_ip = "127.0.1.1"
target_port = input('Enter port --> ')
client_socket.connect((target_ip,int(target_port)))
BUFFERSIZE = 64000
# message = "Hello"
# client_socket.send(message.encode('ascii'))
# reply_from_server = client_socket.recv(BUFFERSIZE)

# if reply_from_server=="":
#     print("Could not open application")
# else:
#     print(str(reply_from_server.decode('ascii')))    


while True:
    start = int(input("For new user sign up press 0 and for login press 1 : "))
    
    if start==0:
        print("Enter username")
        username = input()
        print("Enter password")
        password = input()
        print("Enter name")
        name = input()
        print("Enter email")
        email = input()
        SignUp(client_socket, username, password, name, email)
    else:
        print("For exiting press -1 else,",end="")
        print("Enter username :")
        username = input()
        print("Enter password")
        password = input()
        LoginCheck(client_socket, username, password)
    
    # NewTweet(client_socket)
    if username== "-1":
        break
    else:
        print("You are logged in successfully")
        print("Enter a for new Tweet")
        print("Enter b for searching a person")
        print("Enter c for deleting follower")
        print("Enter n for new tweet")
        print("Enter d for log out")
        while True:    
            query = input()
            if query =="a":
                
                NewTweet(client_socket,username)
            if query =="b":
                SearchPerson(client_socket,username)
            if query =="c":
                DeleteFollower(client_socket,username)
            if query == "n":
                NewTweet(client_socket)
            if query == "d":
                LogOut(client_socket,username)
            else:
                break

client_socket.close()


            


    
