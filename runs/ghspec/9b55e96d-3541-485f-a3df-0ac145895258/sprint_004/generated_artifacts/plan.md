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

## Version
**Version**: 1.0.0  
**Purpose**: Implementation plan for establishing the relationship between Student and Course entities within the educational management system.

## I. Architecture Overview

### 1.1 High-Level Architecture
This implementation will extend the existing architecture by introducing an associative `Enrollment` entity that represents the relationship between `Student` and `Course`. The API layer will be updated to include new endpoints for enrolling, retrieving, and removing Students from Courses. The data access layer will be modified to reflect these additions while maintaining existing functionality.

### 1.2 Technology Stack
- **Programming Language**: Python
- **Web Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing Framework**: pytest

## II. Module Design

### 2.1 API Module
**Responsibilities**:
- Implement new API endpoints for managing student enrollments in courses.
  
**Endpoints**:
1. `POST /students/{student_id}/enroll` - Enroll a Student in a Course
2. `GET /students/{student_id}/courses` - Retrieve Courses for a Student
3. `DELETE /students/{student_id}/courses/{course_id}` - Remove a Student from a Course

### 2.2 Service Layer
**Responsibilities**:
- Handle business logic for enrolling, retrieving, and removing students from courses, including validation checks and error handling.

### 2.3 Data Access Layer
**Responsibilities**:
- Add SQLAlchemy models for the `Enrollment` entity to manage relationships between `Student` and `Course`.

### 2.4 Database Models
**Entities**: Enrollment

```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Enrollment(Base):
    __tablename__ = 'enrollments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")
```

## III. API Contracts

### 3.1 Request and Response Formats

#### 3.1.1 Enroll Student in Course
- **Request**:
  - Method: `POST`
  - URL: `/students/{student_id}/enroll`
  - Body: `{"course_id": 1}`
- **Response**:
  - Status: `200 OK` (or `404 Not Found` if Student or Course does not exist)
  - Body: `{"message": "Student enrolled in course successfully"}`

#### 3.1.2 Retrieve Student's Courses
- **Request**:
  - Method: `GET`
  - URL: `/students/{student_id}/courses`
- **Response**:
  - Status: `200 OK`
  - Body: `{"courses": [{"id": 1, "name": "Mathematics 101", "level": "Beginner"}, {...}]}` 
  or `404 Not Found` if Student does not exist.

#### 3.1.3 Remove Student from Course
- **Request**:
  - Method: `DELETE`
  - URL: `/students/{student_id}/courses/{course_id}`
- **Response**:
  - Status: `200 OK` (or `404 Not Found` if Student or Course does not exist)
  - Body: `{"message": "Student removed from course successfully"}`

### 3.2 Error Responses
- **404 Not Found** for invalid Student or Course IDs: 
  `{"error": {"code": "E001", "message": "Student or Course not found"}}`

## IV. Database Management

### 4.1 Schema Migration
- Use Alembic to create and manage the new `enrollments` table that captures `student_id` and `course_id`.

#### Migration Script Example
```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table('enrollments',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), nullable=False),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), nullable=False)
    )

def downgrade():
    op.drop_table('enrollments')
```

### 4.2 Schema Initialization
- Ensure the `enrollments` table is created during application startup if it does not exist.

## V. Security Considerations
- Validate all incoming requests to check for valid `student_id` and `course_id`.
- Sanitize inputs to prevent SQL injection and ensure robust error handling practices are in place.

## VI. Testing Strategy

### 6.1 Test Coverage
- Target a minimum 70% test coverage for the new Enrollment functionality.

### 6.2 Testing Structure
- Add tests for API endpoints to verify correct enrollments, retrievals, and removals of courses for students.

### 6.3 Example Test Cases
- `test_enroll_student_success()`
- `test_enroll_nonexistent_student_fails()`
- `test_retrieve_student_courses_success()`
- `test_retrieve_courses_for_nonexistent_student_fails()`
- `test_remove_student_from_course_success()`
- `test_remove_student_from_nonexistent_course_fails()`

## VII. Deployment Considerations

### 7.1 Deployment Strategy
- Utilize Docker for packaging the application and ensure the migration script runs as part of the deployment process to create the `enrollments` table.

### 7.2 Health Check Endpoint
- Update existing health check to confirm that enrollment functionality is operational post-deployment.

## VIII. Documentation

### 8.1 Required Documentation
- Update the README.md to document the new Enrollment API endpoints, including details of request formats and responses.
  
### 8.2 API Documentation
- Utilize OpenAPI/Swagger to comprehensively document the new API endpoints associated with student enrollments.

## IX. Project Management and Version Control

### 9.1 Version Control Practices
- Adhere to existing Git practices and update `CHANGELOG.md` to reflect the addition of Enrollment functionality.

## X. Conclusion
This implementation plan provides a structured approach to adding the Course relationship to the Student entity, ensuring maintainability and data integrity while enhancing the educational management system's functionality. 

Existing Code Files:
File: `tests/api/test_enrollment.py`
```python
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_enroll_student_success():
    response = client.post("/students/1/enroll", json={"course_id": 1})
    assert response.status_code == 200
    assert response.json().get("message") == "Student enrolled in course successfully"

def test_enroll_nonexistent_student_fails():
    response = client.post("/students/999/enroll", json={"course_id": 1})
    assert response.status_code == 404
    assert "error" in response.json()
```
Ensure to implement the new endpoint functionality, integrate the service and data access layers appropriately, and conduct thorough testing to validate the feature's correctness against the provided specifications.