from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^populate/?$', views.populate_movies_ex05, name='populate_movies_ex05'),
    re_path(r'^display/?$', views.display_movies_ex05, name='display_movies_ex05'),
    re_path(r'^remove/?$', views.remove_movie_from_table, name='remove_movie_from_table'),
]
