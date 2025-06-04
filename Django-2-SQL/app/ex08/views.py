import psycopg2
import csv
import io
import os
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape
# Create your views here.

def init_tables_ex08(request):
    try:
        # Connect to the PostgreSQL using psycopg2
        connection = psycopg2.connect(
            dbname=os.getenv('NAME'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            host=os.getenv('HOST'),
            port=os.getenv('PORT')
        )

        response = []
        # Create a cursor to execute SQL
        cursor = connection.cursor()

        # Drop table if it exists
        cursor.execute("DROP TABLE IF EXISTS ex08_planets CASCADE")
        cursor.execute("DROP TABLE IF EXISTS ex08_people CASCADE")

        try:
            # SQL to create the table if dont exist
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS ex08_planets (
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) UNIQUE NOT NULL,
                climate VARCHAR,
                diameter INTEGER,
                orbital_period INTEGER,
                population BIGINT,
                rotation_period INTEGER,
                surface_water REAL,
                terrain VARCHAR(128)
            );
            """)

            response.append('OK')
        except Exception as e:
            response.append('Error')
        
        try:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS ex08_people (
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) UNIQUE NOT NULL,
                birth_year VARCHAR(32),
                gender VARCHAR(32),
                eye_color VARCHAR(32),
                hair_color VARCHAR(32),
                height INTEGER,
                mass REAL,
                homeworld VARCHAR(64),
                CONSTRAINT fk_ex08_planets
                    FOREIGN KEY(homeworld)
                    REFERENCES ex08_planets(name)
                );
            """)
            response.append('OK')
        except Exception as e:
            response.append('Error')

        # Commit to database
        connection.commit()

        # Clean up
        cursor.close()
        connection.close()

        return HttpResponse("<br>".join(response))
    except Exception as error:
        return HttpResponse(f'{error}')
    
