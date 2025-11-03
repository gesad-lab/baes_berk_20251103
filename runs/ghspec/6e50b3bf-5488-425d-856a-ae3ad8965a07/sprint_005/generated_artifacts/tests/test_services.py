```python
import pytest
from src.services import create_teacher, get_teacher
from src.models import Teacher
from src.database import get_db_session

@pytest.fixture
def db_session():
    """Provides a transactional scope around a test, rolling back at the end."""
    session = get_db_session()
    yield session
    session.rollback()

@pytest.fixture
def sample_teacher_data():
    """Create sample teacher data for testing."""
    return {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }

def test_create_teacher(db_session, sample_teacher_data):
    """Test creating a teacher successfully."""
    teacher = create_teacher(sample_teacher_data['name'], sample_teacher_data['email'])

    assert teacher.id is not None
    assert teacher.name == sample_teacher_data['name']
    assert teacher.email == sample_teacher_data['email']

def test_retrieve_teacher(db_session, sample_teacher_data):
    """Test retrieving a teacher by ID."""
    teacher = create_teacher(sample_teacher_data['name'], sample_teacher_data['email'])
    retrieved_teacher = get_teacher(teacher.id)

    assert retrieved_teacher is not None
    assert retrieved_teacher.name == sample_teacher_data['name']
    assert retrieved_teacher.email == sample_teacher_data['email']

def test_create_teacher_with_missing_fields(db_session):
    """Test creating a teacher with missing name or email throws an error."""
    with pytest.raises(ValueError) as excinfo:
        create_teacher(None, "missingname@example.com")
    assert "Name is required" in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        create_teacher("Missing Email", None)
    assert "Email is required" in str(excinfo.value)
```