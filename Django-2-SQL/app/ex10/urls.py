from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_table_ex10, name='display_table_ex10'),
]
