#!/bin/bash

# This script initializes a new Python project using Poetry.

# Set the project name
PROJECT_NAME="my_python_project"

# Initialize a new Poetry project
echo "Initializing new Python project with Poetry..."
poetry new $PROJECT_NAME

# Navigate into the project directory
cd $PROJECT_NAME || { echo "Failed to enter the project directory."; exit 1; }

# Add necessary dependencies
echo "Adding dependencies..."
poetry add fastapi sqlalchemy psycopg2-binary

# Create a README.md file with project setup instructions
cat <<EOL > README.md
# $PROJECT_NAME

## Project Setup

1. Install Poetry if you haven't already.
2. Clone the repository or create a new one.
3. Navigate into the project directory: \`cd $PROJECT_NAME\`
4. Install dependencies: \`poetry install\`

## Running the Application

To run the application, use:

\`\`\`bash
poetry run uvicorn main:app --reload
\`\`\`

## Environment Variables

- DATABASE_URL: PostgreSQL connection URL.
EOL

echo "Project initialized successfully."