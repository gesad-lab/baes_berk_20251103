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
# Implementation Plan: Student Entity Web Application

## I. Overview

The purpose of this implementation plan is to establish a relationship between the Student and Course entities in the existing system. This will facilitate better management of student enrollments in multiple courses, enhancing educational tracking and reporting capabilities. The implementation will seamlessly integrate with existing architectures, ensuring backward compatibility and minimal disruption to existing functionalities.

## II. Architecture

### 2.1 Architectural Overview
The application will employ a RESTful architecture to manage relationships between students and courses via well-defined API endpoints. The existing entities will be extended to incorporate this new relationship without affecting current functionalities.

### 2.2 Components
1. **API Layer**: New endpoints will manage course enrollments associated with students.
2. **Service Layer**: Logic for enrollment validation and business rules related to student-course relationships.
3. **Data Access Layer (DAL)**: Responsible for CRUD operations related to course enrollments.
4. **Database**: Existing SQLite database will be modified to include a new linking table (`student_courses`) representing the many-to-many relationship between Student and Course.

## III. Technology Stack

- **Programming Language**: Python 3.11+
- **Web Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing Framework**: Pytest
- **Environment Management**: `pip`
- **Logging**: Python's built-in logging module

## IV. Module Boundaries and Responsibilities

### 4.1 API Module
- Endpoint Definitions:
  - `POST /students/{studentId}/courses`: Enroll a student in a course (requires `courseId`).
  - `GET /students/{studentId}/courses`: Retrieve all courses for a student.
  - `DELETE /students/{studentId}/courses/{courseId}`: Remove a student from a course.

### 4.2 Service Layer
- Business logic will include:
  - Validation of student ID and course ID during enrollment, retrieval, and deletion.
  - Logic to prevent duplicate enrollments.

### 4.3 Data Access Layer
- Responsible for database interactions, including:
  - Implementation of CRUD operations for student-course enrollments.
  - Migration handling for the creation of the `student_courses` linking table.

## V. Data Models

### 5.1 Student-Course Relationship Model
```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StudentCourse(Base):
    __tablename__ = "student_courses"

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")
```

### 5.2 Update Existing Models
- Update the `Student` and `Course` classes to include relationships.
```python
class Student(Base):
    __tablename__ = "students"
    
    # existing fields...
    courses = relationship("StudentCourse", back_populates="student", cascade="all, delete-orphan")


class Course(Base):
    __tablename__ = "courses"
    
    # existing fields...
    students = relationship("StudentCourse", back_populates="course", cascade="all, delete-orphan")
```

## VI. API Contracts

### 6.1 Request/Response Format

1. **Enroll Student in Course** (`POST /students/{studentId}/courses`)
   - **Request**: 
     ```json
     {
         "courseId": 1
     }
     ```
   - **Response** (201 Created):
     ```json
     {
         "studentId": 1,
         "courseId": 1,
         "message": "Student enrolled successfully."
     }
     ```

2. **Retrieve Student Courses** (`GET /students/{studentId}/courses`)
   - **Response** (200 OK):
     ```json
     [
         {
             "id": 1,
             "name": "Mathematics",
             "level": "Beginner"
         },
         {
             "id": 2,
             "name": "Physics",
             "level": "Intermediate"
         }
     ]
     ```

3. **Remove Student from Course** (`DELETE /students/{studentId}/courses/{courseId}`)
   - **Response** (204 No Content):
     `No Response Body`

### 6.2 Error Responses
- **Invalid Student or Course ID**:
```json
{
    "error": {
        "code": "E001",
        "message": "Invalid student ID or course ID."
    }
}
```

## VII. Error Handling

- Validate that both `studentId` and `courseId` are provided for enrollment.
- Check for valid entries in the database to prevent enrolling a student in non-existing courses and vice versa. 
- Provide informative error messages for invalid inputs.

## VIII. Implementation Steps

1. **Database Migration**:
   - Create a migration script to add the `student_courses` linking table.
   ```sql
   CREATE TABLE student_courses (
       student_id INTEGER NOT NULL,
       course_id INTEGER NOT NULL,
       PRIMARY KEY (student_id, course_id),
       FOREIGN KEY (student_id) REFERENCES students(id),
       FOREIGN KEY (course_id) REFERENCES courses(id)
   );
   ```

2. **Update Data Access Layer**:
   - Create the `StudentCourse` model to facilitate CRUD operations related to enrollments.
   - Implement methods to manage enrollments in the database.

3. **Modify API Endpoints**:
   - Implement the `POST /students/{studentId}/courses` endpoint to enroll a student.
   - Implement the `GET /students/{studentId}/courses` endpoint to retrieve courses for a student.
   - Implement the `DELETE /students/{studentId}/courses/{courseId}` endpoint for removing enrollments.

4. **Enhance Service Layer**:
   - Add services to handle business logic for course enrollment and validation.
   - Ensure existing logging and error-handling practices are in place.

5. **Write Tests**:
   - Create unit tests for the new functionalities related to student-course relationships, including success and error scenarios.
   - Target at least 70% test coverage on the new features.

6. **Documentation**:
   - Update API documentation referencing the new endpoints for student enrollments.
   - Ensure the README includes details on the new migration and how it integrates with existing features.

7. **End-to-End Testing**:
   - Perform integration tests to validate the new API endpoints with both valid and invalid data inputs.

8. **Deployment**:
   - Validate changes in a staging environment to ensure existing functionalities remain intact following the migration and new feature integration.

## IX. Testing Strategy

- Implement automated tests aligned with Pytest framework for:
  - Unit tests of service methods related to student-course enrollments.
  - Integration tests to verify the new APIs work seamlessly with the existing system.

## X. Deployment Considerations

- Ensure environment variables are set properly for the database update.
- Document migration processes for rollbacks and validation during production-level deployment.

## XI. Conclusion

This implementation plan outlines a structured approach to linking students and courses in the educational management system. By following best practices and maintaining compatibility, this will enrich the application capabilities while safeguarding existing functionalities.

### Existing Code Modifications:
- **StudentCourse Model**: New model to facilitate student/course associations.
- **Updated API Endpoints**: New endpoints for managing enrollments.
- **Integration of Relationships**: Update the existing Student and Course models to reflect relationships.
- **Testing**: Automation tests to cover new student-course features.

**Example migration script**:
```python
# migration.py
"""Create student_courses table

Revision ID: <unique_id>
"""
from sqlalchemy import Column, Integer, ForeignKey
from alembic import op


def upgrade():
    op.create_table('student_courses',
        Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
        Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
    )


def downgrade():
    op.drop_table('student_courses')
```

### Testing File Example:
File: `tests/test_student_course_api.py`
```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assume your FastAPI app is instantiated in src/main.py

@pytest.fixture(scope="module")
def client():
    """Setup the test client for the FastAPI application."""
    with TestClient(app) as client:
        yield client

def test_enroll_student_in_course(client):
    """Test enrolling a student in a course."""
    response = client.post("/students/1/courses", json={"courseId": 1})
    assert response.status_code == 201
    assert response.json()["message"] == "Student enrolled successfully."

def test_get_student_courses(client):
    """Test retrieving all courses for a student."""
    response = client.get("/students/1/courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Expecting a list of courses
```

**With this structured plan, the implementation of the student-course relationship will enhance the functionality of the educational management system while ensuring backward compatibility and seamless integration with the existing architecture.**