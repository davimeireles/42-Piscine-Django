from .models import Movies
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RemoveMovieForm

# Create your views here.
def populate_movies_ex05(request):
    try:
        movies = [
            ('1', 'The Phantom Menace', 'George Lucas', 'Rick McCallum', '1999-05-19'),
            ('2', 'Attack of the Clones', 'George Lucas', 'Rick McCallum', '2002-05-16'),
            ('3', 'Revenge of the Sith', 'George Lucas', 'Rick McCallum', '2005-05-19'),
            ('4', 'A New Hope', 'George Lucas', 'Rick McCallum', '1977-05-25'),
            ('5', 'The Empire Strikes Back', 'Irvin Kershner', 'Gary Kurtz', '1980-05-17'),
            ('6', 'Return of the Jedi', 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25'),
            ('7', 'The Force Awakens', 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11')
        ]

        response = []

        for movie in movies:
            try:
                movie = Movies(
                    episode_nb=movie[0],
                    title=movie[1],
                    director=movie[2],
                    producer=movie[3],
                    release_date=movie[4]
                    )
                movie.save()
                response.append('OK')
            except Exception as error:
                return HttpResponse(f'{error}')
        return HttpResponse("<br>".join(response))
    except Exception as error:
        return HttpResponse(f'{error}')
    

def display_movies_ex05(request):
    try:
        movies = Movies.objects.all()
        column_names = [field.name for field in Movies._meta.fields]
        html = "<html><body><h1>Movies</h1><table border='1'>"

        html += "<tr>"
        for column in column_names:
            html += f"<th>{column}</th>"
        html += "</tr>"

        for movie in movies:
            html += "<tr>"
            for column in column_names:
                value = getattr(movie, column)
                html += f"<td>{value}</td>"
            html += "</tr>"

        html += "</table></body></html>"

        return HttpResponse(html)
        
    except Exception as e:
        # Return "No data available" for any errors
        return HttpResponse("No data available")
    
def remove_movie_from_table(request):
    try:
        # Check if any movie exist
        if not Movies.objects.exists():
            return HttpResponse("No data available")
        
        if request.method == 'POST':
            form = RemoveMovieForm(request.POST)
            if form.is_valid():
                # Get the select movie title from the form
                selected_title = form.cleaned_data['title'].title

                # Get and delete the movie with that title
                movie = Movies.objects.get(title=selected_title)
                movie.delete()

                # Redirect to refresh the form
                return redirect('/ex05/remove')
        else:
            form = RemoveMovieForm()
        
        return render(request, 'remove_form.html', {'form': form})
    except Exception as error:
        return HttpResponse(f'{error}')

