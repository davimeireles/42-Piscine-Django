"""
URL configuration for d05 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, path
from . import views

urlpatterns = [
    path('', views.display_base_html, name='display_base_html'),
    re_path(r'^django/?$', views.display_django_history, name='display_django_history'),
    re_path(r'^display/?$', views.display_static_info, name='display_static_info'),
    re_path(r'^templates/?$', views.display_template_engine, name='display_template_engine'),
]
