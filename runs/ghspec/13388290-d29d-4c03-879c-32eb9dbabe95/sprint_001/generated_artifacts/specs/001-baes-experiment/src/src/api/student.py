```python
from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields, ValidationError
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the SQLAlchemy base class
Base = declarative_base()

# Define the Student model
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

# Define the StudentSchema with validation for the name
class StudentSchema(Schema):
    name = fields.String(required=True, error_messages={"required": "E001: Name is required."})

# Create a blueprint for the student API
student_api = Blueprint('student_api', __name__)

# Function to create a new student
@student_api.route('/students', methods=['POST'])
def create_student():
    """Create a new student record."""
    schema = StudentSchema()
    try:
        # Validate and deserialize input data
        student_data = schema.load(request.json)
        # Create the Student instance
        new_student = Student(name=student_data['name'])
        # Add to the session and commit (pseudo code, actual DB session handling needed)
        # db_session.add(new_student)
        # db_session.commit()
        
        return jsonify({"message": "Student created successfully", "student": student_data}), 201
    except ValidationError as err:
        # Return validation errors
        return jsonify({"error": err.messages}), 400
    except Exception as e:
        # General error handling
        return jsonify({"error": {"code": "E002", "message": "An error occurred", "details": str(e)}}), 500
```