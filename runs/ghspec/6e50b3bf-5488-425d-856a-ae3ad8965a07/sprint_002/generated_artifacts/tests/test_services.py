```python
import pytest
from src.services import create_student, get_student_by_id
from src.models import Student
from src.database import get_db_session


@pytest.fixture
def db_session():
    """Provides a transactional scope around a test, rolling back at the end."""
    session = get_db_session()
    yield session
    session.rollback()


def test_create_student_success(db_session):
    """Test successful creation of a student with a valid email."""
    email = "test@student.com"
    student = create_student(name="John Doe", email=email, session=db_session)

    assert student.id is not None
    assert student.name == "John Doe"
    assert student.email == email


def test_create_student_missing_email(db_session):
    """Test that trying to create a student without an email raises an error."""
    with pytest.raises(ValueError) as excinfo:
        create_student(name="Jane Doe", email=None, session=db_session)
    assert "Email is required" in str(excinfo.value)


def test_create_student_invalid_email(db_session):
    """Test that trying to create a student with an invalid email raises an error."""
    with pytest.raises(ValueError) as excinfo:
        create_student(name="Jane Doe", email="invalid-email", session=db_session)
    assert "Email format is invalid" in str(excinfo.value)


def test_get_student_by_id_success(db_session):
    """Test retrieving a student by ID."""
    email = "test1@student.com"
    student_created = create_student(name="Alice Smith", email=email, session=db_session)
    student_retrieved = get_student_by_id(student_created.id, session=db_session)

    assert student_retrieved.id == student_created.id
    assert student_retrieved.name == "Alice Smith"
    assert student_retrieved.email == email


def test_get_student_by_id_not_found(db_session):
    """Test retrieving a student by an invalid ID returns None."""
    student_retrieved = get_student_by_id(999999, session=db_session)  # Invalid ID
    assert student_retrieved is None
```