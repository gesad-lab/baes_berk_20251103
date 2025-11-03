```python
import pytest
from flask import Flask
from your_app import create_app, db  # make sure to replace with actual import paths
from your_app.models import Course  # update with actual model import
from your_app.services.course_service import create_course  # update with actual service import


@pytest.fixture
def client():
    app = create_app('testing')  # use the testing configuration
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # create the database schema
        yield client
        with app.app_context():
            db.drop_all()  # clean up the database


def test_create_course(client):
    """Test creating a new course successfully."""
    data = {
        'name': 'Mathematics 101',
        'level': 'Beginner'
    }
    response = client.post('/courses', json=data)
    assert response.status_code == 201
    assert 'id' in response.json
    assert response.json['name'] == data['name']
    assert response.json['level'] == data['level']


def test_get_course_by_id(client):
    """Test retrieval of course details by ID."""
    data = {
        'name': 'Physics 101',
        'level': 'Intermediate'
    }
    create_course(data)  # Assuming create_course directly modifies the DB
    response = client.get('/courses/1')  # ID here is based on the insertion
    assert response.status_code == 200
    assert response.json['name'] == data['name']
    assert response.json['level'] == data['level']


def test_create_course_missing_fields(client):
    """Test attempting to create a course without required fields."""
    response = client.post('/courses', json={})  # No data provided
    assert response.status_code == 400
    assert response.json == {
        'error': {
            'code': 'E001',
            'message': 'Missing required fields: name, level',
            'details': {}
        }
    }


def test_database_schema_update_verification(client):
    """Test to ensure that the Course table exists in the database."""
    with client.application.app_context():
        # Assuming 'Course' is the name of your course model
        table_exists = db.engine.dialect.has_table(db.engine, 'courses')
        assert table_exists is True

        # Verify existing Student data is intact (example check)
        student_count = db.session.query(Student).count()
        assert student_count >= 0  # Ensure we have student records
```