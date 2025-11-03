import pytest
from fastapi.testclient import TestClient
from student_app.main import app
from student_app.models.student import Student
from student_app.db.database import get_db, engine
from sqlalchemy.orm import sessionmaker

# Test client for making requests to the FastAPI application
client = TestClient(app)

# Helper fixture to create a new database session
@pytest.fixture(scope="module")
def db_session():
    """ Fixture to create a database session for tests. """
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    yield db
    db.close()

@pytest.fixture(scope="function")
def create_student(db_session):
    """ Fixture to create a student for testing. """
    new_student = Student(name="Test Student")
    db_session.add(new_student)
    db_session.commit()
    db_session.refresh(new_student)
    return new_student

@pytest.fixture(scope="function")
def setup_database(db_session):
    """ Fixture to setup and teardown database for each test. """
    # Here you would create the database schema and seed necessary data
    db_session.commit()
    yield
    # Here you would drop the database or clean it up

def test_create_student(setup_database):
    """ Test creating a student. """
    response = client.post("/students/", json={"name": "New Student"})
    assert response.status_code == 201
    assert response.json() == {"id": response.json()["id"], "name": "New Student"}

def test_get_student(create_student):
    """ Test retrieving a student by ID. """
    response = client.get(f"/students/{create_student.id}/")
    assert response.status_code == 200
    assert response.json() == {"id": create_student.id, "name": create_student.name}

def test_update_student(create_student):
    """ Test updating a student's name. """
    response = client.put(f"/students/{create_student.id}/", json={"name": "Updated Student"})
    assert response.status_code == 200
    assert response.json() == {"id": create_student.id, "name": "Updated Student"}

def test_delete_student(create_student):
    """ Test deleting a student by ID. """
    response = client.delete(f"/students/{create_student.id}/")
    assert response.status_code == 200
    assert response.json() == {"message": "Student deleted successfully"}
    # Verify that the student is no longer retrievable
    response = client.get(f"/students/{create_student.id}/")
    assert response.status_code == 404

def test_get_nonexistent_student():
    """ Test retrieval of a nonexistent student. """
    response = client.get("/students/9999/")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Student not found", "details": {}}}

def test_update_nonexistent_student():
    """ Test updating a nonexistent student. """
    response = client.put("/students/9999/", json={"name": "Updated Name"})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Student not found", "details": {}}}

def test_delete_nonexistent_student():
    """ Test deleting a nonexistent student. """
    response = client.delete("/students/9999/")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Student not found", "details": {}}}