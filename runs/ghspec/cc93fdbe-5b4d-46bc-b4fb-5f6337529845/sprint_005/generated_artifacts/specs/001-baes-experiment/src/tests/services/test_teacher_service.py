```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app  # Assuming the FastAPI app is defined in main.py
from models import Base, Teacher  # Importing the Teacher model

client = TestClient(app)

# Database setup for testing
DATABASE_URL = "sqlite:///./test.db"  # Use a separate test database for isolated tests
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def setup_db():
    """Setup test database and clean up after tests."""
    # Create the database schema
    Base.metadata.create_all(bind=engine)
    yield
    # Drop the database schema after tests
    Base.metadata.drop_all(bind=engine)

def test_create_teacher_success(setup_db):
    """Test if a teacher can be created successfully with valid data."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201  # Status code for created
    assert response.json() == {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}

def test_create_teacher_missing_fields(setup_db):
    """Test how the application handles missing required fields."""
    response = client.post("/teachers", json={"name": "", "email": ""})
    assert response.status_code == 400  # Bad request
    assert response.json()['error']['message'] == "Name and email are required."

def test_create_teacher_duplicate_email(setup_db):
    """Test if the application prevents creating a teacher with an existing email."""
    client.post("/teachers", json={"name": "Jane Doe", "email": "jane.doe@example.com"})  # Create first teacher
    response = client.post("/teachers", json={"name": "John Smith", "email": "jane.doe@example.com"})  # Duplicate email
    assert response.status_code == 400  # Bad request
    assert response.json()['error']['message'] == "Email must be unique."

# Note: The migration test would typically be placed here, 
# but this is a service test and not directly related to the migration logic.
```