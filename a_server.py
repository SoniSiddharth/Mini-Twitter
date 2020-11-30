import socket
import os
import time
import pickle
import mysql.connector
# import lepl.apps.rfc3696

UniqueTweets = 1


class signup():
    def __init__(self,func,username, password,name,email, flag):
        self.func=func
        self.username = username
        self.password = password
        self.email = email
        self.name = name
        self.flag=flag
         
class login:
    def __init__(self,func,username, password,flag):
        self.func=func
        self.username = username
        self.password = password
        self.flag=flag

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

def SignUp(conn, addr, data):
    credentials = pickle.loads(data)
    username = credentials.username
    password = credentials.password
    email = credentials.email
    name = credentials.name
    # emailchecker = lepl.apps.rfc3696.Email()
    # if not emailchecker(email):
    #     return "Invalid email"
    if len(password)<3:
        #Tell client that signup was not succesful due to weak password
        reply=signup("","","","","",0)
        msg=pickle.dumps(reply)
        conn.send(msg)
        return "Bad password"
    
    query = "INSERT INTO Users (Username, Password, Email, Name) VALUES (%s, %s, %s, %s)"
    val = (username, password, email, name)
    mycursor = mydb.cursor()
    mycursor.execute(query, val)

    val = (username) 
    query = "CREATE TABLE %s (Username varchar(20), FollowBack int)"
    mycursor.execute(query,val)
    mydb.commit()
    
    #Tell client if signup was succesful
    reply=signup("","","","","",1)
    msg=pickle.dumps(reply)
    conn.send(msg)
    return "Done"

def Login(conn):
    data = conn.recv(BUFFERSIZE)
    login_data = pickle.loads(data)
    query = "SELECT * FROM Users where Username='%s' and Password='%s'"
    val = (login_data.username, login_data.password)
    mycursor = mydb.cursor()
    mycursor.execute(query, val)
    result = mycursor.fetchall()

    if(len(result)==0):#not sure how to see if result is empty or not
        reply=login("","",0)
    else:
        reply=login("","",0)
    
    data=pickle.loads(reply)
    conn.send(data)   
    #why??
    # return_arr = [login_data]
    # if len(result)==0:
    #     return_arr.append(0)
    # else:
    #     return_arr.append(1)
    # return return_arr

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
    
    #Tell the client that Tweet was succesful
    reply=newtweet("","",1)
    data=pickle.dumps(reply)
    conn.send(data)
    print("Done tweet")
    
def DeleteFollower(conn, addr,username):
    msg=conn.recv(BUFFERSIZE)
    data=pickle.loads(msg)
    follower=data.follower
    query="DELETE FROM %s WHERE Username ='%s'"
    val=(username,follower)
    mycursor=mydb.cursor()
    mycursor.execute(query,val)
    mydb.commit()
    
    #Tell client that follower was succesfully deleted
    reply=deletefollower("","",1)
    data=pickle.dumps(reply)
    conn.send(data)
    print("Deleted follower")

def ShowAllFollowers(conn,username):
    query="SELECT Username FROM %s" #select all entries from Username column in the database of requesting user
    val=(username,)
    mycursor=mydb.cursor()
    mycursor.execute(query,val)
    arr=mycursor.fetchall()
    results=followers(arr)
    data=pickle.dumps(results)
    conn.send(data)
    print("Followers list sent")
    
def refresh(conn, username):
    query="SELECT Username FROM %s"
    val=(username,)
    mycursor=mydb.cursor()
    mycursor.execute(query,val)
    
    names=mycursor.fetchall()
    dic={}
    for name in names:
        dic[name]=1
        
    query="SELECT * FROM Tweets ORDER BY TweetID DESC" #sort by tweet id in descending order
    val=() #not sure about syntax
    mycursor=mydb.cursor()
    mycursor.execute(query,val) 
    results=mycursor.fetchall()
    
    ls=list()
    count=0
    for row in results:
        if(count==5):
            break
        if(dic[row[0]]==1):
            ls.append(row)
            count+=1   
    if count==0:
        reply=refresh("",ls,0)
    else:
        reply=new_tweets("",ls,5)
    data=pickle.dumps(reply)
    conn.send(data)


def SearchPerson():
    
    


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
