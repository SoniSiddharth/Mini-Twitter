import mysql.connector
from classes import *
from globalvars import *

mydb = mysql.connector.connect(host="localhost",
								user="root",
								password="123456789",
								database="Minitweet",
								)

# signup function
def SignUp(conn, addr, data):
	
	#add a new user into 'Users' table in the database
	query = "INSERT INTO Users (Username, Password, Email, Name, Age, Gender, Status, City, Institute) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
	val = (data.username, data.password, data.email, data.name, data.age, data.gender, data.status, data.city, data.institute)
	mycursor = mydb.cursor()
	mycursor.execute(query, val)
	mydb.commit()

	#create a table that will store followers of this user (once users start following this new user)
	mycursor = mydb.cursor() 
	query = "CREATE TABLE "+ str(data.username) + "_followers"+" (Username varchar(20))"
	mycursor.execute(query)
	mydb.commit()

	#create table to store following (updated when this new user follows someone)
	mycursor = mydb.cursor() 
	query = "CREATE TABLE "+ str(data.username) + "_following"+" (Username varchar(20))"
	mycursor.execute(query)
	mydb.commit()
	
	#Tell client if signup was succesful
	reply=signup("","","","","","","","","","",1)
	msg=pickle.dumps(reply)
	conn.send(msg)
	return "Done"




def ShowTweets(username):#returns a list of recent tweets to the login function

	query="SELECT Username FROM "+str(username)+"_following"
	mycursor=mydb.cursor()
	mycursor.execute(query)
	
	names=mycursor.fetchall()
	dic={}  #key=a following of the user , value=1
	
	for name in names:
		dic[name[0]]=1
		
	query="SELECT * FROM Tweets ORDER BY TweetID DESC" #sort by tweet id in descending order
	val=()
	mycursor=mydb.cursor()
	mycursor.execute(query,val) 
	results=mycursor.fetchall()
	
	ls=list()
	count=0
	for row in results: #get the top 5 tweets from the following of this user 
		if(count==5):
			break
		if(row[0] in dic): #if this user is in the following of our user, then take his/her tweet into the list of top 5 tweets
			ls.append(row)
			count+=1   
	return ls


def Login(conn, loginData):
    	
	#check if supplied credentials are correct
	query = "SELECT * FROM Users where Username=" + "'" +str(loginData.username)+ "'" +" AND Password ="+ "'"+ str(loginData.password)+"'"
	mycursor = mydb.cursor()
	mycursor.execute(query)
	result = mycursor.fetchall()

	if(len(result)==0): #i.e. no username,password in db matches with the given
		reply=login("","","","",0)
	else:#if login was succesful, call show tweets functions and get latest 5(or less) tweets 
		tweets=list()
		tweets=ShowTweets(loginData.username)
		reply=login("","","",tweets,1)
	
	data=pickle.dumps(reply)
	conn.send(data)

	# server side
	return_arr = [loginData]
	if len(result)==0:
		return_arr.append(0)
	else:
		return_arr.append(1)
	return return_arr 





def NewTweet(conn,username, msg):
	#getting the last used tweet ID
	query = "Select TweetID from Tweets"
	mycursor = mydb.cursor()
	mycursor.execute(query)
	arr = mycursor.fetchall()

	num = arr[-1][0]
	tweetid = int(num)+1 #this will be the next tweet_id, to be used for this new tweet
	tweet_id = str(tweetid) 
	
	tag_arr = msg.hashtags
	while(len(tag_arr)<5):
		tag_arr.append("NULL")   

	         
	query = "INSERT INTO Tweets (Username, TweetID, TweetMessage, Hashtag1, Hashtag2, Hashtag3, Hashtag4, Hashtag5,Retweets) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
	val = (username, tweet_id, msg.message, msg.hashtags[0], msg.hashtags[1], msg.hashtags[2], msg.hashtags[3], msg.hashtags[4],0)
	mycursor = mydb.cursor()
	mycursor.execute(query, val)
	mydb.commit()

	query = "SELECT * from Hashtags"
	mycursor = mydb.cursor()
	mycursor.execute(query)
	results = mycursor.fetchall()

	dic={}
	for j in results:
		dic[j[0]] = j[1] #j is a tuple of (hashtag,count)
	for tag in tag_arr:
		if (tag!="NULL"):
			if tag in dic:
				count = dic[tag] + 1
				query = "UPDATE Hashtags SET Count = %s where Tag=%s"
				mycursor = mydb.cursor()
				val = (str(count), str(tag))
				mycursor.execute(query, val)
				mydb.commit()
			else:
				count = 1
				query = "INSERT INTO Hashtags (Tag, Count) VALUES (%s, %s)"
				mycursor = mydb.cursor()
				val = (str(tag),str(count))
				mycursor.execute(query, val)
				mydb.commit()
				print("Tag added")
	#Tell the client that Tweet was succesful
	reply=newtweet("","","",1)
	data=pickle.dumps(reply)
	conn.send(data)
	print("Done tweet")
	return tweet_id
	
