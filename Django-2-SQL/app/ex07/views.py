from .models import Movies
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

# Create your views here.
def populate_movies_ex07(request):
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
    

def display_movies_ex07(request):
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
    
def update_table_row_ex07(request):
    try:
        # Get all titles from the table
        titles = Movies.objects.values_list('title', flat=True)

        if request.method == 'POST':
            # Get the selected title and the new opening crawl text from the form
            selected_title = request.POST.get('title')
            new_craw_text = request.POST.get('craw_text')

            # Get the specific title
            row_to_update = Movies.objects.filter(title=selected_title)
            row_to_update.update(opening_crawl=new_craw_text, updated=timezone.now())
            return redirect('/ex07/update')
        return render(request, 'update_table_row.html', {'titles': titles})
    except Exception as e:
        return HttpResponse('No data avaible')