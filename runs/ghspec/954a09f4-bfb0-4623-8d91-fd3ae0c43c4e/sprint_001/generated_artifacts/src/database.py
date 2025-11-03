import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Define the absolute path for the SQLite database file
DATABASE_FILE = os.path.join(os.path.dirname(__file__), 'students.db')

# Initialize the SQLAlchemy object
db = SQLAlchemy()

def initialize_database(app: Flask) -> None:
    """Initializes the database with the application context."""
    # Set up the SQLAlchemy database URI for SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASE_FILE}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Bind the app to the SQLAlchemy instance
    db.init_app(app)

    with app.app_context():
        # Create the database tables based on the defined models
        db.create_all()
        print("Database initialized and tables created.")  # Log for success confirmation

class Student(db.Model):
    """Model representing a Student entity."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)  # Required field

    def __repr__(self):
        return f'<Student {self.name}>'  # String representation for debugging