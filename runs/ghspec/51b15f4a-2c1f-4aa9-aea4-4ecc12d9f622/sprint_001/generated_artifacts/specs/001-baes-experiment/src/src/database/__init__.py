from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///students.db')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy ORM
db = SQLAlchemy(app)

def init_db():
    """Create the database schema on application startup."""
    with app.app_context():
        # Create the students table
        db.create_all()

# Call the init_db function to create tables
init_db()