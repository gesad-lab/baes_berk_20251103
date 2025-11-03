#!/bin/bash

# This script sets up a Python virtual environment and installs necessary dependencies for the project.

# Exit immediately if a command exits with a non-zero status
set -e

# Create a virtual environment named 'venv'
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip to the latest version
pip install --upgrade pip

# Install the necessary packages for the project
pip install Flask SQLAlchemy

echo "Python virtual environment setup completed successfully."