```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models import Student
from src.database import init_db, get_db
from sqlalchemy.orm import Session

# Setup the test client and initialize the database
@pytest.fixture(scope="module")
def client():
    # Initialize the database and create tables if they don't exist
    init_db()
    
    # Create the FastAPI testing client
    with TestClient(app) as c:
        yield c  # This is where the testing happens

def test_add_student(client: TestClient):
    # Test adding a new student
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 200
    assert response.json() == {"message": "Student added successfully"}

def test_add_student_missing_name(client: TestClient):
    # Test adding a student with missing name
    response = client.post("/students", json={"name": ""})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name is required"}}

def test_get_students(client: TestClient):
    # Test retrieving all students
    response = client.get("/students")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Ensure it's a list
```
