from tkinter import *
from PIL import ImageTk, Image
import os
import time
from tkinter import Tk, Frame, Label, Button, LEFT, RIGHT, BOTTOM, TOP
from tkinter import ttk

#######advance search
from final3 import get_director, get_cast, get_genres, get_release_date, get_rating, get_age, get_mood

####general search
from final3 import get_title_from_index, get_director_from_index
from final3 import get_genres_from_index, get_index_from_title
from final3 import get_cast_from_index, get_movie_by_name, movie_properties

def main():
    global photo, img, img2, photologout
    photo = PhotoImage(file='logo2.png')
    btn = Button(root, image=photo)
    btn.place(x=400,y=0)

    #button5 = Button(root, text="ABOUT", fg='black', width=30, height=1)
    #button5.place(x=200,y=60)
    #button5 = Button(root, text="CONTACT", fg='black', width=30, height=1)
    #button5.place(x=540,y=60)

    def home():
        root.destroy()
        filename = 'homepageguest.py'
        os.system(filename)

    Welcometext = Label(root, text = 'Welcome ')
    Welcometext.place(x=0,y=40)

    logouttext = Label(root, text = 'To exit')
    logouttext.place(x=850, y=40)

    photologout = PhotoImage(file='logout.png')
    btn1 = Button(root, image=photologout, command=lambda:home())
    btn1.place(x=895,y=30)

    img = ImageTk.PhotoImage(Image.open("advsearch.png"))
    panel = Label(root, image = img)
    panel.place(x=550,y=100)

    img2 = ImageTk.PhotoImage(Image.open("Title.png"))
    panel2 = Label(root, image = img2)
    panel2.place(x=30,y=100)


def search(root):

    global phototitle, photoadv

    phototitle = PhotoImage(file='searchbytitle.png')
    button5 = Button(root, image=phototitle,command=main_name, fg='black')
    button5.place(x=120,y=400)

    photoadv = PhotoImage(file='advancedsearch.png')
    button5 = Button(root, image=photoadv,command=main_fun, fg='black')
    button5.place(x=670,y=400)

def main_name():
    global img
    destroy()

    img = ImageTk.PhotoImage(Image.open("sbtbanner.png"))
    panel = Label(root, image = img)
    panel.place(x=200,y=0)
    lbl22 = Label(root, text="Enter Movie Name",font=("Arial", 20),fg='black')
    lbl22.place(x=155, y=190)
    global name
    name = StringVar()
    entry_22 = Entry(root, width=40, textvariable=name)
    entry_22.place(x=400, y=200)

    btn22 = Button(root,text='Search',command=open_window3,width=10,height=1,bg="black",fg="white",font=("Arial", 15))
    btn22.place(x=660, y=190)

def open_window3():
    # print(type(name.get()))
    print(name.get())
    if name.get():
        temp1()
    else:
        root = Tk()
        root.title("OUTPUT")
        root.geometry("984x700")
        lbld2 = Label(root, text="You Have Not Enter Any Value",
                      font=("Arial Bold", 25),
                      fg='RED')
        lbld2.place(x=0, y=0)
    #destroy()

def temp1():
    lbl1 = Label(root, text="1.Similar Movies like " + name.get().title(),font=("Arial", 15), fg='black')
    lbl1.place(x=155, y=250)
    lbl1 = Label(root, text="2.Detail of " + name.get().title() + " movie", font=("Arial", 15), fg='black')
    lbl1.place(x=155, y=280)

    lbl1 = Label(root, text="Enter 1 for Similar Movies or 2 for Details of Movie",font=("Arial", 15), fg='black')
    lbl1.place(x=155, y=310)
    global val
    val = StringVar()
    entry_2 = Entry(root, width=36, textvariable=val)
    entry_2.place(x=610, y=315)

    btn22 = Button(root,text='Search',command=open_window4,width=10,bg="black",fg="white",font=("Arial Bold", 15))
    btn22.place(x=840, y=300)

