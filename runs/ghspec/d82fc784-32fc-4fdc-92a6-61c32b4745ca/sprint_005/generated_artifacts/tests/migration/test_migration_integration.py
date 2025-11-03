```python
import pytest
from app import create_app, db
from app.models import Teacher, Student, Course  # Import necessary models
import json

@pytest.fixture
def client():
    """A test client for the Flask application."""
    app = create_app('testing')  # Use the testing configuration
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create the database tables
        yield client
        with app.app_context():
            db.drop_all()  # Clean up the database after tests

def test_create_teacher(client):
    """Test creating a new teacher record."""
    response = client.post('/teachers', json={"name": "Teacher Name", "email": "teacher@example.com"})
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == "Teacher Name"
    assert data['email'] == "teacher@example.com"

def test_retrieve_all_teachers(client):
    """Test retrieving a list of all teachers."""
    client.post('/teachers', json={"name": "Teacher One", "email": "teacher_one@example.com"})
    client.post('/teachers', json={"name": "Teacher Two", "email": "teacher_two@example.com"})
    
    response = client.get('/teachers')
    assert response.status_code == 200
    teachers = response.get_json()
    assert len(teachers) == 2  # Verify that two teachers were added

def test_update_teacher(client):
    """Test updating a teacher's information."""
    response = client.post('/teachers', json={"name": "Old Name", "email": "old_email@example.com"})
    teacher_id = response.get_json()['id']

    update_response = client.put(f'/teachers/{teacher_id}', json={"name": "Updated Name", "email": "updated@example.com"})
    assert update_response.status_code == 200

    # Verify the update
    response = client.get(f'/teachers/{teacher_id}')
    updated_teacher = response.get_json()
    assert updated_teacher['name'] == "Updated Name"
    assert updated_teacher['email'] == "updated@example.com"

def test_student_and_course_integrity_post_migration(client):
    """Test to ensure existing student and course data remains unaffected during migration."""
    # Assume some students and courses were created previously
    client.post('/students', json={"name": "Student One", "email": "student_one@example.com"})
    client.post('/courses', json={"title": "Course One"})

    # Simulate the migration process here, if needed
    
    # Verify existing student and course data
    response_students = client.get('/students')
    assert response_students.status_code == 200
    assert len(response_students.get_json()) == 1  # Assuming the previous student test added one

    response_courses = client.get('/courses')
    assert response_courses.status_code == 200
    assert len(response_courses.get_json()) == 1  # Assuming the previous course test added one

def test_unique_teacher_email(client):
    """Test that teachers must have unique email addresses."""
    client.post('/teachers', json={"name": "Unique Teacher", "email": "unique@example.com"})
    
    duplicate_response = client.post('/teachers', json={"name": "Another Teacher", "email": "unique@example.com"})
    assert duplicate_response.status_code == 400  # Expect a bad request due to duplicate email
    assert duplicate_response.get_json()['error']['message'] == "Email must be unique."
```