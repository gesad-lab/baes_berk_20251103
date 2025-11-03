```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.main import app
from src.models import Course  # Import Course model for integration testing

# Configure the SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_db.sqlite3"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Fixture to create a new TestClient for each test
@pytest.fixture(scope="module")
def client():
    # Create the testing client and initialize the database
    with TestClient(app) as client:
        yield client

# Fixture to create a test course in the database for testing delete functionality
@pytest.fixture(scope="function")
def test_course(test_db):
    course = Course(name="Test Course", level="Beginner")
    test_db.add(course)
    test_db.commit()
    test_db.refresh(course)  # Ensure the course is committed and retrieved
    yield course
    test_db.delete(course)  # Cleanup after test

def test_delete_course(client, test_course):
    """Test deleting an existing course."""
    response = client.delete(f"/courses/{test_course.id}")
    assert response.status_code == 200  # Expecting a successful deletion response
    assert response.json() == {"message": "Course deleted successfully"}

    # Verify that the course has been deleted
    response = client.get(f"/courses/{test_course.id}")
    assert response.status_code == 404  # Expecting not found for deleted course
    assert response.json() == {"detail": "Course not found"}

def test_delete_non_existing_course(client):
    """Test deleting a non-existing course."""
    response = client.delete("/courses/999")  # ID that doesn't exist
    assert response.status_code == 404  # Expecting not found
    assert response.json() == {"detail": "Course not found"}
```