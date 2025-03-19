def my_var():
    
    # Variables   
    
    # An integer is a data type used in programming, such as a floating point unit, but is used to represent whole numbers rather than numbers with a fraction.
    a = 42
    
    # A string is a data type used in programming, such as an integer and floating point unit, but is used to represent text rather than numbers.
    b = "42"
    c = "quarante-deux"
    
    # A float is a data type composed of a number that is not an integer, because it includes a fraction represented in decimal format.
    d = 42.0
    
    # A boolean is a data type that has one of two possible values (usually denoted true and false)
    e = True
    
    # A list is a collection which is ordered and changeable.
    f = [42]
    
    # A dictionary is a collection which is unordered, changeable and indexed.
    g = {42: 42}
    
    # A tuple is a collection which is ordered and unchangeable.
    h = (42,)
    
    # Set function is used to create a set object in random order
    i = set()
    
    # Print the type of each variable
    print(f"{a} has a type {type(a)}")
    print(f"{b} has a type {type(b)}")
    print(f"{c} has a type {type(c)}")
    print(f"{d} has a type {type(d)}")
    print(f"{e} has a type {type(e)}")
    print(f"{f} has a type {type(f)}")
    print(f"{g} has a type {type(g)}")
    print(f"{h} has a type {type(h)}") 
    print(f"{i} has a type {type(i)}")
    
if __name__ == '__main__':
    my_var()