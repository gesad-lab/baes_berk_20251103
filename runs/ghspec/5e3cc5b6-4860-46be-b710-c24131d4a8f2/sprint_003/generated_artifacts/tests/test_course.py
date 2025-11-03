```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models.student import Student
from src.models.course import Course  # New import for the Course model
from src.database.database import get_db, Base, engine

# Create the FastAPI test client
client = TestClient(app)

# Setup the test database
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)  # Create the database tables
    yield
    Base.metadata.drop_all(bind=engine)    # Drop the database tables after tests

# Test cases for Course entity
def test_create_course():
    response = client.post("/courses", json={"name": "Math 101", "level": "Beginner"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "Math 101", "level": "Beginner"}

def test_get_course():
    response = client.get("/courses/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Math 101", "level": "Beginner"}

def test_update_course():
    response = client.put("/courses/1", json={"name": "Math 101", "level": "Advanced"})
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Math 101", "level": "Advanced"}

def test_get_non_existing_course():
    response = client.get("/courses/999")
    assert response.status_code == 404
```
