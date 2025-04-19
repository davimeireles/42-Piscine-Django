import sys
import os
import re
import settings

def generate_cv_html(file):
    with open(file, "r") as f:
        content = f.read()

    settings_dict = {
        key: str(value)
        for key, value in vars(settings).items()
        if not key.startswith("__") and not callable(value)
    }

    def replace_placeholder(match):
        key = match.group(1)
        return settings_dict.get(key, f"{{{key}}}")  # leave placeholder if not found

    content = re.sub(r"{(\w+)}", replace_placeholder, content)
    with open("myCV.html", "w") as html:
        html.write(content)

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
