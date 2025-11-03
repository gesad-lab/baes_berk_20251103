# Implementation Plan: Add Course Relationship to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## 1. Overview 
This implementation plan outlines the architecture, technologies, and approach for adding a course relationship to the existing Student entity in the Student Management Web Application. This feature allows each Student to enroll in multiple Courses, thereby enhancing the educational data model and enabling better tracking of student enrollments.

## 2. Architecture

### 2.1 Application Structure
- **Frontend**: Not included in this scope (API only).
- **Backend**: RESTful API developed using Python and FastAPI, expanding the existing functionality to include Course relationships with Students.
- **Database**: SQLite for development and testing, with migrations to establish a many-to-many relationship between Students and Courses.

### 2.2 Components
- **API Endpoints**:
  - **POST /students/{studentId}/enroll**: Enroll a Student in a Course.
  - **GET /students/{studentId}/courses**: Retrieve all Courses a Student is enrolled in.

## 3. Technology Stack
- **Programming Language**: Python
- **Web Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy for database interactions
- **Testing Framework**: pytest for unit and integration testing
- **Environment Management**: Poetry for dependency management
- **API Documentation**: OpenAPI provided automatically by FastAPI

## 4. Implementation Approach

### 4.1 Database Design
- **New Enrollment Entity**:
  - `student_id`: Foreign key to Student (integer)
  - `course_id`: Foreign key to Course (integer)

#### 4.1.1 Database Schema Creation
Create a new `Enrollment` association model to establish the relationship:
```python
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Enrollment(Base):
    __tablename__ = "enrollments"

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")
```

### 4.2 Database Migration Strategy
Use Alembic migrations to add the `enrollments` table and change the existing data models without losing any existing data.
1. **Create Migration Script**:
   ```bash
   alembic revision --autogenerate -m "Add enrollments table for student-course relationship"
   ```

2. **Migrations will include**:
   - Creating the `enrollments` table to facilitate the many-to-many relationship.

#### Migration Example
```python
def upgrade():
    op.create_table(
        'enrollments',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True)
    )

def downgrade():
    op.drop_table('enrollments')
```

### 4.3 API Contract

#### 4.3.1 Enroll Student Endpoint
- **Endpoint**: `/students/{studentId}/enroll`
- **Method**: POST
- **Request Body**:
   ```json
   {
       "courseId": "string" (required)
   }
   ```

- **Response** (200 OK): 
```json
{
  "message": "Student enrolled successfully.",
  "courses": ["courseId1", "courseId2"]  // Array of current course IDs
}
```

- **Error Response** (404 Not Found - Course does not exist):
```json
{
  "error": {
    "code": "E001",
    "message": "Specified course not found."
  }
}
```

- **Error Response** (400 Bad Request - Course ID missing):
```json
{
  "error": {
    "code": "E002",
    "message": "Course ID is required."
  }
}
```

#### 4.3.2 Retrieve Student Courses Endpoint
- **Endpoint**: `/students/{studentId}/courses`
- **Method**: GET
- **Response** (200 OK):
```json
{
  "courses": [
    {"id": "courseId1", "name": "Course Name 1", "level": "Beginner"},
    {"id": "courseId2", "name": "Course Name 2", "level": "Intermediate"}
  ]
}
```

- **Error Response** (404 Not Found - Student not found):
```json
{
  "error": {
    "code": "E003",
    "message": "Student not found."
  }
}
```

### 4.4 Error Handling & Validation
- Validate the presence of `courseId` when enrolling a Student in a Course and return structured error messages as per the API contract.
- Use type hints and Pydantic models in FastAPI for automatic validation:
```python
from pydantic import BaseModel

class EnrollRequest(BaseModel):
    courseId: str
```

### 4.5 Testing Strategy
- **Unit Tests**:
  - Create tests for the enrollment functionality and validation of the request body.

- **Integration Tests**:
  - Test endpoints to ensure correct behavior when enrolling in existing courses, handling missing courses, and retrieving course lists for students.

### 4.6 Startup Procedures
- Update FastAPI's startup procedure to apply migrations during startup:
```python
@app.on_event("startup")
async def startup():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")  # Ensure latest migrations run on startup
```

## 5. Scalability, Security, and Maintainability Considerations
- **Scalability**: While SQLite suffices for development, consider transitioning to PostgreSQL for production scalability.
- **Security**: Implement input validation rigorously alongside access controls to prevent unauthorized modifications.
- **Maintainability**: Maintain clean code practices, document API changes, and ensure unit tests are updated with each new endpoint or feature addition.

## 6. Documentation
- Automatic API documentation via FastAPI will be available at `/docs`.
- Update the `README.md` to provide directions regarding the new enrollment functionality and how to utilize the endpoints.

## 7. Milestones
1. **Setup Migration**: Create and apply migrations to establish the `enrollments` table.
2. **Create Enrollment Model**: Implement the Enrollment association model.
3. **Implement API Endpoints**: Develop the `/students/{studentId}/enroll` and `/students/{studentId}/courses` endpoints.
4. **Testing**: Create and run unit tests and integration tests for the new functionality.
5. **Documentation**: Ensure the `README.md` and API documentation reflect the changes made.

## 8. Trade-offs and Decisions
- Utilized SQLite for development to keep the setup straightforward. Note that a move to a more robust database like PostgreSQL is warranted for production.
- Engaged in direct validation of `courseId` at the API level for immediate user feedback.
- Focused solely on creating RESTful API endpoints without changes to UI or advanced features, limiting the scope solely to the API enhancements required for course enrollment.

## Conclusion
This implementation plan provides a comprehensive strategy for incorporating a Course relationship into the Student entity as part of the existing Student Management Web Application. Through following established coding standards, testing rigorously, and maintaining clear documentation, this new feature will enhance the application’s capabilities in managing student enrollments. 

### Existing Code Files
- **File**: `tests/test_enrollments.py` (New Test File)
```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models import Enrollment  # Ensure proper import of enrollment model
from sqlalchemy.orm import Session
from src.database import get_db  # Dependency for database session

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

@pytest.fixture
def enroll_data():
    return {
        "courseId": "some_course_id"
    }

def test_enroll_student(client, enroll_data):
    response = client.post("/students/1/enroll", json=enroll_data)
    assert response.status_code == 200
    assert response.json()["message"] == "Student enrolled successfully."

def test_enroll_student_invalid_course(client):
    response = client.post("/students/1/enroll", json={"courseId": "invalid_course_id"})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E001", "message": "Specified course not found."}}

def test_enroll_student_missing_course(client):
    response = client.post("/students/1/enroll", json={})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Course ID is required."}}

def test_get_student_courses(client):
    response = client.get("/students/1/courses")
    assert response.status_code == 200
    assert "courses" in response.json()

def test_get_student_courses_not_found(client):
    response = client.get("/students/9999/courses")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E003", "message": "Student not found."}}
```

This test suite aims to cover the basics of enrollment functionality, ensuring any modifications remain backward compatible and stable before integration.