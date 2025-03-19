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

if __name__ == '__main__':
    if len(sys.argv) == 2:
        all_in(sys.argv[1])