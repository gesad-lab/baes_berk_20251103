#!/bin/bash

# run_tests.sh
# Script to integrate all components and run tests for the Student API

set -e  # Exit immediately if a command exits with a non-zero status

# Function to print usage information
function usage() {
    echo "Usage: $0 [test|db_setup]"
    exit 1
}

# Check if any argument is passed
if [ $# -eq 0 ]; then
    usage
fi

# Database setup function to create the necessary schema
function setup_database() {
    echo "Setting up database..."
    # Create the SQLite database and schema if not existing
    sqlite3 students.db <<EOF
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
EOF
    echo "Database setup complete."
}

# Run tests function using pytest
function run_tests() {
    echo "Running tests..."
    # Ensure the tests directory is present
    if [ ! -d "tests" ]; then
        echo "Error: Test directory 'tests' not found!"
        exit 1
    fi
    
    # Run the tests using pytest
    pytest tests --disable-warnings -q

    echo "Tests completed successfully."
}

# Main script logic
case "$1" in
    test)
        run_tests
        ;;
    db_setup)
        setup_database
        ;;
    *)
        usage
        ;;
esac

# End of script