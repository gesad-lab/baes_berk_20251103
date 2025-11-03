```python
import pytest
from src.database import get_db, init_db
from fastapi.testclient import TestClient
from src.main import app


@pytest.fixture(scope="module")
def test_client():
    """
    Initialize the test client for the application.
    Ensure the database is set up before tests are run.
    """
    init_db()
    client = TestClient(app)
    yield client


def test_create_student(test_client):
    """
    Test case for creating a student.
    Ensure a new student is created successfully and returns the correct response.
    """
    response = test_client.post('/students', json={"name": "John Doe"})
    assert response.status_code == 201  # Expecting 201 Created
    assert response.json() == {"id": 1, "name": "John Doe"}  # Adjust based on actual response structure


def test_list_students(test_client):
    """
    Test case for retrieving a list of students.
    Verify that the API returns a JSON array of student objects.
    """
    response = test_client.get('/students')
    assert response.status_code == 200  # Expecting 200 OK
    assert isinstance(response.json(), list)  # Check that the response is a list
    assert len(response.json()) > 0  # Check that there is at least one student


def test_update_student(test_client):
    """
    Test case for updating an existing student's name.
    Ensure the update is successful and the modified student details are returned.
    """
    response = test_client.put('/students/1', json={"name": "Jane Doe"})
    assert response.status_code == 200  # Expecting 200 OK
    assert response.json() == {"id": 1, "name": "Jane Doe"}  # Adjust based on actual response structure


def test_delete_student(test_client):
    """
    Test case for deleting a specific student.
    Ensure the student is removed from the database and confirmation is returned.
    """
    response = test_client.delete('/students/1')
    assert response.status_code == 204  # Expecting 204 No Content

    # Trying to retrieve the deleted student should result in a 404
    response = test_client.get('/students/1')
    assert response.status_code == 404  # Expecting 404 Not Found
```