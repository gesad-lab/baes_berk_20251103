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
# Implementation Plan: Student Entity Management

## Version
1.0.0

## Purpose
To establish a relationship between the Student entity and the Course entity, enabling the system to manage Students' enrollments in multiple Courses. This enhancement supports the structure of educational management within the application seamlessly.

## Architecture Overview
The application is built on a microservices architecture utilizing RESTful APIs, developed using Python and FastAPI, with SQLite as the database. The new feature will integrate into the existing architecture, maintaining a clean separation of concerns while enhancing functionality without disrupting current features.

## Technology Stack
- **Backend Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing**: pytest

## Module Boundaries and Responsibilities
1. **API Layer**:
   - Introduce new endpoints for the Course relationship functionalities related to Students.

2. **Service Layer**:
   - Manage the business logic for enrolling and unenrolling Students from Courses, as well as retrieving lists of enrolled Courses.

3. **Persistence Layer**:
   - Extend the existing persistence model to support relational data between Students and Courses.

## Data Models and API Contracts

### Data Model: Student (Modified)
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    courses = relationship('Course', secondary='student_courses', back_populates='students')
```

### Data Model: Course (Existing Structure)
```python
from sqlalchemy import Column, Integer, String
# In models.py (no changes needed for Course)
class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
```

### New Association Table for Student-Course Relationship
```python
class StudentCourse(Base):
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
```

### API Endpoints
1. **Enroll Student in Course**
   - **Endpoint**: `POST /students/{student_id}/enroll`
   - **Request Body**: 
     ```json
     {
       "course_id": integer
     }
     ```
   - **Response**: 
     - 200 OK: `{ "success": true, "student": { "id": integer, "courses": [integer] } }`
     - 400 Bad Request if course_id is missing or invalid.
     - 404 Not Found if the Student ID or Course ID does not exist.

2. **Retrieve Student Courses**
   - **Endpoint**: `GET /students/{student_id}/courses`
   - **Response**: 
     - 200 OK: `[integer]` (list of Course IDs)
     - 404 Not Found if the Student ID does not exist.

3. **Remove Student from Course**
   - **Endpoint**: `DELETE /students/{student_id}/enroll`
   - **Request Body**:
     ```json
     {
       "course_id": integer
     }
     ```
   - **Response**: 
     - 200 OK: `{ "success": true, "message": "Student removed from course." }`
     - 404 Not Found if the Student ID or Course ID does not exist.

## Implementation Approach

### 1. Project Structure Update
- Update the existing FastAPI project structure:
  ```
  src/
  ├── main.py            # Integrate routes
  ├── models.py          # Modify to include Student-Course relationship and association table
  ├── services.py        # Add services for enrollment logic
  ├── api.py             # New API endpoints for enrollment and retrieval
  ├── database.py        # Update database schema with association table
  tests/
  ├── test_api.py        # New tests for Student-Course related API endpoints
  ├── test_services.py    # New tests for enrollment business logic
  ```

### 2. Database Migration Strategy
- **Alembic**: Utilize Alembic to create and modify schema by introducing the `student_courses` association table which connects `Student` and `Course` entities:
```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table('student_courses',
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), primary_key=True)
    )

def downgrade():
    op.drop_table('student_courses')
```

### 3. API Implementation
- In `api.py`, create new endpoints for:
  - Enrolling and unenrolling a student in Courses.
  - Retrieving course listings for a student.

### 4. Business Logic Implementation
- Write new service methods in `services.py`:
  - `enroll_student_in_course(student_id, course_id)`
  - `remove_student_from_course(student_id, course_id)`
  - `get_student_courses(student_id)`

### 5. Input Validation
- Pydantic models for `course_id` validation will be implemented where necessary for enrollment and removal requests:
```python
from pydantic import BaseModel

class EnrollRequest(BaseModel):
    course_id: int

class UnenrollRequest(BaseModel):
    course_id: int
```

### 6. Testing
- Extensive tests will be created in `test_services.py` and `test_api.py`.
- Use HTTP status code verification to ensure endpoint responses are correct.

### 7. Docker Setup
- Ensure ORM configuration is consistent within Docker setup allowing migrations to be applied on new deployments without impacting running services.

## Scalability, Security, and Maintainability Considerations
- Configure all secrets via environment variables.
- Introduce robust input validation and error messaging.
- Organize service functions to encourage ease of future enhancements.

## Trade-Offs and Decisions
- **Relational Integrity**: Utilizing an association table allows for many-to-many relationships but increases complexity in queries and business logic.
- **Error Handling**: The project will ensure clear error codes and messages for invalid enrollments or unenrollments, focusing on user-friendliness.

### Success Criteria
- Adhere to performance benchmarks with a maximum response time of 500 ms for all API calls.
- Maintain at least 70% unit and integration test coverage for the new features.

## Deployment Considerations
- Validate that the Docker images incorporate database migration steps into their startup routines, smoothening the processes involved in deployment.
- Preserve backward compatibility on earlier Student functionalities and maintain data integrity throughout transitions.

## Conclusion
This implementation plan introduces a new Course relationship to the Student entity effectively, laying out the groundwork for managing enrollments in a modular fashion while summoning best practices in coding and software architecture.

Existing Code Files:
### File: tests/test_api.py
```python
import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    # Set up any necessary database state before tests
    yield
    # Clean up database state after tests

def test_enroll_student_success(setup_database):
    """Test that enrolling a student in a course successfully returns the updated student object."""
    response = client.post("/students/1/enroll", json={"course_id": 1})
    assert response.status_code == 200
    assert "success" in response.json()

def test_retrieve_student_courses(setup_database):
    """Test retrieving a student's courses successfully."""
    response = client.get("/students/1/courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
```

### File: tests/test_services.py
```python
import pytest
from sqlalchemy.orm import Session
from src.services import enroll_student_in_course, remove_student_from_course, get_student_courses

@pytest.fixture(scope="module")
def db_session():
    """Set up a test database session."""
    # Setup code for the test database here
    yield db_session  # Replace with the actual session
    # Tear down code would go here

def test_enroll_student_in_course(db_session):
    """Test enrolling a student in a course."""
    result = enroll_student_in_course(db_session, 1, 1)  # student_id 1, course_id 1
    assert result is True  # Assume enroll function returns a boolean

def test_remove_student_from_course(db_session):
    """Test removing a student from a course."""
    result = remove_student_from_course(db_session, 1, 1)  # student_id 1, course_id 1
    assert result is True  # Assuming the function confirms success
``` 

This structured implementation plan effectively outlines how to incorporate the Course relationship into the existing Student entity while ensuring the application's integrity, maintainability, and scalability.