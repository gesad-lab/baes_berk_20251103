```python
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import Base
from app.database import engine

# Create a test client
client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    # Create the database and the tables for testing
    Base.metadata.create_all(bind=engine)
    
    # Optional: Add some test data if needed
    
    yield  # This is where the testing happens

    # Drop the database tables after tests (cleanup)
    Base.metadata.drop_all(bind=engine)

def test_retrieve_all_students(setup_database):
    # Arrange: Optionally add a student record to the database
    response = client.post("/students", json={"name": "Alice"})
    assert response.status_code == 200

    # Act: Retrieve all students
    response = client.get("/students")
    
    # Assert: Check the response structure
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Should be a list
    assert len(response.json()) > 0  # Should return at least one student
    for student in response.json():
        assert "id" in student  # Check id field exists
        assert "name" in student  # Check name field exists
        assert isinstance(student["name"], str)  # name should be a string
```
