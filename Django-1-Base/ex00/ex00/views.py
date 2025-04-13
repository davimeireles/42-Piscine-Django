from django.shortcuts import render
# Create your views here.


def show_markdown(request):
	return render(request, 'index.html')