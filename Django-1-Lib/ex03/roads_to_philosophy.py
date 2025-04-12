import sys
import requests
from bs4 import BeautifulSoup

"""
Function to search inside the wikipedia website
Trying to find the Philosophy article
"""

def road_to_pilho(argument):

    # Replace space for _ to search in the url
    search_argument=argument.replace(' ', '_')

    # Track visited pages to prevent loop
    visited_pages = []

    # Init page title null
    page_title = ''

    while page_title != 'Philosophy':

        # Check if we  already visited the current page
        if search_argument in visited_pages:
            print('It leads to an infinite loop !')
            break

        # Append the current page to visited pages
        visited_pages.append(search_argument)

        # Mix default en url with the argument to search
        wikipedia_url = f'https://en.wikipedia.org/wiki/{search_argument}'

        # Make a request and get the html page
        result = requests.get(wikipedia_url)

        # Use BeautifulSoup to parse the result into a html code
        doc = BeautifulSoup(result.text, 'html.parser')

        # Get the page title to print in terminal
        page_title = doc.find(id='firstHeading').string

        print(page_title)

        # Get content from element id bodyContent
        body_content = doc.find(id='bodyContent')

        next_link = None

        for p in body_content.find_all('p'):
            # Skip empty paragraphs
            if not p.text.strip():
                continue
                
            # Find all links in this paragraph
            links = p.find_all('a')
            
            # Find the first valid link
            for link in links:
                # Check if it's a valid wiki link (not a reference, not in parentheses, etc.)
                if (link.get('href') and 
                    link['href'].startswith('/wiki/') and 
                    ':' not in link['href'] and
                    not link.find_parent('span', class_='reference') and
                    'redlink=1' not in link.get('href', '')):
                    
                    next_link = link
                    break
            
            # If we found a valid link in this paragraph, stop checking paragraphs
            if next_link:
                break
        
        # If no valid link was found
        if not next_link:
            print('It leads to a dead end !')
            break

        # Extract the next page to visit from the link
        search_argument = next_link['href'].split('/wiki/')[1]

    print(f'{len(visited_pages)} roads from {argument} to philosophy !')



if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise Exception('Usage: python3 roads_to_pilhosophy.py [argument]')
        else:
            road_to_pilho(sys.argv[1])
    except Exception as error:
        print(f'{error}')