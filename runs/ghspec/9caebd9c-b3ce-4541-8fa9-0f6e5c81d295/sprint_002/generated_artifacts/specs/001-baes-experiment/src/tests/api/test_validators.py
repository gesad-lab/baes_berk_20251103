```python
import pytest
from api.validators import validate_student_name, validate_student_email
from api.models import Student
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application for testing
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create the database within the testing context
with app.app_context():
    db.create_all()

def test_validate_student_name_success():
    """Test that a valid student name passes the validation."""
    valid_name = "John Doe"
    assert validate_student_name(valid_name) is None  # No exception means valid

def test_validate_student_name_empty():
    """Test that an empty student name raises a validation error."""
    empty_name = ""
    with pytest.raises(ValueError) as excinfo:
        validate_student_name(empty_name)
    assert str(excinfo.value) == "Student name cannot be empty."

def test_validate_student_email_success():
    """Test that a valid student email passes the validation."""
    valid_email = "student@example.com"
    assert validate_student_email(valid_email) is None  # No exception means valid

def test_validate_student_email_empty():
    """Test that an empty student email raises a validation error."""
    empty_email = ""
    with pytest.raises(ValueError) as excinfo:
        validate_student_email(empty_email)
    assert str(excinfo.value) == "Student email cannot be empty."

def test_create_student_success():
    """Test the creation of a valid student entity."""
    new_student = Student(name="Alice Smith", email="alice@example.com")
    db.session.add(new_student)
    db.session.commit()
    
    # Fetch the student from the database
    student = Student.query.filter_by(name="Alice Smith").first()
    assert student is not None
    assert student.email == "alice@example.com"

def test_create_student_missing_email():
    """Test creating a student without an email should raise a validation error."""
    with pytest.raises(ValueError) as excinfo:
        Student(name="Bob Brown", email="")
        db.session.commit()
    assert str(excinfo.value) == "Student email cannot be empty."

def test_retrieve_student_details():
    """Test retrieving student details returns the correct data."""
    new_student = Student(name="Charlie Black", email="charlie@example.com")
    db.session.add(new_student)
    db.session.commit()
    
    # Fetch the student and check details
    student = Student.query.get(1)  # Assuming this is the first student
    assert student.name == "Charlie Black"
    assert student.email == "charlie@example.com"
```