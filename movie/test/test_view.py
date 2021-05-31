import json
from rest_framework import status
from django.test import TestCase, Client
from ..models import Movie
from ..serializers import MovieSerializer


# initialize the APIClient app
client = Client()

class GetAllMovieTest(TestCase):
    """ Test module for GET all movieAPI """

    def setUp(self):
        Movie.objects.create(movie_name='balaji',description='best',released='2019-08-19')
        Movie.objects.create(movie_name='avtar',description='best',released='2018-08-20')
        Movie.objects.create(movie_name='pink',description='best',released='2019-08-20')
        Movie.objects.create(movie_name='bahubali',description='best',released='2017-08-20')

    def test_get_all_movie(self):
        # get API response
        response = client.get('movie_list')
        # get data from db
        movie = Movie.objects.all()
        movie_serializer = MovieSerializer(movie, many=True)
        self.assertEqual(response.data, movie_serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)




