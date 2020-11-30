import pickle
from classes import *
BUFFERSIZE = 6400
    
def SignUp(client_socket, username, password, email, name, age, gender, status, city, institute):
    #client to server
    new_signup = signup("SignUp",username, password, email, name, age, gender, status, city, institute, 0)
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
    credentials = login("Login",username, password,0)
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
    return data.flag
    
def NewTweet(client_socket, username):
    tweet_msg = input("Enter New tweet: ")
    hashtags = input("Provide the hashtags related to the above tweet (separated by space): ")
    tags = list(hashtags.split())
    #client to server
    msg = newtweet("NewTweet",tweet_msg, tags,0)
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
        print("Follower", follower, "unfollowed")#syntax check

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

def Refresh(client_socket):
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
        pass
        #print whatever we want from data
    

def SearchPerson(client_socket, name):
    #client to server
    msg = searchperson("SearchPerson",name,name,"","","","","",0)
    data = pickle.dumps(msg)
    client_socket.send(data)

    #server to client
    reply = client_socket.recv(BUFFERSIZE)
    while(len(reply)==0):
        reply = client_socket.recv(BUFFERSIZE) 
    data = pickle.loads(reply)
    if(len(data.name)>0 or len(data.username)>0):
        print("Name: ",data.name)
        print("Username: ",data.username)
        print("Age: ",data.age)
        print("Gender: ",data.gender)
        print("Status: ",data.status)
        print("City: ",data.city)
        print("Education: ",data.institute)
    else:
        print("No such user")

def Follow(client_socket,username):
    #check if username to be followed exists
    msg=follow("Follow",username,username)
    data=pickle.dumps(msg)
    client_socket.send(data)

    reply = client_socket.recv(BUFFERSIZE)
    while(len(reply)==0):
        reply = client_socket.recv(BUFFERSIZE) 
    data = pickle.loads(reply)
    if(data.flag==0):
        print("Invalid name/username")
    else:
        print("Following ",username)

def SearchByHashtag(client_socket, hashtag):
    #client to server
    tweets=list()
    msg=searchbyhashtag("SearchByHashtag",hashtag,tweets)
    data=pickle.dumps(msg)
    client_socket.send(data)

    #server to client
    reply = client_socket.recv(BUFFERSIZE)
    while(len(reply)==0):
        reply = client_socket.recv(BUFFERSIZE) 
    data = pickle.loads(reply)
    if(len(data.tweets)==0):
        print("No tweets with this hashtag")
    else:
        for tweet in data.tweets:
            print("Tweet done by: ")
            print(tweet[0])
            print("Tweet ID: ")
            print(tweet[1])
            print("Tweet: ")
            print(tweet[2])
            print("Following hashtags were used in this tweet")
            for j in range(3,8):
                if(tweet[j]!="NULL"):
                    print(tweet[j])
                else:
                    break
            print("\n")

def TrendingHashtags(client_socket):
    #client to server
    message = trendinghashtags("TrendingHashtags", list())
    data=pickle.dumps(message)
    client_socket.send(data)

    #server to client
    reply = client_socket.recv(BUFFERSIZE)
    while(len(reply)==0):
        reply = client_socket.recv(BUFFERSIZE) 
    data = pickle.loads(reply)
    result = data.hashtags
    print("Following are the top 5 trending hashtags")
    for j in result:
        print(j)

def LogOut():
    pass
