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
    photo = PhotoImage(file='logo.png')
    btn = Button(root, image=photo)
    btn.place(x=540,y=0)

    #button5 = Button(root, text="ABOUT", fg='black', width=30, height=1)
    #button5.place(x=200,y=60)
    #button5 = Button(root, text="CONTACT", fg='black', width=30, height=1)
    #button5.place(x=540,y=60)

    def home():
        root.destroy()
        filename = 'homepageguest.py'
        os.system(filename)

    Welcometext = Label(root, text = 'Welcome to Movie Recommendation System ')
    Welcometext.place(x=30,y=50)

    logouttext = Label(root, text = 'To exit the system')
    logouttext.place(x=1100, y=50)

    photologout = PhotoImage(file='logout.png')
    btn1 = Button(root, image=photologout, command=lambda:home())
    btn1.place(x=1200,y=40)

    img = ImageTk.PhotoImage(Image.open("advsearch.png"))
    panel = Label(root, image = img)
    panel.place(x=740,y=100)

    img2 = ImageTk.PhotoImage(Image.open("Totles.png"))
    panel2 = Label(root, image = img2)
    panel2.place(x=30,y=100)


def search(root):

    global phototitle, photoadv

    phototitle = PhotoImage(file='searchbytitle.png')
    button5 = Button(root, image=phototitle,command=main_name, fg='black')
    button5.place(x=200,y=450)

    photoadv = PhotoImage(file='advancedsearch.png')
    button5 = Button(root, image=photoadv,command=main_fun, fg='black')
    button5.place(x=950,y=450)

    generaltext = Label(root,font=("Arial",12), text = 'When to use General Search feature? \n This feature is helpful if you know the name of a movie and \n want to watch similar movies like them. You can also see the \n details of the movie and search for similar movies.')
    generaltext.place(x=100,y=500)

    advancedtext = Label(root,font=("Arial",12), text = 'When to use Advanced Search feature? \n This feature is useful if you do not know the name of a movie \n that you want to watch. You will be asked to input movie attributes \n like name of director, genre, age, mood, e.t.c and the system \n  will show output based on your preference.')
    advancedtext.place(x=820,y=500)


def main_name():
    global img
    destroy()
    img = ImageTk.PhotoImage(Image.open("sbtbanner.png"))
    panel = Label(root, image = img)
    panel.place(x=0,y=0)
    lbl22 = Label(root, text="Enter Movie Name",font=("Arial", 20),fg='black')
    lbl22.place(x=255, y=220)
    global name
    name = StringVar()
    entry_22 = Entry(root, width=40, textvariable=name)
    entry_22.place(x=500, y=230)

    btn22 = Button(root,text='Search',command=open_window3,width=10,height=1,bg="black",fg="white",font=("Arial", 15))
    btn22.place(x=760, y=220)

    #btn27 = Button(root,text='Go Back',width=15,height='1', command=main,bg="black", fg="white", font=("Arial", 15))
    #btn27.place(x=540, y=650)


def open_window3():
    # print(type(name.get()))
    print(name.get())
    if name.get():
        temp1()
    else:
        root = Tk()
        root.title("OUTPUT")
        root.state('zoomed')
        lbld2 = Label(root, text="You Have Not Enter Any Value",font=("Arial Bold", 25),fg='RED')
        lbld2.place(x=0, y=0)
    #destroy()

def temp1():
    lbl1 = Label(root, text="1. Similar Movies like " + name.get().title(),font=("Arial", 15), fg='black')
    lbl1.place(x=255, y=270)
    lbl1 = Label(root, text="2. Details of " + name.get().title() + " movie", font=("Arial", 15), fg='black')
    lbl1.place(x=255, y=300)

    btn22 = Button(root,text='Search',command=open_window5,width=10, height=1,bg="black",fg="white",font=("Arial Bold", 15))
    btn22.place(x=650, y=260)

    btn22 = Button(root,text='Search',command=open_window4,width=10,height=1,bg="black",fg="white",font=("Arial Bold", 15))
    btn22.place(x=650, y=300)



def open_window5():
    action_basis()

