```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.database import init_db, Student
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Setup the database for testing
Base = declarative_base()
engine = create_engine('sqlite:///test_students.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Initialize the database
@pytest.fixture(scope='module')
def test_client():
    # Create the database schema
    Base.metadata.create_all(bind=engine)
    # Create a new FastAPI test client
    with TestClient(app) as client:
        yield client
    # Cleanup: Drop the database schema after tests
    Base.metadata.drop_all(bind=engine)

def test_delete_student(test_client):
    # Create a new student to delete later
    response = test_client.post("/students", json={"name": "John Doe"})
    assert response.status_code == 201
    created_student = response.json()

    # Now delete the created student
    delete_response = test_client.delete(f"/students/{created_student['id']}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": "Student deleted successfully."}

    # Verify the student is no longer in the database
    get_response = test_client.get(f"/students/{created_student['id']}")
    assert get_response.status_code == 404  # Should return not found
    assert get_response.json() == {"error": {"code": "E404", "message": "Student not found."}}
```