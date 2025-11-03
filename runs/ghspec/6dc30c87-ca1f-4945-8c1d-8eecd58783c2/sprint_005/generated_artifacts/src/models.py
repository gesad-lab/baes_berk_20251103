```bash
#!/bin/bash

# Script to set up a Python virtual environment and install required dependencies

# Define the project directory and virtual environment name
PROJECT_DIR="$(pwd)"
VENV_NAME="venv"

# Check if Python 3 and pip are available
if ! command -v python3 &>/dev/null; then
    echo "Python 3 is not installed. Please install Python 3."
    exit 1
fi

if ! command -v pip &>/dev/null; then
    echo "pip is not installed. Please install pip."
    exit 1
fi

# Create virtual environment
if [ ! -d "$PROJECT_DIR/$VENV_NAME" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$PROJECT_DIR/$VENV_NAME"
else
    echo "Virtual environment already exists."
fi

# Activate the virtual environment
source "$PROJECT_DIR/$VENV_NAME/bin/activate"

# Upgrade pip to the latest version
pip install --upgrade pip

# Install required dependencies
echo "Installing required dependencies..."
pip install fastapi sqlalchemy sqlite

# Notify user of successful setup
echo "Setup complete! Virtual environment is ready and dependencies installed."
```