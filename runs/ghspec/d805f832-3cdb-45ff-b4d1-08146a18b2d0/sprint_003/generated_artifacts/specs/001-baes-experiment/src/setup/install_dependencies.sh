#!/bin/bash

# This script sets up the Python environment and installs necessary dependencies.

set -e  # Exit immediately if a command exits with a non-zero status

# Check for Python 3.11+ installation
if ! command -v python3 &> /dev/null || [[ "$(python3 --version | awk '{print $2}' | cut -d. -f1)" -lt 3 ]] || [[ "$(python3 --version | awk '{print $2}' | cut -d. -f2)" -lt 11 ]]; then
    echo "Python 3.11 or higher is required. Please install it and try again."
    exit 1
fi

# Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating a virtual environment..."
    python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip to the latest version
pip install --upgrade pip

# Install necessary dependencies
echo "Installing required Python dependencies..."
pip install fastapi[all] sqlalchemy

echo "Dependencies installed successfully."