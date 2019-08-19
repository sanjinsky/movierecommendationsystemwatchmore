from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import messagebox as ms

root = Tk()

menubar = Menu(root)
root.config(menu=menubar)

submenu = Menu(menubar)
menubar.add_cascade(label='WatchMore', menu=submenu)
submenu.add_command(label='Exit')

root.title("WatchMore")
root.iconbitmap(r'logo.ico')
root.state('zoomed')

photo = PhotoImage(file='logo.png')
btn = Button(root, image=photo)
btn.place(x=540,y=0)

Welcometext = Label(root, text = 'Welcome GUEST,')
Welcometext.place(x=0,y=50)

logintext = Label(root, text = 'For search options please LOGIN')
logintext.place(x=1020, y=50)

def loginfunc():

    root.destroy()
    filename = 'dbms.py'
    os.system(filename)


photo1 = PhotoImage(file='login.png')
btn1 = Button(root, image=photo1, command=lambda:loginfunc())
btn1.place(x=1200,y=40)

img = ImageTk.PhotoImage(Image.open("banner1.png"))
panel = Label(root, image = img)
panel.place(x=0,y=100)

workingtext = Label(root,text = 'What does it do? \n WatchMore is a movie recommendation syste. Based on the input you give, \n the app searches the similar movies for you.')
workingtext.place(x=200,y=580)


workingtext4 = Label(root,text = 'How does it work? \n Step 1) You give the search input to the system. \nStep 2) The system will give you output based on your input search. ')
workingtext4.place(x=750,y=580)

root.mainloop()
