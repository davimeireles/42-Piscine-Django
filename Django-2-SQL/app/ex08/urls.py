from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^init/?$', views.init_tables_ex08, name='init_tables_ex08'),
    re_path(r'^populate/?$', views.populate_tables_ex08, name='populate_tables_ex08'),
    #re_path(r'^display/?$'),
]
