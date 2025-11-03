import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming the FastAPI app is created in main.py

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    # You would typically set up your database here
    # This might include dropping and creating tables,
    # and inserting any initial data needed for your tests
    pass

def test_create_student_success(setup_database):
    """Test creating a student successfully"""
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == "John Doe"

def test_create_student_missing_name(setup_database):
    """Test creating a student with missing name"""
    response = client.post("/students", json={})
    assert response.status_code == 400
    assert response.json() == {"detail": "Name field is required."}

def test_get_all_students_empty(setup_database):
    """Test retrieval of students when no students are present"""
    response = client.get("/students")
    assert response.status_code == 200
    assert response.json() == []

def test_get_all_students_success(setup_database):
    """Test retrieval of students after creating one"""
    client.post("/students", json={"name": "Jane Doe"})
    response = client.get("/students")
    
    assert response.status_code == 200
    students = response.json()
    assert len(students) == 1  # We should have one student
    assert "id" in students[0]
    assert students[0]["name"] == "Jane Doe"