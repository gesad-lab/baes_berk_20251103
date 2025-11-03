```python
import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_students():
    # Create a few students for testing
    response = client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201
    student_id_1 = response.json().get("id")

    response = client.post("/students", json={"name": "Jane Smith"})
    assert response.status_code == 201
    student_id_2 = response.json().get("id")

    yield {
        "student_id_1": student_id_1,
        "student_id_2": student_id_2
    }

def test_retrieve_all_students(setup_students):
    """Test that all students can be retrieved successfully."""
    response = client.get("/students")
    assert response.status_code == 200
    
    students = response.json()
    # Verify that we have at least as many entries as created
    assert len(students) >= 2
    
    # Optionally check that the students returned are the ones created
    student_ids = {student['id'] for student in students}
    assert setup_students["student_id_1"] in student_ids
    assert setup_students["student_id_2"] in student_ids
```