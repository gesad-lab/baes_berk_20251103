```python
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import Base, Student
from app.database import engine

# Create a test client
client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    # Create the database and the tables for testing
    Base.metadata.create_all(bind=engine)
    
    yield  # This is where the testing happens

    # Drop the database tables after tests are done
    Base.metadata.drop_all(bind=engine)

def test_create_student_with_email(setup_database):
    """Test creating a student with valid email."""
    response = client.post("/students/", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john.doe@example.com"

def test_create_student_without_email(setup_database):
    """Test attempting to create a student without an email."""
    response = client.post("/students/", json={"name": "Jane Doe"})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json()["detail"][0]["msg"] == "field required"

def test_retrieve_all_students_with_emails(setup_database):
    """Test retrieving all students to ensure email is included."""
    client.post("/students/", json={"name": "John Doe", "email": "john.doe@example.com"})
    client.post("/students/", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    
    response = client.get("/students/")
    assert response.status_code == 200
    students = response.json()
    assert len(students) == 2
    assert all("email" in student for student in students)

def test_database_schema_migration_contains_email_field(setup_database):
    """Test that the email field exists in the Student model."""
    # Reflect the current schema
    inspector = inspect(engine)
    columns = [column['name'] for column in inspector.get_columns('students')]
    assert "email" in columns, "Email field should exist in the students table"
```