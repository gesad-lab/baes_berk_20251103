```python
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate

# Initialize the database
db = SQLAlchemy()

class Course(db.Model):
    """Course model to represent a course in the database."""
    
    __tablename__ = 'courses'  # Specify table name

    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each course
    name = db.Column(db.String(128), nullable=False)  # Name of the course
    level = db.Column(db.String(128), nullable=False)  # Level of the course

    def __init__(self, name: str, level: str) -> None:
        """
        Initialize a Course instance.

        Args:
            name (str): The name of the course.
            level (str): The level of the course.
        """
        self.name = name
        self.level = level

class CourseSchema(Schema):
    """Schema for validating Course data."""
    
    name = fields.Str(required=True, validate=validate.Length(min=1), error_messages={"required": "Name is required."})
    level = fields.Str(required=True, validate=validate.Length(min=1), error_messages={"required": "Level is required."})

# Here we will add the methods for any additional behaviors related to the Course model if needed.
```