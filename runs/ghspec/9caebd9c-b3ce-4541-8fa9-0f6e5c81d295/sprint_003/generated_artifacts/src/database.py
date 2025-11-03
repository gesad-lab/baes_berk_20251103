```python
import pytest
from api.validators import validate_course_name, validate_course_level
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

def test_validate_course_name_valid():
    """Ensure that the validator accepts a valid course name."""
    assert validate_course_name("Introduction to Programming") == True

def test_validate_course_name_empty():
    """Ensure that an empty course name raises a validation error."""
    with pytest.raises(ValueError) as excinfo:
        validate_course_name("")
    assert str(excinfo.value) == "Course name must not be empty."

def test_validate_course_level_valid():
    """Ensure that the validator accepts a valid course level."""
    assert validate_course_level("Intermediate") == True

def test_validate_course_level_empty():
    """Ensure that an empty course level raises a validation error."""
    with pytest.raises(ValueError) as excinfo:
        validate_course_level("")
    assert str(excinfo.value) == "Course level must not be empty."

def test_validate_course_creation_valid():
    """Test validation logic for course creation."""
    name = "Data Structures"
    level = "Advanced"
    assert validate_course_name(name) == True
    assert validate_course_level(level) == True

def test_validate_course_creation_invalid():
    """Test validation logic for course creation with missing fields."""
    with pytest.raises(ValueError) as excinfo:
        validate_course_name("")  # Invalid name
    assert str(excinfo.value) == "Course name must not be empty."
    
    with pytest.raises(ValueError) as excinfo:
        validate_course_level("")  # Invalid level
    assert str(excinfo.value) == "Course level must not be empty."
```