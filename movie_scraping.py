# IMDb stands for Internet Movie Database. It is an online database of movies and television programmes

pip install imdb   #install if needed
from imdb import IMDb
movie = IMDb().get_movie('012346')
print(movie)
for i in movie["directors"]:
    print(i)
movies = IMDb().get_top250_movies()
for i in movies:
    print(i)
