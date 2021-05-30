from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/movie$', views.movie_list),
    url(r'^api/movie/(?P<pk>[0-9]+)$', views.movie_details),
    url(r'^api/movie/released$', views.movie_released)
]