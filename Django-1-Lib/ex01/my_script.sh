#!/bin/bash

# Display pip version
echo "Using pip version:"
pip --version

# Create local_lib directory if it doesn't exist
mkdir -p local_lib

# Install path.py from GitHub repo into local_lib folder
# The -f flag forces reinstallation if already installed
echo "Installing path.py library..."
pip install -f https://github.com/jaraco/path.git --target=./local_lib path.py > installation.log 2>&1

# Check if installation was successful
if [ $? -eq 0 ]; then
    echo "path.py successfully installed in local_lib folder"
    # Execute the Python program
    python3 my_program.py
else
    echo "Failed to install path.py. Check installation.log for details"
    exit 1
fi