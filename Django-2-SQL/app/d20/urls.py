"""
URL configuration for d20 project.

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
from django.urls import re_path, path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^ex00/', include('ex00.urls')),
    re_path(r'^ex02/', include('ex02.urls')),
    re_path(r'^ex03/', include('ex03.urls')),
    re_path(r'^ex04/', include('ex04.urls')),
    re_path(r'^ex05/', include('ex05.urls')),
    re_path(r'^ex06/', include('ex06.urls')),
    re_path(r'^ex07/', include('ex07.urls')),
    re_path(r'^ex08/', include('ex08.urls')),
    re_path(r'^ex09/', include('ex09.urls')),
    re_path(r'^ex10/?', include('ex10.urls')),
]
