# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 16:34:45 2019

@author: SUDEEP
"""
# Python Tkinter and Sqlite3 Login Form
# Made By Namah Jain Form Youtube Channel All About Code
# Please Subscribe To Our Youtube Channel.
# https://www.youtube.com/channel/UCUGAq4ALoWW4PDU6Cm1riSg?view_as=subscriber

# imports
from tkinter import *
from tkinter import messagebox as ms
import sqlite3
import system
import os
import hashlib,binascii,os

def loginfunc(username):
    master.destroy()
    filename = 'system.py'
    os.system(filename)
# Login Function
def login():

    # Establish Connection
    with sqlite3.connect('quit.db') as db:
        c = db.cursor()

    # Find user If there is any take proper action
    # salt = hashlib.sha256(os.urandom(10)).hexdigest().encode('ascii')
    # pwdhash = hashlib.pbkdf2_hmac('sha512', password.get().encode('utf-8'), salt, 100)
    # pwdhash = binascii.hexlify(pwdhash)
    # print(pwdhash)
    password1 = hashlib.md5(str.encode(password.get()))
    print(password1.hexdigest())
    find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
    c.execute(find_user, [(username.get()), (password1.hexdigest())])
    result = c.fetchall()
    if result:
        loginfunc(username.get())
        # head['text'] = username.get() + '\n Loged In'
        # head['pady'] = 150
    else:
        ms.showerror('Oops!', 'Username Not Found.')



def new_user():
    # Establish Connection
    with sqlite3.connect('quit.db') as db:
        c = db.cursor()

        # Find Existing username if any take proper action
        find_user = ('SELECT * FROM user WHERE username = ?')
        c.execute(find_user, [(username.get())])
        print(c.fetchall())
        result=c.fetchall()
        if result:
            ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
        else:
            ms.showinfo('Success!', 'Account Created!')

        # Create New Account
        # salt=hashlib.sha256(os.urandom(10)).hexdigest().encode('ascii')
        # pwdhash=hashlib.pbkdf2_hmac('sha512',n_password.get().encode('utf-8'),salt,100)
        # pwdhash=binascii.hexlify(pwdhash)
        # print(pwdhash)
        password1=hashlib.md5(str.encode(n_password.get()))
        insert = 'INSERT INTO user(username,password) VALUES(?,?)'
        c.execute(insert, [(n_username.get()), (password1.hexdigest())])
        db.commit()

        # Frame Packing Methords


def log():
    username.set('')
    password.set('')
    crf.pack_forget()
    #head['text'] = 'LOGIN'
    logf.pack()



def cr():
    n_username.set('')
    n_password.set('')
    logf.pack_forget()
    #head['text'] = 'Create Account'
    crf.pack()


    # Draw Widgets


def widgets():
    head = Label(master, text='Login', font=('', 35), pady=10)
    head.pack()
    global logf
    logf = Frame(master, padx=10, pady=10)
    Label(logf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
    Entry(logf, textvariable=username, bd=5, font=('', 15)).grid(row=0, column=1)
    Label(logf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
    Entry(logf, textvariable=password, bd=5, font=('', 15), show='*').grid(row=1, column=1)
    Button(logf, text=' Login ', bd=3, font=('', 15), padx=5, pady=5, command=login).grid()
    Button(logf, text=' Create Account ', bd=3, font=('', 15), padx=5, pady=5, command=cr).grid(row=2,
                                                                                                          column=1)
    logf.pack()
    global crf
    crf = Frame(master, padx=10, pady=10)

    Label(crf, text='Username: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
    Entry(crf, textvariable=n_username, bd=5, font=('', 15)).grid(row=0, column=1)

    Label(crf, text='Password: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
    Entry(crf, textvariable=n_password, bd=5, font=('', 15), show='*').grid(row=1, column=1)

    Label(crf, text='Email: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
    Entry(crf, textvariable=n_email, bd=5, font=('', 15)).grid(row=2, column=1)

    Label(crf, text='Address: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
    Entry(crf, textvariable=n_age, bd=5, font=('', 15)).grid(row=3, column=1)

    Label(crf, text='Gender: ', font=('', 20), pady=5, padx=5).grid(sticky=W)
    Entry(crf, textvariable=n_gender, bd=5, font=('', 15)).grid(row=4, column=1)

    Button(crf, text='Go to Login', bd=3, font=('', 15), padx=5, pady=5, command=log).grid()
    Button(crf, text='Create Account', bd=3, font=('', 15), padx=5, pady=5, command=new_user).grid(row=5,
                                                                                                     column=1)



    # create window and application object
master = Tk()


# root.title("Login Form")
# make database and users (if not exists already) table at programme start up
with sqlite3.connect('quit.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL ,password TEXT NOT NULL);')
db.commit()
db.close()

# main Class
# Window

# Some Usefull variables
username = StringVar()
password = StringVar()
n_username = StringVar()
n_password = StringVar()
n_email = StringVar()
n_age = StringVar()
n_gender = StringVar()

# Create Widgets
widgets()


master.mainloop()
