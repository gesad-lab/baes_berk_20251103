import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is defined in main.py


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


def test_create_student(client):
    """
    Test creating a new student with valid data.
    """
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201  # 201 Created
    assert response.json() == {"id": 1, "name": "John Doe"}
    

def test_create_student_missing_name(client):
    """
    Test creating a new student without a name field.
    """
    response = client.post("/students", json={})
    assert response.status_code == 422  # 422 Unprocessable Entity
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "name"],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }


def test_get_student(client):
    """
    Test retrieving an existing student by ID.
    """
    # First, create a student to retrieve
    create_response = client.post("/students", json={"name": "Jane Doe"})
    created_student_id = create_response.json()["id"]
    
    # Now retrieve the student
    response = client.get(f"/students/{created_student_id}")
    assert response.status_code == 200  # 200 OK
    assert response.json() == {"id": created_student_id, "name": "Jane Doe"}
    

def test_get_student_not_found(client):
    """
    Test retrieving a student that does not exist.
    """
    response = client.get("/students/999")  # Assuming 999 is an id that does not exist
    assert response.status_code == 404  # 404 Not Found
    assert response.json() == {"detail": "Student not found"}