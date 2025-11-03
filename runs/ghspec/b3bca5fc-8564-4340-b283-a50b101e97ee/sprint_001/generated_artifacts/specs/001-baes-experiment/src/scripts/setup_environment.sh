#!/bin/bash

# This script sets up a virtual environment for the student management application.

# Check if the script is being run from the correct directory
if [ ! -d "src" ]; then
  echo "This script must be run from the project root directory."
  exit 1
fi

# Set the name of the virtual environment
VENV_DIR="venv"

# Create a virtual environment
if [ ! -d "$VENV_DIR" ]; then
  echo "Creating virtual environment in $VENV_DIR..."
  python3 -m venv $VENV_DIR
else
  echo "Virtual environment already exists in $VENV_DIR."
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source $VENV_DIR/bin/activate

# Install the required packages
echo "Installing required packages..."
pip install fastapi uvicorn sqlalchemy sqlite

echo "Setup complete. You can now run the application."