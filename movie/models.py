from django.db import models


class Movie(models.Model):
    movie_name = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    released = models.DateField()