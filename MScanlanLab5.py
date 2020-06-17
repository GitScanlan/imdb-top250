## Michael Scanlan
## Everything has been completed

import imdb

ia = imdb.IMDb()
top250 = ia.get_top250_movies()
movie_title = [] #we use a list at the beginning as a way to neatly store the movie titles
moviedict = {}

for x in range(250):
    movie_title.append(str(top250[x])) #this performs a loop through the top250 movies, adding them to a list

while True: #program will always run
    user = input("Please provide a movie title that you would like to know the plot of.")
    if user in movie_title: #this checks whether or not the user's submitted movie is in our list
        movie_name = user
        movies = ia.search_movie(movie_name) #this searches for the user's movie of choice
        movie = movies[0]
        ia.update(movie, info= ['plot']) #this updates the user's movie with a plot
        moviedict[user] = movie['plot'] # we add the user's movie to the dictionary as user's movie of choice : plot of that movie
        print(moviedict) #this prints the dictionary as movie : plot
        final = int(input("Would you like to search for another movie? Type 1 for yes or 2 for no.")) #we ask the user whether they want to search for other plots
        if final == 1:
            continue #if the user wants to look for more plots, we restart from the beginning
        if final == 2:
            break #if the user is happy and doesn't want to continue, we break/end the loop
    else:
        print("Sorry, that is not a valid movie title. Please try again.") #this only prints if the user submits a title that either isn't a top 250 movie, or if they didn't spell it exactly as the IMDb website indicts it as
        break
