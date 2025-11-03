import pytest
from fastapi.testclient import TestClient
from src.app import app
from src.db import get_db
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.models import Base, Student


# Setting up the test database in memory
@pytest.fixture(scope="module")
def test_db():
    # Create a new SQLite database in memory
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)

    # Create a new session for testing
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    yield db  # This will be available in tests

    # Cleanup after tests
    db.close()

# Dependency override
def override_get_db():
    db = next(test_db())
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="module")
def client():
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c


def test_create_student(client):
    # Test creating a new student
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == "John Doe"


def test_get_student(client):
    # Test retrieving an existing student
    response = client.post("/students", json={"name": "Jane Doe"})
    student_id = response.json()["id"]

    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json()["id"] == student_id
    assert response.json()["name"] == "Jane Doe"


def test_get_student_not_found(client):
    # Test retrieving a student that does not exist
    response = client.get("/students/999")  # Assuming 999 doesn't exist
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Student not found"}}