from tkinter import *
from client_func import *
from functools import partial
import socket
from uifunctions import * 
from threading import Thread



# global client_socket
global cntr
cntr =1.0
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
target_ip = "127.0.1.1"
print("Enter the port address:")
target_port = input()
client_socket.connect((target_ip,int(target_port)))
print("Connected with server")

def callback(sv,len1):
	c = sv.get()[0:len1]
	# print("c=" , c)
	sv.set(c)

#######tweeting#######################################
def maketwt(twt,twt2,username):
	textt = twt.get(1.0,END)
	hasht = twt2.get(1.0,END)
	print(hasht)
	if(len(textt)==0):
		txt("Give some text")
	else:
		print(len(textt))
		a = NewTweet(client_socket,textt,hasht,username)
		print(a)
		if(a!=0):
			txt("tweeted successfully")
		else:
			txt("some error while tweeting")


def maketweetscreen(username):
	global screen
	root = screen
	root.destroy()
	root = Tk()
	screen = root
	root.title("Mini Tweet")
	root.geometry("950x600")  
	# refresh1(root)
	frame1 = Frame(root)
	aa1 = partial(Actionspage,username,[])
	Button(frame1,text="go to main window",command=aa1).pack()    
	
	frame1.pack(side=TOP)


	frame = Frame(root)
	
	l0 =Label(frame,text="Write tweet here:",font=("Calibri",15))
	twt = StringVar()
	twt = Text(frame, height = 10, width = 50)
	twt2 = Text(frame,height =2,width = 50)
  
	l1 = Label(frame,text="Put at max 5 space separated hashtag below:",font=("Calibri",15))
	tweet1 = partial(maketwt,twt,twt2,username)
	b1 = Button(frame,text="Tweet",command=tweet1)
	
	frame.pack()
	l0.pack()
	twt.pack()
	l1.pack()
	twt2.pack()
	b1.pack()
	root.mainloop()

###########################################

##### Searching a person ####################################

def srcAux(twt):
	textt = twt.get(1.0,END)
	if(len(textt)==0):
		txt("Give some text")
	else:
		print(len(textt))
		a = SearchPerson(client_socket,textt.strip())
		if(a!=0 and a!=None):
			txt("Person is found and email is :"+a.name + "\nHis/her username is :" + a.username+"\nHis/her age,gender,city,education is as follows:"+str(a.age)+","+a.gender+","+a.city+","+a.institute)
		else:
			txt("some error while searching or not found")
	

def SearchPersonv(username):
	global screen
	root = screen
	root.destroy()
	root = Tk()
	screen = root
	root.title("Mini Tweet")
	root.geometry("950x600")  
	# refresh1(root)
	frame1 = Frame(root)
	frame = Frame(root)
	twt = StringVar()
	twt = Text(frame, height = 10, width = 50)

	# search11 = partial(srcAux,twt)
	# Button(frame1,text="Search a person",command = search11).pack(side=LEFT)
	aa1 = partial(Actionspage,username,[])
	Button(frame1,text="go to main window",command=aa1).pack()
	frame1.pack(side=TOP)



	# twt2 = Text(frame,height =2,width = 50)
  
	tweet1 = partial(srcAux,twt)
	b1 = Button(frame,text="Search",command=tweet1)
	
	frame.pack()
	twt.pack()
	# twt2.pack()
	b1.pack()
	root.mainloop()

	
######### Unfollow someone #########
def Unfollow2(twt,username):
	textt = twt.get(1.0,END)
	if(len(textt)==0):
		txt("Give some text")
	else:
		print(len(textt))
		a = Unfollow(client_socket,textt.strip())
		if(a!=0 and a!=None):
			txt("Unfollowed Successfully")

		else:
			txt("some error while searching or not found")


