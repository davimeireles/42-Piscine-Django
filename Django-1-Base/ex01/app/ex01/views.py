from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display_django_history(request):
	return HttpResponse('display django history')

def display_static_info(request):
	return HttpResponse('display static info')

def display_template_engine(request):
	return HttpResponse('display template engine')