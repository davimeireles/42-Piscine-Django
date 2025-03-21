import sys
import os
import re
import settings

def generate_cv_html(file):

    with open(file, "r") as f:
        content = f.read()

    content = re.sub("{name}", settings.name, content, flags=re.DOTALL)
    content = re.sub("{age}", settings.age, content, flags=re.DOTALL)
    content = re.sub("{profession}", settings.profession, content, flags=re.DOTALL)
    content = re.sub("{surname}", settings.surname, content, flags=re.DOTALL)

    with open("myCV.html", "w") as html:
        html.write("<!DOCTYPE html>\n")
        html.write("<html lang=\"en\">\n")
        html.write("<head>\n")
        html.write("<meta charset=\"utf-8\">\n")
        html.write("<title>Generated custom CV</title>\n")
        html.write("</head>\n")
        html.write("<body>\n")
        html.write(content)
        html.write("</body>\n")
        html.write("</html>\n")

    print("Generated custom CV HTML")

if __name__ == "__main__":

    try:
        if len(sys.argv) != 2 or sys.argv[1].find(".template") == -1:
            raise Exception("Usage: python3 render.py <file.template>")
        if os.path.isfile(sys.argv[1]) is False:
            raise Exception("Invalid file path")
        generate_cv_html(sys.argv[1])
    except Exception as error:
        print(f"{error}")
