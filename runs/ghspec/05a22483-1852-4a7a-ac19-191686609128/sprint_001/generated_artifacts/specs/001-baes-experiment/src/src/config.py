import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Load configuration from environment variables
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///students.db')  # Default to SQLite database

# Configure the application to use the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications to save memory

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Check the database connection
try:
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
except Exception as e:
    # Log the error for debugging purposes
    print(f"Error connecting to the database: {e}")  # In production, use a logging framework

# Export the Flask app and database session for use in other modules
def get_app():
    return app

def get_db():
    return db