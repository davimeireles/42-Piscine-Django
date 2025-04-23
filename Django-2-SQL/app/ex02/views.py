import psycopg2
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def create_movies_table_ex02(request):
    try:
        # Connect to the PostgreSQL using psycopg2
        connection = psycopg2.connect(
            dbname='djangotraining',
            user='djangouser',
            password='secret',
            host='127.0.0.1',
            port=5433
        )

        # Create a cursor to execute SQL
        cursor = connection.cursor()

        # SQL to create the table if dont exist
        query = """
        CREATE TABLE IF NOT EXISTS ex02_movies (
            episode_nb INTEGER PRIMARY KEY,
            title VARCHAR(64) UNIQUE NOT NULL,
            opening_crawl TEXT,
            director VARCHAR(32) NOT NULL,
            producer VARCHAR(128) NOT NULL,
            release_date TIMESTAMP NOT NULL
        );
        """

        # Execute and commit
        cursor.execute(query)
        connection.commit()

        # Clean up
        cursor.close()
        connection.close()

        return HttpResponse('OK')
    except Exception as error:
        return HttpResponse(f'{error}')
    

def populate_table_movies(request):
    try:
        # Connect to the PostgreSQL using psycopg2
        connection = psycopg2.connect(
            dbname='djangotraining',
            user='djangouser',
            password='secret',
            host='127.0.0.1',
            port=5433
        )

        # Create a cursor to execute SQL
        cursor = connection.cursor()

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
                cursor.execute("""
                    INSERT INTO ex02_movies(episode_nb, title, director, producer, release_date)
                    VALUES (%s, %s, %s, %s, %s)
                """, movie)
                connection.commit()
                response.append("OK")
            except Exception as e:
                response.append(f"Error: {e}")
                break

        cursor.close()
        connection.close()

        return HttpResponse("<br>".join(response))
    except Exception as error:
        return HttpResponse(f'Error: {error}')


def display_movies_table(request):
    try:
        # Connect to the PostgreSQL using psycopg2
        connection = psycopg2.connect(
            dbname='djangotraining',
            user='djangouser',
            password='secret',
            host='127.0.0.1',
            port=5433
        )

        # Create a cursor to execute SQL
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM ex02_movies")

        # Fetch rolls from query result
        movies = cursor.fetchall()

        # Get column names
        column_names = [desc[0] for desc in cursor.description]

        # Close cursor and connection
        cursor.close()
        connection.close()

        if not movies:
            return HttpResponse('No data avaible.')

        # Build HTML table
        html = "<html><body><h1>Movies</h1><table border='1'>"
        
        # Add header row
        html += "<tr>"
        for column in column_names:
            html += f"<th>{column}</th>"
        html += "</tr>"
        
        # Add data rows
        for movie in movies:
            html += "<tr>"
            for value in movie:
                # Handle None values (void fields)
                if value is None:
                    html += "<td>(empty)</td>"
                else:
                    html += f"<td>{value}</td>"
            html += "</tr>"
        
        html += "</table></body></html>"
        
        return HttpResponse(html)
        
    except Exception as e:
        # Return "No data available" for any errors
        return HttpResponse("No data available")