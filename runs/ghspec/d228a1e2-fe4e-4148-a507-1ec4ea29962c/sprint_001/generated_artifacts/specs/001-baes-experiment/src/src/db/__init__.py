from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize the Flask application
app = Flask(__name__)

# Set up the database configuration (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Import models
from .models import Student

def init_db():
    """Create the database and tables if they do not exist."""
    with app.app_context():
        db.create_all()  # Create all tables
        
# Call the initialization function to set up the database on startup
init_db()