```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Adjust the import based on your actual project structure
from src.models import Teacher  # Import the Teacher model
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db_setup import Base

# Setup the database for testing
@pytest.fixture(scope='module')
def test_client():
    engine = create_engine("sqlite:///test.db")  # Use a test database
    Base.metadata.create_all(engine)  # Create all tables including Teacher

    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    with TestingSessionLocal() as session:
        yield TestClient(app)

    Base.metadata.drop_all(engine)  # Drop all tables after tests are done

# Test to create a teacher
def test_create_teacher(test_client):
    response = test_client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["name"] == "John Doe"
    assert data["email"] == "john.doe@example.com"

# Test to view a teacher
def test_view_teacher(test_client):
    # First, create a teacher to ensure there is a record to retrieve
    create_response = test_client.post("/teachers", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    teacher_id = create_response.json()["id"]
    
    # Now, retrieve the teacher information
    response = test_client.get(f"/teachers/{teacher_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == teacher_id
    assert data["name"] == "Jane Doe"
    assert data["email"] == "jane.doe@example.com"

# Test to update a teacher's information
def test_update_teacher(test_client):
    # Create a teacher to be updated
    create_response = test_client.post("/teachers", json={"name": "Alice Smith", "email": "alice.smith@example.com"})
    teacher_id = create_response.json()["id"]
    
    # Update the teacher's information
    update_response = test_client.put(f"/teachers/{teacher_id}", json={"name": "Alice Johnson"})
    assert update_response.status_code == 200
    updated_data = update_response.json()
    assert updated_data["id"] == teacher_id
    assert updated_data["name"] == "Alice Johnson"  # Check the updated name
    assert updated_data["email"] == "alice.smith@example.com"  # Email should stay the same
```