```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Adjust based on your project structure
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db_setup import Base
from src.models import Course, Teacher  # Import the necessary models

# Setup the database for testing
@pytest.fixture(scope='module')
def test_client():
    engine = create_engine("sqlite:///test.db")  # Use a test database
    Base.metadata.create_all(engine)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Dependency override for testing
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    yield TestClient(app)

    Base.metadata.drop_all(engine)  # Clean up the database after tests

# Test assigning a teacher to a course
def test_assign_teacher(test_client):
    # Setup course and teacher for the test
    test_client.post("/courses/", json={"name": "Test Course"})
    test_client.post("/teachers/", json={"name": "Test Teacher"})
    
    response = test_client.post("/courses/1/assign-teacher", json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json()["message"] == "Teacher assigned successfully to course."

# Test removing a teacher from a course
def test_remove_teacher(test_client):
    response = test_client.delete("/courses/1/remove-teacher")
    assert response.status_code == 200
    assert response.json()["message"] == "Teacher removed successfully from the course."

# Test viewing course with teacher information
def test_view_course_with_teacher(test_client):
    response = test_client.get("/courses/1")  # Adjust ID as necessary
    assert response.status_code == 200
    response_data = response.json()
    assert "teacher_id" in response_data
    # Further assertions can be made based on how the teacher_id is expected to appear
    assert response_data["teacher_id"] == 1  # Assuming a teacher has been assigned
```