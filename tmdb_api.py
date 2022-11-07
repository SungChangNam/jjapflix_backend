import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jjapflix.settings')
import dotenv
dotenv.read_dotenv()
import django
django.setup()


import requests

from articles.models import Category, Movie

import json


lang = 'ko-KR'
page = 1
region = 'KR'
apikey = '92cc157f474166ebd92c78636aa052a4'


genre_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={apikey}&language={lang}'
genre_response = requests.get(genre_url).json().get('genres')


for name in genre_response:
    category = Category()
    category.id = name['id']
    category.name = name['name']
    category.save()

for i in range(1,11):
    movie_url = f'https://api.themoviedb.org/3/discover/movie?api_key={apikey}&language=ko-KR&sort_by=popularity.desc&include_adult=false&include_video=false&page={i}&with_watch_providers=providers%3A8&with_watch_monetization_types=flatrate'
    movie_response = requests.get(movie_url).json().get('results')
    
    for name in movie_response:
       
        movie = Movie()
        movie.title = name['title']
        movie.original_title = name['original_title']
        movie.rating = name['vote_average']
        movie.movie_id = name['id']
        movie.image = name['poster_path']
        movie.description = name['overview']
        movie.release_year = name['release_date']

        movie.save()

        for cate in name['genre_ids']:
            movie.category.add(cate)



