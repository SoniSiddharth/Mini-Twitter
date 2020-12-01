import pickle
import socket
BUFFERSIZE = 6400
class signup():
    def __init__(self,func,username, password,name,email,age,gender,status,city,institute,flag):
        self.func=func
        self.username = username
        self.password = password
        self.email = email
        self.name = name
        self.age=age
        self.gender=gender
        self.status=status
        self.city=city
        self.institute=institute
        self.flag=flag
    def send(self,conn):
        a = pickle.dumps(self)
        conn.send(a)
    def receive(self,conn):
        data = conn.recv(BUFFERSIZE)
        b = pickle.loads(data)
        return b

         
class login:
    def __init__(self,func,username, password,tweets,flag):             #here
        self.func=func
        self.username = username
        self.password = password
        self.flag=flag
        self.tweets=tweets                                              #here
    def send(self,conn):
        a = pickle.dumps(self)
        conn.send(a)
    def receive(self,conn):
        data = conn.recv(BUFFERSIZE)
        b = pickle.loads(data)
        return b


class newtweet():
    def __init__(self,func,message, hashtags,flag):
        self.func=func
        self.message = message
        self.hashtags = hashtags
        self.flag=flag

    def send(self,conn):
        a = pickle.dumps(self)
        conn.send(a)
    def receive(self,conn):
        data = conn.recv(BUFFERSIZE)
        b = pickle.loads(data)
        return b


class unfollow():
    def __init__(self,func,following,flag):
        self.func=func
        self.following=following
        self.flag=flag
    def send(self,conn):
        a = pickle.dumps(self)
        conn.send(a)
    def receive(self,conn):
        data = conn.recv(BUFFERSIZE)
        b = pickle.loads(data)
        return b

class deletefollower():
    def __init__(self,func,follower,flag):
        self.func=func
        self.follower=follower
        self.flag=flag
    def send(self,conn):
        a = pickle.dumps(self)
        conn.send(a)
    def receive(self,conn):
        data = conn.recv(BUFFERSIZE)
        b = pickle.loads(data)
        return b
        
class showallfollowers():
    def __init__(self,func,arr,flag):
        self.func=func
        self.arr=arr
        self.flag=flag
    def send(self,conn):
        a = pickle.dumps(self)
        conn.send(a)
    def receive(self,conn):
        data = conn.recv(BUFFERSIZE)
        b = pickle.loads(data)
        return b

        
class refresh():
    def __init__(self,func,tweets, count):
        self.func=func
        self.tweets=tweets
        self.count=count
    def send(self,conn):
        a = pickle.dumps(self)
        conn.send(a)
    def receive(self,conn):
        data = conn.recv(BUFFERSIZE)
        b = pickle.loads(data)
        return b

class logout:
    def __init__(self,func):
        self.func = func
    def send(self,conn):
        a = pickle.dumps(self)
        conn.send(a)
    def receive(self,conn):
        data = conn.recv(BUFFERSIZE)
        b = pickle.loads(data)
        return b

class searchperson:
    def __init__(self,func,username,name,age,gender,status,city,institute,flag):
        self.func=func
        self.username=username
        self.name=name
        self.age=age
        self.gender=gender
        self.status=status
        self.city=city
        self.institute=institute
        self.flag = flag
    def send(self,conn):
        a = pickle.dumps(self)
        conn.send(a)
    def receive(self,conn):
        data = conn.recv(BUFFERSIZE)
        b = pickle.loads(data)
        return b

class follow:
    def __init__(self, func, username, name):
        self.func = func
        self.username = username
        self.name = name

class searchbyhashtag:
    def __init__(self,func,hashtag,tweets):
        self.func=func
        self.hashtag=hashtag
        self.tweets=tweets

class trendinghashtags:
    def __init__(self, func, hashtags):
        self.func = func
        self.hashtags = hashtags

class enterchatroom:
    def __init__(self,func):
        self.func=func

class retweet:
    def __init__(self,func,id):
        self.func=func
        self.id=id
