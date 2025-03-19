# Import to use argv with the script
import sys

def display_capital_city(state):

    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }
    
    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    
    # Boolean variable to check if its necessary to print Unknown state
    found = False
    
    # Check if the state exists in the states dictionary
    for state_key, state_value in states.items():
        # If exists
        if state == state_key:
            # Search inside the capital dictionary
            for capital_key, capital_value in capital_cities.items():
                # If exists
                if state_value == capital_key:
                    # Display the capital value
                    print(f"{capital_value}")
                    found = True

    # If found == False, display Unknown state    
    if not found:
        print("Unknown state")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        display_capital_city(sys.argv[1])