def open_window4():
    v = val.get()
    if v:
        if v == '1':
            action_basis()
        elif v == '2':
            movie_name = name.get()
            x = movie_name.title()
            print(x)
            movie_index = int(get_index_from_title(x))
            print(movie_index)

            root = Tk()
            root.title("OUTPUT")
            root.geometry("984x700")
            print(movie_index)
            print(get_title_from_index(movie_index))
            try:
                print("asd")
                a, b, c, d, e, f, g, h, i, j, k, l, m = movie_properties(movie_index)
                print(a)
                print(b)

                lbla2 = Label(root,
                              text=str(
                                  j) + "\n" + a + "\n" + d + "\n" + b + "\n" + e + "\n" + f + "\n" + h + "\n" + i + "\n" + j + "\n" + k + "\n" + m + "\n",
                              font=("Arial Bold", 10),fg='black')
                lbla2.place(x=0, y=0)
                lbld23 = Label(root, text="Do you want to watch  " + name.get().title() + "  movie online ", font=("Arial", 15),fg='black')
                lbld23.place(x=155, y=320)
                btn22 = Button(root,text='Click Here',command=open_online,width=15, bg="black", fg="white",font=("Arial", 15))
                btn22.place(x=550, y=310)
            except:
                lbla3 = Label(root, text="Not Found",font=("Arial", 15),fg='black')
                lbla3.grid(row=1, column=0)


        else:
            root = Tk()
            root.title("OUTPUT")
            root.geometry("200x50")
            lbld4 = Label(root, text="Wrong Entry",font=("Arial", 15),fg='black')
            lbld4.place(x=0, y=0)



    else:
        root = Tk()
        root.title("OUTPUT")
        root.geometry("1200x700")
        lbld23 = Label(root, text="You Have Not Enter Any Value ",
                       font=("Arial Bold", 25),
                       fg='ORANGE')
        lbld23.place(x=0, y=0)
    # destroy()

def canvas():
    toolbar = Frame()
    toolbar.pack(side=TOP)




#####################################advance serch#################################################################################

def open_window1():
    destroy()
    name_system()

def open_window2():
    destroy()
    name_user()

def title():
    tops = Frame(root, width=100, height=100, bd=0, relief="raise")
    tops.place(x=40,relheight=0.2,relwidth=0.99)
    #tops.grid(row=0,column=1,columnspan=15)
    #tops.pack(side=BOTTOM)
     # tops.pack(anchor="ne")
    lbl = Label(tops,text="Welcome \n Movie Recommendation System",font=("Arial Bold", 40),fg='Blue')
    lbl.place(y=0)
    #lbl.grid(row=0, column=1)
    #lbl.pack(anchor='center')
    destroy()

def advance():
    global img, img1, img2
    img = ImageTk.PhotoImage(Image.open("advbanner.png"))
    panel = Label(root, image = img)
    panel.place(x=200,y=0)

    img1 = ImageTk.PhotoImage(Image.open("userpref.png"))
    panel = Label(root, image = img1)
    panel.place(x=520,y=180)

    img2 = ImageTk.PhotoImage(Image.open("details.png"))
    panel = Label(root, image = img2)
    panel.place(x=60,y=180)

    lbl2 = Label(root, text="On The Basis of Movie Details", font=("Arial", 13),fg='black')
    lbl2.place(x=60,y=500)
    btn2 = Button(root,text='Click',command=open_window1,width=15,bg="black",fg="white",font=("times 10", 15))
    btn2.place(x=300,y=490)

    lbl3 = Label(root, text="On The Basis Of User Preference",font=("Arial", 13),fg='black')
    lbl3.place(x=520,y=500)
    btn3 = Button(root,text='Click',command=open_window2,bg="black", width=15, fg="white", font=("times 10", 15))
    btn3.place(x=780,y=490)
    btn = Button(root, text='Homepage', font=("Arial", 15))
    btn.place(width=200, x=1350, y=0)

def destroy():
    for window in root.winfo_children():
        window.destroy()

