import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_db_session(mocker):
    """
    Fixture to mock the database session for testing purposes.

    Returns:
        MagicMock: Mocked database session to simulate database interactions.
    """
    mock_session = MagicMock()
    
    # Mock methods for CRUD operations
    mock_session.add = mocker.Mock()
    mock_session.delete = mocker.Mock()
    mock_session.commit = mocker.Mock()
    mock_session.rollback = mocker.Mock()
    mock_session.query = mocker.Mock()

    # Return the mocked session
    yield mock_session

@pytest.fixture
def mock_student_model(mocker):
    """
    Fixture to mock the Student model for testing purposes.

    Returns:
        MagicMock: Mocked Student model to simulate interactions with the student database entity.
    """
    mock_student = mocker.Mock()
    
    # Mock attributes and methods of the student model
    mock_student.id = 1
    mock_student.name = "Test Student"

    return mock_student

@pytest.fixture(autouse=True)
def setup_database(mocker, mock_db_session):
    """
    Fixture to set up the database context for each test, using a mock 
    database session to ensure isolation between tests.

    This fixture also yields the mocked database session for use in tests.
    """
    # Mock the database session context manager
    mocker.patch("src.app.db.session", new=mock_db_session)

    yield mock_db_session

    # Cleanup code (if any) can go here
    mock_db_session.rollback.assert_called_once()  # Ensure rollback is called after tests
