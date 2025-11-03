import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from models.teacher import Teacher
from database import get_db, init_db

# Initialize the FastAPI app and the test client
app = FastAPI()

# Dependency override for testing
@app.on_event("startup")
def startup():
    init_db()

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    # Assuming we have a function to set up the database for tests
    init_db()


def test_create_teacher(client):
    """Test the creation of a new teacher."""
    response = client.post(
        "/teachers/",
        json={"name": "John Doe", "email": "john.doe@example.com"}
    )
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}


def test_retrieve_teacher(client):
    """Test retrieving a teacher by ID."""
    response = client.get("/teachers/1/")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}


def test_create_teacher_missing_name(client):
    """Test error handling for missing name while creating a teacher."""
    response = client.post("/teachers/", json={"email": "john.doe@example.com"})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {
        "detail": [{"loc": ["body", "name"],
                    "msg": "field required",
                    "type": "value_error.missing"}]
    }


def test_create_teacher_missing_email(client):
    """Test error handling for missing email while creating a teacher."""
    response = client.post("/teachers/", json={"name": "John Doe"})
    assert response.status_code == 422  # Unprocessable Entity
    assert response.json() == {
        "detail": [{"loc": ["body", "email"],
                    "msg": "field required",
                    "type": "value_error.missing"}]
    }


def test_update_teacher(client):
    """Test updating a teacher's information."""
    response = client.put(
        "/teachers/1/",
        json={"name": "John Doe Updated", "email": "john.doe.updated@example.com"}
    )
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Doe Updated", "email": "john.doe.updated@example.com"}

    # Verify the update
    response = client.get("/teachers/1/")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "John Doe Updated", "email": "john.doe.updated@example.com"}