def name_system():
    def action_director():
        root1= Tk()
        root1.title("OUTPUT")
        root1.geometry("984x700")
        lbld1 = Label(root1, text="List Of Movies On The Basis Of Director\n " + " " + "" + director.get(),font=("Arial", 15),fg='black')
        lbld1.grid(row=2, column=0)

        if director.get():
            df1, di = get_director(director.get())
            details(root1, df1, di)
        else:
            #destroy(root)
            lbld2 = Label(root1, text="You Have Not Enter Any Value",
                          font=("Arial Bold", 25),
                          fg='ORANGE')
            lbld2.grid(row=3, column=0)

    def action_cast():
        root1 = Tk()
        root1.title("OUTPUT")
        root1.geometry("1200x700")
        lblc1 = Label(root1, text="List Of Movies On The Basis Of Cast\n " + " " + "" + cast.get(),
                      font=("Arial Bold", 25),
                      fg='Red')
        lblc1.grid(row=2, column=0)

        if cast.get():
            df1, di = get_cast(cast.get())
            details(root, df1, di)
        else:
            lblc2 = Label(root1, text="You Have Not Enter Any Value",
                          font=("Arial Bold", 25),
                          fg='ORANGE')
            lblc2.grid(row=3, column=0)

    def action_rating():
        root1 = Tk()
        root1.title("OUTPUT")
        root1.geometry("1200x700")
        lblr1 = Label(root1, text="List Of Movies On The Basis Of Rating\n " + " " + "" + rating.get(),
                      font=("Arial Bold", 25),
                      fg='Red')
        lblr1.grid(row=2, column=0)

        if rating.get():
            df1, di = get_rating(rating.get())
            details(root1, df1, di)
        else:
            lblr2 = Label(root1, text="You Have Not Enter Any Value",
                          font=("Arial Bold", 25),
                          fg='ORANGE')
            lblr2.grid(row=3, column=0)

    def action_genres():
        root1 = Tk()
        root1.title("OUTPUT")
        root1.geometry("1200x700")
        lblg1 = Label(root1, text="List Of Movies On The Basis Of Genres\n " + " " + "" + genre.get(),
                      font=("Arial Bold", 25),
                      fg='Red')
        lblg1.grid(row=2, column=0)

        if genre.get():
            df1, di = get_genres(genre.get())
            details(root1, df1, di)
        else:
            lblg2 = Label(root1, text="You Have Not Enter Any Value",
                          font=("Arial Bold", 25),
                          fg='ORANGE')
            lblg2.grid(row=3, column=0)

    def action_release():
        get_release_date(release.get())
        root1 = Tk()
        root1.title("OUTPUT")
        root1.geometry("1200x700")
        lblrd1 = Label(root1, text="List Of Movies On The Basis Of Release Date\n " + " " + "" + release.get(),
                       font=("Arial Bold", 25),
                       fg='Red')
        lblrd1.grid(row=2, column=0)

        if release.get():
            df1, di = get_release_date(release.get())
            details(root1, df1, di)
        else:
            lblrd2 = Label(root1, text="You Have Not Enter Any Value",
                           font=("Arial Bold", 25),
                           fg='ORANGE')
            lblrd2.grid(row=3, column=0)

    def details(root, df1, di):
        if di:
            j = 0
            for i in di:
                i = int(i)
                j = j + 1
                try:
                    print(j)
                    a = "TITLE:" + df1.loc[i]['title']
                    b = "Director:" + df1.loc[i]['director']
                    c = "Release_date:" + df1.loc[i]['release_date']
                    e = "Genres:" + df1.loc[i]['genres']
                    f = "Cast:" + df1.loc[i]['cast']


                    lbla2 = Label(root,text=str(j) + "\n" + a + "\n" + c + "\n" + b + "\n" + e + "\n" + f + "\n",
                                  font=("Arial Bold", 10),
                                  fg='BLACK')
                    lbla2.grid(row=2 + j, column=0)

                except:
                    lbla3 = Label(root, text="Error",
                                  font=("Arial Bold", 25),
                                  fg='ORANGE')
                    lbla3.grid(row=j + 2, column=0)
        else:
            lbla3 = Label(root, text="Not Found",
                          font=("Arial Bold", 25),
                          fg='ORANGE')
            lbla3.grid(row=4, column=0)

    global img11
    img11 = ImageTk.PhotoImage(Image.open("basisofmovie.png"))
    panel = Label(root, image = img11)
    panel.place(x=200,y=0)

    lbl22 = Label(root, text="Search By Director",font=("Arial", 15),fg='black')
    lbl22.place(x=100,y=180)
    # lbl1.pack(anchor='nw')
    director = StringVar()
    entry_22 = Entry(root, width=46,textvariable=director)
    entry_22.place(x=300, y=180)
    # tops = Frame(root, width=1365, height=100, bd=3, relief="raise")

    btn22 = Button(root,text='Director',command=action_director,width=15,bg="black",fg="white", font=("Arial", 15))
    btn22.place(x=600, y=170)
    # btn2.pack(anchor="nw")

    lbl23 = Label(root, text="Search By Cast",font=("Arial", 15),fg='black')
    lbl23.place(x=100, y=220)
    # lbl1.pack(anchor='nw')
    cast = StringVar()
    entry_23 = Entry(root, width=46, textvariable=cast)
    entry_23.place(x=300, y=220)
    btn23 = Button(root,text='Cast',command=action_cast,width=15,bg="black",fg="white",font=("Arial", 15))
    btn23.place(x=600, y=210)
    # btn2.pack(anchor="nw")

    lbl24 = Label(root, text="Search By Rating", font=("Arial", 15), fg='black')
    lbl24.place(x=100, y=260)
    # lbl1.pack(anchor='nw')
    rating = StringVar()
    entry_24 = Entry(root, width=46, textvariable=rating)
    entry_24.place(x=300, y=260)
    btn24 = Button(root,text='Rating',command=action_rating,width=15,bg="black",fg="white",font=("Arial", 15))
    btn24.place(x=600, y=250)
    # btn2.pack(anchor="nw")

    lbl25 = Label(root, text="Search By Genres",font=("Arial", 15),fg='black')
    lbl25.place(x=100, y=300)
    # lbl1.pack(anchor='nw')
    genre = StringVar()
    entry_25 = Entry(root, width=46, textvariable=genre)
    entry_25.place(x=300, y=300)
    btn25 = Button(root,text='Genres',command=action_genres,width=15, bg="black", fg="white", font=("Arial", 15))
    btn25.place(x=600, y=290)
    # btn2.pack(anchor="nw")

    lbl26 = Label(root, text="Search By Release Date", font=("Arial", 15), fg='black')
    lbl26.place(x=100, y=340)
    # lbl1.pack(anchor='nw')
    release = StringVar()
    entry_26 = Entry(root, width=40, textvariable=release)
    entry_26.place(x=340, y=340)
    btn26 = Button(root,text='Release Date',command=action_release, width=15,bg="black",  fg="white", font=("Arial", 15))
    btn26.place(x=600, y=330)
    # btn2.pack(anchor="nw")

    btn27 = Button(root,text='Back',width=15,height='1', command=main_fun,font=("Arial", 15))
    btn27.place(x=340, y=380)

