import pickle
import sys
import select
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
    credentials = login("Login",username, password,list(),0)            
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
        print("Recent tweets from your following")
        for tweet in data.tweets:
            print(tweet)
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


def Unfollow(client_socket ,following):
    #client to server, request server to unfollow 
    msg=unfollow("Unfollow",following,0)
    data=pickle.dumps(msg)
    client_socket.send(data)
    
    #server's reply
    reply=client_socket.recv(BUFFERSIZE)
    while(len(reply)==0):
        reply=client_socket.recv(BUFFERSIZE) 
    data=pickle.loads(reply)
    if(data.flag==1):
        print(following, "unfollowed")

def DeleteFollower(client_socket ,follower):
    #client to server, request server to unfollow 
    msg=deletefollower("DeleteFollower",follower,0)
    data=pickle.dumps(msg)
    client_socket.send(data)
    
    #server's reply
    reply=client_socket.recv(BUFFERSIZE)
    while(len(reply)==0):
        reply=client_socket.recv(BUFFERSIZE) 
    data=pickle.loads(reply)
    if(data.flag==1):
        print(follower, "deleted")

def ShowAllFollowers(client_socket, username):
    arr=list()
    msg=showallfollowers("ShowAllFollowers",arr,0)
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
        # return 0
    else:
        for name in names:
            print(name[0])

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
    data = pickle.loads(reply)
    if(data.count==0):
        print("No new Tweets")
    else:
        response = data.tweets
        for j in response:
            print(j)
    return

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

def EnterChatRoom(client_socket):

    #notify server
    flag=0
    message = enterchatroom("EnterChatRoom")
    data = pickle.dumps(message)
    client_socket.send(data)

    while True: 
        sockets_list = [sys.stdin, client_socket] 
        read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 

        for socks in read_sockets: 
            if socks == client_socket: 
                message = socks.recv(2048) 
                print (message.decode('ascii')) 
            else: 
                message = sys.stdin.readline().strip()
                if(str(message)=="exit"):
                    print("exiting")
                    flag=1
                    break
                client_socket.send(message.encode('ascii')) 
                sys.stdout.write("<You>\n") 
                sys.stdout.write(message+'\n') 
                sys.stdout.flush() 
                

        if flag==1:
            break
    sys.stdout.write("Chat room exited\n") 
    sys.stdout.flush() 

def Retweet(client_socket, id):
    #ask server to update database
    msg=retweet("Retweet",id)
    data=pickle.dumps(msg)
    client_socket.send(data)

    #get confirmation of new tweet, this comes from newtweet function
    reply=client_socket.recv(BUFFERSIZE)
    while(len(reply)==0):
        reply=client_socket.recv(BUFFERSIZE) 
    data=pickle.loads(reply)
    if(data.flag==0):
        print("Could not Tweet, try again later")
    else:
        #ready to take the new tweet
        client_socket.send(bytes("1".encode('ascii')))
        # #get the retweeted tweet and print it, this comes from retweet function
        reply=client_socket.recv(BUFFERSIZE)
        while(len(reply)==0):
            reply=client_socket.recv(BUFFERSIZE) 
        data=pickle.loads(reply)
        print("Message:\n",data.message)
        print("Hashtags:")
        for i in range(len(data.hashtags)):
            if(data.hashtags[i]!="NULL"):
                print("#"+data.hashtags[i])

def LogOut():
    pass
