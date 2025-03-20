# Import to use argv with the script
import sys

def all_in(string):
    
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
    
    args = string.split(',')
        
    for line in args:
        found = False    
        x = line.strip()
        lower_x = x.casefold()

        if len(x) > 0:
            for states_key, states_value in states.items():
                lower_key = states_key.casefold()
                if lower_x == lower_key:
                    for capital_key, capital_value in capital_cities.items():
                        if states_value == capital_key:
                            print(f"{capital_value} is the capital of {states_key}")              
                            found = True

            for capital_key, capital_value in capital_cities.items():
                lower_key = capital_value.casefold()
                if lower_x == lower_key:
                    for states_key, states_value in states.items():
                        if capital_key == states_value:
                            print(f"{capital_value} is the capital of {states_key}")
                            found = True

            if not found:
                print(f"{x} is neither a capital city nor a state")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        all_in(sys.argv[1])