def name_user():
    def details(root, df1, di):
        if di:
            j = 0
            lbx = Listbox(root,height=100,width=104,
                          font=('verdena', 16), )

            lbx.insert(ACTIVE,'1')
            for i in di:
                i = int(i)
                j = j + 1
                lbx.insert(ACTIVE, j)
                try:
                    a = "       TITLE:" + df1.loc[i]['title']
                    lbx.insert(ACTIVE, a)
                    b = "       Director:" + df1.loc[i]['director']
                    lbx.insert(ACTIVE, b)
                    c = "       Release_date:" + df1.loc[i]['release_date']
                    lbx.insert(ACTIVE, c)
                    d = "       Rating:" + df1.loc[i]['vote_average']
                    lbx.insert(ACTIVE, d)
                    e = "       Genres:" + df1.loc[i]['genres']
                    lbx.insert(ACTIVE, e)
                    f = "       Cast:" + df1.loc[i]['cast']
                    lbx.insert(ACTIVE, f)
                    lbx.insert(ACTIVE,"\n ")


                    # lbla2 = Label(root,
                    #               text=str(j) + "\n" + a + "\n" + d + "\n" + c + "\n" + b + "\n" + e + "\n" + f + "\n",
                    #               font=("Arial Bold", 10),
                    #               fg='ORANGE')
                    # lbla2.pack(side=LEFT,fill="both",expand=True)
                   # lbx.insert(str(j),"\n"+ str(j) + "\n" + a + "\n" + d + "\n" + c + "\n" + b + "\n" + e + "\n" + f + "\n")




                except:
                    lbla3 = Label(root, text="",
                                  font=("Arial Bold", 25),
                                  fg='ORANGE')
                    lbla3.grid()

            lbx.grid(row=0,column=0)

            #sbr.config(root, command=lbx.yview)
            #lbx.config(yscrollcommand=sbr.set)


        else:
            lbla3 = Label(root, text="not found",
                          font=("Arial Bold", 25),
                          fg='ORANGE')
            lbla3.pack()


    def action_age():
        root1 = Tk()
        root1.title("OUTPUT")
        root1.geometry("1200x700")
        lbla1 = Label(root1, text="List Of Movies On The Basis Of Age\n " + " " + "Your age is" + "" + userName1.get(),
                      font=("Arial Bold", 25),
                      fg='Red')
        lbla1.grid()

        if userName1.get():
            df1, di = get_age(userName1.get())
            details(root1, df1, di)

        else:
            lbla2 = Label(root1, text="You Have Not Enter Any Value",
                          font=("Arial Bold", 25),
                          fg='ORANGE')
            lbla2.grid()


    def action_mood():
        root1 = Tk()
        root1.title("OUTPUT")
        root1.geometry("1200x700")
        lbla3 = Label(root1, text="List Of Movies On The Basis Of Mood\n " + "" + userName2.get() + "!!!",
                      font=("Arial Bold", 25),
                      fg='Red')
        lbla3.grid(row=2, column=0)
        if userName2.get():
            df1, di = get_mood(userName2.get())
            details(root1, df1, di)
        else:
            lbla3 = Label(root1, text="You Have Not Enter Any Value",
                          font=("Arial Bold", 25),
                          fg='ORANGE')
            lbla3.grid(row=3, column=0)

    global img12, img13, img14

    img12 = ImageTk.PhotoImage(Image.open("basisofuserpref.png"))
    panel = Label(root, image = img12)
    panel.place(x=200,y=0)
    # lbl1.pack(fill=BOTH,anchor='nw')

    img13 = ImageTk.PhotoImage(Image.open("age.png"))
    panel = Label(root, image = img13)
    panel.place(x=60,y=180)

    img14 = ImageTk.PhotoImage(Image.open("mood.png"))
    panel = Label(root, image = img14)
    panel.place(x=540,y=180)

    lbl12 = Label(root, text="Search By Age",font=("Arial", 15), fg='black')
    lbl12.place(x=40, y=500)
    # lbl1.pack(anchor='nw')
    userName1 = StringVar()
    entry_12 = Entry(root, width=20, textvariable=userName1)
    entry_12.place(x=180, y=500)
    # entry_1.pack(anchor='nw')
    btn12 = Button(root, text='Search',command=action_age, width=8, bg="black", fg="white",  font=("Arial", 15))
    btn12.place(x=360, y=490)
    # btn2.pack(anchor="nw")

    lbl13 = Label(root, text="Search By Mood", font=("Arial", 15), fg='black')
    lbl13.place(x=500, y=500)
    # lbl1.pack(anchor='nw')
    userName2 = StringVar()
    entry_13 = Entry(root, width=20, textvariable=userName2)
    entry_13.place(x=660, y=500)
    # entry_1.pack(anchor='nw')
    btn13 = Button(root, text='Search', command=action_mood,  width=8, bg="black",  fg="white", font=("Arial", 15))
    btn13.place(x=820, y=490)
    # btn2.pack(anchor="nw")

    btn = Button(root,text='Back to previous page',command=main_fun,font=("Arial", 15))
    btn.place(x=400,y=560)

