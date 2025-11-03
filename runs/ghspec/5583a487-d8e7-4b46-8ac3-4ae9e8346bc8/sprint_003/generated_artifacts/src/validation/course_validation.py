```python
from flask import jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the database
db = SQLAlchemy()

# Define the Course model
class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    level = db.Column(db.String, nullable=False)

# Define a schema for course validation
class CourseSchema(Schema):
    name = fields.String(required=True)
    level = fields.String(required=True)

# Function to validate course creation input
def validate_course_input(data):
    """
    Validates the course creation input.
    
    Args:
        data (dict): The input data for the course.
    
    Returns:
        dict: The validated data.
    
    Raises:
        ValidationError: If validation fails.
    """
    schema = CourseSchema()
    return schema.load(data)

# Error handling for validation errors
def handle_validation_error(error):
    """
    Handles validation errors by returning a JSON response.
    
    Args:
        error (ValidationError): The validation error raised.
    
    Returns:
        tuple: A JSON error response and status code.
    """
    return jsonify({"error": {"code": "E001", "message": "Invalid input", "details": error.messages}}), 400
```