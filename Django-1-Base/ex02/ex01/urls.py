from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.display_base_html, name='display_base_html'),
    re_path(r'^django/?$', views.display_django_history, name='display_django_history'),
    re_path(r'^display/?$', views.display_static_info, name='display_static_info'),
    re_path(r'^templates/?$', views.display_template_engine, name='display_template_engine'),
]
