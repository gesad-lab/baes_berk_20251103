#!/bin/bash

# setup/virtual_environment_setup.sh

# This script sets up a Python virtual environment for the project,
# ensuring that the necessary dependencies are installed.

set -e  # Exit immediately if a command exits with a non-zero status

# Define the Python version required for the project
REQUIRED_PYTHON_VERSION="3.11"

# Check if the correct version of Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python is not installed. Please install Python $REQUIRED_PYTHON_VERSION or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | awk '{print $2}')
if [[ "$PYTHON_VERSION" < "$REQUIRED_PYTHON_VERSION" ]]; then
    echo "Python version $REQUIRED_PYTHON_VERSION or higher is required. Found version $PYTHON_VERSION."
    exit 1
fi

# Create a virtual environment in the 'venv' directory
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
else
    echo "Virtual environment already exists. Skipping creation."
fi

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip  # Upgrade pip to the latest version
pip install fastapi[all] sqlalchemy

echo "Virtual environment setup complete. Activate it using 'source venv/bin/activate'."