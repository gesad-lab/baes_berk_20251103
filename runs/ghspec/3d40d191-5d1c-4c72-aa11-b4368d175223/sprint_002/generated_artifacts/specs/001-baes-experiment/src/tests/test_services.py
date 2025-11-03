```python
import pytest
from fastapi.testclient import TestClient
from src.api import app
from src.models import Student
from src.database import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create a new SQLite database for testing
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Fixture to provide a test client and database session
@pytest.fixture()
def client():
    """Create a test client for the FastAPI app."""
    with TestClient(app) as client:
        yield client

@pytest.fixture(scope="module")
def setup_database():
    """Create tables for testing and clean up afterward."""
    # Create tables
    Student.metadata.create_all(bind=engine)
    yield
    # Drop tables
    Student.metadata.drop_all(bind=engine)

def test_create_student_with_email(client, setup_database):
    """Test creating a student with a valid name and email."""
    response = client.post("/students", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john@example.com"

def test_create_student_without_email(client, setup_database):
    """Test creating a student without an email returns an error."""
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Email field is required."
```