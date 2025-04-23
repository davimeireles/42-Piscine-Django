from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^populate/?$', views.populate_movies_ex03, name='populate_movies_ex03'),
    re_path(r'^display/?$', views.display_movies_ex03, name='display_movies_ex03'),
]
