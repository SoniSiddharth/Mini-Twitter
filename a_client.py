import socket
import os
from _thread import *
import threading
import pickle
#Prasad127@
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
        print("Enter Age")
        age = input()
        print("Enter Gender")
        gender = input()
        print("Enter Status")
        status = input()
        print("Enter City")
        city = input()
        print("Enter Institute")
        institute = input()
        SignUp(client_socket, username, password, name, email, age, gender, status, city, institute)
    else:
        print("For exiting press -1 else,",end="")
        print("Enter username :")
        username = input()
        print("Enter password")
        password = input()
        Login(client_socket, username, password)
    
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
