```python
import pytest
from fastapi.testclient import TestClient
from src.api.student_api import app  # Assuming the FastAPI instance is in this module
from src.database import get_db, Database  # Assuming there's a database module

client = TestClient(app)

@pytest.fixture(scope="module")
def db():
    # Create a new in-memory database or use a test database
    test_db = Database()
    test_db.create_tables()
    yield test_db
    test_db.drop_tables()

def test_list_students_empty(db):
    # Test that listing students returns an empty list when no students are present
    response = client.get("/students")
    assert response.status_code == 200
    assert response.json() == []

def test_list_students_with_email(db):
    # Test that listing students returns the correct student details including emails
    # First, create a student
    client.post("/students", json={"name": "John Doe", "email": "john.doe@example.com"})
    client.post("/students", json={"name": "Jane Doe", "email": "jane.doe@example.com"})

    # Now, retrieve the list of students
    response = client.get("/students")
    assert response.status_code == 200
    students = response.json()

    # Check response contains two students with correct information
    assert len(students) == 2
    assert any(student['name'] == "John Doe" and student['email'] == "john.doe@example.com" for student in students)
    assert any(student['name'] == "Jane Doe" and student['email'] == "jane.doe@example.com" for student in students)

def test_list_students_with_invalid_email(db):
    # Validate that creating a student with an invalid email returns the correct error
    response = client.post("/students", json={"name": "Invalid Email", "email": "invalidemail"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid email format"}

```