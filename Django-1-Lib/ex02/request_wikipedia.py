import sys
import json
import requests
import dewiki

def request_wikipedia(string):
    
    # Replace spaces for %20 to use in url
    string_to_search = string.replace(' ','%20')
    
    # Replace spaces for filename to _
    filename = string.replace(' ', '_').lower() + '.wiki'

    # English Wikipedia API    
    en_endpoint='https://en.wikipedia.org/w/api.php'


    # Search to get the Page ID
    search_params = {
        'action': 'query',
        'list': 'search',
        'srsearch': string_to_search,
        'format': 'json'
    }

    # Fetch to API using the Params that we defined
    response = requests.get(en_endpoint, params=search_params)
    # Parse information to JSON
    data = response.json()
    
    # Check if we find something
    if 'query' in data and 'search' in data['query'] and data['query']['search']:
        # Get the first result
        first_result = data['query']['search'][0]
        page_id = first_result.get('pageid')
        
        # Get the full content of the page
        content_params = {
            'action': 'query',
            'prop': 'extracts',
            'explaintext': True,
            'pageids': page_id,
            'format': 'json'
        }
        
        # Fetch to API to get information from page
        content_response = requests.get(en_endpoint, params=content_params)
        # Parse infomation to JSON
        content_data = content_response.json()
        
        # Extract the page content
        if 'query' in content_data and 'pages' in content_data['query']:
            page_content = content_data['query']['pages'][str(page_id)].get('extract', '')
            
            # Use dewiki module to clean Wiki Markup
            try:
                new_content = dewiki.from_string(page_content)
                
                # Write the new content to a file
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                
                # Display a console message to confirm the execution
                print(f'Content written to {filename}')
            except Exception as error:
                raise Exception(f'Error while processing wiki content: {error}')
        else:
            raise Exception('Could not retrieve page content')
        

if __name__ == "__main__":
    
    try:
        if len(sys.argv) != 2:
            raise Exception('Usage: python3 request_wiki.py [argument]')
        request_wikipedia(string=sys.argv[1])
    except Exception as error:
        print(f'{error}')