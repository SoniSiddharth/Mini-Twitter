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
    def __init__(self,func,username, password,flag):
        self.func=func
        self.username = username
        self.password = password
        self.flag=flag
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
    def __init__(self,func,arr):
        self.func=func
        self.arr=arr
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

class searchperson():
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
