# Implementation Plan: Create Teacher Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:  
# Implementation Plan: Add Email Field to Student Entity

---

INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:  
# Implementation Plan: Student Management Web Application

## I. Architecture Overview

The architecture will expand the existing microservice model by introducing the "Teacher" entity into the existing student management system. This will adhere to the established RESTful API approach with all data persistence tasks also handled by SQLite, ensuring a seamless integration with existing entities.

### 1.1 Module Structure

1. **API Module**: Will handle all HTTP requests for teacher management.
2. **Service Module**: Contains the business logic related to teacher operations.
3. **Data Access Layer (DAL)**: Manages database interactions related to Teacher data.
4. **Model Layer**: Defines the data model for the Teacher entity ensuring integration with the existing Student and Course models.

## II. Technology Stack

- **Backend Language**: Python 3.11+
- **Web Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing**: pytest
- **Environment Management**: pip and virtual environment

## III. Implementation Plan Breakdown

### 3.1 Module Definitions

#### API Module
- **Responsibilities**:
  - Define endpoints for creating and retrieving teachers.
  - Validate inputs for teacher creation.
  - Return structured JSON responses including success/error messages.

- **Endpoints**:
  - `POST /teachers`: Create a new teacher.
  - `GET /teachers/{id}`: Retrieve details of an existing teacher.

#### Service Module
- **Responsibilities**:
  - Implement logic for teacher creation and retrieval, including validating inputs.
  - Process and fulfill requests from the API module.

- **Key Functions**:
  - `create_teacher(name: str, email: str) -> Dict`: Handles the creation of a new teacher.
  - `get_teacher_by_id(teacher_id: int) -> Teacher`: Retrieves a specific teacher record by ID.

#### Data Access Layer (DAL)
- **Responsibilities**:
  - Execute all database operations related to the Teacher entity.
  - Ensure that existing Student and Course data remains unaffected.

- **Key Functions**:
  - `add_teacher(name: str, email: str)`: Inserts a new teacher record into the database.
  - `find_teacher_by_id(teacher_id: int)`: Fetches the teacher details given their ID.

#### Model Layer
- **Responsibilities**:
  - Define the Teacher model using SQLAlchemy ORM.

- **Model Definition**:
  ```python
  from sqlalchemy import Column, Integer, String
  from sqlalchemy.ext.declarative import declarative_base

  Base = declarative_base()

  class Teacher(Base):
      __tablename__ = 'teachers'
      
      id = Column(Integer, primary_key=True, autoincrement=True)
      name = Column(String, nullable=False)
      email = Column(String, nullable=False, unique=True)
  ```

### 3.2 Database Schema Update

- **Teachers Table**:
  - **id**: Integer (Auto-incrementing Primary Key)
  - **name**: String (Required)
  - **email**: String (Required, Unique)

### 3.3 API Contracts

1. **POST /teachers**
   - **Request**:
     - Body: `{"name": "John Doe", "email": "john.doe@example.com"}`
   - **Response**:
     - On Success: 
       ```json
       {
         "message": "Teacher created successfully."
       }
       ```
     - On Error (missing fields or duplicate email):
       - Status Code: 400
       - Body:
       ```json
       {
         "error": {"code": "E001", "message": "Name and email fields are required."}
       }
       ```

2. **GET /teachers/{id}**
   - **Request**:
     - Params: `id` (Integer)
   - **Response**:
     - On Success:
       ```json
       {
         "id": 1,
         "name": "John Doe",
         "email": "john.doe@example.com"
       }
       ```
     - On Error (teacher not found):
       - Status Code: 404
       - Body:
       ```json
       {
         "error": {"code": "E002", "message": "Teacher not found."}
       }
       ```

### 3.4 Error Handling
- Input validation for name and email should be implemented.
- Meaningful error messages must be returned according to the error type.
- Specific exceptions should be raised on failure to provide clear feedback.

## IV. Testing Strategy

### 4.1 Test Coverage
- Minimum of 70% coverage for newly implemented functionality with critical path coverage above 90%.

