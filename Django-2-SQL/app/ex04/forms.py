import psycopg2
from django import forms

class RemoveMovieForm(forms.Form):
    title = forms.ChoiceField(choices=[], label="Movie Title")


    def __init__(self, *args, **kwargs):
        super(RemoveMovieForm, self).__init__(*args, **kwargs)
        connection = psycopg2.connect(
            dbname='djangotraining',
            user='djangouser',
            password='secret',
            host='127.0.0.1',
            port=5433
        )

        # Get movie titles from database
        cursor = connection.cursor()
        cursor.execute("SELECT title FROM ex04_movies ORDER BY title")
        choices = [(row[0], row[0]) for row in cursor.fetchall()]
        self.fields['title'].choices = choices
        
        # Close cursor and connection
        cursor.close()
        connection.close()
        