#!/bin/bash

VENV_NAME="django_venv"

# Create the virtual environment in the local folder of the script
python3 -m venv $VENV_NAME

# Install requirements inside virtual env
$VENV_NAME/bin/python3 -m pip install -r requirement.txt

# Display succes message
echo "Requirements installed succesfully"

# Activate virtual environment
source $VENV_NAME/bin/activate