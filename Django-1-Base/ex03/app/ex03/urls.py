from django.urls import path
from . import views

urlpatterns = [
    path('', views.draw_table, name='draw_table'),
]