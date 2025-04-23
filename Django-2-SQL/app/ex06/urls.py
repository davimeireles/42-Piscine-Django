from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^init/?$', views.create_movies_table_ex06, name='create_movies_table_ex06'),
    re_path(r'^populate/?$', views.populate_table_movies, name='populate_table_movies'),
    re_path(r'^display/?$', views.display_movies_table, name='display_movies_table'),
    re_path(r'^update/?$', views.update_table_row, name='update_table_row'),
]
