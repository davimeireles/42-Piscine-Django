from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from .models import People, Planets, Movies
from .forms import Ex10form

# Create your views here.
def display_table_ex10(request):

    try:

        people_data = People.objects.all()
        planets_data = Planets.objects.all()
        movies_data = Movies.objects.all()

        if not people_data or not planets_data or not movies_data:
            raise Exception('No data available, please use the following command line before use: python3 manage.py loaddata ex10_initial_data.json')
    except Exception as error:
        return HttpResponse(f'{error}')

    try:
        if request.method == 'POST':
            form = Ex10form(request.POST)
            if form.is_valid():
                # Extract data from form
                min_date = form.cleaned_data['mov_min_release_date']
                max_date = form.cleaned_data['mov_max_release_date']
                min_diameter = form.cleaned_data['plan_diameter_grater_than']
                gender = form.cleaned_data['character_gender']

                # Query the database
                results = People.objects.filter(
                    gender=gender,
                    homeworld_diamater_gte=min_diameter,
                    movies_release_date_range=(min_date, max_date)
                ).select_related('homeworld').prefetch_related('movies')

                if not results.exists():
                    return HttpResponse('Nothing corresponding to your research')
                
                # Build the response
                response = []
                for person in results:
                    for movie in person.movies.all():
                        response.append(
                            f"{movie.title} - {person.name} - {person.gender} - {person.homeworld.name} - {person.homeworld.diameter}"
                        )
                return HttpResponse("<br>".join(response))
        else:
            form = Ex10form()
        
        return render(request, 'ex10_form.html', {'form': form})
    except Exception as error:
        return HttpResponse(f'{error}')