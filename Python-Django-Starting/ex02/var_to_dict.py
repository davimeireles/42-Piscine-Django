def copy_list_of_tuples_to_dict(d):
        
    # Initialize the dictionary
    dic = {}
    
    # Loop into list of tuples to obtain key and value for dictonary
    for key, value in d:
        dic[key] = value
    
    # Loop into dictonary and print the key and value for each
    for key, value in dic.items():
       print(f"{value} : {key}")
    
if __name__ == '__main__':

    d = [
    ('Hendrix' , '1942'),
    ('Allman' , '1946'),
    ('King' , '1925'),
    ('Clapton' , '1945'),
    ('Johnson' , '1911'),
    ('Berry' , '1926'),
    ('Vaughan' , '1954'),
    ('Cooder' , '1947'),
    ('Page' , '1944'),
    ('Richards' , '1943'),
    ('Hammett' , '1962'),
    ('Cobain' , '1967'),
    ('Garcia' , '1942'),
    ('Beck' , '1944'),
    ('Santana' , '1947'),
    ('Ramone' , '1948'),
    ('White' , '1975'),
    ('Frusciante', '1970'),
    ('Thompson' , '1949'),
    ('Burton' , '1939')
    ]

    copy_list_of_tuples_to_dict(d)