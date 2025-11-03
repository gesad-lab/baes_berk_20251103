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

The architecture will expand the existing microservice model by introducing a many-to-many relationship between the Student and Course entities using a junction table. The application will maintain its RESTful API approach with all data persistence tasks handled by SQLite.

### 1.1 Module Structure

1. **API Module**: Will handle all HTTP requests for student-course associations.
2. **Service Module**: Contains the business logic related to student-course relationships.
3. **Data Access Layer (DAL)**: Manages database interactions, including the new Student-Course junction table operations.
4. **Model Layer**: Defines the data model for the new StudentCourse association and ensures it interacts well with both Student and Course models.

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
  - Define endpoints for associating courses with students.
  - Validate inputs on course associations.
  - Return structured JSON responses including success/error messages.

- **Endpoints**:
  - `POST /students/{id}/courses`: Associate given courses with a student.
  - `GET /students/{id}/courses`: Retrieve courses associated with a student.

#### Service Module
- **Responsibilities**:
  - Implement logic to associate courses with students and validate inputs for course IDs.
  - Process and fulfill requests from the API module regarding student-course relationships.

- **Key Functions**:
  - `associate_courses(student_id: int, course_ids: List[int]) -> Dict`: Associates one or more courses with a student.
  - `get_student_courses(student_id: int) -> List[Course]`: Retrieves a list of courses associated with a student.

#### Data Access Layer (DAL)
- **Responsibilities**:
  - Execute all database operations related to the student-course junction table.
  - DB operations must maintain existing student and course data while adding new relationships.

- **Key Functions**:
  - `add_student_courses(student_id: int, course_ids: List[int])`: Inserts entries into the StudentCourse junction table.
  - `get_courses_for_student(student_id: int)`: Fetches courses linked to a specific student.

#### Model Layer
- **Responsibilities**:
  - Define the StudentCourse association model using SQLAlchemy ORM.

- **Model Definition**:
  ```python
  from sqlalchemy import Column, Integer, ForeignKey
  from sqlalchemy.ext.declarative import declarative_base

  Base = declarative_base()

  class StudentCourse(Base):
      __tablename__ = 'student_courses'
      
      student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
      course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
  ```

### 3.2 Database Schema Update

- **StudentCourse Junction Table**:
  - **student_id**: Integer (Foreign Key referencing Student)
  - **course_id**: Integer (Foreign Key referencing Course)

### 3.3 API Contracts

1. **POST /students/{id}/courses**
   - **Request**:
     - Body: `{"course_ids": [1, 2, 3]}`
   - **Response**:
     - On Success: 
       ```json
       {
         "message": "Courses associated successfully with the student."
       }
       ```
     - On Error (invalid student or course IDs):
       - Status Code: 400
       - Body:
       ```json
       {
         "error": {"code": "E001", "message": "One or more course IDs are invalid."}
       }
       ```

2. **GET /students/{id}/courses**
   - **Request**:
     - Params: `id` (Integer)
   - **Response**:
     - On Success:
       ```json
       [{"course_id": 1, "name": "Mathematics", "level": "Beginner"}, ...]
       ```
     - On Error (student not found):
       - Status Code: 404
       - Body:
       ```json
       {
         "error": {"code": "E002", "message": "Student not found."}
       }
       ```

### 3.4 Error Handling
- Input validation for valid course IDs should be implemented.
- Meaningful error messages must be returned according to the error type.
- Specific exceptions should be raised on failure, providing clear feedback to the API consumers.

## IV. Testing Strategy

### 4.1 Test Coverage
- Minimum of 70% coverage for newly implemented functionality with critical path coverage above 90%.

### 4.2 Test Types
- **Unit Tests**: For service functions managing student-course associations.
- **Integration Tests**: For overall functionality of the newly added API endpoints.

### 4.3 Test Organization
- Structure test cases mirroring the source structure:
  - `tests/api/test_student_courses.py`
  - `tests/service/test_student_course_service.py`

## V. Security Considerations

- Input validation must occur at the API layer to avoid malformed data.
- Sensitive configurations should be managed using environment variables.
- Ensure that no sensitive information about students or courses is logged.

## VI. Deployment Considerations

### 6.1 Production Readiness
- Ensure the system initializes and creates the new junction table on startup without manual intervention.
- Health check endpoint to confirm operational readiness.

### 6.2 Configuration Management
- Utilize a `.env` file for deployment-specific configurations.
- Document configurations required in a `.env.example`.

### 6.3 Database Migration Strategy
- Utilize SQLAlchemy with Alembic for schema migrations.
- Create and test a migration script for setting up the `student_courses` table.

## VII. Documentation

- Update the `README.md` to include:
  - New API endpoints for student-course associations.
  - Description of the StudentCourse model.
  - Examples of how to use the new endpoints.

## VIII. Modifications to Existing Files

### Modifications Needed
- **Model Layer**: Add the `StudentCourse` model definition.
- **Service Module**: Implement `associate_courses` and `get_student_courses` functions.
- **API Module**: Create new endpoint handlers for `POST /students/{id}/courses` and `GET /students/{id}/courses`.
- **Tests**: Add new tests in `tests/api/test_student_courses.py` and `tests/service/test_student_course_service.py`.

## IX. Conclusion

This implementation plan provides a structured approach to introducing the course association functionality within the existing student management system. Each component has been outlined to ensure seamless integration with current modules while adhering to established coding standards and ensuring backward compatibility. Effective testing and careful management of the database schema will allow this enhancement to proceed smoothly.

Existing Code Files:
File: `tests/api/test_student_courses.py`
```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is defined in main.py

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

def test_associate_courses_with_valid_data(client):
    """Test associating courses with a student."""
    response = client.post("/students/1/courses", json={"course_ids": [1, 2, 3]})
    assert response.status_code == 200  # 200 OK
    assert response.json() == {"message": "Courses associated successfully with the student."}

def test_get_student_courses(client):
    """Test retrieving a student's courses."""
    response = client.get("/students/1/courses")
    assert response.status_code == 200  # 200 OK
    assert isinstance(response.json(), list)

```

File: `tests/service/test_student_course_service.py`
```python
import pytest
from unittest.mock import MagicMock
from src.service.student_course_service import associate_courses, get_student_courses  # Import the functions to be tested
from src.model.student_course import StudentCourse  # Import the StudentCourse model

@pytest.fixture
def mock_db_session():
    """Create a mock database session for testing."""
    session = MagicMock()
    yield session

def test_associate_courses_success(mock_db_session):
    """Test successfully associating courses with a student."""
    # Mock the database session's behavior
    mock_db_session.add.side_effect = None  # Simulate successful add operation
    result = associate_courses(1, [1, 2, 3], mock_db_session) # The mock database session will be adjusted accordingly
    assert result is None  # Ensure no exception was raised

```
The modifications ensure integration into the current system with the defined new functionality while adhering to the established standards.