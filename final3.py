##path where data set is stored
import sys
sys.path.append('D:\code\Pycharm\complete')

#################################################
##import library
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

###### ################################### #######

##get title from index
def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]

##get director name from index
def get_director_from_index(index):
    return df[df.index == index]["director"].values[0]

##get rating name from index
def get_vote_average_from_index(index):
    return df[df.index == index]["vote_average"].values[0]


#get generes from index
def get_genres_from_index(index):
    return df[df.index == index]["genres"].values[0]

#get release date from index
def get_release_date_from_index(index):
    return df[df.index == index]["release_date"].values[0]

##get cast name from index
def get_cast_from_index(index):
    return df[df.index == index]["cast"].values[0]

#################################################
def get_index_from_title(title):
    return df[df.title == title]["index"].values[0]


###############################################################################################################
###############################################################################################################
def function(movie_user_likes,movie_index,temp):
    ## Select Features
    features=[]


    if temp == 1:
        features.append("director")
    elif temp == 2:
        features.append("genres")
    elif temp == 3:
        features = ['budget', 'runtime', 'keyword']
    elif temp == 4:
        features.append("cast")
    elif temp == 5:
        features.append("vote_average")
    # elif temp==6:
    #     features.append("director")
    else:
        features = ['keywords', 'cast', 'genres', 'director']


    ##Step 3: Create a column in DF which combines all selected features
    for feature in features:
        df[feature] = df[feature].fillna('')

    def combine_features(row):
        try:
            if temp == 1:
                return row["director"]
            elif temp == 2:
                return row["genres"]
            elif temp == 3:
                return row["budget"]+" "+row["runtime"]+" "+row["keyword"]
            elif temp == 4:
                return row["cast"]
            elif temp == 5:
                return row["vote_average"]
            # elif temp==6:
            #     return row["director"]
            else:
                #return row['budget'] + " " + row['cast'] + " " + row["genres"] + " " + row["director"] + " " + row[ "vote_average"]+ " " + row[ "keyword"]
                return row['keywords'] + " " + row['cast'] + " " + row["genres"] + " " + row["director"]
        except:
            print("Error:", row)

    df["combined_features"] = df.apply(combine_features, axis=1)

    # print "Combined Features:", df["combined_features"].head()

    ## Create count matrix from this new combined column
    cv = CountVectorizer()

    count_matrix = cv.fit_transform(df["combined_features"])

    ## Compute the Cosine Similarity based on the count_matrix
    cosine_sim = cosine_similarity(count_matrix)



    # global variable
    movie_name = movie_user_likes.title()
    index = movie_index
    # print(movie_index)
    similar_movies = list(enumerate(cosine_sim[movie_index]))
    ##  Get a list of similar movies in descending order of similarity score
    sorted_similar_movie = sorted(similar_movies, key=lambda x: x[1], reverse=True)
    return sorted_similar_movie


def all_movies():
      #print("\nSearch by:\nTitle,Director,Cast,Genres\n")
      #tem=input("Enter column name:\t")
      temp=temp.lower()
      if temp=="title":
          a=list(df.title)
          # print(sorted(a))
          # print(a[1])
          # exit()
      elif temp=="director":
          a=list(df.director)
      elif temp=="cast":
          a=list(df.cast)
      elif temp=="genres":
          a=list(df.genres)
      # elif temp=="keywords":
      #     a=list(df.keywords)
      else:
          a=["Not_found"]
      j=0
      for i in a:
          j=j+1
          if i:
              print(j,i)
          else:
              print("Not Found")


def movie_properties(movie_index):
    ####print the detail of movie name enter by user

    a = "Title:" + get_title_from_index(movie_index)
    b = "Budget:" + df.budget[movie_index]
    c = "Overview:" + df.overview[movie_index]
    d = "Genres:" + df.genres[movie_index]
    e = "Homepage:" + df.homepage[movie_index]
    f = "Keywords: " + df.keywords[movie_index]
    g = "Crew: " + df.crew[movie_index]
    h = "Cast: " + df.cast[movie_index]
    i = "Tagline:" + df.tagline[movie_index]
    j = "Runtime: " + df.runtime[movie_index]
    k = "Vote_average:" + df.vote_average[movie_index]
    l = "Rroduction_companies:" + df.production_companies[movie_index]
    m = "Rroduction_countries:" + df.production_countries[movie_index]

    return a,b,c,d,e,f,g,h,i,j,k,l,m


def get_movie_by_name(movie_name,movie_index,ab,temp):
    abs=int(ab)
    print(abs)

    if abs == 1:
        sorted_similar_movies=function(movie_name,movie_index,temp)
        return sorted_similar_movies


##to get title from director name
def get_director(director_name):
    df1 = df.iloc[:, :24]
    di = list(df1.loc[df1['director'] == director_name.title()]["index"])
    if di:
        return df1, di
    else:
        return 0, 0


##to get title from Cast):
def get_cast(cast_name):
    df1 = df.iloc[:, :24]
    di = list(df1.loc[df1['cast'] == cast_name.title()]["index"])
    if di:
        return df1,di
    else:
        return 0, 0

##to get title from releasing date
def get_release_date(date):
    df1 = df.iloc[:, :24]
    di = list(df1.loc[df1['release_date'] == date.title()]["index"])
    if di:
        return df1, di
    else:
        return 0, 0

####to get title from genres
def get_genres(type):

    df1 = df.iloc[:, :24]
    di = list(df1.loc[df1['genres'] == type.title()]["index"])
    if di:
        return df1, di
    else:
        return 0,0

####to get title from age
def get_age(ages):
   # age = input("Enter your age:\t")
    age=int(ages)
    print("hello")
    if age < 16:
        type='Comedy'
        type=str(type)
    elif age > 15 and age < 30:
         type="Adventure"
    elif age > 29 and age < 40:
         type = "Thriller"
    elif age >39 and age < 100:
         type="Drama"
    else:
        type= 0
    if type:
        df1 = df.iloc[:, :24]
        di = list(df1.loc[df1['genres'] == type]["index"])

        return df1, di
    else:
        return 0,0

def get_mood(mood):
   # print("Happy,Sad,Romantic,Fear")
    #mood = input("Enter your mood:\t")
    mood=mood.lower()
    if mood =="action":
         type='Action'
    elif mood== 'adventure' :
         type="Adventure Action Science Fiction"
    elif mood=='romance':
         type = "Romance"
    elif mood=='fear':
         type="Horror Thriller"
    elif mood=='drama':
         type="Drama"
    elif mood=='comedy':
         type="Comedy"
    elif mood=='science fiction':
         type="Science Fiction"
    elif mood == 'thriller':
        type = "Thriller"
    else:
        type= 0
    if type:
        df1 = df.iloc[:, :24]
        di = list(df1.loc[df1['genres'] == type]["index"])

        return df1,di
###to get title from rating(vote_average)
def get_rating(rating):
    df1 = df.iloc[:, :24]
    di = list(df1.loc[df1['vote_average'] == rating.title()]["index"])
    if di:
        return df1, di
    else:
        return 0, 0


###############################################################################################################
###############################################################################################################

## Read CSV File
df = pd.read_csv("movie_dataset.csv")
# print df.colum

###global variabe
movie_name = 0
index = 0

######################################    main function   #########################################

def name_enter(movie_user_likes ):

    movie_index = int(get_index_from_title(movie_user_likes.title()))

    try:
        get_movie_by_name(movie_user_likes, movie_index)
    except:
        print("Movie does not match:")
        exit()


print("###########################  MOVIE RECOMMENDATION SYSTEM    ##########################\n\n")
