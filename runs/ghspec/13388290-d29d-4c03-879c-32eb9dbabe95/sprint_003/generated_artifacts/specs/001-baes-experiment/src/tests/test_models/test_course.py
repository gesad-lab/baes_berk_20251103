```python
import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.models import Course

# Setup Flask and SQLAlchemy for testing
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create the database schema for testing
with app.app_context():
    db.create_all()

def test_create_course():
    """Test successful creation of a course with valid data."""
    course = Course(name="Biology 101", level="Intermediate")
    db.session.add(course)
    db.session.commit()

    # Retrieve the course to verify it was created
    created_course = Course.query.filter_by(name="Biology 101").first()
    assert created_course is not None
    assert created_course.name == "Biology 101"
    assert created_course.level == "Intermediate"

def test_create_course_without_name():
    """Test creation fails when name is not provided."""
    course = Course(name="", level="Advanced")
    db.session.add(course)
    
    # Expecting an error due to missing required fields
    with pytest.raises(Exception) as exc_info:
        db.session.commit()
    
    assert "UNIQUE constraint failed" not in str(exc_info.value)  # Ensure not failing due to uniqueness
    # Check if the course was not added to the database
    no_course = Course.query.filter_by(level="Advanced").first()
    assert no_course is None

def test_create_course_without_level():
    """Test creation fails when level is not provided."""
    course = Course(name="Math 101", level="")
    db.session.add(course)

    # Expecting an error due to missing required fields
    with pytest.raises(Exception) as exc_info:
        db.session.commit()
    
    assert "UNIQUE constraint failed" not in str(exc_info.value)  # Ensure not failing due to uniqueness
    # Check if the course was not added to the database
    no_course = Course.query.filter_by(name="Math 101").first()
    assert no_course is None
```