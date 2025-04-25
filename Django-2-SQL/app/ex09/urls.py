from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^display/?$', views.display_table_data, name='display_table_data'),
]
