#!/bin/bash

# setup/git_init.sh

# Script to initialize a Git repository for version control

# Exit immediately if a command exits with a non-zero status
set -e

# Check if .git directory already exists
if [ -d .git ]; then
    echo "A Git repository already exists in this directory."
    exit 1
fi

# Initialize a new Git repository
git init

# Create a .gitignore file to exclude unnecessary files
echo "Creating .gitignore file..."
cat <<EOL > .gitignore
# Python cache files
__pycache__/
*.py[cod]

# Virtual environment directories
env/
venv/

# Database files
*.sqlite3

# Environment variable files
.env
EOL

echo "Initialized a new Git repository and created .gitignore."