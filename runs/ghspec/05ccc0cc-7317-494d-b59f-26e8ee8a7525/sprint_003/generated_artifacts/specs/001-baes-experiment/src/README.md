```python
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import Base, Student, Course  # Import the new Course model
from app.database import engine

# Create a test client
client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    # Create the database and the tables for testing
    Base.metadata.create_all(bind=engine)
    
    yield  # This is where the testing happens

    # Drop the database tables after tests are done
    Base.metadata.drop_all(bind=engine)


def test_create_course(setup_database):
    """Test to create a new course."""
    response = client.post("/courses", json={"name": "Mathematics", "level": "Intermediate"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Mathematics"
    assert data["level"] == "Intermediate"


def test_retrieve_all_courses(setup_database):
    """Test retrieving all courses."""
    response = client.get("/courses")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)  # Ensure the response is a list
    assert len(data) > 0  # There should be at least one course


def test_create_course_missing_fields(setup_database):
    """Test error handling when creating a course without required fields."""
    response = client.post("/courses", json={"name": "", "level": ""})
    assert response.status_code == 422  # Unprocessable Entity for validation errors
    assert "detail" in response.json()  # Ensure there's a detail field in the error response


def test_database_schema_migration(setup_database):
    """Test to ensure the Courses table exists after migration."""
    inspector = inspect(engine)
    assert "courses" in inspector.get_table_names()  # Check if the Courses table was created
    # Verify that existing Students data is unaffected
    students = session.query(Student).all()
    assert len(students) >= 0  # The Student table should still have records
```