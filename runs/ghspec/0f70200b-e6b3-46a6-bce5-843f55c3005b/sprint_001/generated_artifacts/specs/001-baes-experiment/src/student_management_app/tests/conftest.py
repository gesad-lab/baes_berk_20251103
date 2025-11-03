```python
import pytest
from student_management_app.models import Student
from student_management_app.database import db

@pytest.fixture
def new_student():
    """Fixture to create a new student for testing."""
    student = Student(name="Test Student")
    db.session.add(student)
    db.session.commit()
    yield student
    db.session.delete(student)
    db.session.commit()

@pytest.fixture
def sample_students():
    """Fixture to create multiple students for testing retrievals."""
    students = [
        Student(name="Student One"),
        Student(name="Student Two"),
        Student(name="Student Three"),
    ]
    db.session.add_all(students)
    db.session.commit()
    yield students
    for student in students:
        db.session.delete(student)
    db.session.commit()
    
@pytest.fixture
def student_data():
    """Fixture to provide valid student data."""
    return {"name": "Valid Student"}

@pytest.fixture
def invalid_student_data():
    """Fixture to provide invalid student data (missing name)."""
    return {}

@pytest.fixture(autouse=True)
def set_up_database():
    """Set up the database for testing."""
    db.create_all()
    yield
    db.drop_all()
```