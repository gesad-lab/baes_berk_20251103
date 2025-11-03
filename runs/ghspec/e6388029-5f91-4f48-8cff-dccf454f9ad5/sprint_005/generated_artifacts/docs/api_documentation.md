```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.main import app
from src.models import Teacher  # Import the Teacher model for testing
from src.database import get_db

# Configure the SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_db.sqlite3"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the testing client
@pytest.fixture(scope="module")
def test_client():
    # Override the database session for testing
    app.dependency_overrides[get_db] = lambda: TestingSessionLocal()
    with TestClient(app) as client:
        yield client

@pytest.fixture(scope="module")
def setup_database():
    # Create the database and tables
    with TestingSessionLocal() as session:
        # Create all tables (e.g. Teacher)
        session.execute("CREATE TABLE teachers (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)")
        session.commit()
    yield
    # Clean up the database after tests
    with TestingSessionLocal() as session:
        session.execute("DROP TABLE teachers")
        session.commit()

def test_create_teacher(test_client, setup_database):
    # Test creating a new teacher
    response = test_client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}

def test_create_teacher_with_invalid_data(test_client, setup_database):
    # Test creating a teacher with missing email
    response = test_client.post("/teachers", json={"name": "Jane Doe"})
    assert response.status_code == 422  # Unprocessable Entity for missing fields

def test_teacher_retrieval(test_client, setup_database):
    # Test retrieving a teacher by ID
    response = test_client.post("/teachers", json={"name": "Alice Smith", "email": "alice.smith@example.com"})
    teacher_id = response.json()["id"]

    response = test_client.get(f"/teachers/{teacher_id}")
    assert response.status_code == 200
    assert response.json() == {"id": teacher_id, "name": "Alice Smith", "email": "alice.smith@example.com"}

def test_teacher_not_found(test_client):
    # Test retrieving a non-existent teacher
    response = test_client.get("/teachers/999")
    assert response.status_code == 404  # Not Found for non-existing teacher
```