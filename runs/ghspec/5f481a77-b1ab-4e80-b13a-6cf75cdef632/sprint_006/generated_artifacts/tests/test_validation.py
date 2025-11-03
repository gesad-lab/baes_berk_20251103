```python
import pytest
from flask import json
from src.app import app  # Assuming the Flask app is initialized in app.py
from marshmallow.exceptions import ValidationError
from src.schemas import TeacherSchema  # Assuming TeacherSchema exists
from src.models import Course  # Assuming Course model is defined and imported correctly

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

class TestAssignTeacherValidation:
    @pytest.fixture
    def course_with_valid_teacher(self):
        """Fixture to create a course and assign a valid teacher."""
        # You may need to create a valid course and teacher in the database here
        return Course(id=1, name='Introduction to Programming')

    def test_assign_teacher_with_valid_teacher_id(self, client, course_with_valid_teacher):
        """Test assigning a teacher with a valid teacher_id."""
        response = client.post('/courses/1/assign-teacher', data=json.dumps({'teacher_id': 1}),
                                content_type='application/json')
        assert response.status_code == 200  # Assuming the assignment is successful

    def test_assign_teacher_with_invalid_course_id(self, client):
        """Test assigning a teacher to a non-existent course."""
        response = client.post('/courses/999/assign-teacher', data=json.dumps({'teacher_id': 1}),
                                content_type='application/json')
        assert response.status_code == 404  # Verify not-found status for invalid course

    def test_assign_teacher_with_invalid_teacher_id(self, client):
        """Test assigning a teacher with an invalid teacher_id."""
        response = client.post('/courses/1/assign-teacher', data=json.dumps({'teacher_id': 999}),
                                content_type='application/json')
        assert response.status_code == 400  # Assuming the teacher_id is invalid

    def test_assign_teacher_without_teacher_id(self, client):
        """Test the response when no teacher_id is provided."""
        response = client.post('/courses/1/assign-teacher', data=json.dumps({}),
                                content_type='application/json')
        assert response.status_code == 400  # Bad Request for missing data

    def test_assign_teacher_with_non_integer_teacher_id(self, client):
        """Test assigning a teacher with a non-integer teacher_id."""
        response = client.post('/courses/1/assign-teacher', data=json.dumps({'teacher_id': 'abc'}),
                                content_type='application/json')
        assert response.status_code == 400  # Bad Request for invalid teacher ID type
```