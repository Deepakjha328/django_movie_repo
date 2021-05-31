from django.db import models


class Movie(models.Model):
    movie_name = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    released = models.DateTimeField(auto_now_add=True)

    def get_name(self):
        return self.movie_name + ' is ' + self.description + ' movie.'

    def __repr__(self):
        return self.movie_name + 'is added.'