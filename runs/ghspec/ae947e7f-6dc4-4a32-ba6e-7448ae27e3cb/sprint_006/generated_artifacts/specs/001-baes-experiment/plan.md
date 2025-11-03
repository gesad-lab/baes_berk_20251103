# Implementation Plan: Add Teacher Relationship to Course Entity

---
### INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:  
# Implementation Plan: Create Teacher Entity

---
### INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:  
# Implementation Plan: Add Course Relationship to Student Entity

---
### INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:  
# Implementation Plan: Create Course Entity

---
### INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:  
# Implementation Plan: Add Email Field to Student Entity

---
### INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:  
# Implementation Plan: Student Management Web Application

## I. Architecture Overview

This feature implementation will integrate a relationship between the Course and Teacher entities within the existing student management system, following the established RESTful API architecture. The integration will involve modifications to the existing Course model and appropriate corresponding changes to the API endpoints.

### 1.1 Module Structure

1. **API Module**: Handles HTTP requests related to teacher-course associations.
2. **Service Module**: Contains business logic for managing teacher relationships with courses.
3. **Data Access Layer (DAL)**: Manages interactions between the application and the database.
4. **Model Layer**: Updates the existing Course model to introduce a teacher reference.

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
  - Define endpoints for associating and dissociating teachers to courses.
  - Retrieve course details including teacher information.
  - Validate inputs and return structured JSON responses.

- **Endpoints**:
  - `POST /courses/{id}/teacher`: Associate a teacher with a course.
  - `GET /courses/{id}`: Retrieve course details with associated teacher.
  - `DELETE /courses/{id}/teacher`: Dissociate a teacher from a course.

#### Service Module
- **Responsibilities**:
  - Implement logic for associating and dissociating teachers with courses.
  - Validate course and teacher existence.

- **Key Functions**:
  - `associate_teacher(course_id: int, teacher_id: int) -> Dict`: Links a teacher to a course.
  - `retrieve_course(course_id: int) -> Dict`: Gets course details alongside associated teacher information.
  - `dissociate_teacher(course_id: int) -> Dict`: Removes the teacher association from the course.

#### Data Access Layer (DAL)
- **Responsibilities**:
  - Execute database operations for teacher-course associations.
  - Ensure that existing Course and Teacher data are kept intact.

- **Key Functions**:
  - `link_teacher_to_course(course_id: int, teacher_id: int)`: Updates the Course table with the associated teacher ID.
  - `get_course_details(course_id: int)`: Fetches course details with the related teacher's info.
  - `remove_teacher_from_course(course_id: int)`: Updates the Course table by setting `teacher_id` to NULL.

#### Model Layer
- **Responsibilities**:
  - Update the Course model to include the `teacher_id` property.

- **Model Definition**:
  ```python
  from sqlalchemy import Column, Integer, String, ForeignKey
  from sqlalchemy.ext.declarative import declarative_base

  Base = declarative_base()

  class Course(Base):
      __tablename__ = 'courses'
      
      id = Column(Integer, primary_key=True, autoincrement=True)
      name = Column(String, nullable=False)
      level = Column(String, nullable=False)
      teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New teacher relationship
  ```

### 3.2 Database Schema Update

- **Courses Table**:
  - **teacher_id**: Integer (foreign key referencing Teacher, nullable to preserve existing data)

### 3.3 API Contracts

1. **POST /courses/{id}/teacher**
   - **Request**:
     - Params: course ID in the URL
     - Body: `{"teacher_id": 1}`
   - **Response**:
     - On Success:
       ```json
       {
         "message": "Teacher associated successfully."
       }
       ```
     - On Error (invalid course or teacher ID):
       - Status Code: 400
       - Body:
       ```json
       {
         "error": {"code": "E001", "message": "Invalid course or teacher ID."}
       }
       ```

2. **GET /courses/{id}**
   - **Request**:
     - Params: course ID in the URL
   - **Response**:
     - On Success:
       ```json
       {
         "id": 1,
         "name": "Math 101",
         "level": "Beginner",
         "teacher": {"id": 1, "name": "John Doe", "email": "john.doe@example.com"}
       }
       ```
     - On Error (course not found):
       - Status Code: 404
       - Body:
       ```json
       {
         "error": {"code": "E002", "message": "Course not found."}
       }
       ```

3. **DELETE /courses/{id}/teacher**
   - **Request**:
     - Params: course ID in the URL
   - **Response**:
     - On Success:
       ```json
       {
         "message": "Teacher dissociated successfully."
       }
       ```
     - On Error (course not found):
       - Status Code: 404
       - Body:
       ```json
       {
         "error": {"code": "E002", "message": "Course not found."}
       }
       ```

