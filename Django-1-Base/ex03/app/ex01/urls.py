from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_base_html, name='display_base_html'),
    path('django/', views.display_django_history, name='display_django_history'),
    path('display/', views.display_static_info, name='display_static_info'),
    path('templates/', views.display_template_engine, name='display_template_engine'),
]
