```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app  # Assuming the FastAPI app is defined in main.py
from models import Base, Course, Teacher  # Importing the Course and Teacher models

client = TestClient(app)

# Database setup for testing
DATABASE_URL = "sqlite:///./test.db"  # Use a separate test database for isolated tests
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create migration and test database
@pytest.fixture(scope="module")
def test_db():
    # Create the database tables
    Base.metadata.create_all(bind=engine)
    yield
    # Drop the database tables after tests
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function", autouse=True)
def override_get_db(test_db):
    # Session management for each test
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_assign_teacher_success(override_get_db):
    # Arrange
    # Create a test teacher and course
    with SessionLocal() as db:
        teacher = Teacher(name="John Doe")
        db.add(teacher)
        db.commit()
        db.refresh(teacher)
        
        course = Course(title="Math 101")
        db.add(course)
        db.commit()
        db.refresh(course)

    # Act
    response = client.patch(f"/courses/{course.id}", json={"teacher_id": teacher.id})

    # Assert
    assert response.status_code == 200
    assert response.json()["teacher_id"] == teacher.id
    assert response.json()["id"] == course.id  # Confirming we get the right course back

def test_assign_teacher_invalid_course(override_get_db):
    # Act
    response = client.patch("/courses/999", json={"teacher_id": 1})  # Assuming 999 does not exist

    # Assert
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Course not found", "details": {}}}

def test_assign_teacher_invalid_teacher(override_get_db):
    # Arrange
    with SessionLocal() as db:
        course = Course(title="Biology 101")
        db.add(course)
        db.commit()
        db.refresh(course)

    # Act
    response = client.patch(f"/courses/{course.id}", json={"teacher_id": 999})  # Assuming 999 does not exist

    # Assert
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E404", "message": "Teacher not found", "details": {}}}
```