def open_window4():
    movie_name = name.get()
    x = movie_name.title()
    print(x)
    movie_index = int(get_index_from_title(x))
    print(movie_index)

    root = Tk()
    root.title("OUTPUT")
    root.state('zoomed')
    print(movie_index)
    print(get_title_from_index(movie_index))
    try:
        print("asd")
        a, b, c, d, e, f, g, h, i, j, k, l, m = movie_properties(movie_index)

        lbla2 = Label(root,
                      text=str(
                          j) + "\n" + a + "\n" + d + "\n" + b + "\n" + e + "\n" + f + "\n" + h + "\n" + i + "\n" + j + "\n" + k + "\n" + m + "\n",
                      font=("Arial Bold", 10), fg='black')
        lbla2.place(x=0, y=0)
        lbld23 = Label(root, text="Do you want to watch  " + name.get().title() + "  movie online ", font=("Arial", 15),
                       fg='black')
        lbld23.place(x=155, y=320)
        btn22 = Button(root, text='Click Here', command=open_online, width=15, bg="black", fg="white",
                       font=("Arial", 15))
        btn22.place(x=550, y=310)
    except:
        lbla3 = Label(root, text="Not Found", font=("Arial", 15), fg='black')
        lbla3.grid(row=1, column=0)





    # destroy()

def canvas():
    toolbar = Frame()
    toolbar.pack(side=TOP)




#####################################avance serch#################################################################################

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
    panel.place(x=0,y=0)

    img1 = ImageTk.PhotoImage(Image.open("userpref.png"))
    panel = Label(root, image = img1)
    panel.place(x=800,y=220)

    img2 = ImageTk.PhotoImage(Image.open("details.png"))
    panel = Label(root, image = img2)
    panel.place(x=200,y=220)

    lbl2 = Label(root, text="On The Basis of Movie Details", font=("Arial", 13),fg='black')
    lbl2.place(x=200,y=500)
    btn2 = Button(root,text='Click',command=open_window1,width=15,bg="black",fg="white",font=("times 10", 15))
    btn2.place(x=430,y=490)

    lbl3 = Label(root, text="On The Basis Of Movie Preference",font=("Arial", 13),fg='black')
    lbl3.place(x=800,y=500)
    btn3 = Button(root,text='Click',command=open_window2,bg="black", width=15, fg="white", font=("times 10", 15))
    btn3.place(x=1060,y=490)
    btn = Button(root, text='Homepage', font=("Arial", 15))
    btn.place(width=200, x=1350, y=0)

    generaltext = Label(root,font=("Arial",12), text = 'When to use this feature? \n This feature is helpful if you know the name of a director, gemre, release date,\n cast e.t.c and want to watch similar movies like them. You can simply give genre \n(Action) and the system will give you output based on your preferred genre.')
    generaltext.place(x=100,y=550)

    advancedtext = Label(root,font=("Arial",12), text = 'When to use this feature? \n This feature helps you to search and recommend movies according to your age or movie \n preference. Search by age is not a precise method but a simple guess about \n about what kind of movie certain aged person can like.')
    advancedtext.place(x=720,y=550)


    #btn27 = Button(root,text='Back',width=15,height='1',bg="black", fg="white", command=main,font=("Arial", 15))
    #btn27.place(x=620, y=650)

def destroy():
    for window in root.winfo_children():
        window.destroy()

