```python
import pytest

# Assuming the existence of a client fixture for the FastAPI application
@pytest.fixture
def client():
    from main import app  # Importing the FastAPI application
    from fastapi.testclient import TestClient
    return TestClient(app)

def test_list_students(client):
    # Step 1: Create a couple of students
    client.post('/students', json={"name": "Alice Smith", "email": "alice.smith@example.com"})
    client.post('/students', json={"name": "Bob Johnson", "email": "bob.johnson@example.com"})
    
    # Step 2: Verify that the list of students is correct
    response = client.get('/students')
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]["name"] == "Alice Smith"
    assert response.json()[1]["name"] == "Bob Johnson"

def test_create_student(client):
    response = client.post('/students', json={"name": "Charlie Brown", "email": "charlie.brown@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "Charlie Brown"

def test_create_student_without_email(client):
    response = client.post('/students', json={"name": "Daisy Green"})
    assert response.status_code == 400  # Expecting a bad request due to missing email

    # Assert that the response contains the appropriate error message
    assert response.json() == {"error": {"code": "E001", "message": "Email is required", "details": {}}}

def test_student_course_relationship(client):
    # Step 1: Create a student
    response = client.post('/students', json={"name": "Eve White", "email": "eve.white@example.com"})
    student_id = response.json()["id"]

    # Step 2: Create a course
    course_response = client.post('/courses', json={"name": "History 101", "level": "Intermediate"})
    course_id = course_response.json()["id"]

    # Step 3: Enroll the student in the created course
    enrollment_response = client.post(f'/students/{student_id}/courses', json={"course_id": course_id})
    assert enrollment_response.status_code == 200
    assert enrollment_response.json()["course_id"] == course_id

    # Step 4: Verify that the student is now associated with the course
    student_courses_response = client.get(f'/students/{student_id}/courses')
    assert student_courses_response.status_code == 200
    assert len(student_courses_response.json()) == 1
    assert student_courses_response.json()[0]["id"] == course_id
```