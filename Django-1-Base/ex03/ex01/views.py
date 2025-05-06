from django.shortcuts import render

# Create your views here.
def display_base_html(request):
	return render(request, 'base.html')

def display_django_history(request):
	return render(request, 'ex01/templates/django.html')

def display_static_info(request):
	return render(request, 'ex01/templates/display.html')

def display_template_engine(request):
	return render(request, 'ex01/templates/templates.html')