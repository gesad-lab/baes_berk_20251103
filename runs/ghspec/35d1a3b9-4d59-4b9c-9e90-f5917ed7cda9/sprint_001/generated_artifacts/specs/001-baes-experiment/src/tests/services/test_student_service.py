import pytest
from fastapi.testclient import TestClient
from src.services.student_service import create_student, get_students
from src.repository import models, create_db

# Setup for tests
@pytest.fixture(scope="module")
def client():
    # Create an instance of the TestClient
    app = create_db()  # Assuming create_db initializes and sets up the FastAPI app
    yield TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    # Initialize the database schema for testing
    models.Base.metadata.create_all(bind=models.engine)
    yield
    # Drop the database schema after tests
    models.Base.metadata.drop_all(bind=models.engine)

def test_create_student(client):
    # Test creating a new student with a valid name
    response = client.post('/students/', json={"name": "John Doe"})
    
    # Assert the response status code and the response contents
    assert response.status_code == 201
    assert response.json() == {"message": "Student created successfully"}

def test_create_student_empty_name(client):
    # Test creating a student with an empty name
    response = client.post('/students/', json={"name": ""})
    
    # Assert the response status code and the response contents
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Name cannot be empty",
            "details": {}
        }
    }

def test_get_students_empty(client):
    # Test retrieving the list of students when none exist
    response = client.get('/students/')
    
    # Assert the response status code and the response contents
    assert response.status_code == 200
    assert response.json() == []

def test_get_students(client):
    # Create a student first
    client.post('/students/', json={"name": "Jane Smith"})
    
    # Test retrieving the list of students
    response = client.get('/students/')
    
    # Assert the response status code and the response contents
    assert response.status_code == 200
    assert response.json() == ["Jane Smith"]