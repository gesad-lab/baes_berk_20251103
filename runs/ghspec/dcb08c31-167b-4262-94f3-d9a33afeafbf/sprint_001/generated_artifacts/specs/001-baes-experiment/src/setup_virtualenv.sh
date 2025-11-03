#!/bin/bash

# This script sets up a Python virtual environment for the project

# Define the name of the virtual environment directory
VENV_DIR="venv"

# Check if virtualenv is installed
if ! command -v virtualenv &> /dev/null; then
    echo "virtualenv could not be found, please install it first."
    exit 1
fi

# Create a virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment in the $VENV_DIR directory..."
    virtualenv "$VENV_DIR"
else
    echo "Virtual environment already exists in the $VENV_DIR directory."
fi

# Activate the virtual environment
echo "Activating the virtual environment..."
source "$VENV_DIR/bin/activate"

# Install required packages
echo "Installing required packages..."
pip install Flask pytest

# Done
echo "Virtual environment is set up and activated. Required packages installed."