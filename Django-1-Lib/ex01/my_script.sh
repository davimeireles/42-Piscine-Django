#!/bin/bash

# LOG file
LOG_FILE='pathpy.log'

# Show pip version.
pip --version

# Install Dependencies(numpy && spicy)
sudo apt install python3-numpy
dpkg --install spicy.deb

# Create the folder to put pathpy from github.
mkdir local_lib

# Move to local_lib folder.
cd local_lib

# Check if pathpy is already installed.
if python3 -m pip show pathpy &>/dev/null; then
    echo "Pathpy is already installed. Uninstalling..." | tee -a "$LOG_FILE"
    # Uninstall pathpy
    python3 -m pip uninstall -y pathpy >> "$LOG_FILE" 2>&1
else
    echo "pathpy is not installed." | tee -a "$LOG_FILE"
fi


echo "Installing pathpy..." | tee -a "$LOG_FILE"

# Installing pathpy
pip install git+https://github.com/pathpy/pathpy.git#egg=pathpy >> "$LOG_FILE" 2>&1