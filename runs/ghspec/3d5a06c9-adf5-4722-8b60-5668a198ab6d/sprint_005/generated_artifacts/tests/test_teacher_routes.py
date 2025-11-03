```python
import pytest
from main import app  # Importing the FastAPI application
from fastapi.testclient import TestClient

# Assuming the existence of a client fixture for the FastAPI application
@pytest.fixture
def client():
    return TestClient(app)

def test_create_teacher(client):
    # Step 1: Create a new Teacher
    response = client.post('/teachers', json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    assert response.status_code == 201  # Check if creation is successful
    data = response.json()
    assert data['name'] == "Jane Doe"
    assert data['email'] == "jane.doe@example.com"

def test_create_teacher_missing_fields(client):
    # Step 2: Attempt to create a Teacher without required fields
    response = client.post('/teachers', json={"name": "", "email": ""})
    assert response.status_code == 400  # Check if bad request is returned
    assert response.json() == {"detail": "Both name and email are required."}

def test_create_teacher_invalid_email_format(client):
    # Step 3: Attempt to create a Teacher with an invalid email format
    response = client.post('/teachers', json={"name": "Jane", "email": "notanemail"})
    assert response.status_code == 400  # Check if bad request is returned
    assert response.json() == {"detail": "Invalid email format."}

def test_database_migration_verification(client):
    # Step 4: Verify that migration does not affect existing data
    existing_students = client.get('/students')
    existing_courses = client.get('/courses')
    
    assert existing_students.status_code == 200
    assert existing_courses.status_code == 200
    # Assuming a method to check the length of existing data
    assert len(existing_students.json()) > 0  
    assert len(existing_courses.json()) > 0
```