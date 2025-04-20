import datetime
from d05 import settings
from ex02.forms import PersonForm
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.
def render_form(request):

    history = []

    # Load previous submissions from the file (persistent history)
    try:
        with open(settings.LOG_FILE_PATH, 'r') as file:
            for line in file.readlines():
                history.append(line.strip())
    except FileNotFoundError:
        pass

    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            # Get the cleaned data from the form
            name = form.cleaned_data['input_name']
            last_name = form.cleaned_data['input_last_name']
            age = form.cleaned_data['input_age']
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Format log to append
            log = f"[{timestamp}] Name: {name}, Last Name: {last_name}, Age: {age}"

            # Append to log file
            with open(settings.LOG_FILE_PATH, 'a') as file:
                file.write(log + '\n')
            
            # Add to the in-memory history for display
            history.append(log)

            return redirect(reverse('render_form'))
    else:
        form = PersonForm()
    return render(request, 'form.html', {'form': form, 'history': history})