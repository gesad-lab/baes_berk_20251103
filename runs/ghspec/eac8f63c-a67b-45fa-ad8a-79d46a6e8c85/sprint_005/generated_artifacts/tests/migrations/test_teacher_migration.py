# tests/migrations/test_teacher_migration.py

import logging
import pytest
from unittest.mock import MagicMock
from src.repositories.teacher_repository import TeacherRepository
from src.services.teacher_service import TeacherService

# Configure structured logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')


@pytest.fixture
def setup_teacher_data():
    # Setup code to create initial teacher data for testing
    pass


def log_response(action: str, response: dict):
    """Log the API response in a structured manner."""
    logging.info({
        'action': action,
        'status': response.get('status', 'Unknown'),
        'message': response.get('message', 'No message provided'),
        'data': response.get('data', None)
    })


@pytest.fixture
def mock_teacher_repository():
    """Mock the TeacherRepository for testing purposes."""
    repository = MagicMock(spec=TeacherRepository)
    return repository


@pytest.fixture
def teacher_service(mock_teacher_repository):
    """Fixture that creates an instance of TeacherService with a mocked repository."""
    return TeacherService(mock_teacher_repository)


def test_create_teacher_success(teacher_service):
    """Test: Creating a teacher with valid data should succeed."""
    teacher_data = {
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }
    teacher_service.repository.create_teacher.return_value = teacher_data

    response = teacher_service.create_teacher(teacher_data)
    
    log_response("Create Teacher", response)
    assert response == teacher_data
    teacher_service.repository.create_teacher.assert_called_once_with(teacher_data)


def test_create_teacher_missing_name(teacher_service):
    """Test: Attempting to create a teacher without a name should return an error."""
    teacher_data = {
        'email': 'john.doe@example.com'
    }
    teacher_service.repository.create_teacher.side_effect = ValueError("Missing required field: name")

    with pytest.raises(ValueError) as exc_info:
        teacher_service.create_teacher(teacher_data)

    assert str(exc_info.value) == "Missing required field: name"
    teacher_service.repository.create_teacher.assert_not_called()


def test_get_teacher_success(teacher_service):
    """Test: Retrieving a teacher's information should return correct details."""
    teacher_id = 1
    teacher_data = {
        'id': teacher_id,
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }
    teacher_service.repository.get_teacher.return_value = teacher_data

    response = teacher_service.get_teacher(teacher_id)

    log_response("Get Teacher", response)
    assert response['name'] == 'John Doe'
    teacher_service.repository.get_teacher.assert_called_once_with(teacher_id)