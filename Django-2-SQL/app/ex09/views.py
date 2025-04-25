from django.http import HttpResponse
from .models import Planets, People
from django.utils.html import escape
from django.db.models import Q

# Create your views here.
def display_table_data(request):
    try:
        people_data = People.objects.all()
        planets_data = Planets.objects.all()

        if not people_data or not planets_data:
            raise Exception('No data available, please use the following command line before use: python3 manage.py loaddata ex09_initial_data.json')
        
        windy_planets = Planets.objects.filter(
            Q(climate__icontains='windy')
            )
        
        if not windy_planets.exists():
            raise Exception('No data avaible for windy planets')
        
        people_from_windy_planets = People.objects.filter(
            homeworld__in = windy_planets
        ).order_by('name')
        
        if not people_from_windy_planets.exists():
            raise Exception('No data avaible for people from windy planets')

        html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>People from Windy Planets</title>
            <style>
                table { border-collapse: collapse; width: 100%; }
                th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
                th { background-color: #f2f2f2; }
                tr:nth-child(even) { background-color: #f9f9f9; }
                h1 { color: #333; }
            </style>
        </head>
        <body>
            <h1>People from Windy Planets</h1>
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Homeworld</th>
                        <th>Climate</th>
                    </tr>
                </thead>
                <tbody>
        """
        # Loop through people and add them to the table
        for person in people_from_windy_planets:
            # Get planet name and climate
            planet_name = escape(person.homeworld.name if person.homeworld else "Unknown")
            planet_climate = escape(person.homeworld.climate if person.homeworld else "Unknown")

            html += f"""
                <tr>
                    <td>{escape(person.name)}</td>
                    <td>{escape(planet_name)}</td>
                    <td>{escape(planet_climate)}</td>
                </tr>
            """ 

        # Close the HTML structure
        html += """
                </tbody>
            </table>
        </body>
        </html>
        """
        return HttpResponse(html)
    except Exception as error:
        return HttpResponse(f'{error}')