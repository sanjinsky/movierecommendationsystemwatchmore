from tkinter import *
from PIL import ImageTk, Image
import os
root = Tk()


menubar = Menu(root)
root.config(menu=menubar)

submenu = Menu(menubar)
menubar.add_cascade(label='WatchMore', menu=submenu)
submenu.add_command(label='Exit')

root.title("WatchMore")
root.iconbitmap(r'logo.ico')
root.state('zoomed')

def homepagelogo():
    exec(open(homepageguest.py).read())

photo = PhotoImage(file='logo.png')
btn = Button(root, image=photo, command=homepagelogo)
btn.place(x=540,y=0)

Welcometext = Label(root, text = 'Welcome to the Movie Recommendation System,')
Welcometext.place(x=30,y=40)

logintext = Label(root, text = 'Exit from the system')
logintext.place(x=1160, y=45)

photo1 = PhotoImage(file='logout.png')
btn1 = Button(root, image=photo1,command=homepagelogo)
btn1.place(x=1278,y=30)

img = ImageTk.PhotoImage(Image.open("advsearch.png"))
panel = Label(root, image = img)
panel.place(x=550,y=80)

img2 = ImageTk.PhotoImage(Image.open("Totles.png"))
panel2 = Label(root, image = img2)
panel2.place(x=30,y=80)

photo2 = PhotoImage(file='searchbytitle.png')
btn2 = Button(root, image=photo2, command=homepagelogo)
btn2.place(x=200,y=450)

photo3 = PhotoImage(file='advancedsearch.png')
btn3 = Button(root, image=photo3, command=homepagelogo)
btn3.place(x=650,y=370)

root.mainloop()
