from tkinter import *
from tkinter import messagebox as ms
import sqlite3
import system
import os

# Establish Connection
def history():
    moviename=name
    with sqlite3.connect('quit_history.db') as db:
            c = db.cursor()

    c.execute('CREATE TABLE IF NOT EXISTS user1 (moviename TEXT NOT NULL );')
    db.commit()
    db.close()

    # Find Existing username if any take proper action
    find_user = ('SELECT * FROM user WHERE moviename = ?')
    c.execute(find_user, [(moviename.get())])
    print(c.fetchall())
    result=c.fetchall()
    if result:
        ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
    else:
        ms.showinfo('Success!', 'Account Created!')

    # Create New Account
    insert = 'INSERT INTO user(moviename) VALUES(?)'
    c.execute(insert, [(moviename.get())])
    db.commit()
