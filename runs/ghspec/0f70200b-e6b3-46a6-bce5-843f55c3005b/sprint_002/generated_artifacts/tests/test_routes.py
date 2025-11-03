```python
import pytest
from fastapi.testclient import TestClient
from src.app import app
from src.models import Student

client = TestClient(app)

@pytest.fixture(scope="module")
def test_students():
    """Setup test students in the database before any tests run."""
    # Assume a setup function exists to clear and populate the database
    clear_and_seed_database_with_students()
    yield
    # Tear down test database cleanup
    clear_test_database()

def test_retrieve_all_students_has_email(test_students):
    """Test retrieval of all students to ensure emails are present."""
    response = client.get("/students")
    assert response.status_code == 200, "Expected status code 200"
    
    students = response.json()
    assert isinstance(students, list), "Expected a JSON array of students"
    
    for student in students:
        assert "email" in student, f"Student ID {student['id']} does not have an email field"
        assert isinstance(student["email"], str) and student["email"], f"Student ID {student['id']} has an invalid email"
```
