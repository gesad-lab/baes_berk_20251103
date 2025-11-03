#!/bin/bash

# heroku_setup.sh
# This script sets up the application for deployment on Heroku

# Exit immediately if a command exits with a non-zero status
set -e

# Function to install necessary dependencies
install_dependencies() {
    echo "Installing necessary dependencies..."
    pip install -r requirements.txt
}

# Function to create a Heroku app
create_heroku_app() {
    echo "Creating a new Heroku application..."
    heroku create "$HEROKU_APP_NAME"
}

# Function to set up SQLite database
setup_database() {
    echo "Setting up the SQLite database..."
    # Command to initialize the database schema if necessary
    python -c "from your_application import db; db.create_all()"
}

# Function to configure environment variables
configure_env() {
    echo "Configuring environment variables..."
    # Setting environment variables for Heroku
    heroku config:set FLASK_ENV=production
    heroku config:set DATABASE_URL=sqlite:///your_database_name.db
}

# Function to deploy the application
deploy_app() {
    echo "Deploying the application to Heroku..."
    git add .
    git commit -m "Prepare for Heroku deployment"
    git push heroku master
}

# Main function to coordinate setup
main() {
    if [[ -z "$HEROKU_APP_NAME" ]]; then
        echo "ERROR: HEROKU_APP_NAME variable is not set."
        exit 1
    fi
    
    # Install dependencies
    install_dependencies
    # Create a Heroku app
    create_heroku_app
    # Setup the SQLite database
    setup_database
    # Configure environment variables
    configure_env
    # Deploy the application
    deploy_app

    echo "Deployment to Heroku completed successfully!"
}

# Run the main function
main "$@"