from client_func import NewTweet
from functools import partial
from tkinter import Button, Entry, StringVar
def callback(sv,len1):
    c = sv.get()[0:len1]
    # print("c=" , c)
    sv.set(c)
