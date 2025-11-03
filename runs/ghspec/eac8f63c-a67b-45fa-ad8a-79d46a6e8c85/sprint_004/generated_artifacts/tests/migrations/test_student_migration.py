```python
# tests/migrations/test_student_migration.py

import logging
import pytest

# Configure structured logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')


@pytest.fixture
def setup_student_data():
    # Setup code to create initial student data for testing
    pass


def log_response(action: str, response: dict):
    """Log the API response in a structured manner."""
    logging.info({
        'action': action,
        'status': response.get('status'),
        'data': response.get('data'),
        'error': response.get('error')
    })


def test_associate_course_with_student(setup_student_data):
    """Test case for associating a course with a student."""
    response = {}  # Assume this contains the response from the API call
    # Simulate API call to associate course with student
    log_response('associate_course_with_student', response)
    assert response.get('status') == 'success'


def test_retrieve_student_courses(setup_student_data):
    """Test case for retrieving student details with associated courses."""
    response = {}  # Assume this contains the API call response
    # Simulate API call to retrieve student courses
    log_response('retrieve_student_courses', response)
    assert response.get('status') == 'success'
    assert 'courses' in response.get('data')


def test_error_handling_invalid_course(setup_student_data):
    """Test case for handling invalid course association."""
    response = {}  # Assume this simulates the API call with an invalid course ID
    # Simulate API call to associate invalid course with student
    log_response('error_handling_invalid_course', response)
    assert response.get('status') == 'error'
    assert response.get('error') == 'Invalid course ID provided'
```