### 3.4 Error Handling
- Validate the existence of both course and teacher before establishing the relationship.
- Return meaningful error messages for validation failures and missing entities.

## IV. Testing Strategy

### 4.1 Test Coverage
- Aim for at least 70% coverage for the new functionality, ensuring critical paths (associations) maintain a minimum of 90% coverage.

### 4.2 Test Types
- **Unit Tests**: For individual service functions handling logic.
- **Integration Tests**: For API endpoint interactions including associated entities.

### 4.3 Test Organization
- Test files should reflect the structure within the source code:
  - `tests/api/test_courses.py`
  - `tests/service/test_course_service.py`

## V. Security Considerations

- Ensure validation of all inputs at the API layer to prevent SQL injections and malformed data submissions.
- Configurations must be securely managed using environment variables.
- Guard against unauthorized access to sensitive data (teacher information).

## VI. Deployment Considerations

### 6.1 Production Readiness
- Ensure system startup automatically applies the new `teacher_id` column without manual intervention.
- Implement a health-check endpoint to confirm operational status.

### 6.2 Configuration Management
- Utilize a `.env` file for configuration settings.
- Provide a `.env.example` to outline all required configurations.

### 6.3 Database Migration Strategy
- Use SQLAlchemy with Alembic for schema migrations. 
- Create a migration script to add the `teacher_id` column to the `courses` table, ensuring nullable constraints.

## VII. Documentation

- Update the `README.md` with:
  - New API endpoints for associating and dissociating teachers with courses.
  - Examples for how to use the new teacher relationship endpoints.
  - Changes made to the Course entity.

## VIII. Modifications to Existing Files

### Modifications Needed
- **Model Layer**: Update the Course model to include the `teacher_id` column and its foreign key relationship towards the `teachers` table.
- **Service Module**: Implement the logic to associate and dissociate teachers from courses within the `course_service.py`.
- **API Module**: Create new handlers for `/courses/{id}/teacher` endpoints and modify `/courses/{id}` to return teacher associations.
- **Tests**: Add tests in `tests/api/test_courses.py` for new API functionality and in `tests/service/test_course_service.py` for service logic.

## IX. Conclusion

This implementation plan outlines the steps necessary to establish a relationship between courses and teachers, enhancing the current student management system while adhering to established architecture and coding standards. Careful consideration is given to security, testing, and documentation to ensure maintainability and readiness for production deployment.

Existing Code Files:
File: `tests/api/test_courses.py`
```python
import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming the FastAPI app is defined in main.py

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

def test_associate_teacher_with_course(client):
    """Test associating a teacher with a course."""
    response = client.post("/courses/1/teacher", json={"teacher_id": 1})
    assert response.status_code == 200  # 200 OK
    assert response.json() == {"message": "Teacher associated successfully."}

def test_get_course_with_teacher(client):
    """Test getting course details including teacher's information."""
    response = client.get("/courses/1")
    assert response.status_code == 200  # 200 OK
    assert "teacher" in response.json()

def test_dissociate_teacher_from_course(client):
    """Test dissociating a teacher from a course."""
    response = client.delete("/courses/1/teacher")
    assert response.status_code == 200  # 200 OK
    assert response.json() == {"message": "Teacher dissociated successfully."}
```

File: `tests/service/test_course_service.py`
```python
import pytest
from unittest.mock import MagicMock
from src.service.course_service import associate_teacher, retrieve_course, dissociate_teacher

@pytest.fixture
def mock_db_session():
    """Create a mock database session for testing."""
    mock_session = MagicMock()
    yield mock_session

def test_associate_teacher(mock_db_session):
    """Test successfully associating a teacher to a course."""
    mock_db_session.query.return_value.filter.return_value.first.return_value = ...  # Stub course
    result = associate_teacher(1, 1, mock_db_session)  # Course ID, Teacher ID
    assert result is None  # Ensure no errors; check DB interactions if necessary

def test_retrieve_course(mock_db_session):
    """Test successfully retrieving a course and teacher info."""
    mock_db_session.query.return_value.filter.return_value.first.return_value = ...  # Stubbed course
    result = retrieve_course(1, mock_db_session)
    assert result["teacher"]["name"] == "John Doe"  # Check associated teacher name

def test_dissociate_teacher(mock_db_session):
    """Test successfully dissociating a teacher from a course."""
    mock_db_session.query.return_value.filter.return_value.first.return_value = ...  # Stub course
    result = dissociate_teacher(1, mock_db_session)
    assert result is None  # Ensure no errors; check state change
```

This plan ensures that all modifications are carefully integrated while adhering to existing code practices and maintaining system integrity.