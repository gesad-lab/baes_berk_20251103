```python
import pytest
from unittest.mock import MagicMock, patch
from fastapi import HTTPException
from src.service.teacher_service import create_teacher, get_teacher_by_id
from src.model.teacher import Teacher  # Import the Teacher model

@pytest.fixture
def mock_db_session():
    """Create a mock database session for testing."""
    session = MagicMock()
    yield session

def test_create_teacher_with_valid_data(mock_db_session):
    """Test creating a teacher with valid data."""
    teacher_data = {"name": "John Doe", "email": "john.doe@example.com"}
    
    with patch('src.service.teacher_service.Session') as MockSession:
        mock_session_instance = MockSession.return_value
        mock_session_instance.add.return_value = None

        response = create_teacher(mock_db_session, teacher_data)
        
        # Verify the teacher was added to the session
        mock_session_instance.add.assert_called_once()
        assert response == {"message": "Teacher created successfully."}

def test_create_teacher_with_missing_fields(mock_db_session):
    """Test creating a teacher with missing fields."""
    teacher_data = {"name": "", "email": ""}

    with pytest.raises(HTTPException) as excinfo:
        create_teacher(mock_db_session, teacher_data)
    
    assert excinfo.value.status_code == 400
    assert excinfo.value.detail == {"error": {"code": "E001", "message": "Name and email fields are required."}}

def test_get_teacher_information(mock_db_session):
    """Test getting a teacher's information."""
    teacher = Teacher(id=1, name="John Doe", email="john.doe@example.com")
    
    # Mock the `get` method to return a teacher instance
    with patch('src.service.teacher_service.Session') as MockSession:
        mock_session_instance = MockSession.return_value
        mock_session_instance.query.return_value.filter_by.return_value.first.return_value = teacher
        
        response = get_teacher_by_id(mock_db_session, 1)
        
        assert response == {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}

def test_create_teacher_with_duplicate_email(mock_db_session):
    """Test creating a teacher with a duplicate email."""
    teacher_data = {"name": "Jane Doe", "email": "duplicate@example.com"}
    
    # Simulate that the email already exists in the database
    with patch('src.service.teacher_service.Session') as MockSession:
        mock_session_instance = MockSession.return_value
        mock_session_instance.query.return_value.filter_by.return_value.first.return_value = Teacher(name="Existing", email="duplicate@example.com")

        with pytest.raises(HTTPException) as excinfo:
            create_teacher(mock_db_session, teacher_data)

        assert excinfo.value.status_code == 400
        assert excinfo.value.detail == {"error": {"code": "E002", "message": "Email address already associated with another teacher."}}
```