def main_fun():
    destroy()
    title()
    advance()

##############################################general search#######################

def action_basis():
    lbl1 = Label(root, text="Search Similar Movie on the Basis of:",font=("Arial", 15),fg='black')
    lbl1.place(x=155, y=350)
    lbl1 = Label(root, text="1.Director",font=("Arial", 15),fg='black')
    lbl1.place(x=165, y=380)
    lbl1 = Label(root, text="2.Genres",font=("Arial", 15),fg='black')
    lbl1.place(x=165, y=410)
    lbl1 = Label(root, text="3.Keyword",font=("Arial", 15), fg='black')
    lbl1.place(x=165, y=440)
    lbl1 = Label(root, text="4.Cast", font=("Arial", 15), fg='black')
    lbl1.place(x=165, y=470)
    lbl1 = Label(root, text="5.Vote_average",font=("Arial", 15), fg='black')
    lbl1.place(x=165, y=500)
    lbl1 = Label(root, text="6.All Features",font=("Arial", 15),fg='black')
    lbl1.place(x=165, y=530)
    lbl1 = Label(root, text="Enter Number From 1 to 6",font=("Arial", 15),fg='black')
    lbl1.place(x=165, y=560)
    global num
    num = StringVar()
    entry_22 = Entry(root, width=36, textvariable=num)
    entry_22.place(x=410, y=565)
    btn22 = Button(root,text='Search',command=action_name,width=15,bg="black",fg="white", font=("Arial Bold", 15))
    btn22.place(x=640, y=550)
    global temp
    temp = num.get()



