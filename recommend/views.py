from django.shortcuts import render, redirect
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from articles.models import Movie, Category, Taste
from django.db.models import Max
from recommend.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

trends = pd.read_csv('recommend/trend.csv')
netflix = pd.read_csv('recommend/netflix.csv')

movie_ratings = pd.merge(trends, netflix, on='movie_id')

user_title = movie_ratings.pivot_table('rating_x', index='title', columns='user_id')
user_title = user_title.fillna(0)

item_based_collab = cosine_similarity(user_title, user_title)
item_based_collab = pd.DataFrame(item_based_collab, index=user_title.index, columns=user_title.index)


def item_based_filtering(movie):
        movie_list = item_based_collab[movie].sort_values(ascending=False)[1:21]
        print(movie_list)
        return movie_list.index
class TasteView(APIView):
    
    def get(self, request, movie_title):
        item_based_filtering(movie_title)
        movie = get_object_or_404(Movie, id=movie_title)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MovieRefresh(APIView):  #영화리스트(노우석님)
    def get(self, request):
        movie = Movie.objects.filter(rating__gt=3.5).order_by('?')
        movie = list(movie)[0:10]
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)