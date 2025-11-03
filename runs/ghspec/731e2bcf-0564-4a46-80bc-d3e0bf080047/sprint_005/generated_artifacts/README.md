```
# File: tests/test_database_migrations.py

import pytest
from flask import json
from src.app import create_app, db
from src.models.student import Student
from src.models.course import Course
from src.models.teacher import Teacher  # Importing the Teacher model

@pytest.fixture
def app():
    """Fixture for creating a Flask application with test configuration."""
    app = create_app({'TESTING': True})

    with app.app_context():
        # Create the database and tables for Student, Course, and Teacher
        db.create_all()
        yield app
        # Drop the database after tests are finished
        db.drop_all()

def test_teacher_table_creation(app):
    """Test that the Teacher table is created in the database."""
    with app.app_context():
        # Verify that the Teacher table exists
        assert 'teachers' in db.metadata.tables

def test_teacher_model(app):
    """Test the Teacher model's creation and persistence."""
    with app.app_context():
        # Create a new teacher instance
        teacher = Teacher(name='John Doe', email='john.doe@example.com')
        db.session.add(teacher)
        db.session.commit()

        # Verify the teacher is saved correctly
        assert teacher.id is not None  # Ensure teacher has been assigned an ID
        assert Teacher.query.filter_by(email='john.doe@example.com').first() is not None

def test_duplicate_teacher_email(app):
    """Test that adding a teacher with a duplicate email raises an error."""
    with app.app_context():
        # Add the first teacher
        teacher1 = Teacher(name='Jane Doe', email='jane.doe@example.com')
        db.session.add(teacher1)
        db.session.commit()

        # Attempt to add another teacher with the same email
        teacher2 = Teacher(name='Mary Smith', email='jane.doe@example.com')
        db.session.add(teacher2)

        with pytest.raises(Exception):
            db.session.commit()  # This should raise an exception for the duplicate email

        # Rollback the session to clean up
        db.session.rollback()
```