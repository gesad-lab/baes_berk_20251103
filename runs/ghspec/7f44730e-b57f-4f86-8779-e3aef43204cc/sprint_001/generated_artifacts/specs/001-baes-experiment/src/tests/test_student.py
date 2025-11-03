from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_student_valid():
    """Test creating a student with a valid name."""
    response = client.post("/students", json={"name": "John Doe"})
    # Assert that the creation was successful and response format is as expected
    assert response.status_code == 200
    assert response.json() == {"message": "Student created successfully", "student": {"name": "John Doe"}}

def test_create_student_empty_name():
    """Test that creating a student without a name returns an error."""
    response = client.post("/students", json={"name": ""})
    # Assert that the response indicates a bad request with the appropriate error message
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name is required"}}

def test_get_students():
    """Test retrieving all student records."""
    # First, create a student to test the retrieval
    client.post("/students", json={"name": "Jane Doe"})
    
    # Now, retrieve the list of students
    response = client.get("/students")
    # Assert that the retrieval was successful and check response structure
    assert response.status_code == 200
    json_response = response.json()
    assert "students" in json_response
    assert len(json_response["students"]) > 0  # Ensure that there is at least one student
    assert any(student["name"] == "Jane Doe" for student in json_response["students"])  # Ensure the created student is in the list