from client_func import EnterChatRoom
import socket
import os
import time
import pickle
import mysql.connector
from classes import *
from server_func import *
from globalvars import *
from _thread import *
# import lepl.apps.rfc3696

UniqueTweets = 1

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
port = int(input('Enter desired port --> '))

server_socket.bind((ip,port))

server_socket.listen(100)
# BUFFERSIZE = 64000
print('Running on IP: '+ip)
print('Running on port: '+str(port))

# Connecting with database
# mydb = mysql.connector.connect(host="localhost",
#                                 user="root",
#                                 password="123456789",
#                                 database="Minitweet",
#                                 )
list_of_clients = []
chatroom_clients = []

def clientthread(conn, addr): 
	msg = conn.recv(BUFFERSIZE)
	while(len(msg)==0):
		msg=conn.recv(BUFFERSIZE)
	data=pickle.loads(msg)
	query = data.func

	if(query=="SignUp"):
		SignUp(conn,addr,data)
		# result = Login(conn)
		# continue
		# conn.close()
	else:
		flag = 0
		while(flag==0):#wait until user logs in successfully
			if(query=="Login"):
				returnedArr = Login(conn, data)
				if (returnedArr[-1]==1):
					flag=1									
					break
			else:
				print("please login first")
				msg = conn.recv(BUFFERSIZE)
				data=pickle.loads(msg)
				query = data.func
		username = returnedArr[0].username
		print(username)
		while True:
			msg = conn.recv(BUFFERSIZE)
			while len(msg)==0:
				msg = conn.recv(BUFFERSIZE)
			# print(msg)
			data=pickle.loads(msg)
			query = data.func
			if(query=="NewTweet"):
				NewTweet(conn,username, data)
			elif(query == "DeleteFollower"):
				print("deleting follower")
				DeleteFollower(conn,addr,username,data)
			elif(query == "ShowAllFollowes"):
				ShowAllFollowers(conn, addr, username, data)
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
				# Logout(conn, addr, username, data)
				conn.send(bytes("bye"))
				conn.close()
				break

while True:
	conn, addr = server_socket.accept()
	list_of_clients.append(conn) 

	print (str(addr[0]) + str(addr[1]) + " connected") 
	start_new_thread(clientthread,(conn,addr))
server_socket.close()