def Unfollow1(username):
	global screen
	root = screen
	root.destroy()
	root = Tk()
	screen = root
	root.title("Mini Tweet")
	root.geometry("950x600")  
	# refresh1(root)
	frame1 = Frame(root)
	frame = Frame(root)
	l0 =Label(frame,text="Write name here:",font=("Calibri",15))
	twt = StringVar()
	twt = Text(frame, height = 10, width = 50)

	# search11 = partial(srcAux,twt)
	# Button(frame1,text="Search a person",command = search11).pack(side=LEFT)
	aa1 = partial(Actionspage,username,[])
	Button(frame1,text="go to main window",command=aa1).pack()
	frame1.pack(side=TOP)



	# twt2 = Text(frame,height =2,width = 50)
  
	tweet1 = partial(Unfollow2,twt,username.strip())
	b1 = Button(frame,text="Search",command=tweet1)
	
	frame.pack()
	l0.pack()
	twt.pack()
	# twt2.pack()
	b1.pack()
	root.mainloop()

####################################################################

################### Delete Follower ##############
def Deleteflwr2(twt,username):
	textt = twt.get(1.0,END)
	if(len(textt)==0):
		txt("Give some text")
	else:
		print(len(textt))
		a = DeleteFollower(client_socket,textt.strip())
		if(a!=0 and a!=None):
			txt("Deleted Successfully")

		else:
			txt("some error while searching or not found")


def Deleteflwr1(username):
	global screen
	root = screen
	root.destroy()
	root = Tk()
	screen = root
	root.title("Mini Tweet")
	root.geometry("950x600")  
	# refresh1(root)
	frame1 = Frame(root)
	frame = Frame(root)
	l0 =Label(frame,text="Write name here:",font=("Calibri",15))
	twt = StringVar()
	twt = Text(frame, height = 10, width = 50)

	# search11 = partial(srcAux,twt)
	# Button(frame1,text="Search a person",command = search11).pack(side=LEFT)
	aa1 = partial(Actionspage,username,[])
	Button(frame1,text="go to main window",command=aa1).pack()
	frame1.pack(side=TOP)



	# twt2 = Text(frame,height =2,width = 50)
  
	tweet1 = partial(Deleteflwr2,twt,username.strip())
	b1 = Button(frame,text="Search",command=tweet1)
	
	frame.pack()
	l0.pack()
	twt.pack()
	# twt2.pack()
	b1.pack()
	root.mainloop()



###################################################


	
	


############Search by Hashtag #########
def searchbyhst(twt,username):
	textt = twt.get(1.0,END)
	if(len(textt)==0):
		txt("Give some text")
	else:
		print(len(textt))
		a = SearchByHashtag(client_socket,textt.strip())
		if(a!=0 and a!=None):
			arr =[]
			arr.append("Here is the list of tweets in this hashtag")
			for i in a:
				if(i!="NULL"):
					arr.append(i)
			Actionspage(username,arr)
		else:
			txt("some error while searching or not found")

	


def searchbyhst1(username):
	global screen
	root = screen
	root.destroy()
	root = Tk()
	screen = root
	root.title("Mini Tweet")
	root.geometry("950x600")  
	# refresh1(root)
	frame1 = Frame(root)
	frame = Frame(root)
	l0 =Label(frame,text="Write hashtag here:",font=("Calibri",15))
	twt = StringVar()
	twt = Text(frame, height = 10, width = 50)

	# search11 = partial(srcAux,twt)
	# Button(frame1,text="Search a person",command = search11).pack(side=LEFT)
	aa1 = partial(Actionspage,username,[])
	Button(frame1,text="go to main window",command=aa1).pack()
	frame1.pack(side=TOP)



	# twt2 = Text(frame,height =2,width = 50)
  
	tweet1 = partial(searchbyhst,twt,username)
	b1 = Button(frame,text="Search",command=tweet1)
	
	frame.pack()
	l0.pack()
	twt.pack()
	# twt2.pack()
	b1.pack()
	root.mainloop()


######Go to chatroom ###########

#########################

################ Follow someone ##########
def follow2(twt,username):
	textt = twt.get(1.0,END)
	if(len(textt)==0):
		txt("Give some text")
	else:
		print(len(textt))
		a = Follow(client_socket,textt.strip())
		if(a!=0 and a!=None):
			txt("followed "+textt + "Successfully")
		else:
			txt("some error while searching or not found")

	


