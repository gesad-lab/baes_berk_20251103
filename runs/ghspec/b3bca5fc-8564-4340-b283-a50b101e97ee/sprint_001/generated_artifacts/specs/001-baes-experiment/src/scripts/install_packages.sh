#!/bin/bash

# install_packages.sh
# Script to set up Python dependencies for the Student Management application.

# Exit immediately if a command exits with a non-zero status
set -e

# Create a virtual environment using venv
echo "Creating virtual environment..."
python3 -m venv venv

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install required packages
echo "Installing required packages..."
pip install fastapi uvicorn sqlalchemy sqlite

# Freeze the current package versions to requirements.txt
pip freeze > requirements.txt

echo "All packages installed successfully."