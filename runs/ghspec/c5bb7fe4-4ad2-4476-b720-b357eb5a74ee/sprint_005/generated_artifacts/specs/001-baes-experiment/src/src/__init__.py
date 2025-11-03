```python
# src/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy part of the app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Importing models
from src.models.student import Student  # Assuming Student is defined in src/models
from src.models.course import Course      # Assuming Course is defined in src/models
from src.models.teacher import Teacher    # New Teacher model import

# Ensure the database is created
with app.app_context():
    db.create_all()  # Create database tables based on models


# New Teacher model to be implemented in src/models/teacher.py
class Teacher(db.Model):
    """Database model for Teacher."""
    
    __tablename__ = 'teachers'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)

    def __repr__(self):
        return f"<Teacher(id={self.id}, name={self.name}, email={self.email})>"
```