def follow1(username):
	global screen
	root = screen
	root.destroy()
	root = Tk()
	screen = root
	root.title("Mini Tweet")
	root.geometry("950x600")  
	# refresh1(root)
	frame1 = Frame(root)
	frame = Frame(root)
	l0 =Label(frame,text="Write name here:",font=("Calibri",15))
	twt = StringVar()
	twt = Text(frame, height = 10, width = 50)

	# search11 = partial(srcAux,twt)
	# Button(frame1,text="Search a person",command = search11).pack(side=LEFT)
	aa1 = partial(Actionspage,username,[])
	Button(frame1,text="go to main window",command=aa1).pack()
	frame1.pack(side=TOP)



	# twt2 = Text(frame,height =2,width = 50)
  
	tweet1 = partial(follow2,twt,username)
	b1 = Button(frame,text="Follow",command=tweet1)
	
	frame.pack()
	l0.pack()
	twt.pack()
	# twt2.pack()
	b1.pack()
	root.mainloop()
##################################
#######Trending Hashtags ###########
# def Trendhst1(twt,username):
#     textt = twt.get(1.0,END)
#     if(len(textt)==0):
#         txt("Give some text")
#     else:
#         print(len(textt))
#         a = TrendingHashtags(client_socket)
#         if(a!=0 and a!=None):
#             arr =[]
#             arr.append("These are the trending Hashtags")
#             for i in a:
#                 if(i!="NULL"):
#                     arr.append(i)
#             # Actionspage(username,arr)
#             for i in arr:
#                 twt.insert(END, i+"\n")
#         else:
#             txt("some error while searching or not found")

	


def Trendhst2(username):
	global screen
	root = screen
	root.destroy()
	root = Tk()
	screen = root
	root.title("Mini Tweet")
	root.geometry("950x600")  
	# refresh1(root)
	frame1 = Frame(root)
	frame = Frame(root)
	l0 =Label(frame,text="Write tweet here:",font=("Calibri",15))
	twt = StringVar()
	twt = Text(frame, height = 10, width = 50)

	# search11 = partial(srcAux,twt)
	# Button(frame1,text="Search a person",command = search11).pack(side=LEFT)
	aa1 = partial(Actionspage,username,[])
	Button(frame1,text="go to main window",command=aa1).pack()
	frame1.pack(side=TOP)



	# twt2 = Text(frame,height =2,width = 50)
  
	# tweet1 = partial(Trendhst1,twt,username)
	# b1 = Button(frame,text="Search",command=tweet1)

	a1 = TrendingHashtags(client_socket)
	if(len(a1)==0):
		txt("Error in fetching or no activity yet")
	else:
		for i in a1:
			twt.insert(END,i+"\n")
	
	frame.pack()
	twt.pack()
	# twt2.pack()
	# b1.pack()
	root.mainloop()
######################################




######### Show all followers ############
def Showfollowers1(twt,username):
	textt = twt.get(1.0,END)
	if(len(textt)==0):
		txt("Give some text")
	else:
		print(len(textt))
		a = ShowAllFollowers(client_socket,textt.strip())
		if(a!=0 and a!=None):
			arr =[]
			arr.append("This is the list of followers")
			for i in a:
				if(i!="NULL"):
					twt.insert(END,i+'\n')
			
			# Actionspage(username,arr)
		else:
			txt("some error while searching or not found")

	


def Showfollowers2(username):
	global screen
	root = screen
	root.destroy()
	root = Tk()
	screen = root
	root.title("Mini Tweet")
	root.geometry("950x600")  
	# refresh1(root)
	frame1 = Frame(root)
	frame = Frame(root)
	twt = StringVar()
	twt = Text(frame, height = 10, width = 50)

	# search11 = partial(srcAux,twt)
	# Button(frame1,text="Search a person",command = search11).pack(side=LEFT)
	aa1 = partial(Actionspage,username,[])
	Button(frame1,text="go to main window",command=aa1).pack()
	frame1.pack(side=TOP)
	# twt2 = Text(frame,height =2,width = 50)
  
	# tweet1 = partial(Showfollowers1,twt,username)
	# b1 = Button(frame,text="Search",command=tweet1)
	a = ShowAllFollowers(client_socket)
	if(a!=0 and a!=None):
		arr =[]
		arr.append("This is the list of followers")
		for i in a:
			if(i!="NULL"):
				twt.insert(END,i+'\n')
	else:
		twt.insert(END,"There are no followers")
	
	frame.pack()
	twt.pack()
	# twt2.pack()
	# b1.pack()
	root.mainloop()


