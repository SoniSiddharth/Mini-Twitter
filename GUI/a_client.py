import socket
import os
from _thread import *
import threading
import pickle
#Prasad127@
import random
# https://docs.google.com/document/d/1Q-nVq89qVQUU5DyaO6mRzTyLZm5R6URW4Xdqkk-VsOM/edit#heading=h.p2nityf5kx5q


from classes import *
from client_func import *    

#opening twitter

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
target_ip = "127.0.1.1"
target_port = input('Enter port --> ')
client_socket.connect((target_ip,int(target_port)))
# BUFFERSIZE = 64000
# message = "Hello"
# client_socket.send(message.encode('ascii'))
# reply_from_server = client_socket.recv(BUFFERSIZE)

# if reply_from_server=="":
#     print("Could not open application")
# else:
#     print(str(reply_from_server.decode('ascii')))    
username ="fweufe8339"
password ="Bhadwa"
while True:
    start = int(input("For new user sign up press 0 and for login press 1 : "))
    
    if start==0:
        print("Enter username")
        # username = input()
        username = "b" + str(random.randint(1,10000))
        print("Enter password")
        # password = input()
        password = "b"
        print("Enter email")
        # email = input()
        email = "b@gmail.com"
        print("Enter name")
        # name = input()
        name = "soni"
        print("Enter Age")
        # age = input()
        age = 2
        print("Enter Gender")
        # gender = input()
        gender = "F"
        print("Enter Status")
        # status = input()
        status = "single"
        print("Enter City")
        # city = input()
        city = "Saudi"
        print("Enter Institute")
        # institute = input()
        institute = "ITI"
        SignUp(client_socket, username, password, email, name, age, gender, status, city, institute)
    else:
        print("For exiting press -1 else,",end="")
        print("Enter username :")
        # username = input()

        print("Enter password")
        # password = input()

        Login(client_socket, username, password)
    
        if username== "-1":
            break
        else:
            print("You are logged in successfully")
            print("Enter a for new Tweet")
            print("Enter b for searching a person")
            print("Enter c for deleting follower")
            print("Enter n for new tweet")
            print("Enter f to follow someone")
            print("Enter x to search by hashtag")
            print("Enter t for trending hashtags")
            print("Enter d for log out")
            while True:   
                print("Enter your query") 
                query = input()
                if query =="a":
                    NewTweet(client_socket,username)
                if query =="b":
                    username = input("Enter the username of the person: ")
                    SearchPerson(client_socket,username)
                if query =="c":
                    DeleteFollower(client_socket,username)
                if query=="n":
                    NewTweet(client_socket, username)
                if query =="f":
                    username = input("Enter the username of the person: ")
                    Follow(client_socket, username)
                if query=="x":
                    hashtag=input("Enter hashtag ")
                    SearchByHashtag(client_socket,hashtag)
                if query=="t":
                    TrendingHashtags(client_socket)
                if query == "d":
                    LogOut(client_socket,username)
            