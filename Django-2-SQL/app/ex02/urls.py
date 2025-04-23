from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^init/?$', views.create_movies_table_ex02, name='create_movies_table_ex02'),
    re_path(r'^populate/?$', views.populate_table_movies, name='populate_table_movies'),
    re_path(r'^display/?$', views.display_movies_table, name='display_movies_table'),
]
