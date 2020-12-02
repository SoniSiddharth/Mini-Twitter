import socket
import os
import sys
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
# client_socket.setblocking(0)	
# BUFFERSIZE = 64000
# message = "Hello"
# client_socket.send(message.encode('ascii'))
# reply_from_server = client_socket.recv(BUFFERSIZE)

# if reply_from_server=="":
#     print("Could not open application")
# else:
#     print(str(reply_from_server.decode('ascii')))    
username ="alexandra"
password ="b"
while True:
    start = int(input("For new user sign up press 0 and for login press 1 : "))
    
    if start==0:
        print("Enter username: ")
        username = input()
        print("Enter password: ")
        password = input()
        print("Enter email: ")
        email = input()
        # email = "b@gmail.com"
        print("Enter name: ")
        name = input()
        # name = "ajinkya"
        print("Enter Age: ")
        age = input()
        # age = 2
        print("Enter Gender: ")
        gender = input()
        # gender = "F"
        print("Enter Status: ")
        status = input()
        # status = "single"
        print("Enter City: ")
        city = input()
        # city = "Saudi"
        print("Enter Institute: ")
        institute = input()
        # institute = "ITI"
        SignUp(client_socket, username, password, email, name, age, gender, status, city, institute)
    else:
        print("For exiting press -1 else,",end="")
        print("\nEnter username: ")
        username = input()

        print("Enter password: ")
        password = input()

        Login(client_socket, username, password)
    
        if username== "-1":
            break
        else:
            while True:   
                print("\nEnter refresh to refresh tweets")
                print("Enter search for searching a person")
                print("Enter unfollow to unfollow")
                print("Enter newtweet for new tweet")
                print("Enter follow to follow someone")
                print("Enter sbh to search by hashtag")
                print("Enter th for trending hashtags")
                print("Enter chat to enter chat room")
                print("Enter retweet to retweet a tweet")
                print("Enter showf to show all followers")
                print("Enter deletef for deleting follower")
                print("Enter logout for log out")
                print("\n")
                query = input("What do you wish to do? ")
                if query =="refresh":
                    Refresh(client_socket)
                if query =="search":
                    username = input("Enter the username of the person: ")
                    SearchPerson(client_socket,username)
                if query =="unfollow":
                    username=input("Enter the username to unfollow")
                    Unfollow(client_socket,username)
                if query=="newtweet":
                    NewTweet(client_socket, username)
                if query =="follow":
                    username = input("Enter the username of the person: ")
                    Follow(client_socket, username)
                if query=="sbh":
                    hashtag=input("Enter hashtag ")
                    SearchByHashtag(client_socket,hashtag)
                if query=="th":
                    TrendingHashtags(client_socket)
                if query=="chat":
                    EnterChatRoom(client_socket)
                if query=="retweet":
                    id=input("Enter tweet id: ")
                    Retweet(client_socket,id)
                if query=="showf":
                    ShowAllFollowers(client_socket,username)
                if query=="deletef":
                    username=input("Enter follower's username: ")
                    DeleteFollower(client_socket,username)
                if query == "logout":
                    Logout(client_socket)
                    break