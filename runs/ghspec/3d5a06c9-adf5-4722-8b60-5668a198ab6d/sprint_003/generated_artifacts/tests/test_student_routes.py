```python
import pytest

# Assuming the existence of a client fixture for the FastAPI application
@pytest.fixture
def client():
    from main import app  # Importing the FastAPI application
    from fastapi.testclient import TestClient
    return TestClient(app)

def test_create_course(client):
    # Step 1: Send a request to create a new course
    response = client.post('/courses', json={"name": "Mathematics 101", "level": "Beginner"})
    
    # Step 2: Validate the response
    assert response.status_code == 201  # Check if course was created successfully
    assert response.json() == {"name": "Mathematics 101", "level": "Beginner"}  # Check course details

def test_list_courses(client):
    # Ensure the list_courses function works by first creating courses
    client.post('/courses', json={"name": "Physics 101", "level": "Intermediate"})
    client.post('/courses', json={"name": "Chemistry 101", "level": "Beginner"})
    
    # Step 1: Retrieve the courses
    response = client.get('/courses')
    
    # Step 2: Validate the response
    assert response.status_code == 200
    courses = response.json()
    assert len(courses) == 2
    assert {"name": "Physics 101", "level": "Intermediate"} in courses
    assert {"name": "Chemistry 101", "level": "Beginner"} in courses

def test_create_course_invalid(client):
    # Step 1: Attempt to create a course without name
    response = client.post('/courses', json={"level": "Advanced"})
    assert response.status_code == 400  # Check for bad request
    assert response.json() == {"error": {"code": "E001", "message": "Both name and level are required"}} 

    # Step 2: Attempt to create a course without level
    response = client.post('/courses', json={"name": "Biology 101"})
    assert response.status_code == 400  # Check for bad request
    assert response.json() == {"error": {"code": "E001", "message": "Both name and level are required"}} 

def test_database_integrity_after_migration(client):
    # This assumes that the migration has been run previously
    # Fetch existing student data and verify it remains intact
    response = client.get('/students')  # Assuming this is the endpoint for students
    assert response.status_code == 200
    students_data = response.json()
    
    # Ensure students data is present (the check can be modified based on actual data)
    assert len(students_data) > 0  # Ensure that existing students are still present
```