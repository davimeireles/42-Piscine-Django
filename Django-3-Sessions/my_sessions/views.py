import random
import time
from d02 import settings
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def set_username(request):
    # Check if username and timestamp exist in the session
    current_time = time.time()
    username = request.session.get('username')
    timestamp = request.session.get('timestamp')

    # If no username or timestamp, or if 42 seconds have passed, generate a new username
    if not username or not timestamp or current_time - timestamp > settings.VALIDATION_TIME:
        username = random.choice(settings.AVAIBLE_NAMES)
        request.session['username'] = username
        request.session['timestamp'] = current_time
    
    # Display the username
    return render(request, 'index.html', {'choosen_name': username})

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')