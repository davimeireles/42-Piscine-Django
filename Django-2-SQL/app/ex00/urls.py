from django.urls import path
from . import views

urlpatterns = [
    path('init/', views.create_movies_table, name='create_movies_table'),
]
