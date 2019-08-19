from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()


menubar = Menu(root)
root.config(menu=menubar)

submenu = Menu(menubar)
menubar.add_cascade(label='WatchMore', menu=submenu)
submenu.add_command(label='Exit')

root.geometry('984x600')
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

advsearchtext = Label(root, text = 'Search Movies in Details here')
advsearchtext.place(x=400,y=70)

img = ImageTk.PhotoImage(Image.open("Cast.png"))
panel = Label(root, image = img)
panel.place(x=400,y=100)

img2 = ImageTk.PhotoImage(Image.open("directors.png"))
panel2 = Label(root, image = img2)
panel2.place(x=30,y=100)

img3 = ImageTk.PhotoImage(Image.open("Ratings.png"))
panel3 = Label(root, image = img3)
panel3.place(x=750,y=100)

img4 = ImageTk.PhotoImage(Image.open("genre.png"))
panel4 = Label(root, image = img4)
panel4.place(x=100,y=350)

img5 = ImageTk.PhotoImage(Image.open("reldates.png"))
panel5 = Label(root, image = img5)
panel5.place(x=600,y=350)




root.mainloop()
