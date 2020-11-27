import socket
import os
import time
import pickle
import mysql.connector
import lepl.apps.rfc3696

UniqueTweets = 1

class authenticate:
    def __init__(self,username, password):
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

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
port = int(input('Enter desired port --> '))

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

def SignUp(conn, addr):
    data = conn.recv(BUFFERSIZE)
    credentials = pickle.loads(data)
    username = credentials.username
    password = credentials.password
    email = credentials.email
    name = credentials.name
    # emailchecker = lepl.apps.rfc3696.Email()
    # if not emailchecker(email):
    #     return "Invalid email"
    if len(password)<3:
        return "Bad password"
    
    query = "INSERT INTO Users (Username, Password, Email, Name) VALUES (%s, %s, %s, %s)"
    val = (username, password, email, name)
    mycursor = mydb.cursor()
    mycursor.execute(query, val)

    val = (username) 
    query = "CREATE TABLE %s (Username varchar(20), FollowBack int)"
    mycursor.execute(query,val)
    mydb.commit()
    return "Done"

def Login(conn):
    data = conn.recv(BUFFERSIZE)
    login_data = pickle.loads(data)
    query = "SELECT * FROM Users where Username='%s' and Password='%s'"
    val = (login_data.username, login_data.password)
    mycursor = mydb.cursor()
    mycursor.execute(query, val)
    result = mycursor.fetchall()

    return_arr = [login_data]
    if len(result)==0:
        return_arr.append(0)
    else:
        return_arr.append(1)
    return return_arr

def NewTweet(conn, addr,username):
    # username = ""
    data = conn.recv(BUFFERSIZE)
    msg = pickle.loads(data)
    print(msg)
    global UniqueTweets
    tweet_id = str(UniqueTweets)
    UniqueTweets+=1
    tag_arr = msg.hashtags
    while(len(tag_arr)<5):
        tag_arr.append("NULL")            
    query = "INSERT INTO Tweets (Username, TweetID, TweetMessage, Hashtag1, Hashtag2, Hashtag3, Hashtag4, Hashtag5) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (username, tweet_id, msg.message, msg.hashtags[0], msg.hashtags[1], msg.hashtags[2], msg.hashtags[3], msg.hashtags[4])
    mycursor = mydb.cursor()
    mycursor.execute(query, val)
    mydb.commit()
    print("Done tweet")
    
def DeleteFollower(conn, addr,username):
    data=conn.recv(BUFFERSIZE)
    # username =""
    follower=data.decode('ascii')
    query="DELETE FROM %s WHERE Username ='%s'"
    val=(username,follower)
    mycursor=mydb.cursor()
    mycursor.execute(query,val)
    mydb.commit()
    print("Deleted follower")

def showAllFollowers(username):
    query="SELECT * FROM %s"
    val=(username)
    # mycursor=mydb.cursor()
    # mycursor.execute(query,val)
    # mydb.commit()

while True:
    conn, addr = server_socket.accept()
    # print(conn)
    # data = conn.recv(BUFFERSIZE)
    # received_msg = data.decode('ascii')
    # print("message received is ", received_msg)

    # response = "Welcome to the Mini Twitter"
    # data = response.encode('ascii')
    # conn.send(data)


    
    data = conn.recv(BUFFERSIZE)
    query = data.decode('ascii')
    query = query.strip()

    if(query=="a"):
        result = Login(conn)
        # conn.close()
    if(query=="b"):
        SignUp(conn,addr,username)
        # conn.close()
    if(query=="c"):
        DeleteFollower(conn,addr,username)
        # conn.close()
    if(query == "d"):
        NewTweet(conn,addr,username)
        # conn.close()
    
    

    # result = SignUp(conn, addr)
    # print(result)
    # NewTweet(conn, addr, "prasad")
    # conn.shutdown(socket.SHUT_RDWR)
    # conn.close()
server_socket.close()
