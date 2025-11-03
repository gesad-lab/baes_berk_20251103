from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, get_db
from models.student import Student

app = FastAPI()

# Dependency to get the database session
def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Override the dependency in the FastAPI app
app.dependency_overrides[get_db] = override_get_db

# Initialize the SQLite database for testing
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

# Create a TestClient instance for the tests
client = TestClient(app)

def test_create_student():
    """Test creating a new student."""
    response = client.post("/students/", json={"name": "John Doe"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "John Doe"}

def test_get_student():
    """Test retrieving an existing student."""
    response = client.get("/students/1/")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Doe"}

def test_update_student():
    """Test updating an existing student's name."""
    response = client.put("/students/1/", json={"name": "Jane Doe"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Jane Doe"}

def test_delete_student():
    """Test deleting an existing student."""
    response = client.delete("/students/1/")
    assert response.status_code == 204

def test_get_nonexistent_student():
    """Test retrieving a nonexistent student."""
    response = client.get("/students/999/")
    assert response.status_code == 404

def test_create_student_invalid_name():
    """Test creating a student without a name."""
    response = client.post("/students/", json={"name": ""})
    assert response.status_code == 400
    assert "error" in response.json()  # Ensure error message is returned