#########################################

#################Refresh####################
# def refres1(twt,username):
#     textt = twt.get(1.0,END)
#     if(len(textt)==0):
#         txt("Give some text")
#     else:
#         print(len(textt))
#         a = Refresh(client_socket)
#         if(a!=0 and a!=None):
#             arr =[]
#             arr.append("Here is the list of tweets in this hashtag")
#             for i in a:
#                 if(i!="NULL"):
#                     arr.append(i)
#             Actionspage(username,arr)
#         else:
#             txt("some error while searching or not found")

	


def refers2(username):
	global screen
	root = screen
	root.destroy()
	root = Tk()
	screen = root
	root.title("Mini Tweet")
	root.geometry("950x600")  
	# refresh1(root)
	frame1 = Frame(root)
	a = Refresh(client_socket)
	if(a!=0 and a!=None):
		arr =[]
		# arr.append("Here is the list of tweets in this hashtag")
		for i in a:
			if(i!="NULL"):
				arr.append(i)
		Actionspage(username,arr)
	else:
		Actionspage(username,[])

	frame1.pack()
	
	root.mainloop()

#########################################

##############Retweet####################
def rtwt1(twt):
	textt = twt.get(1.0,END)
	# hasht = twt2.get(1.0,END)
	
	if(len(textt)==0):
		txt("Give some text")
	else:
		print("Going to call retweet")
		print(int(textt.strip()))
		a = Retweet(client_socket,int(textt.strip()))
		if(a!=0):
			txt("retweeted successfully")
		else:
			txt("some error while tweeting")


def rtwt2(username):
	global screen
	root = screen
	root.destroy()
	root = Tk()
	screen = root
	root.title("Mini Tweet")
	root.geometry("950x600")  
	# refresh1(root)
	frame1 = Frame(root)
	aa1 = partial(Actionspage,username,[])
	Button(frame1,text="go to main window",command=aa1).pack()    
	
	frame1.pack(side=TOP)
	frame = Frame(root)
	l0 =Label(frame,text="Write tweet id which you want to retweet here:",font=("Calibri",15))
	twt = StringVar()
	twt = Text(frame, height = 10, width = 50)
	# twt2 = Text(frame,height =2,width = 50)
	tweet1 = partial(rtwt1,twt)
	b1 = Button(frame,text="Tweet",command=tweet1)
	
	frame.pack()
	l0.pack()
	twt.pack()
	# twt2.pack()
	b1.pack()
	root.mainloop()
#########################################

###########chatroom###############




def send1(myls,txtt):
	data1 = txtt.get()
	txtt.set("")
	myls.insert(END,"<You>:"+data1)
	# client_socket.send(bytes(data1,"ascii"))
	Texting("ChatRoom",data1).sendit(client_socket)

	if data1=="exit":
		client_socket.close()

def receive(myls):
	while True:
		try:
			data1 = client_socket.recv(BUFFERSIZE)
			while(len(data1)==0):
				data1 = client_socket.recv(BUFFERSIZE)
			val1 = pickle.loads(data1)
			if(val1.func!="ChatRoom"):
				break
			msg1 = val1.message
			myls.insert(END, msg1)     
		except OSError:
			break       

def Exitchat(client_socket,username):
	# client_socket.send(bytes("exit",'ascii'))
	Texting("ChatRoom","exit").sendit(client_socket)
	Actionspage(username,[])



