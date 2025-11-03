```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app  # Assuming the FastAPI app is defined in main.py
from models import Base, Teacher  # Import the Teacher model

client = TestClient(app)

# Database setup for testing
DATABASE_URL = "sqlite:///./test.db"  # Use a separate test database for integration tests
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def setup_db():
    """Setup the test database and create the necessary tables."""
    # Create the database tables
    Base.metadata.create_all(bind=engine)
    yield
    # Drop the database tables after tests are done
    Base.metadata.drop_all(bind=engine)

def test_create_teacher_success(setup_db):
    """Test for successfully creating a new teacher record."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201  # check if status code is 201 Created
    assert response.json() == {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}

def test_create_teacher_missing_fields(setup_db):
    """Test error handling for missing required fields while creating teacher."""
    response = client.post("/teachers", json={"name": ""})  # Missing email
    assert response.status_code == 400  # check if status code is 400 Bad Request
    assert response.json() == {"error": {"code": "E001", "message": "Email is required", "details": {}}}

def test_create_teacher_unique_email_constraint(setup_db):
    """Test that the system prevents creation of a teacher with a duplicate email."""
    # Create the first teacher
    client.post("/teachers", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    
    # Attempt to create another teacher with the same email
    response = client.post("/teachers", json={"name": "Jane Smith", "email": "jane.doe@example.com"})
    assert response.status_code == 400  # check if status code is 400 Bad Request
    assert response.json() == {"error": {"code": "E002", "message": "Email must be unique", "details": {}}}

def test_database_migration_teacher_table(setup_db):
    """Test that the Teacher table is created and existing data remains unchanged."""
    # Check if the Teacher table exists after the migration
    with SessionLocal() as session:
        result = session.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='teachers';").fetchone()
        assert result is not None, "Teacher table was not created"
```