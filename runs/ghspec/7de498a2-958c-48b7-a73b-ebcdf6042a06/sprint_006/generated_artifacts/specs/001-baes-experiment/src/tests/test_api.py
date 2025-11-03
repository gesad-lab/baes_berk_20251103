```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from pydantic import BaseModel

client = TestClient(app)

# Pydantic models for input validation
class AssignTeacher(BaseModel):
    teacher_id: int

class RemoveTeacher(BaseModel):
    pass

@pytest.fixture(scope="module")
def setup_database():
    # Set up any necessary database state before tests
    yield
    # Clean up database state after tests

def test_assign_teacher_success(setup_database):
    """Test assigning a teacher to a course successfully."""
    response = client.put("/courses/1/assign_teacher", json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json()["teacher_id"] == 1

def test_remove_teacher_success(setup_database):
    """Test removing a teacher from a course successfully."""
    response = client.put("/courses/1/remove_teacher")
    assert response.status_code == 200
    assert response.json()["teacher_id"] is None
```