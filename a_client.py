import socket
import os
from _thread import *
import threading
import pickle
#Prasad127@
# https://docs.google.com/document/d/1Q-nVq89qVQUU5DyaO6mRzTyLZm5R6URW4Xdqkk-VsOM/edit#heading=h.p2nityf5kx5q


class signup():
    def __init__(self,func,username, password,name,email, flag):
        self.func=func
        self.username = username
        self.password = password
        self.email = email
        self.name = name
        self.flag=flag
         
class login:
    def __init__(self,func,username, password,msg):
        self.func=func
        self.username = username
        self.password = password
        self.msg=msg
        
class newtweet():
    def __init__(self,func,message, hashtags,flag):
        self.func=func
        self.message = message
        self.hashtags = hashtags
        self.flag=flag

class deletefollower():
    def __init__(self,func,follower,flag):
        self.func=func
        self.follower=follower
        self.flag=flag

class showallfollowers():
    def __init__(self,func,arr):
        self.func=func
        self.arr=arr
        
class refresh():
    def __init__(self,func,tweets, count):
        self.func=func
        self.tweets=tweets
        self.count=count
    
def SignUp(client_socket, username, password, name, email):
    #client to server
    new_signup = signup(username,"SignUp",password, name, email,0)
    data = pickle.dumps(new_signup)
    client_socket.send(data)
    
    #server to client
    reply=client_socket.recv(BUFFERSIZE)
    while(len(reply)==0):
        reply=client_socket.recv(BUFFERSIZE) 
    data=pickle.loads(reply)
    if(data.flag==0):
        print("Weak password")
    else:
        print("Signed up")
    return

def Login(client_socket, username, password):
    #client to server
    credentials = login(username,"Login",password,0)
    data = pickle.dumps(credentials)
    client_socket.send(data)
    
    #server to client
    reply=client_socket.recv(BUFFERSIZE)
    while(len(reply)==0):
        reply=client_socket.recv(BUFFERSIZE) 
    data=pickle.loads(reply)
    if(data.flag==0):
        print("Login failed, invalid credentials")
    else:
        print("Login Succesful")
    return
    
def NewTweet(client_socket):
    tweet_msg = input("Enter New tweet: ")
    hashtags = input("Provide the hashtags related to the above tweet (separated by space): ")
    tags = list(hashtags.split())
    #client to server
    msg = tweet_info("NewTweet",tweet_msg, tags,0)
    data = pickle.dumps(msg)
    client_socket.send(data)
    
    #server to client
    reply=client_socket.recv(BUFFERSIZE)
    while(len(reply)==0):
        reply=client_socket.recv(BUFFERSIZE) 
    data=pickle.loads(reply)
    if(data.flag==0):
        print("Could not Tweet, try again later")
    else:
        print("Tweeted")
    return


def DeleteFollower(client_socket ,follower):
    #client to server
    msg=deletefollower("DeleteFollower",follower,0)
    data=pickle.dumps(msg)
    client_socket.send(data)
    
    #server to client
    reply=client_socket.recv(BUFFERSIZE)
    while(len(reply)==0):
        reply=client_socket.recv(BUFFERSIZE) 
    data=pickle.loads(reply)
    if(data.flag==1):
        print("Follower {%s} unfollowed".follower)#syntax check

def ShowAllFollowers(client_socket, username):
    arr=list()
    msg=showallfollowers("ShowAllFollowers",arr)
    #client to server
    data=pickle.dumps(msg)
    client_socket.send(data)
    
    #server to client
    reply=client_socket.recv(BUFFERSIZE)
    while(len(reply)==0):
        reply=client_socket.recv(BUFFERSIZE) 
    data=pickle.loads(reply)
    names=data.arr #want the list in data to be stored in var names, check syntax
    if len(names)==0:
        print("No followers")
    else:
        for name in names:
            print(name)

def Refresh():
    #client to server
    tweets=list()
    msg=refresh("Refresh",tweets,0)
    data=pickle.dumps(msg)
    client_socket.send(data)
    
    #server to client
    reply=client_socket.recv(BUFFERSIZE)
    while(len(reply)==0):
        reply=client_socket.recv(BUFFERSIZE) 
    data=pickle.loads(reply)
    if(data.count==0):
        print("No new Tweets")
    else:
        #print whatever we want from data
    

def SearchPerson(name):
    #sending request from here itself
    client_socket.send(bytes(name))
    


def LogOut():
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


            


    
