from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^populate/?$', views.populate_movies_ex07, name='populate_movies_ex07'),
    re_path(r'^display/?$', views.display_movies_ex07, name='display_movies_ex07'),
    re_path(r'^update/?$', views.update_table_row_ex07, name='update_table_row_ex07'),
]