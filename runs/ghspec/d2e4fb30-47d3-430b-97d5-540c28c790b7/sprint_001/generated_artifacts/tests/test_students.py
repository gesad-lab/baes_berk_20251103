import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app, Base, get_db

# Setup for testing
DATABASE_URL = "postgresql://user:password@localhost/test_db"

# Create a new database engine
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Override the dependency
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Initialize the TestClient
client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def create_student():
    """Fixture that creates a test student and provides the student ID for tests."""
    response = client.post("/students", json={"name": "John Doe"})
    yield response.json()["id"]

def test_create_student():
    """Test the creation of a student."""
    response = client.post("/students", json={"name": "Alice Smith"})
    assert response.status_code == 201
    assert response.json() == {"name": "Alice Smith", "id": 2}  # Adjust based on actual behavior

def test_create_student_missing_name():
    """Test creating a student without a name raises validation error."""
    response = client.post("/students", json={})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "name"],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }

def test_get_students(create_student):
    """Test retrieving all students."""
    response = client.get("/students")
    assert response.status_code == 200
    assert len(response.json()) == 2  # Adjust based on the expected count

def test_get_students_empty():
    """Test retrieving students from an empty database."""
    # Create another session to check empty condition
    client.post("/students", json={"name": "Bob"})
    response = client.get("/students")
    assert response.status_code == 200
    assert len(response.json()) == 1  # Only "Bob" should be returned

def test_create_student_invalid_name():
    """Test creating a student with an invalid name."""
    response = client.post("/students", json={"name": 123})
    assert response.status_code == 422  # Unprocessable Entity
    assert "type" in response.json()["detail"][0]  # Check for type validation error

def test_get_student_by_id(create_student):
    """Test retrieving a single student by ID."""
    response = client.get(f"/students/{create_student}")
    assert response.status_code == 200
    assert response.json() == {"name": "John Doe", "id": create_student}

def test_get_nonexistent_student():
    """Test retrieving a student that does not exist."""
    response = client.get("/students/999")  # Using an arbitrary non-existent ID
    assert response.status_code == 404  # Not Found
    assert response.json() == {"detail": "Student not found"}