# Import to use argv with the script
import sys

def display_matching_state(capital_city):
    
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
    
    found = False
    
    # Check if the capital city exists in the capital cities dictionary
    for capital_key, capital_value in capital_cities.items():
        # If exists
        if capital_city == capital_value:
            # Search inside the states dictionary
            for states_key, states_value in states.items():
                # If exists
                if capital_key == states_value:
                    # Display the state value
                    print(f"{states_key}")
                    found = True

    # If found == False, display Unknown state
    if not found:
        print("Unknown capital city")
    

if __name__ == '__main__':
    if len(sys.argv) == 2:
        display_matching_state(sys.argv[1])
    