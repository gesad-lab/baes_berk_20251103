import pytest
from fastapi.testclient import TestClient
from main import app
from models import Student
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Set up the database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Create a new test client
client = TestClient(app)

@pytest.fixture(scope="module")
def setUp():
    # Initialize the database
    Base.metadata.create_all(bind=engine)
    yield
    # Drop the database at the end of tests
    Base.metadata.drop_all(bind=engine)

def test_create_student_with_email(setUp):
    response = client.post("/students/", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["email"] == "john@example.com"

def test_create_student_without_email(setUp):
    response = client.post("/students/", json={"name": "Jane Doe"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Email field is required."}

def test_retrieve_students(setUp):
    # Creating a student for retrieval
    client.post("/students/", json={"name": "John Doe", "email": "john@example.com"})
    response = client.get("/students/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == "John Doe"
    assert data[0]["email"] == "john@example.com"