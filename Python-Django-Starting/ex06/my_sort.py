def sort_dictionary():

    """
    Sorts a dictionary of guitarists and their birth years, then prints
    the names of the guitarists in the sorted order.

    The dictionary is sorted first by birth year (ascending) and then
    alphabetically by guitarist name (ascending) to handle ties in birth years.
    """


    # Dictionary of guitarists and their birth years
    d = {
        'Hendrix': '1942',
        'Allman': '1946',
        'King': '1925',
        'Clapton': '1945',
        'Johnson': '1911',
        'Berry': '1926',
        'Vaughan': '1954',
        'Cooder': '1947',
        'Page': '1944',
        'Richards': '1943',
        'Hammett': '1962',
        'Cobain': '1967',
        'Garcia': '1942',
        'Beck': '1944',
        'Santana': '1947',
        'Ramone': '1948',
        'White': '1975',
        'Frusciante': '1970',
        'Thompson': '1949',
        'Burton': '1939',
    }

    # Sort the dictionary items (key-value pairs)
    # The sorting is done using a lambda function that specifies a sorting key:
    # - First, sort by the value (year)
    # - If birth years are the same, sort by the key (name)
    sorted_dictionary = sorted(d.items(), key=lambda kv: (kv[1], kv[0]))

    # Iterate through the sorted list of tuples and print the names
    for index in sorted_dictionary:
        print(index[0])


if __name__ == '__main__':
    sort_dictionary()
