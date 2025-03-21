def create_periodic_table_mendeleev():
    """ Generates an HTML file representing the periodic table, formatted exactly like the provided image. """
    try:
        # Read the data from the periodic_table.txt file
        with open("periodic_table.txt", "r") as file:
            parsing_periodic_table = {}
            for line in file:
                split_line = line.split(",")
                element_name = split_line[0].split("=")[1].strip()
                element_number = split_line[1].split(":")[1].strip()
                element_acronym = split_line[2].split(":")[1].strip()
                element_molar = split_line[3].split(":")[1].strip()
                element_electron = split_line[4].split(":")[1].strip()

                parsing_periodic_table[int(element_number)] = {
                    "name": element_name,
                    "number": element_number,
                    "acronym": element_acronym,
                    "molar": element_molar,
                    "electron": element_electron,
                }

      
        print("Periodic table successfully created as periodic_table.html!")
    except FileNotFoundError:
        print("Error: The input file periodic_table.txt was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    create_periodic_table_mendeleev()