def name_system():
    def action_director():
        root1= Tk()
        root1.title("OUTPUT")
        root.state('zoomed')
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
        print(di)
        if di:
            j = 0
            lbx = Listbox(root, height=100, width=104,
                          font=('verdena', 16), )

            lbx.insert(ACTIVE, '1')
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
                    e = "       Genres:" + df1.loc[i]['genres']
                    lbx.insert(ACTIVE, e)
                    f = "       Cast:" + df1.loc[i]['cast']
                    lbx.insert(ACTIVE, f)
                    lbx.insert(ACTIVE, "\n ")


                    # lbla2 = Label(root,text=str(j) + "\n" + a + "\n" + c + "\n" + b + "\n" + e + "\n" + f + "\n",
                    #               font=("Arial Bold", 10),
                    #               fg='BLACK')
                    # lbla2.grid(row=2 + j, column=0)

                except:
                    lbla3 = Label(root, text="",
                                  font=("Arial Bold", 25),
                                  fg='ORANGE')
                    lbla3.grid(row=j + 2, column=0)

            lbx.grid(row=0, column=0)
        else:
            lbla3 = Label(root, text="Not Found",
                          font=("Arial Bold", 25),
                          fg='ORANGE')
            lbla3.grid(row=4, column=0)

    global img11
    img11 = ImageTk.PhotoImage(Image.open("basisofmovie.png"))
    panel = Label(root, image = img11)
    panel.place(x=0,y=0)

    lbl22 = Label(root, text="Search By Director",font=("Arial", 15),fg='black')
    lbl22.place(x=300,y=220)
    # lbl1.pack(anchor='nw')
    director = StringVar()
    entry_22 = Entry(root, width=44,textvariable=director)
    entry_22.place(x=500, y=220)
    # tops = Frame(root, width=1365, height=100, bd=3, relief="raise")

    btn22 = Button(root,text='Director',command=action_director,width=15,bg="black",fg="white", font=("Arial", 15))
    btn22.place(x=780, y=210)
    # btn2.pack(anchor="nw")

    lbl23 = Label(root, text="Search By Cast",font=("Arial", 15),fg='black')
    lbl23.place(x=300, y=280)
    # lbl1.pack(anchor='nw')
    cast = StringVar()
    entry_23 = Entry(root, width=44, textvariable=cast)
    entry_23.place(x=500, y=280)
    btn23 = Button(root,text='Cast',command=action_cast,width=15,bg="black",fg="white",font=("Arial", 15))
    btn23.place(x=780, y=270)
    # btn2.pack(anchor="nw")

    lbl24 = Label(root, text="Search By Rating", font=("Arial", 15), fg='black')
    lbl24.place(x=300, y=340)
    # lbl1.pack(anchor='nw')
    rating = StringVar()
    entry_24 = Entry(root, width=44, textvariable=rating)
    entry_24.place(x=500, y=340)
    btn24 = Button(root,text='Rating',command=action_rating,width=15,bg="black",fg="white",font=("Arial", 15))
    btn24.place(x=780, y=330)
    # btn2.pack(anchor="nw")

    lbl25 = Label(root, text="Search By Genres",font=("Arial", 15),fg='black')
    lbl25.place(x=300, y=400)
    # lbl1.pack(anchor='nw')
    genre = StringVar()
    entry_25 = Entry(root, width=44, textvariable=genre)
    entry_25.place(x=500, y=400)
    btn25 = Button(root,text='Genres',command=action_genres,width=15, bg="black", fg="white", font=("Arial", 15))
    btn25.place(x=780, y=390)
    # btn2.pack(anchor="nw")

    lbl26 = Label(root, text="Search By Release Date", font=("Arial", 15), fg='black')
    lbl26.place(x=300, y=460)
    # lbl1.pack(anchor='nw')
    release = StringVar()
    entry_26 = Entry(root, width=40, textvariable=release)
    entry_26.place(x=550, y=460)
    btn26 = Button(root,text='Release Date',command=action_release, width=15,bg="black",  fg="white", font=("Arial", 15))
    btn26.place(x=800, y=450)
    # btn2.pack(anchor="nw")

    btn27 = Button(root,text='Go Back',width=15,height='1', command=main_fun,font=("Arial", 15))
    btn27.place(x=540, y=500)

def name_user():
    def details(root, df1, di):
        if di:
            j = 0
            lbx = Listbox(root, height=100, width=104,
                          font=('verdena', 16), )
            lbx.insert(ACTIVE, '1')
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
                    lbx.insert(ACTIVE, "\n ")


                except:
                    lbla3 = Label(root, text="",
                                  font=("Arial Bold", 25),
                                  fg='ORANGE')
                    lbla3.grid()

            lbx.grid(row=0, column=0)

            # sbr.config(root, command=lbx.yview)
            # lbx.config(yscrollcommand=sbr.set)


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
        lbla1.grid(row=1, column=0)

        if userName1.get():
            df1, di = get_age(userName1.get())
            a="age"
            details(root1, df1, di)
        else:
            lbla2 = Label(root1, text="You Have Not Enter Any Value",
                          font=("Arial Bold", 25),
                          fg='ORANGE')
            lbla2.grid(row=3, column=0)

    def action_mood():
        root1 = Tk()
        root1.title("OUTPUT")
        root1.geometry("1200x700")
        lbla3 = Label(root1, text="List Of Movies On The Basis Of Mood\n " + "" + userName2.get() + "!!!",
                      font=("Arial Bold", 25),
                      fg='Red')
        lbla3.grid(row=1, column=0)
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
    panel.place(x=0,y=0)
    # lbl1.pack(fill=BOTH,anchor='nw')

    img13 = ImageTk.PhotoImage(Image.open("age.png"))
    panel = Label(root, image = img13)
    panel.place(x=200,y=220)

    img14 = ImageTk.PhotoImage(Image.open("mood.png"))
    panel = Label(root, image = img14)
    panel.place(x=750,y=220)

    lbl12 = Label(root, text="Search By Age",font=("Arial", 15), fg='black')
    lbl12.place(x=200, y=500)
    # lbl1.pack(anchor='nw')
    userName1 = StringVar()
    entry_12 = Entry(root, width=20, textvariable=userName1)
    entry_12.place(x=340, y=505)
    # entry_1.pack(anchor='nw')
    btn12 = Button(root, text='Search',command=action_age, width=8, bg="black", fg="white",  font=("Arial", 15))
    btn12.place(x=500, y=490)
    # btn2.pack(anchor="nw")

    lbl13 = Label(root, text="Search By Mood", font=("Arial", 15), fg='black')
    lbl13.place(x=750, y=500)
    # lbl1.pack(anchor='nw')
    userName2 = StringVar()
    entry_13 = Entry(root, width=20, textvariable=userName2)
    entry_13.place(x=920, y=505)
    # entry_1.pack(anchor='nw')
    btn13 = Button(root, text='Search', command=action_mood,  width=8, bg="black",  fg="white", font=("Arial", 15))
    btn13.place(x=1060, y=490)
    # btn2.pack(anchor="nw")
    generaltext = Label(root,font=("Arial",12), text = 'When to use Search By Age feature? \n This is not a precise feature but a simple guess about  \n a certain aged person. You can simply provide age and the system\n will provide you some movies accordingly.')
    generaltext.place(x=100,y=550)

    advancedtext = Label(root,font=("Arial",12), text = 'When to use Search by Mood feature? \n This feature is useful if you know what kind of movies you want to watch. \n For example: if you are in a mood to watch action movies then enter action and \n the system will recommend you some action movies. This is \n also a kind of Search by Genre.')
    advancedtext.place(x=720,y=550)

    btn = Button(root,text='Go Back',command=main_fun,bg="black", fg="white", font=("Arial", 15))
    btn.place(x=630,y=650)

