```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models import Teacher
from src.database import Base, engine

# Setup a test client and database connection for the tests
@pytest.fixture(scope='module')
def test_client():
    # Create the database schema
    Base.metadata.create_all(bind=engine)
    client = TestClient(app)
    yield client
    # Teardown the database after tests
    Base.metadata.drop_all(bind=engine)

def test_create_teacher_valid_data(test_client):
    # Test creating a teacher with valid data
    response = test_client.post('/teachers', json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["name"] == "John Doe"
    assert data["email"] == "john.doe@example.com"

def test_create_teacher_missing_name(test_client):
    # Test creating a teacher without a name
    response = test_client.post('/teachers', json={"email": "john.doe@example.com"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Missing field: name"}}

def test_create_teacher_missing_email(test_client):
    # Test creating a teacher without an email
    response = test_client.post('/teachers', json={"name": "John Doe"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Missing field: email"}}

def test_create_teacher_invalid_email_format(test_client):
    # Test creating a teacher with an invalid email format
    response = test_client.post('/teachers', json={"name": "John Doe", "email": "invalid-email"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Invalid email format"}}

def test_existing_student_and_course_data(test_client):
    # Ensure that existing functionality for students and courses remains unaffected
    response_students = test_client.get('/students')  # assuming this endpoint exists
    response_courses = test_client.get('/courses')    # assuming this endpoint exists
    assert response_students.status_code == 200
    assert response_courses.status_code == 200
    # Add assertions to verify that students and courses data is unchanged if applicable
```