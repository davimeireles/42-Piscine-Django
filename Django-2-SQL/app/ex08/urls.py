from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^init/?$', views.init_tables_ex08, name='init_tables_ex08'),
    re_path(r'^populate/?$', views.populate_tables_ex08, name='populate_tables_ex08'),
    re_path(r'^populate2/?$', views.populate_table_with_psycopg_copy_from, name='populate_table_with_psycopg_copy_from'),
    re_path(r'^display/?$', views.display_table_sorted, name='display_table_sorted'),
]
