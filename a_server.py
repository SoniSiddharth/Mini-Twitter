from client_func import DeleteFollower, EnterChatRoom
import socket
import os
import time
import pickle
import mysql.connector
from classes import *
from server_func import *
from globalvars import *
from _thread import *
import sys

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# ip = str(sys.argv[1])
ip = socket.gethostbyname(socket.gethostname())
print(ip)
port = int(input('Enter desired port --> '))
# sqladdr = sys.argv[3]
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
list_of_clients = []
chatroom_clients = [] #list of clients currently in the chatroom

def clientthread(conn, addr): #server assigns a thread to every client connection

	while True:
		msg = conn.recv(BUFFERSIZE) #server can wait indefinitely
		data=pickle.loads(msg)
		query = data.func

		if(query=="SignUp"):
			SignUp(conn,addr,data)
		else:
			flag = 0
			while(flag==0):#wait until user logs in successfully
				if(query=="Login"):
					returnedArr = Login(conn, data)
					if (returnedArr[-1]==1): #successful login
						flag=1
						print("Logged in succesfully")									
						break
				else:  							#if flag=0 and user sends some other query, then he/she should be prompted to login first
					print("please login first") 
					msg = conn.recv(BUFFERSIZE)
					data=pickle.loads(msg)
					query = data.func

			username = returnedArr[0].username
			# print(username)
			while True: 
				msg = conn.recv(BUFFERSIZE)
				# while len(msg)==0:
				# 	msg = conn.recv(BUFFERSIZE)
				data=pickle.loads(msg)
				query = data.func
				if(query=="NewTweet"):
					NewTweet(conn,username, data)
				elif(query == "Unfollow"):
					Unfollow(conn,username,data)
				elif(query == "DeleteFollower"):
					DeleteFollower(conn,username,data)
				elif(query == "ShowAllFollowers"):
					ShowAllFollowers(conn, username, data)
				elif(query == "SearchPerson"):
					SearchPerson(conn, addr, username, data)
				elif(query =="Follow"):
					Follow(conn, addr, username, data)
				elif(query == "SearchByHashtag"):
					SearchByHashtag(conn,data)
				elif(query == "TrendingHashtags"):
					TrendingHashtags(conn, data)
				elif(query == "EnterChatRoom"):
					chatroom_clients.append(conn)
					EnterChatRoom(conn, addr, data, chatroom_clients, username)
				elif(query == "Refresh"):
					Refresh(conn, username, data)
				elif(query == "Retweet"):
						Retweet(conn,data.id,username)
				elif(query == "Logout"):
					print("logging out")
					break

while True:
	conn, addr = server_socket.accept()
	list_of_clients.append(conn) 
	print (str(addr[0]) + str(addr[1]) + " connected") 
	start_new_thread(clientthread,(conn,addr)) #allocate a new thread to this connection
server_socket.close()



