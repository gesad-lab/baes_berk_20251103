```python
import json
import pytest
from your_application import app, db, Teacher, Course  # Adjust import based on your structure

# Reinitialize the Flask application and SQLAlchemy for testing
@pytest.fixture(scope='module')
def test_client():
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database and tables for testing
            # Create a teacher for testing
            teacher = Teacher(name="Test Teacher")
            db.session.add(teacher)
            db.session.commit()
            yield client
            db.drop_all()  # Clean up after tests

def test_retrieve_course_with_teacher_success(test_client):
    """Test successful retrieval of course details with assigned teacher."""
    # Setup: Create a course and assign a teacher
    teacher = Teacher.query.first()  # Assume there is at least one teacher
    course = Course(title="Test Course", teacher_id=teacher.id)
    db.session.add(course)
    db.session.commit()
    
    # Act: Retrieve course details
    response = test_client.get(f'/courses/{course.id}')
    
    # Assert: Check that response includes course and teacher details
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['id'] == course.id
    assert data['title'] == "Test Course"
    assert data['teacher']['id'] == teacher.id
    assert data['teacher']['name'] == "Test Teacher"

def test_retrieve_course_with_no_teacher(test_client):
    """Test retrieval of course details that has no assigned teacher."""
    # Setup: Create a course without a teacher
    course = Course(title="Untaught Course")
    db.session.add(course)
    db.session.commit()
    
    # Act: Retrieve course details
    response = test_client.get(f'/courses/{course.id}')
    
    # Assert: Check that teacher details are None
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['id'] == course.id
    assert data['title'] == "Untaught Course"
    assert data['teacher'] is None

def test_teacher_assignment_error_handling(test_client):
    """Test error handling for course retrieval with invalid teacher ID."""
    # Setup: Create a course with a non-existent teacher ID (simulate)
    course = Course(title="Invalid Teacher Course")
    db.session.add(course)
    db.session.commit()
    
    # Act: Attempt to assign a non-existing teacher
    response = test_client.put(f'/courses/{course.id}/assign-teacher', 
                                json={"teacher_id": "invalid_id"})
    
    # Assert: Check that the response indicates error
    assert response.status_code == 400  # Assuming 400 for bad request
    data = json.loads(response.data)
    assert data['error']['code'] == "E001"  # Assume this is the error code for invalid teacher ID
    assert "Invalid teacher ID" in data['error']['message']
```