def Unfollow(conn,username, data):
    
	#remove the person(to be unfollowed by curr client) from the following of username
	query="DELETE FROM "+str(username) + "_following"+" WHERE Username ='" + str(data.following) +"'"
	mycursor=mydb.cursor()
	mycursor.execute(query)
	mydb.commit()
	
	#remove username from the followers of the person
	query="DELETE FROM "+str(data.following)+"_followers"+" WHERE Username ='" + str(username) +"'"
	mycursor=mydb.cursor()
	mycursor.execute(query)
	mydb.commit()

	#Tell client that the person was succesfully unfollowed
	reply=unfollow("","",1)
	data=pickle.dumps(reply)
	conn.send(data)
	# print("Unfollowed ",data.following)


def DeleteFollower(conn,username, data):
    
	#remove the person(follower to be deleted by curr client) from the followers of username
	query="DELETE FROM "+str(username) + "_followers"+" WHERE Username ='" + str(data.follower) +"'"
	mycursor=mydb.cursor()
	mycursor.execute(query)
	mydb.commit()
	
	#remove username from the person's following
	query="DELETE FROM "+str(data.follower)+"_following"+" WHERE Username ='" + str(username) +"'"
	mycursor=mydb.cursor()
	mycursor.execute(query)
	mydb.commit()

	#Tell client that the person was succesfully unfollowed
	reply=deletefollower("","",1)
	data=pickle.dumps(reply)
	conn.send(data)
	# print("Deleted ",data.follower)

def ShowAllFollowers(conn, username, data):

	query="SELECT Username FROM " + str(username) + "_followers"
	mycursor=mydb.cursor()
	mycursor.execute(query)
	arr=mycursor.fetchall()
	# print(arr)
	if (len(arr)==0):
		results=showallfollowers("",arr,0)
		data=pickle.dumps(results)
		conn.send(data)
	else:
		results=showallfollowers("",arr,1)
		data=pickle.dumps(results)
		conn.send(data)
		print("Followers list sent")
	
def Refresh(conn, username, data):

	query="SELECT Username FROM "+ username + "_following"
	mycursor=mydb.cursor()
	mycursor.execute(query)
	
	names=mycursor.fetchall()
	dic={}
	for name in names:
		dic[name[0]]=1
	query="SELECT * FROM Tweets ORDER BY TweetID DESC" #sort by tweet id in descending order
	val=() 
	mycursor=mydb.cursor()
	mycursor.execute(query,val) 
	results=mycursor.fetchall()
	ls=[] #will be the list of recent tweets
	count=0
	for row in results:
		if(count==5):
			break
		if(row[0] in dic): #if the username was in the curr clients following, then add his latest tweet to the list of recent tweets
			ls.append(row)
			count+=1
	if count==0:
		reply=refresh("",ls,0)
	else:
		reply=refresh("",ls,5)
	
	data=pickle.dumps(reply)
	conn.send(data)
	

def SearchPerson(conn, addr, username, data):

	query="SELECT Username, Name, Age, Gender, Status, City, Institute FROM Users where Username = %s or Name = %s"
	val = (data.username, data.name)
	mycursor = mydb.cursor()
	mycursor.execute(query,val)
	results = mycursor.fetchall()
	if len(results)==0:
		message = searchperson("SearchPerson", "", "", "", "", "", "", "", 0)
	else:
		results = results[0]
		print(results)
		message = searchperson("SearchPerson", results[0], results[1], results[2], results[3], results[4], results[5], results[6], 1)
	data=pickle.dumps(message)
	conn.send(data)
	print("Data of the searched person sent")
	return message.flag

