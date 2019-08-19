from tkinter import *
from PIL import ImageTk, Image
import os
from dbms import widgets
root = Tk()



menubar = Menu(root)
root.config(menu=menubar)

submenu = Menu(menubar)
menubar.add_cascade(label='WatchMore', menu=submenu)
submenu.add_command(label='Exit')

root.geometry('984x700')
root.title("WatchMore")
root.iconbitmap(r'logo.ico')

def homepagelogo():
    print("You're in homepage")

photo = PhotoImage(file='logo2.png')
btn = Button(root, image=photo, command=homepagelogo)
btn.place(x=400,y=0)

Welcometext = Label(root, text = 'Welcome {{username}},')
Welcometext.place(x=0,y=40)


logintext = Label(root, text = 'CLick on Logout to Sign Out')
logintext.place(x=700, y=40)

photo1 = PhotoImage(file='logout.png')
btn1 = Button(root, image=photo1, command=widgets)
btn1.place(x=895,y=30)

img = ImageTk.PhotoImage(Image.open("MR.png"))
panel = Label(root, image = img)
panel.place(x=0,y=80)

btn2 = Button(root, text='Go to Search Options')
btn2.place(x=500,y=550)

root.mainloop()