def enchtrm(client_socket,username):
	#notify server
	abc = enterchatroom("EnterChatRoom")
	dta = pickle.dumps(abc)
	client_socket.send(dta)



	global cntr
	global screen
	root = screen
	root.destroy()
	root = Tk()
	screen = root
	root.title("Chat room")
	root.geometry("950x600")
	frame1 = Frame(root)
	mnscrn = partial(Exitchat,client_socket,username)
	Button(frame1,text="Go to main menu",command=mnscrn).pack()
	frame1.pack(side=TOP)

	frame = Frame(root)
	Label(frame,text="").pack(side=TOP)
	scroll = Scrollbar(frame,orient=VERTICAL)
	myls = Listbox(frame,selectmode=EXTENDED,width=80,height=20,yscrollcommand=scroll.set,cursor="tcross")
	#config scrollbar
	scroll.config(command=myls.yview)
	scroll.pack(side=RIGHT,fill=Y)
	# myls.pack()
	frame.pack(side=TOP)
	myls.pack(pady=25,side=LEFT)

	frame3 = Frame(root)
	textt = StringVar()
	textt_etry = Entry(frame3,textvariable=textt)
	textt_etry.pack(side=TOP)


	wrk = partial(send1,myls,textt)
	b11 = Button(frame3,text="Send",command=wrk)
	b11.pack(side=TOP)
	frame3.pack(side=TOP)
	# flag=0
	# frame.pack()

	
	rcvtrd = Thread(target=receive,args=[myls])
	rcvtrd.start()

	root.mainloop()


###################################





def Actionspage(username,arr):
	global screen
	root = screen
	root.destroy()
	root = Tk()

	screen = root
	root.title("Main Screen")
	root.geometry("950x600")
	# refresh1(root)
	frame1 = Frame(root)
	frame = Frame(root)
	nt = partial(maketweetscreen,username)
	Button(frame1,text="NewTweet",command=nt).pack(side=LEFT)

	thst = partial(Trendhst2,username)
	Button(frame1,text="Trending Hashtags",command=thst).pack(side=LEFT)
	aa = partial(SearchPersonv,username)
	Button(frame1,text="Search a person",command = aa).pack(side=LEFT)

	unf1 = partial(Unfollow1,username)
	Button(frame1,text="unfollow",command=unf1).pack(side=LEFT)
	sea1 = partial(searchbyhst1,username)
	Button(frame1,text="Search by Hastag",command=sea1).pack(side=LEFT)

	ctrm = partial(enchtrm,client_socket,username)
	Button(frame1,text="Go to chatroom",command=ctrm).pack(side=LEFT)
	rtwt = partial(rtwt2,username)
	Button(frame1,text="Retweet",command=rtwt).pack(side=LEFT)
	frame1.pack(side=TOP)
	
	frame2 = Frame(root)
	flw = partial(follow1,username)
	Button(frame2,text="Follow",command=flw).pack(side=LEFT)
	sflw = partial(Showfollowers2,username)
	Button(frame2,text="Show All followers",command=sflw).pack(side=LEFT)
	rfrs = partial(refers2,username)
	Button(frame2,text="Refresh",command=rfrs).pack(side=LEFT)
	dflr = partial(Deleteflwr1,username)
	Button(frame2, text="Delete Follower",command=dflr).pack(side=LEFT)

	frame2.pack(side=TOP)
	
	Label(frame,text="").pack(side=TOP)
	scroll = Scrollbar(frame,orient=VERTICAL)
	myls = Listbox(frame,selectmode=EXTENDED,width=80,height=20,yscrollcommand=scroll.set,cursor="tcross")
	#config scrollbar
	scroll.config(command=myls.yview)
	scroll.pack(side=RIGHT,fill=Y)
	# myls.pack()
	frame.pack()
	myls.pack(pady=25,side=LEFT)
	
	# arr = Refresh(client_socket)

	# myls.insert(END,"Item")
	# myls.insert(END,"Item")
	# myls.insert(END,"Item")
	if(len(arr)!=0):
		for i in arr:
			myls.insert(END,i)
	#add items
	frame2 = Frame(root)
	frame2.pack()
	root.mainloop()