def populate_tables_ex08(request):
    try:
        # List to store all planetes data
        planets_data_list = []

        # Read csv using the csv module
        with open('planets.csv', 'r') as planets_file:
            csv_reader = csv.reader(planets_file, delimiter='\t')
            
            # Process each row
            for row in csv_reader:
                # handle any conversion errors.
                try:
                    diameter = int(row[2]) if row[2] and row[2].strip().upper() not in ['NA', 'NULL', 'UNKNOWN', ''] else None
                except ValueError:
                    diameter = None
                try:
                    orbital_period = int(row[3]) if row[3] and row[3].strip().upper() not in ['NA', 'NULL', 'UNKNOWN', ''] else None
                except ValueError:
                    orbital_period = None
                try:
                    population = int(row[4]) if row[4] and row[4].strip().upper() not in ['NA', 'NULL', 'UNKNOWN', ''] else None
                except ValueError:
                    population = None
                try:
                    rotation_period = int(row[5]) if row[5] and row[5].strip().upper() not in ['NA', 'NULL', 'UNKNOWN', ''] else None
                except ValueError:
                    rotation_period = None
                try:
                    surface_water = int(row[6]) if row[6] and row[6].strip().upper() not in ['NA', 'NULL', 'UNKNOWN', ''] else None
                except ValueError:
                    surface_water = None

                planet = {
                    'name': row[0].strip(),
                    'climate': row[1].strip() if row[1] else None,
                    'diameter': diameter,
                    'orbital_period': orbital_period,
                    'population': population,
                    'rotation_period': rotation_period,
                    'surface_water': surface_water,
                    'terrain': row[7].strip() if row[7] else None
                }
                planets_data_list.append(planet)

            try:
                # Connect to the PostgreSQL using psycopg2
                connection = psycopg2.connect(
                dbname=os.getenv('NAME'),
                user=os.getenv('USER'),
                password=os.getenv('PASSWORD'),
                host=os.getenv('HOST'),
                port=os.getenv('PORT')
                )

                cursor = connection.cursor()
                
                # First check if table exists
                cursor.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'ex08_planets')")
                table_exists = cursor.fetchone()[0]
                
                if not table_exists:
                    cursor.close()
                    connection.close()
                    return HttpResponse("No data available")
                
                # Check if any planets need to be inserted
                inserted_count = 0
                
                for planet in planets_data_list:
                    # Check if the planet already exists
                    cursor.execute("SELECT 1 FROM ex08_planets WHERE name = %s", [planet['name']])
                    exists = cursor.fetchone()
                    
                    if not exists:
                        cursor.execute("""
                        INSERT INTO ex08_planets
                        (name, climate, diameter, orbital_period, population, rotation_period, surface_water, terrain)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                        """, [
                            planet['name'],
                            planet['climate'],
                            planet['diameter'],
                            planet['orbital_period'],
                            planet['population'],
                            planet['rotation_period'],
                            planet['surface_water'],
                            planet['terrain']
                        ])
                        inserted_count += 1
                
                connection.commit()
                cursor.close()
                connection.close()
                
                if inserted_count == 0:
                    return HttpResponse("No new data to insert")
                else:
                    return HttpResponse(f"Successfully inserted {inserted_count} planet(s)")
                    
            except Exception as insert_error:
                return HttpResponse("No data available")
    except FileNotFoundError:
        return HttpResponse('Error: planets.csv file not found')
    except csv.Error as csv_error:
        return HttpResponse(f'CSV parsing error: {csv_error}')
    except Exception as error:
        return HttpResponse(f"{error}")

    try:
        # List to store all people data
        people_data_list = []
        # Read csv using the csv module
        with open('people.csv', 'r') as people_file:
            csv_reader = csv.reader(people_file, delimiter='\t')

            # Process each row
            for row in csv_reader:
                try:
                    height = int(row[5]) if row[5] and row[5].strip().upper() not in ['NA', 'NULL', 'UNKNOWN', ''] else None
                except ValueError:
                    height = None
                try:
                    mass = float(row[6]) if row[6] and row[6].strip().upper() not in ['NA', 'NULL', 'UNKNOWN', ''] else None
                except ValueError:
                    mass = None
                
                person = {
                    'name': row[0].strip(),
                    'birth_year': row[1].strip() if row[1] else None,
                    'gender': row[2].strip() if row[2] else None,
                    'eye_color': row[3].strip() if row[3] else None,
                    'hair_color': row[4].strip() if row[4] else None,
                    'height': height,
                    'mass': mass,
                    'homeworld': row[7].strip() if row[7] else None,
                }
                people_data_list.append(person)

            try:
                # Connect to the PostgreSQL using psycopg2
                connection = psycopg2.connect(
                dbname=os.getenv('NAME'),
                user=os.getenv('USER'),
                password=os.getenv('PASSWORD'),
                host=os.getenv('HOST'),
                port=os.getenv('PORT')
                )

                cursor = connection.cursor()
                
                # First check if table exists
                cursor.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'ex08_people')")
                table_exists = cursor.fetchone()[0]
                
                if not table_exists:
                    cursor.close()
                    connection.close()
                    return HttpResponse("No data available")
                
                # Check if any people need to be inserted
                inserted_count = 0
                
                for person in people_data_list:
                    # Check if the person already exists
                    cursor.execute("SELECT 1 FROM ex08_people WHERE name = %s", [person['name']])
                    exists = cursor.fetchone()
                    
                    if not exists:
                        # Before inserting, check if homeworld exists
                        homeworld = person['homeworld']
                        if homeworld is not None:
                            cursor.execute("SELECT 1 FROM ex08_planets WHERE name = %s", [homeworld])
                            if cursor.fetchone() is None:
                                # Homeworld doesn't exist, set to NULL
                                person['homeworld'] = None
                    
                        cursor.execute("""
                        INSERT INTO ex08_people
                        (name, birth_year, gender, eye_color, hair_color, height, mass, homeworld)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
                        """, [
                            person['name'],
                            person['birth_year'],
                            person['gender'],
                            person['eye_color'],
                            person['hair_color'],
                            person['height'],
                            person['mass'],
                            person['homeworld']
                        ])
                        inserted_count += 1
            
                connection.commit()
                cursor.close()
                connection.close()
                
                if inserted_count == 0:
                    return HttpResponse("No new data to insert")
                else:
                    return HttpResponse(f"Successfully inserted {inserted_count} person/people")
                
            except Exception as insert_error:
                return HttpResponse("No data available")
    
    except FileNotFoundError:
        return HttpResponse('Error: people.csv file not found')
    except csv.Error as csv_error:
        return HttpResponse(f'CSV parsing error: {csv_error}')
    except Exception as error:
        return HttpResponse(f'Unexpected error: {error}')

