from django.shortcuts import render
from django.http import HttpResponse
import psycopg2
import os

def create_movies_table(request):
    try:
        # Connect to the PostgreSQL using psycopg2
        connection = psycopg2.connect(
            dbname=os.getenv('NAME'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            host=os.getenv('HOST'),
            port=os.getenv('PORT')
        )

        # Create a cursor to execute SQL
        cursor = connection.cursor()

        # SQL to create the table if dont exist
        query = """
        CREATE TABLE IF NOT EXISTS ex00_movies (
            episode_nb INTEGER PRIMARY KEY,
            title VARCHAR(64) UNIQUE NOT NULL,
            opening_crawl TEXT,
            director VARCHAR(32) NOT NULL,
            producer VARCHAR(128) NOT NULL,
            release_date DATE NOT NULL
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