def txt(name):
	# tt1 = Label(screen,text="name is :"+name.get())
	tt1 = Tk()
	tt1.title("!")
	label = Label(tt1,text = name,font=("Calibri,15"))
	label.pack()
	B1 = Button(tt1,text="Okay",command=tt1.destroy)
	B1.pack()

	tt1.mainloop()
	# screen.destroy()
	#usrname, password.strip(), eml, na1, ag, gend, stat, ci, ins



def rregister(client_socket, username, password, email, name, age, gender, status, city, institute):
	usrname = username.get().strip()
	pswd = password.get().strip()
	eml = email.get().strip()
	na1 = name.get().strip()
	ag = age.get()
	gend =gender.get().strip()
	stat = status.get().strip()
	ci = city.get().strip()
	ins = institute.get().strip()
	print(usrname, password.get().strip(), eml, na1, ag, gend, stat, ci, ins)
	flg = SignUp(client_socket, usrname, pswd, eml, na1, ag, gend, stat, ci, ins)
	if(flg==0):
		txt("Some error in giving data")
	else:
		txt("Go to login")




def register(frame):
	for widget in frame.winfo_children():
		widget.destroy()
	frame.pack_forget()
	
	frame = LabelFrame(screen,text="")

	Label(frame,pady=5,text="Please Enter your details",width="300",height=2,font=("Calibri",15)).pack()
	username = StringVar()
	username.trace("w", lambda name, index, mode, username=username: callback(username,20))   

	email1 = StringVar()
	email1.trace("w", lambda name, index, mode, email1=email1: callback(email1,30))
	 
	
	name1 = StringVar()
	name1.trace("w", lambda name, index, mode, name1 =name1: callback(name1,20))

	email = StringVar()
	email.trace("w", lambda name, index, mode, email=email: callback(email,30))
	
	age = IntVar()
	
	gender = StringVar()
	gender.trace("w", lambda name, index, mode, gender=gender: callback(gender,1))
	
	institute = StringVar()
	institute.trace("w", lambda name, index, mode, institute=institute: callback(institute,30))
	
	status = StringVar()
	status.trace("w", lambda name, index, mode, status=status: callback(status,20))
	
	city = StringVar()
	city.trace("w", lambda name, index, mode, city=city: callback(status,20))
	
	
	
	Label(frame,text="Username").pack()
	username_entry = Entry(frame,textvariable=username)
	username_entry.pack()
	# Label(frame,text="").pack()

	# Label(frame,text="").pack()

	Label(frame,text="Name").pack()
	name_entry = Entry(frame,textvariable=name1)
	name_entry.pack()
	# Label(frame,text="").pack()


	Label(frame,text="email").pack()
	email_entry = Entry(frame,textvariable=email)
	email_entry.pack()
	# Label(frame,text="").pack()

	Label(frame,text="pswd").pack()
	email1_entry = Entry(frame,textvariable=email1,show="*")
	email1_entry.pack()



	Label(frame,text="gender").pack()
	gender_entry = Entry(frame,textvariable=gender)
	gender_entry.pack()
	# Label(frame,text="").pack()


	Label(frame,text="status").pack()
	status_entry = Entry(frame,textvariable=status)
	status_entry.pack()
	# Label(frame,text="").pack()
	Label(frame,text="age").pack()
	age_entry = Entry(frame,textvariable=age)
	age_entry.pack()

	Label(frame,text="city").pack()
	city_entry = Entry(frame,textvariable=city)
	city_entry.pack()    
	
	Label(frame,text="institute").pack()
	institute_entry = Entry(frame,textvariable=institute)
	institute_entry.pack()    
	# usrname = username.get().strip()
	# # pswd = password.get().strip()
	# eml = email.get().strip()
	# na1 = name1.get().strip()
	# ag = age.get()
	# gend =gender.get().strip()
	# stat = status.get().strip()
	# ci = city.get().strip()
	# ins = institute.get().strip()

	# print(usrname, password.strip(), eml, na1, ag, gend, stat, ci, ins)

	print(type(email1))
	print(type(email))

	makeregister = partial(rregister,client_socket,username, email1, email, name1, age, gender, status, city, institute)
	Button(frame,text="Register",width=10,height=1,command=makeregister).pack()
	# Label(frame,text="").pack()

	mm = partial(main1,frame)
	Button(frame,text="Go to login",width=10,height=1,command=mm).pack() 
	
	frame.pack(expand="yes")  


