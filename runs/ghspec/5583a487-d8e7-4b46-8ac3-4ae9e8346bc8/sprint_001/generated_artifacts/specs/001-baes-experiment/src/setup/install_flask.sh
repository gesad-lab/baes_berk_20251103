#!/bin/bash

# install_flask.sh
# Script to install Python and Flask for the development environment.

# Exit immediately if any command fails
set -e

# Function to install Python
install_python() {
    echo "Installing Python..."
    
    # Update package manager and install Python
    if [[ $(uname) == "Linux" ]]; then
        # For Ubuntu/Debian-based systems
        sudo apt update
        sudo apt install -y python3 python3-pip
    elif [[ $(uname) == "Darwin" ]]; then
        # For macOS
        brew install python
    else
        echo "Unsupported OS. Please install Python manually."
        exit 1
    fi
    
    echo "Python installation completed."
}

# Function to install Flask
install_flask() {
    echo "Installing Flask..."
    
    # Install Flask using pip
    pip3 install Flask

    echo "Flask installation completed."
}

# Run the installation functions
install_python
install_flask

echo "Setup completed. Python and Flask are installed."