def populate_table_with_psycopg_copy_from(request):
    connection = None
    cursor = None
    
    try:
        # Connect to PostgreSQL
        connection = psycopg2.connect(
            dbname=os.getenv('NAME'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            host=os.getenv('HOST'),
            port=os.getenv('PORT')
        )
        cursor = connection.cursor()
        
        # Process planets first
        planets_count = process_planets_with_copy(cursor)
        
        # Add an "unknown" planet if it doesn't exist
        cursor.execute("""
        INSERT INTO ex08_planets (name, climate, diameter, orbital_period, population, rotation_period, surface_water, terrain)
        VALUES ('unknown', NULL, NULL, NULL, NULL, NULL, NULL, NULL)
        ON CONFLICT (name) DO NOTHING
        """)
        
        # Process people
        people_count = process_people_with_copy(cursor)
        
        # Commit all changes
        connection.commit()
        
        return HttpResponse(f'Successfully processed {planets_count} planets and {people_count} people records')
    
    except FileNotFoundError as e:
        if connection:
            connection.rollback()
        return HttpResponse(f'File not found: {e}')
    except csv.Error as csv_error:
        if connection:
            connection.rollback()
        return HttpResponse(f'CSV parsing error: {csv_error}')
    except Exception as error:
        if connection:
            connection.rollback()
        return HttpResponse(f'Unexpected error: {error}')
    finally:
        # Close resources
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def process_planets_with_copy(cursor):
    # Create a StringIO object to hold the CSV data
    planets_data = io.StringIO()
    planets_count = 0
    
    # Change the null representation from '\n' to '\N' (PostgreSQL's default)
    null_marker = r'\N'
    
    # Read and transform the input CSV
    with open('planets.csv', 'r') as planets_file:
        csv_reader = csv.reader(planets_file, delimiter='\t')
        for row in csv_reader:
            if len(row) < 8:
                continue
            
            planets_count += 1
            name = row[0].strip()
            climate = row[1].strip() if row[1] else null_marker
            
            # Handle numeric conversions
            try:
                diameter = row[2].strip() if row[2] and row[2].strip().upper() not in ['NA', 'NULL', 'UNKNOWN', ''] else null_marker
                if diameter != null_marker:
                    int(diameter)  # Just to validate it's an integer
            except ValueError:
                diameter = null_marker
            
            # Apply the same pattern to the rest of the fields
            try:
                orbital_period = row[3].strip() if row[3] and row[3].strip().upper() not in ['NA', 'NULL', 'UNKNOWN', ''] else null_marker
                if orbital_period != null_marker:
                    int(orbital_period)
            except ValueError:
                orbital_period = null_marker
                
            try:
                population = row[4].strip() if row[4] and row[4].strip().upper() not in ['NA', 'NULL', 'UNKNOWN', ''] else null_marker
                if population != null_marker:
                    int(population)
            except ValueError:
                population = null_marker
                
            try:
                rotation_period = row[5].strip() if row[5] and row[5].strip().upper() not in ['NA', 'NULL', 'UNKNOWN', ''] else null_marker
                if rotation_period != null_marker:
                    int(rotation_period)
            except ValueError:
                rotation_period = null_marker
                
            try:
                surface_water = row[6].strip() if row[6] and row[6].strip().upper() not in ['NA', 'NULL', 'UNKNOWN', ''] else null_marker
                if surface_water != null_marker:
                    float(surface_water)
            except ValueError:
                surface_water = null_marker
                
            terrain = row[7].strip() if row[7] else null_marker
            
            # Write the formatted line to our StringIO object
            planets_data.write(f"{name}\t{climate}\t{diameter}\t{orbital_period}\t{population}\t{rotation_period}\t{surface_water}\t{terrain}\n")
    
    # Reset the position to the beginning of the StringIO object
    planets_data.seek(0)
    
    # Use copy_from to bulk load the data
    cursor.copy_from(
        planets_data, 
        'ex08_planets', 
        columns=('name', 'climate', 'diameter', 'orbital_period', 'population', 'rotation_period', 'surface_water', 'terrain'),
        null=r'\N'  # Use PostgreSQL's default null marker
    )
    
    return planets_count

def process_people_with_copy(cursor):
    # Create a StringIO object to hold the CSV data
    people_data = io.StringIO()
    people_count = 0
    
    # Change the null representation
    null_marker = r'\N'
    
    # Read and transform the input CSV
    with open('people.csv', 'r') as people_file:
        csv_reader = csv.reader(people_file, delimiter='\t')
        for row in csv_reader:
            if len(row) < 8:
                continue
            
            people_count += 1
            name = row[0].strip()
            birth_year = row[1].strip() if row[1] else null_marker
            gender = row[2].strip() if row[2] else null_marker
            eye_color = row[3].strip() if row[3] else null_marker
            hair_color = row[4].strip() if row[4] else null_marker
            
            # Handle numeric conversions
            try:
                height = row[5].strip() if row[5] and row[5].strip().upper() not in ['NA', 'NULL', 'UNKNOWN', ''] else null_marker
                if height != null_marker:
                    int(height)
            except ValueError:
                height = null_marker
                
            try:
                mass = row[6].strip() if row[6] and row[6].strip().upper() not in ['NA', 'NULL', 'UNKNOWN', ''] else null_marker
                if mass != null_marker:
                    float(mass)
            except ValueError:
                mass = null_marker
            
            # Check if homeworld is valid, otherwise use 'unknown'
            homeworld = row[7].strip() if row[7] and row[7].strip().upper() not in ['NA', 'NULL', 'UNKNOWN', ''] else 'unknown'
            
            # Check if the homeworld exists in planets table (except for 'unknown' which we already added)
            if homeworld != 'unknown':
                cursor.execute("SELECT 1 FROM ex08_planets WHERE name = %s", [homeworld])
                if cursor.fetchone() is None:
                    homeworld = 'unknown'  # Set to 'unknown' if homeworld doesn't exist
            
            # Write the formatted line to our StringIO object
            people_data.write(f"{name}\t{birth_year}\t{gender}\t{eye_color}\t{hair_color}\t{height}\t{mass}\t{homeworld}\n")
    
    # Reset the position to the beginning of the StringIO object
    people_data.seek(0)
    
    # Use copy_from to bulk load the data
    cursor.copy_from(
        people_data, 
        'ex08_people', 
        columns=('name', 'birth_year', 'gender', 'eye_color', 'hair_color', 'height', 'mass', 'homeworld'),
        null=r'\N'  # Use PostgreSQL's default null marker
    )
    
    return people_count


def display_table_sorted(request):
    try:
        # Connect to PostgreSQL
        connection = psycopg2.connect(
            dbname=os.getenv('NAME'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            host=os.getenv('HOST'),
            port=os.getenv('PORT')
        )

        cursor = connection.cursor()

        # Use JOIN to get people from planets with windy climate
        cursor.execute("""
            SELECT
                ex08_people.name,
                ex08_people.homeworld,
                ex08_planets.climate
            FROM
                ex08_people
            JOIN
                ex08_planets ON ex08_people.homeworld = ex08_planets.name
            WHERE
                ex08_planets.climate LIKE '%windy%'
            ORDER BY
                ex08_people.homeworld, ex08_people.name
        """)

        # Fetch all data
        data = cursor.fetchall()

        # Close cursor and connection
        cursor.close()
        connection.close()

        if not data:
            return HttpResponse('No data available')
        
        # Create proper HTML with DOCTYPE, charset, and structure
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

        for row in data:
            html += f"""
                <tr>
                    <td>{escape(str(row[0]))}</td>
                    <td>{escape(str(row[1]))}</td>
                    <td>{escape(str(row[2]))}</td>
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
        return HttpResponse("No data available")