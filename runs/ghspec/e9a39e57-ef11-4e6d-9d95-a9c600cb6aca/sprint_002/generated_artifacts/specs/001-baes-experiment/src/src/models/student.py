```python
# File: src/models/student.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define the Student model
class Student(db.Model):
    __tablename__ = 'students'  # Specify table name for the model
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)  # New email field

    def __init__(self, name: str, email: str):
        """Initialize a new Student instance.

        Args:
            name (str): The student's name.
            email (str): The student's email.
        """
        self.name = name
        self.email = email
```