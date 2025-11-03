```python
# tests/test_teacher.py

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import Base, Teacher
from app.database import engine

# Set up the test database for teacher entity tests
@pytest.fixture(scope="module")
def test_db():
    # Create the database schema, including the Teacher table
    Base.metadata.create_all(bind=engine)
    yield
    # Drop the database schema after tests are done
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

def test_create_teacher(client, test_db):
    # Test creating a new teacher
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john.doe@example.com"

def test_create_teacher_without_name(client, test_db):
    # Test creating a teacher without a name
    response = client.post("/teachers", json={"email": "john.doe@example.com"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name is required."}}

def test_create_teacher_without_email(client, test_db):
    # Test creating a teacher without an email
    response = client.post("/teachers", json={"name": "John Doe"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Email is required."}}

def test_get_teacher(client, test_db):
    # First, create a teacher to retrieve
    create_response = client.post("/teachers", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    teacher_id = create_response.json()["id"]
    
    # Test retrieving the created teacher's details
    response = client.get(f"/teachers/{teacher_id}")
    assert response.status_code == 200
    assert response.json()["id"] == teacher_id
    assert response.json()["name"] == "Jane Doe"
    assert response.json()["email"] == "jane.doe@example.com"

def test_get_nonexistent_teacher(client, test_db):
    # Test retrieving a nonexistent teacher
    response = client.get("/teachers/999")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E003", "message": "Teacher not found."}}
```