def open_online():
    import webbrowser
    webbrowser.open("https://www.123movies.to/")





def details(movie_index):
    af = int(val.get())
    bf = int(num.get())
    x = get_movie_by_name(name.get(), movie_index, af, bf)
    print(x)
    if x:
        root = Tk()
        root.title("OUTPUT")
        root.geometry("1200x700")
        j = 0
        i = 0
        for element in x:
            j = j + 1
            try:
                print(j)
                a = "title_name:" + get_title_from_index(element[0])
                b = "Type:" + get_genres_from_index(element[0])
                c = "Cast:" + get_cast_from_index(element[0])
                d = "Director:" + get_director_from_index(element[0]) + "\n"

                lbla2 = Label(root,
                              text=str(j) + "\n" + a + "\n" + d + "\n" + b + "\n" + c + "\n",
                              font=("Arial Bold", 10),
                              fg='ORANGE')
                lbla2.grid(row=2 + j, column=0)
                i = i + 1
                if i > 50:
                    break
            except:
                lbla3 = Label(root, text="Error",
                              font=("Arial Bold", 25),
                              fg='ORANGE')
                lbla3.grid(row=j + 1, column=0)
    else:
        lbla3 = Label(root, text="not found",
                      font=("Arial Bold", 25),
                      fg='ORANGE')
        lbla3.grid(row=3, column=0)

def action_name():
    a = name.get()
    n = num.get()
    if num.get():
        try:
            if n == '1' or n == '2' or n == '3' or n == '4' or n == '5' or n == '6':
                movie_index = int(get_index_from_title(a.title()))
                details(movie_index)
            else:
                root = Tk()
                root.title("OUTPUT")
                root.geometry("1200x700")
                lbld4 = Label(root, text="You Have Enter Wrong",
                              font=("Arial Bold", 25),
                              fg='ORANGE')
                lbld4.place(x=0, y=0)

        except:
            root = Tk()
            root.title("OUTPUT")
            root.geometry("1200x700")
            lbld2 = Label(root, text="Not Match",
                          font=("Arial Bold", 25),
                          fg='ORANGE')
            lbld2.grid(row=0, column=0)

    else:
        root = Tk()
        root.title("OUTPUT")
        root.geometry("1200x700")
        lbld2 = Label(root, text="You Have Not Enter Any Value",
                      font=("Arial Bold", 25),
                      fg='ORANGE')
        lbld2.grid(row=0, column=0)



if __name__ == '__main__':
    root = Tk()
    root.title("WatchMore")
    root.iconbitmap(r'logo.ico')
    root.geometry("984x700")

    menubar = Menu(root)
    root.config(menu=menubar)

    submenu = Menu(menubar)
    menubar.add_cascade(label='WatchMore', menu=submenu)
    submenu.add_command(label='Exit')

    searchtemp=1### assign variable to restrict showing multiple times search option
    search(root)
    main()
    root.mainloop()
