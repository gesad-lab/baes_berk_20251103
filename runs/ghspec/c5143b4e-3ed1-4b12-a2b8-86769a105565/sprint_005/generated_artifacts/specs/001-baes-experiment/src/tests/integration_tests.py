```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.database import get_db
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.models import Base, Teacher

# Set up test database
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"  # Using in-memory SQLite for tests
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables
Base.metadata.create_all(bind=engine)

@pytest.fixture(scope="module")
def client():
    # Override the dependency to use the test database
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c

def test_create_teacher(client):
    # Test creating a teacher with valid data
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["name"] == "John Doe"
    assert data["email"] == "john.doe@example.com"

def test_create_teacher_missing_fields(client):
    # Test creating a teacher without a name
    response = client.post("/teachers", json={"email": "john.doe@example.com"})
    
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json()["detail"][0]["msg"] == "field required"  # Check error message for name

    # Test creating a teacher without an email
    response = client.post("/teachers", json={"name": "John Doe"})
    
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json()["detail"][0]["msg"] == "field required"  # Check error message for email

def test_create_teacher_invalid_email(client):
    # Test creating a teacher with an invalid email format
    response = client.post("/teachers", json={"name": "John Doe", "email": "invalid-email-format"})
    
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json()["detail"][0]["msg"] == "value is not a valid email address"  # Check error message for email

def test_create_teacher_duplicate_email(client):
    # Create a teacher with a unique email
    client.post("/teachers", json={"name": "Jane Smith", "email": "jane.smith@example.com"})
    
    # Test creating another teacher with the same email
    response = client.post("/teachers", json={"name": "Duplicate User", "email": "jane.smith@example.com"})
    
    assert response.status_code == 400  # Bad Request for duplicate email
    assert response.json()["detail"] == "Email already exists"  # Check error message for duplicate
```