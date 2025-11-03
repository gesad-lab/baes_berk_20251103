import pytest
from fastapi.testclient import TestClient
from main import app
from models import Student
from sqlalchemy.orm import Session
from database import get_db, Base, engine

# Create the test client used for sending requests to the application
client = TestClient(app)

# Dependency override for the database session
def override_get_db():
    db = Session(bind=engine)
    yield db
    db.close()

# Setup the test database and create the necessary tables
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

# Use the fixture to override the database dependency
app.dependency_overrides[get_db] = override_get_db

def test_create_student():
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"

def test_retrieve_student():
    response = client.post("/students", json={"name": "Jane Doe"})
    student_id = response.json()["id"]

    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Jane Doe"

def test_update_student():
    response = client.post("/students", json={"name": "Mark Smith"})
    student_id = response.json()["id"]

    response = client.put(f"/students/{student_id}", json={"name": "Mark Twain"})
    assert response.status_code == 200

    response = client.get(f"/students/{student_id}")
    assert response.json()["name"] == "Mark Twain"

def test_delete_student():
    response = client.post("/students", json={"name": "Lucy Brown"})
    student_id = response.json()["id"]

    response = client.delete(f"/students/{student_id}")
    assert response.status_code == 204

    response = client.get(f"/students/{student_id}")
    assert response.status_code == 404  # Student should not be found