```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.main import app
from src.models import Teacher  # Import the Teacher model
from src.database import get_db

# Configure the SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_db.sqlite3"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency override for testing
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture
def test_client():
    with TestClient(app) as client:
        yield client

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    # Set up the database schema
    import src.models  # Ensure models are imported to create tables
    from sqlalchemy import create_all

    # Create all tables
    src.models.Base.metadata.create_all(bind=engine)
    yield
    # Drop the tables afterwards
    src.models.Base.metadata.drop_all(bind=engine)

def test_create_teacher(test_client):
    # Test creating a new teacher with valid data
    response = test_client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    
    assert response.status_code == 201
    assert response.json() == {
        "id": 1,  # Assuming this is the first teacher and ID starts from 1
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

def test_create_teacher_with_invalid_email(test_client):
    # Test creating a teacher with an invalid email
    response = test_client.post("/teachers", json={"name": "Jane Doe", "email": "not-an-email"})
    
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid email format"  # Adjust according to your error handling message
    }

def test_create_teacher_without_name(test_client):
    # Test creating a teacher without a name
    response = test_client.post("/teachers", json={"email": "jane.doe@example.com"})
    
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Field 'name' is required"  # Adjust according to your error handling message
    }

def test_fetch_teacher(test_client):
    # Test fetching an existing teacher
    response = test_client.get("/teachers/1")
    
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

def test_fetch_non_existing_teacher(test_client):
    # Test fetching a teacher that does not exist
    response = test_client.get("/teachers/999")
    
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Teacher not found"  # Adjust according to your error handling message
    }
```