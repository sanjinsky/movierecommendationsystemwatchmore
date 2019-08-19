from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()


menubar = Menu(root)
root.config(menu=menubar)

submenu = Menu(menubar)
menubar.add_cascade(label='WatchMore', menu=submenu)
submenu.add_command(label='Exit')

root.geometry('984x500')
root.title("WatchMore")
root.iconbitmap(r'logo.ico')


def homepagelogo():
    print('You are a faggot')

photo = PhotoImage(file='logo2.png')
btn = Button(root, image=photo, command=homepagelogo)
btn.place(x=400,y=0)

Welcometext = Label(root, text = 'Welcome @Title,')
Welcometext.place(x=0,y=40)

logintext = Label(root, text = 'Exit')
logintext.place(x=860, y=45)

photo1 = PhotoImage(file='logout.png')
btn1 = Button(root, image=photo1,command=homepagelogo)
btn1.place(x=895,y=30)

advsearchtext = Label(root, text = 'This is Advanced Search Page')
advsearchtext.place(x=400,y=70)

img = ImageTk.PhotoImage(Image.open("details.png"))
panel = Label(root, image = img)
panel.place(x=550,y=100)

img2 = ImageTk.PhotoImage(Image.open("moods.png"))
panel2 = Label(root, image = img2)
panel2.place(x=30,y=100)

photo2 = PhotoImage(file='searchbymood.png')
btn2 = Button(root, image=photo2, command=homepagelogo)
btn2.place(x=100,y=390)

photo3 = PhotoImage(file='searchbymoviedetails.png')
btn3 = Button(root, image=photo3, command=homepagelogo)
btn3.place(x=650,y=390)

root.mainloop()
