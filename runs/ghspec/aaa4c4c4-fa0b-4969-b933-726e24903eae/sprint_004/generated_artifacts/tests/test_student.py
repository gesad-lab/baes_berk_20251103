import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is instantiated in main.py

# Initialize the test client
client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    """Fixture to set up the database state before tests and clean up afterwards."""
    # Assume setup logic is handled here, e.g., creating tables and seeding data
    pass

@pytest.fixture(scope="module")
def create_student(setup_database):
    """Fixture to create a student for testing purposes."""
    response = client.post("/students", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    return response.json()  # Return the created student data

@pytest.fixture(scope="module")
def create_course(setup_database):
    """Fixture to create a course for testing purposes."""
    response = client.post("/courses", json={"name": "Mathematics", "level": "Beginner"})
    assert response.status_code == 201
    return response.json()  # Return the created course data

def test_enroll_student_in_course(create_student, create_course):
    """Test enrolling a student in a course successfully."""
    enrollment_response = client.post("/enrollments", json={
        "student_id": create_student["id"],
        "course_id": create_course["id"]
    })
    assert enrollment_response.status_code == 201
    assert enrollment_response.json() == {"message": "Enrollment successful"}

def test_retrieve_student_with_courses(create_student, create_course):
    """Test retrieving student data including enrolled courses."""
    client.post("/enrollments", json={
        "student_id": create_student["id"],
        "course_id": create_course["id"]
    })  # Enroll the student for retrieval test
    
    student_response = client.get(f"/students/{create_student['id']}")
    
    assert student_response.status_code == 200
    student_data = student_response.json()
    
    # Check that the response includes the correct student information
    assert student_data["name"] == create_student["name"]
    assert student_data["email"] == create_student["email"]
    assert len(student_data["courses"]) == 1  # Expecting one course
    assert student_data["courses"][0]["name"] == create_course["name"]

def test_enrollment_not_found(create_student):
    """Test handling of enrollment for a nonexistent course."""
    enrollment_response = client.post("/enrollments", json={
        "student_id": create_student["id"],
        "course_id": 99999  # Nonexistent course ID
    })
    assert enrollment_response.status_code == 404
    assert enrollment_response.json() == {"error": {"code": "E404", "message": "Course not found", "details": {}}}