# Import to use argv with the script
import sys

def all_in(string):
    
    """
    This function takes a string of comma-separated values and determines if each value is a state or a capital city.
    It prints the corresponding capital city and state if found, otherwise it indicates that the value is neither.

    Args:
    string (str): A string of comma-separated values representing state names or capital cities.
    """
    
    # Dictionary mapping state names to their abbreviations
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    
    # Dictionary mapping state abbreviations to their capital cities
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    
    # Split the input string by commas to get individual values
    args = string.split(',')
        
    for line in args:
        found = False    
        x = line.strip()
        lower_x = x.casefold()

        if len(x) > 0:
            # Check if the value is a state name
            for states_key, states_value in states.items():
                lower_key = states_key.casefold()
                if lower_x == lower_key:
                    for capital_key, capital_value in capital_cities.items():
                        if states_value == capital_key:
                            print(f"{capital_value} is the capital of {states_key}")              
                            found = True

            # Check if the value is a capital city
            for capital_key, capital_value in capital_cities.items():
                lower_key = capital_value.casefold()
                if lower_x == lower_key:
                    for states_key, states_value in states.items():
                        if capital_key == states_value:
                            print(f"{capital_value} is the capital of {states_key}")
                            found = True

            # If the value is neither a state nor a capital city
            if not found:
                print(f"{x} is neither a capital city nor a state")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        all_in(sys.argv[1])