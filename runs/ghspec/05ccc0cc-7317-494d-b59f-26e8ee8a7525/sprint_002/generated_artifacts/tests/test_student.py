```python
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import Base, Student
from app.database import engine

# Set up the test database
@pytest.fixture(scope="module")
def test_db():
    # Create the database schema
    Base.metadata.create_all(bind=engine)
    yield
    # Drop the database schema after tests are done
    Base.metadata.drop_all(bind=engine)

# Test client instance for making API requests
@pytest.fixture(scope='module')
def client(test_db):
    with TestClient(app) as c:
        yield c

# Test: Create a Student with Email
def test_create_student_with_email(client):
    response = client.post("/students", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john@example.com"

# Test: Error Handling for Missing Email
def test_create_student_without_email(client):
    response = client.post("/students", json={"name": "Jane Doe"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Email is required.", "details": {}}}

# Test: Retrieve All Students with Emails
def test_retrieve_all_students_with_emails(client):
    # First, create a student to ensure we have data to retrieve
    client.post("/students", json={"name": "Alice Smith", "email": "alice@example.com"})
    response = client.get("/students")
    assert response.status_code == 200
    students = response.json()
    assert len(students) > 0
    assert all("email" in student for student in students)

# Test: Database Schema Migration for Email Field
def test_migration_includes_email_field(test_db):
    # This test checks if the email column exists in the Student table
    from sqlalchemy import inspect
    inspector = inspect(engine)
    columns = [col['name'] for col in inspector.get_columns('students')]
    assert 'email' in columns
```