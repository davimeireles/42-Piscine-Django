import sys
import requests
from bs4 import BeautifulSoup

def road_to_pilho(argument):

    wikipedia_url = 'https://pt.wikipedia.org/'
    
    result = requests.get(wikipedia_url)
    doc = BeautifulSoup(result.text, 'html.parser')
    print(doc.prettify)    


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise Exception('Usage: python3 roads_to_pilhosophy.py [argument]')
        else:
            road_to_pilho(sys.argv[1])
    except Exception as error:
        print(f'{error}')