from django.test import TestCase
from ..models import Movie


class MovieTest(TestCase):
    """ Test module for Movie model """

    def setUp(self):
        Movie.objects.create(movie_name='balaji',description='best',released='2018-08-21')
        Movie.objects.create(movie_name='avtar',description='best',released='2018-08-20')





    def test_movie_detail(self):
        movie_balaji = Movie.objects.get(movie_name='balaji')
        movie_avtar = Movie.objects.get(movie_name='avtar')
        self.assertEqual(
            movie_balaji.get_name(), "balaji is best movie.")
        self.assertEqual(
            movie_avtar.get_name(), "avtar is best movie.")