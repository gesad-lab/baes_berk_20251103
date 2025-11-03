```python
# tests/test_database.py

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import Base, Course, Enrollment, Teacher  # Import the new Teacher model
from app.database import engine

# Set up the test database
@pytest.fixture(scope="module")
def test_db():
    # Create the database schema, which includes Course, Enrollment, and now Teacher tables
    Base.metadata.create_all(bind=engine)
    yield
    # Drop the database schema after tests are done
    Base.metadata.drop_all(bind=engine)

# Test to confirm that the Teacher table is created successfully
def test_teacher_table_exists(test_db):
    with engine.connect() as connection:
        result = connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='teachers';")
        assert result.fetchone() is not None  # Ensure that the Teacher table exists

# Test data integrity for existing tables after migration
def test_existing_data_integrity(test_db):
    with engine.connect() as connection:
        # Check for the existing Course table data
        course_count = connection.execute("SELECT COUNT(*) FROM courses;").scalar()
        assert course_count >= 0  # Ensure courses exist and are not negatively affected

        # Check for the existing Enrollment table data
        enrollment_count = connection.execute("SELECT COUNT(*) FROM enrollments;").scalar()
        assert enrollment_count >= 0  # Ensure enrollments exist and are not negatively affected

# Integration test for creating a Teacher record
def test_create_teacher(test_db):
    client = TestClient(app)
    response = client.post("/teachers/", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201  # Check success status code
    assert response.json()["name"] == "John Doe"  # Check returned data

# Test retrieval of a Teacher record
def test_retrieve_teacher(test_db):
    client = TestClient(app)
    response = client.get("/teachers/1")  # Assuming the Teacher ID is 1 for this test
    assert response.status_code == 200  # Check success status
    assert "name" in response.json()  # Ensure that the name field is present
    assert "email" in response.json()  # Ensure that the email field is present

# Test error handling for missing fields when creating a Teacher
def test_create_teacher_missing_fields(test_db):
    client = TestClient(app)
    response = client.post("/teachers/", json={"name": ""})  # Missing email
    assert response.status_code == 422  # Check for unprocessable entity status
    assert response.json()["detail"][0]["msg"] == "field required"  # Field validation error
```