def logverify(username,password):
	usrname = username.get().strip()
	pswd = password.get().strip()
	print(usrname)
	print(pswd)
	print("in log verify clalled for Login")
	flg = Login(client_socket,usrname,pswd)
	if(flg!=0):
		Actionspage(usrname,flg)
	else:
		txt("Your details are invalid")






def lloginpage(frame):
	# screen1 = Tk()
	# screen1.title("Minitweeter Login")
	# screen1.geometry("950x600")
	# Label(screen1,pady=25,text="Please Enter your details",width="300",height=2,font=("Calibri",15)).pack()
	# screen1.mainloop()

	for widget in frame.winfo_children():
		widget.destroy()
	frame.pack_forget()

	frame = LabelFrame(screen,text="")
	Label(frame,pady=25,text="Please Enter your details",width="300",height=2,font=("Calibri",15)).pack()
	
	
	username = StringVar()
	Label(frame,text="Username").pack()
	username_entry = Entry(frame,textvariable=username)
	username_entry.pack()
	
	
	Label(frame,text="Password").pack()
	
	password = StringVar()
	password_entry = Entry(frame,textvariable=password,show="*")
	password_entry.pack()
	Label(frame,text="").pack()


	kk = partial(logverify,username,password)
	Button(frame,text="Login",width=10,height=2,command=kk).pack()
	Label(frame,text="").pack()

	mm = partial(main1,frame)
	Button(frame,text="goback",width=10,height=2,command=mm).pack()  
	frame.pack()  






	
	# pass
def main1(frame):
	for widget in frame.winfo_children():
		widget.destroy()
	frame.pack_forget()
	frame = LabelFrame(screen,text="",padx=2,pady=2)

	Label(frame,pady=50,text="Welcome To mini-twitter",width="300",height="2",font=("Calibri",40)).pack()
	# Label(pady=200,text="Welcome to twitter 2").pack()
	Label(frame,text="").pack()

	abc = partial(lloginpage,frame)
	Button(frame, text="Login",height="2",width="30",command=abc).pack()
	Label(frame, text="").pack()
	rr = partial(register,frame)
	Button(frame, text="Sign Up",height="2",width="30",command=rr).pack()
	Label(frame, text="").pack()
	
	
	# fwith_args = partial(with_args,1,2)
	
	# Button(frame, text="With Args",height="2",width="30",command=fwith_args).pack()
	# Label(frame, text="").pack()



	Button(frame, text="Quit",height="2",width="30",command=screen.destroy).pack()
	Label(frame, text="").pack()
	frame.pack()



def main():
	global screen
	screen = Tk()
	screen.geometry("950x600")
	screen.title("Minitweeter")
	frame = LabelFrame(screen,text="",padx=2,pady=2)

	Label(frame,pady=50,text="Welcome To mini-twitter",width="300",height="2",font=("Calibri",40)).pack()
	# Label(pady=200,text="Welcome to twitter 2").pack()
	Label(frame,text="").pack()

	abc = partial(lloginpage,frame)
	Button(frame, text="Login",height="2",width="30",command=abc).pack()
	Label(frame, text="").pack()
	rr = partial(register,frame)
	Button(frame, text="Sign Up",height="2",width="30",command=rr).pack()
	Label(frame, text="").pack()
	
	
	# fwith_args = partial(with_args,1,2)
	
	# Button(frame, text="With Args",height="2",width="30",command=fwith_args).pack()
	# Label(frame, text="").pack()
	# ak = partial(Actionspage,"prasad")
	# Button(frame,text="Actionpage",height=2,width=30,command=ak).pack()
	# Label(frame, text="").pack()


	Button(frame, text="Quit",height="2",width="30",command=screen.destroy).pack()
	Label(frame, text="").pack()
	
	
		
	frame.pack()
	screen.mainloop()
	client_socket.close()








main()