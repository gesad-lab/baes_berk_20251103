```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Adjust based on your project structure
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db_setup import Base

# Setup the database for testing
@pytest.fixture(scope="module")
def test_client():
    engine = create_engine("sqlite:///test.db")  # Use a test database
    Base.metadata.create_all(bind=engine)  # Create the schema for testing
    connection = engine.connect()
    transaction = connection.begin()
    
    # Use context manager to provide a session to the tests
    with sessionmaker(bind=engine)() as session:
        yield TestClient(app)
    
    transaction.rollback()  # Roll back the transaction after tests are done
    connection.close()

# Integration test for assigning a teacher to a course
def test_assign_teacher_integration(test_client):
    response = test_client.post("/courses/1/assign-teacher", json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json()["message"] == "Teacher assigned successfully to course."

# Integration test for removing a teacher from a course
def test_remove_teacher_integration(test_client):
    response = test_client.delete("/courses/1/remove-teacher")
    assert response.status_code == 200
    assert response.json()["message"] == "Teacher removed successfully from the course."

# Integration test for viewing a course with teacher information
def test_view_course_with_teacher_integration(test_client):
    response = test_client.get("/courses/1")  # Adjust ID as necessary
    assert response.status_code == 200
    # Additional assertions can be added to check teacher_id in response
    assert "teacher_id" in response.json()  # Assuming the response contains teacher_id
```