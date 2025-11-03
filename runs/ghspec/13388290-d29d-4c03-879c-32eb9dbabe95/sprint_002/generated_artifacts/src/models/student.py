```python
# src/models/student.py

from app import db

class Student(db.Model):
    """Model representing a student in the database."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)  # Required name field
    email = db.Column(db.String, nullable=False)  # New required email field

    def __init__(self, name: str, email: str):
        """Initialize a new student with name and email."""
        self.name = name
        self.email = email

    def to_dict(self):
        """Convert the Student model to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
        }
```