def main_fun():
    destroy()
    title()
    advance()

##############################################general search#######################

def action_basis():
    lbl1 = Label(root, text="Search Similar Movie on the Basis of:",font=("Arial", 15),fg='black')
    lbl1.place(x=255, y=350)
    lbl1 = Label(root, text="1.Director",font=("Arial", 15),fg='black')
    lbl1.place(x=265, y=380)
    lbl1 = Label(root, text="2.Genres",font=("Arial", 15),fg='black')
    lbl1.place(x=265, y=410)

    lbl1 = Label(root, text="3.Keyword",font=("Arial", 15), fg='black')
    lbl1.place(x=265, y=440)

    lbl1 = Label(root, text="4.Cast", font=("Arial", 15), fg='black')
    lbl1.place(x=265, y=470)

    lbl1 = Label(root, text="5.Vote Average",font=("Arial", 15), fg='black')
    lbl1.place(x=265, y=500)

    lbl1 = Label(root, text="6.All Features",font=("Arial", 15),fg='black')
    lbl1.place(x=265, y=530)

    lbl1=Label(root,text="Enter number from 1 to 6",font=("Arial",15),fg='black')
    lbl1.place(x=265,y=560)
    global num
    num=StringVar()
    entry_22=Entry(root,width=36,textvariable=num)
    entry_22.place(x=500,y=565)
    btn22=Button(root,text='search',command=action_name,width=15,bg='black',fg='white',font=("Arial Bold",15))
    btn22.place(x=800,y=550)
    global temp
    temp=num.get()




def open_online():
    import webbrowser
    webbrowser.open("https://www.123movies.to/")





def details(movie_index):
    af = 1
    bf = int(num.get())
    x = get_movie_by_name(name.get(), movie_index, af, bf)
    print(x)
    if x:
        root = Tk()
        root.title("OUTPUT")
        root.geometry("1200x700")
        j = 0
        i = 0
        lbx = Listbox(root, height=100, width=104,
                      font=('verdena', 16), )

        lbx.insert(ACTIVE, '1')
        for element in x:
            j = j + 1
            lbx.insert(ACTIVE, j)
            try:

                a = "title_name:" + get_title_from_index(element[0])
                lbx.insert(ACTIVE, a)
                b = "Type:" + get_genres_from_index(element[0])
                lbx.insert(ACTIVE, b)
                c = "Cast:" + get_cast_from_index(element[0])
                lbx.insert(ACTIVE, c)
                d = "Director:" + get_director_from_index(element[0])
                lbx.insert(ACTIVE, d)
                lbx.insert(ACTIVE, "\n ")

                # lbla2 = Label(root,
                #               text=str(j) + "\n" + a + "\n" + d + "\n" + b + "\n" + c + "\n",
                #               font=("Arial Bold", 10),
                #               fg='Black')
                # lbla2.grid(row=2 + j, column=0)
                i = i + 1
                if i > 50:
                    break
            except:
                lbla3 = Label(root, text="Error",
                              font=("Arial Bold", 25),
                              fg='ORANGE')
                lbla3.grid(row=j + 1, column=0)
        lbx.grid(row=0, column=0)
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
    root.state('zoomed')

    menubar = Menu(root)
    root.config(menu=menubar)

    submenu = Menu(menubar)
    menubar.add_cascade(label='WatchMore', menu=submenu)
    submenu.add_command(label='Exit')

    searchtemp=1### assign variable to restrict showing multiple times search option
    search(root)
    main()
    root.mainloop()
