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
                html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Periodic Table</title>
    <style>
        body { font-family: Arial, sans-serif; }
        table { border-collapse: collapse; width: 100%; }
        td {
            border: 1px solid #ccc;
            width: 60px;
            height: 80px;
            text-align: center;
            vertical-align: top;
            padding: 4px;
        }
        .element {
            background-color: #f0f0f0;
        }
        .empty {
            border: none;
        }
        .number { font-size: 0.8em; color: #666; }
        .symbol { font-size: 1.2em; font-weight: bold; }
        .name { font-size: 0.8em; }
        .molar { font-size: 0.7em; color: #999; }
    </style>
</head>
<body>
    <h1>Periodic Table of the Elements</h1>
    <table>
"""

        # Layout for Mendeleev table (simplified; customize for accurate layout)
        layout = [
            [1] + [0]*16 + [2],
            [3, 4] + [0]*10 + [5, 6, 7, 8, 9, 10],
            [11,12] + [0]*10 + [13,14,15,16,17,18],
            [19,20] + [21,22,23,24,25,26,27,28,29,30] + [31,32,33,34,35,36],
            [37,38] + [39,40,41,42,43,44,45,46,47,48] + [49,50,51,52,53,54],
            [55,56] + [0]*1 + [72,73,74,75,76,77,78,79,80] + [81,82,83,84,85,86],
            [87,88] + [0]*1 + [104,105,106,107,108,109,110,111,112] + [113,114,115,116,117,118],
            [0]*1 + [57,58,59,60,61,62,63,64,65,66,67,68,69,70,71] + [0]*1,
            [0]*1 + [89,90,91,92,93,94,95,96,97,98,99,100,101,102,103] + [0]*1
        ]

        for row in layout:
            html += "<tr>"
            for atomic_number in row:
                if atomic_number == 0:
                    html += '<td class="empty"></td>'
                else:
                    el = parsing_periodic_table.get(atomic_number)
                    if el:
                        html += f"""
<td class="element">
    <div class="number">{el['number']}</div>
    <div class="symbol">{el['acronym']}</div>
    <div class="name">{el['name']}</div>
    <div class="molar">{el['molar']}</div>
</td>"""
                    else:
                        html += '<td class="empty"></td>'
            html += "</tr>\n"

        html += """
    </table>
</body>
</html>"""

        # Write to HTML file
        with open("periodic_table.html", "w", encoding="utf-8") as f:
            f.write(html)

        print("✅ Periodic table successfully created as periodic_table.html!")
      
        print("Periodic table successfully created as periodic_table.html!")
    except FileNotFoundError:
        print("Error: The input file periodic_table.txt was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    create_periodic_table_mendeleev()