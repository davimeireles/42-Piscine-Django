from django.urls import path
from . import views

urlpatterns = [
	path('', views.render_form, name='render_form'),
    path('form/', views.render_form, name='render_form'),
]