def Follow(conn, addr, username, data):
	#check if such name/username exists
	available = SearchPerson(conn, addr, username, data)
	if (available==1):
		#update curr client's following
		query = "INSERT INTO "+ str(username)+"_following" + " (Username)" + " VALUES("+ "'"+str(data.username)+"'" ")"
		mycursor = mydb.cursor()
		mycursor.execute(query)
		mydb.commit()

		#update his(the person whon client wants to follow) followers
		query = "INSERT INTO "+ str(data.username)+"_followers" + " (Username)" + " VALUES("+ "'"+str(username)+"'" ")"
		mycursor = mydb.cursor()
		mycursor.execute(query)
		mydb.commit()
		print("Following ", data.username)
	else:
		print("person not found")

def SearchByHashtag(conn,data):
	hashtag=data.hashtag
	query="SELECT * FROM Tweets where Hashtag1=%s or Hashtag2=%s or Hashtag3=%s or Hashtag4=%s or Hashtag5=%s"
	val=(hashtag,hashtag,hashtag,hashtag,hashtag)
	mycursor=mydb.cursor()
	mycursor.execute(query,val)
	results=mycursor.fetchall() 

	#send data to client
	reply=searchbyhashtag("","",results)
	data=pickle.dumps(reply)
	conn.send(data)

def TrendingHashtags(conn, data):
	query = "SELECT Tag from Hashtags ORDER BY Count DESC"
	mycursor=mydb.cursor()
	mycursor.execute(query)
	results=mycursor.fetchall()
	arr = list() 
	# print(results)
	counter = 0
	for j in results:
		if counter==5:
			break
		counter+=1
		arr.append(j[0])
	reply = trendinghashtags("", arr)
	data = pickle.dumps(reply)
	conn.send(data)
	print("trending hashtags sent")

def broadcast(message, connection, chatroom_clients): 
	for clients in chatroom_clients: 
		if clients!=connection:
			try: 
				print(message)
				clients.send(message.encode('ascii')) 
			except: 
				clients.close() 
				if connection in chatroom_clients: 
					chatroom_clients.remove(connection)

def EnterChatRoom(conn, addr, data, chatroom_clients, username):
	conn.send("Welcome to this chatroom!".encode('ascii')) 
	while True:
		message = conn.recv(2048) #the client in this connection sent a message to be broadcasted
		# while(len(message)==0):
		# 	message=conn.recv(2048)
		if message:
			print ("<" + username + "> " + message.decode('ascii')) 
			message_to_send = "<" + username + "> " + message.decode('ascii')
			if (message.decode('ascii')=="exit"):
				chatroom_clients.remove(conn)
				break
			else:
				broadcast(message_to_send, conn, chatroom_clients) 
		else: 
			print("Connection broken")
			if conn in chatroom_clients:
				chatroom_clients.remove(conn)

def Retweet(conn, id,username):
	#get the tweet to be retweeted
	query="SELECT * FROM Tweets where TweetID=" +str(id)
	mycursor=mydb.cursor()
	mycursor.execute(query)
	result=mycursor.fetchall()
	#increase the retweets of this particular tweet
	query = "UPDATE Tweets SET Retweets = %s where TweetID=%s"
	mycursor = mydb.cursor()
	val = (str(int(result[0][8])+1), str(id))
	mycursor.execute(query, val)
	mydb.commit()
	#update the message and make a new tweet (retweet) by you
	hashtags=[]
	for i in range(5):
		hashtags.append(result[0][3+i])
	message=result[0][2]
	message="Retweet by "+str(username)+"\n"+str(message)
	msg = newtweet("",message,hashtags,0)
	#make a new tweet and notify client
	tweet_id=NewTweet(conn,username,msg)

	#send the new tweet to the client as a newtweet object, only after client is ready
	client_reply=conn.recv(BUFFERSIZE)
	# while(len(client_reply)==0):
	# 	client_reply=conn.recv(BUFFERSIZE)
	if(client_reply.decode('ascii')=="1"):
		#now send
		reply=newtweet("",message,hashtags,1)
		data=pickle.dumps(reply)
		conn.send(data)




