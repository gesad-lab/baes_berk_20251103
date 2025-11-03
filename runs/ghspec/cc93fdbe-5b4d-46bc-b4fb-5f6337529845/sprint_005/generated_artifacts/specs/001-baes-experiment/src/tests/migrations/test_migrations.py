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
    """Test creating a teacher record with valid data."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201  # 201 Created
    assert response.json() == {"message": "Teacher created successfully"}


def test_create_teacher_missing_fields(setup_db):
    """Test error handling when required fields are missing."""
    response = client.post("/teachers", json={"name": "", "email": ""})
    assert response.status_code == 422  # 422 Unprocessable Entity
    assert response.json()['detail'] == [
        {"loc": ["body", "name"], "msg": "field required", "type": "value_error.missing"},
        {"loc": ["body", "email"], "msg": "field required", "type": "value_error.missing"}
    ]


def test_create_teacher_unique_email_constraint(setup_db):
    """Test to prevent creating a teacher with a duplicate email."""
    client.post("/teachers", json={"name": "John Doe", "email": "john@example.com"})  # Create first teacher
    response = client.post("/teachers", json={"name": "Jane Doe", "email": "john@example.com"})  # Attempt to create second
    assert response.status_code == 400  # 400 Bad Request
    assert response.json() == {"detail": "Email address must be unique"}


def test_database_migration_creates_teacher_table(setup_db):
    """Test to ensure that the Teacher table is created without data loss."""
    # Check if the teacher table exists
    with SessionLocal() as session:
        result = session.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='teachers';")
        assert result.fetchone() is not None  # Teacher table should exist
```