### 4.2 Test Types
- **Unit Tests**: For service functions managing teacher operations.
- **Integration Tests**: For the overall functionality of newly added API endpoints.

### 4.3 Test Organization
- Structure test cases mirroring the source structure:
  - `tests/api/test_teachers.py`
  - `tests/service/test_teacher_service.py`

## V. Security Considerations

- Input validation must occur at the API layer to avoid malformed data.
- Sensitive configurations should be managed using environment variables.
- Ensure that no sensitive information about teachers is logged.

## VI. Deployment Considerations

### 6.1 Production Readiness
- Ensure the system initializes and creates the new teacher table on startup without manual intervention.
- Health check endpoint to confirm operational readiness.

### 6.2 Configuration Management
- Utilize a `.env` file for deployment-specific configurations.
- Document configurations required in a `.env.example`.

### 6.3 Database Migration Strategy
- Utilize SQLAlchemy with Alembic for schema migrations.
- Create and test a migration script for setting up the `teachers` table, including unique constraints for the email field.

## VII. Documentation

- Update the `README.md` to include:
  - New API endpoints for teacher management.
  - Description of the Teacher model.
  - Examples of how to use the new endpoints.

## VIII. Modifications to Existing Files

### Modifications Needed
- **Model Layer**: Add the `Teacher` model definition.
- **Service Module**: Implement `create_teacher` and `get_teacher_by_id` functions.
- **API Module**: Create new endpoint handlers for `POST /teachers` and `GET /teachers/{id}`.
- **Tests**: Add new tests in `tests/api/test_teachers.py` and `tests/service/test_teacher_service.py`.

## IX. Conclusion

This implementation plan provides a structured approach to introducing the Teacher entity within the existing student management system. Each component has been outlined to ensure seamless integration with current modules while adhering to established coding standards and ensuring backward compatibility. Effective testing and careful management of the database schema will allow this enhancement to proceed smoothly.

Existing Code Files:
File: `tests/api/test_teachers.py`
```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is defined in main.py

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

def test_create_teacher_with_valid_data(client):
    """Test creating a teacher with valid data."""
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 200  # 200 OK
    assert response.json() == {"message": "Teacher created successfully."}

def test_create_teacher_with_duplicate_email(client):
    """Test creating a teacher with a duplicate email."""
    client.post("/teachers", json={"name": "Jane Doe", "email": "john.doe@example.com"})
    response = client.post("/teachers", json={"name": "John Smith", "email": "john.doe@example.com"})
    assert response.status_code == 400  # 400 Bad Request
    assert response.json() == {"error": {"code": "E001", "message": "Name and email fields are required."}}

def test_get_teacher(client):
    """Test getting a teacher's details."""
    # Setup by creating a teacher first
    client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    response = client.get("/teachers/1")
    assert response.status_code == 200  # 200 OK
    assert response.json()["name"] == "John Doe"
```

File: `tests/service/test_teacher_service.py`
```python
import pytest
from unittest.mock import MagicMock
from src.service.teacher_service import create_teacher, get_teacher_by_id  # Import the functions to be tested
from src.model.teacher import Teacher  # Import the Teacher model

@pytest.fixture
def mock_db_session():
    """Create a mock database session for testing."""
    session = MagicMock()
    yield session

def test_create_teacher_success(mock_db_session):
    """Test successfully creating a teacher."""
    # Mock the database session's behavior
    mock_db_session.add.side_effect = None  # Simulate successful add operation
    result = create_teacher("John Doe", "john.doe@example.com", mock_db_session)  # Adjust accordingly
    assert result is None  # Ensure no exception was raised

def test_get_teacher_by_id_success(mock_db_session):
    """Test successfully retrieving a teacher by ID."""
    teacher = Teacher(id=1, name="John Doe", email="john.doe@example.com")
    mock_db_session.query.return_value.filter.return_value.first.return_value = teacher
    result = get_teacher_by_id(1, mock_db_session)
    assert result.name == "John Doe"  # Check the retrieved name
```

The modifications ensure integration into the current system with the defined new functionality while adhering to the established standards.