# Import path from the local installation
import sys
import os

# Add the local_lib directory to Python's path
script_dir = os.path.dirname(os.path.abspath(__file__))
local_lib_path = os.path.join(script_dir, 'local_lib')
sys.path.insert(0, local_lib_path)

# Now import path
from path import Path

print("Successfully imported path library from local installation")

# Create a folder
new_folder = Path("new_folder")
if not new_folder.exists():
    new_folder.mkdir()
    print(f"Created folder: {new_folder}")
else:
    print(f"Folder already exists: {new_folder}")

# Create a file inside the folder and write to it
file_path = new_folder / "my_file.txt"
file_content = "This is a test file created using the path library.\nIt demonstrates how to use path.py functionality."
file_path.write_text(file_content)
print(f"Created and wrote to file: {file_path}")

# Read and display the file content
read_content = file_path.read_text()
print("\nFile content:")
print(read_content)