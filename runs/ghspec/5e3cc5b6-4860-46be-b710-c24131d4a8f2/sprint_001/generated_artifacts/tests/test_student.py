import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models.student import Student
from src.database.database import get_db, Base, engine

# Create the FastAPI test client
client = TestClient(app)

# Setup the test database
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)  # Create the database tables
    yield
    Base.metadata.drop_all(bind=engine)    # Drop the database tables after tests


@pytest.fixture()
def create_student():
    # Create a default student for testing
    student_data = {"name": "John Doe"}
    response = client.post("/students", json=student_data)
    return response.json()


def test_delete_student(create_student):
    student_id = create_student["id"]
    
    # Ensure that the student can be deleted successfully
    response = client.delete(f"/students/{student_id}")
    assert response.status_code == 204  # Check for No Content response

    # Ensure that trying to retrieve the deleted student returns a 404 status
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 404  # Check for Not Found response


def test_delete_nonexistent_student():
    # Attempt to delete a student that does not exist
    response = client.delete("/students/9999")  # Assume 9999 is an invalid student ID
    assert response.status_code == 404  # Check for Not Found response
    assert response.json() == {"detail": "Student not found"}  # Ensure the error message is correct


def test_delete_student_invalid_id_format():
    # Attempt to delete a student with an invalid ID format
    response = client.delete("/students/abc")  # Invalid ID
    assert response.status_code == 422  # Check for Unprocessable Entity response
    assert response.json()["detail"][0]["msg"] == "value is not a valid integer"  # Validate the error message