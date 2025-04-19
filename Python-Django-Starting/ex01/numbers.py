def display_numbers_from_file():
    
    # Open the file in read mode
    file = open("numbers.txt", "r")
    
    # Read the content of the file
    numbers = file.read()
    
    # Split the content of the file into lines
    lines = numbers.strip().split(',')
    
    # Print the content of the file
    for lines in lines:
        print(lines)
    
    # Close the file
    file.close()

if __name__ == '__main__':
    display_numbers_from_file()
    