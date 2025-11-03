```python
import pytest
import subprocess

# Assuming the existence of a client fixture for the FastAPI application
@pytest.fixture
def client():
    from main import app  # Importing the FastAPI application
    from fastapi.testclient import TestClient
    return TestClient(app)

def test_enroll_student(client):
    # Step 1: Create a new student and course for the test
    student_response = client.post('/students', json={"name": "John Doe"})
    course_response = client.post('/courses', json={"name": "Physics 101", "level": "Intermediate"})
    
    # Extract student_id and course_id from responses
    student_id = student_response.json()['id']
    course_id = course_response.json()['id']
    
    # Step 2: Enroll the created student in the created course
    enrollment_response = client.post('/enrollments', json={"student_id": student_id, "course_id": course_id})
    
    # Step 3: Validate the enrollment response
    assert enrollment_response.status_code == 201
    assert enrollment_response.json()['student_id'] == student_id
    assert enrollment_response.json()['course_id'] == course_id

def test_retrieve_enrolled_courses(client):
    # Step 1: Create a student and a course first
    student_response = client.post('/students', json={"name": "Jane Doe"})
    course_response = client.post('/courses', json={"name": "Biology 101", "level": "Beginner"})

    student_id = student_response.json()['id']
    course_id = course_response.json()['id']

    # Enroll the student in the course
    client.post('/enrollments', json={"student_id": student_id, "course_id": course_id})

    # Step 2: Retrieve courses for the enrolled student
    response = client.get(f'/students/{student_id}/courses')
    
    # Step 3: Validate the response
    assert response.status_code == 200
    enrolled_courses = response.json()
    assert len(enrolled_courses) == 1
    assert enrolled_courses[0]['id'] == course_id

def test_invalid_enrollment(client):
    # Attempt to enroll with invalid IDs
    response = client.post('/enrollments', json={"student_id": "invalid_id", "course_id": "invalid_id"})
    
    # Validate the error response
    assert response.status_code == 400  # Expecting a Bad Request
    assert response.json()['error']['code'] == "E001"

def test_database_migration_script_generation():
    """Test that the Alembic migration generates successfully."""
    try:
        # Run the Alembic command to generate migration script
        result = subprocess.run(
            ['alembic', 'revision', '--autogenerate', '-m', 'Create Enrollments table and relationships'],
            check=True,
            capture_output=True,
            text=True
        )
        assert result.returncode == 0  # Ensure the command was successful
    except subprocess.CalledProcessError as e:
        pytest.fail(f"Alembic migration generation failed: {e.stderr.strip()}")
```