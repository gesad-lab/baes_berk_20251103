#!/bin/bash

# This script sets up the virtual environment for the application.

# Exit immediately if a command exits with a non-zero status.
set -e

# Print each command before executing it.
set -x

# Create a virtual environment named 'venv'
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the required Python packages
pip install Flask==2.0.3 Flask-SQLAlchemy==2.5.1

# Create a requirements.txt file
echo "Flask==2.0.3" > requirements.txt
echo "Flask-SQLAlchemy==2.5.1" >> requirements.txt

# Install testing frameworks
pip install pytest pytest-flask

# Print success message
echo "Virtual Environment setup complete. Activate it using 'source venv/bin/activate'."