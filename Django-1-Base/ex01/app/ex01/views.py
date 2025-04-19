from django.shortcuts import render

# Create your views here.
def display_django_history(request):
	return render(request, 'django.html')

def display_static_info(request):
	return render(request, 'display.html')

def display_template_engine(request):
	return render(request, 'templates.html')