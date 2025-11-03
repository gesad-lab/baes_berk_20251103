#!/bin/bash

# setup_env.sh
# This script sets up a virtual environment for the project and installs dependencies.

set -e  # Exit immediately if a command exits with a non-zero status.

# Define the virtual environment directory
VENV_DIR="venv"

# Check if the virtual environment already exists
if [ -d "$VENV_DIR" ]; then
    echo "Virtual environment already exists. Activating it..."
else
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
fi

# Activate the virtual environment
source "$VENV_DIR/bin/activate"

# Install project dependencies
echo "Installing dependencies..."
pip install --upgrade pip  # Upgrade pip to the latest version
pip install Flask Flask-RESTful Marshmallow pytest  # Install required packages

echo "Virtual environment setup complete."
echo "To activate the virtual environment, run: source $VENV_DIR/bin/activate"