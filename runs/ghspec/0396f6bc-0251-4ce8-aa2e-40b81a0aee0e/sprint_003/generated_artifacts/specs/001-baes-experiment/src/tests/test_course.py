```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Course  # Adjusted to include Course model
from your_app import create_course  # Adjust the import based on your application structure
from fastapi.testclient import TestClient

# Setup for SQLite in-memory database for testing
@pytest.fixture(scope='module')
def test_database():
    # Create a new SQLite database (in-memory)
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)  # Create all tables
    connection = engine.connect()
    transaction = connection.begin()

    yield connection  # This will be passed to the tests

    transaction.rollback()
    connection.close()

@pytest.fixture(scope='function')
def client(test_database):
    # Create a TestClient for the FastAPI application
    from your_app import app  # Adjust the import based on your application structure
    return TestClient(app)

def test_create_course_without_name(client):
    response = client.post("/courses", json={"level": "Beginner"})
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E400",
            "message": "Field 'name' is required."
        }
    }

def test_create_course_without_level(client):
    response = client.post("/courses", json={"name": "Mathematics"})
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E400",
            "message": "Field 'level' is required."
        }
    }

def test_create_course_with_both_fields(client):
    response = client.post("/courses", json={"name": "Mathematics", "level": "Beginner"})
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["name"] == "Mathematics"
    assert data["level"] == "Beginner"

def test_create_course_without_fields(client):
    response = client.post("/courses", json={})
    assert response.status_code == 400
    assert response.json() == {
        "error": {
            "code": "E400",
            "message": "Fields 'name' and 'level' are required."
        }
    }
```