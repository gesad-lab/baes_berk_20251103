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
# Implementation Plan: Student Entity Management Web Application

## Overview
This implementation plan outlines the technical design and changes required to establish a many-to-many relationship between the Student and Course entities. By creating an intermediary join table (`student_courses`), the application will effectively manage student enrollments in multiple courses, thereby enhancing tracking and management features for educational progress.

## 1. Architecture

### 1.1 Application Structure
- **Framework**: FastAPI
- **Database**: SQLite
- **Programming Language**: Python 3.11+

**Project Layout**
```
student_management/
    ├── src/
    │   ├── main.py               # Entry point for the FastAPI application
    │   ├── models.py             # Database models for SQLAlchemy
    │   ├── schemas.py            # Pydantic schemas for request/response validation
    │   ├── database.py           # Database connection and setup
    │   ├── routes/
    │   │   ├── students.py       # API endpoints for student management
    │   │   ├── courses.py        # API endpoints for course management
    │   │   └── enrollments.py     # New API endpoints for enrolling students in courses
    ├── tests/
    │   ├── test_routes.py        # Test cases for API endpoints
    │   ├── test_courses.py       # Test cases for course management
    │   └── test_enrollments.py    # New test cases for enrollment management
    ├── requirements.txt           # Project dependencies
    ├── .env.example               # Environment variable example
    └── README.md                  # Project documentation
```

## 2. Technology Stack
- **Web Framework**: FastAPI
- **Database ORM**: SQLAlchemy
- **Database**: SQLite
- **Serialization**: Pydantic for data validation
- **Testing Framework**: pytest for unit and integration tests

## 3. Module Boundaries and Responsibilities

### 3.1 New Modules
- **`models.py`**: Create a join table `student_courses` to establish a many-to-many relationship.
- **`routes/enrollments.py`**: Implement API endpoints for enrolling students in courses and retrieving courses for a specific student.

### 3.2 Existing Modules Updates
- **`models.py`**: Update to include the new join table definition.
- **`schemas.py`**: Create a new schema for enrollment and modify existing schemas as needed for course data.
- **`routes/students.py` and `routes/courses.py`**: Add functionality for the new enrollment feature through interaction with these routes.

## 4. Data Models and API Contracts

### 4.1 Data Model Creation
```python
# models.py
from sqlalchemy import create_engine, Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

class StudentCourse(Base):
    __tablename__ = 'student_courses'
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

# Update Student and Course models to establish relationships
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    courses = relationship("StudentCourse", back_populates="student")

Course.students = relationship("StudentCourse", back_populates="course")
```

### 4.2 API Endpoints
- **POST /students/{student_id}/courses**
    - **Request**: 
        ```json
        { "course_id": 1 }
        ```
    - **Response**: 
        - Success: `201 Created` with `{ "message": "Student enrolled in course." }`
        - Error: `400 Bad Request` for invalid course IDs.

- **GET /students/{student_id}/courses**
    - **Response**:
        - Success: `200 OK` with JSON array of course objects: `[ { "id": 1, "name": "Data Science 101", "level": "Intermediate"}, ... ]`

### 4.3 Response Format
All responses will maintain a consistent JSON format:
```json
{
  "error": {
      "code": "E001",
      "message": "Invalid course ID",
      "details": {}
  }
}
```

## 5. Implementation Approach

### 5.1 Development Phases
1. **Setup Project Environment**:
    - Ensure that the `requirements.txt` includes necessary dependencies for inclusion of new features.

2. **Database and Model Implementation**:
    - Create the `student_courses` model in `models.py` and ensure proper relationships.
    - Prepare and conduct database migrations using Alembic to create the `student_courses` table.

3. **API Development**:
    - Implement the `/students/{student_id}/courses` POST and GET endpoints in `routes/enrollments.py`.
    - Utilize Pydantic for validation of requests.

4. **Testing**:
    - Introduce new tests in `tests/test_enrollments.py` focused on the enrollment functionality.

5. **Documentation**:
    - Update `README.md` with the new API endpoint descriptions and examples.

## 6. Testing Strategy

### 6.1 API Tests
- Develop tests ensuring:
  - Successful enrollment of students in courses.
  - Retrieval of all courses associated with a specific student.
  - Appropriate handling of validation errors when invalid data is provided.

### 6.2 Example Test Case
```python
# tests/test_enrollments.py
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming app is imported from main.py

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

# Test enrollment of student in a course
def test_enroll_student_in_course(client):
    response = client.post("/students/1/courses", json={"course_id": 1})
    assert response.status_code == 201
    assert response.json() == {"message": "Student enrolled in course."}

# Test for invalid course enrollment
def test_enroll_student_invalid_course(client):
    response = client.post("/students/1/courses", json={"course_id": 999})
    assert response.status_code == 400
    assert response.json()["error"]["code"] == "E001"  # Invalid course ID
```

## 7. Database Migration Strategy
- Use Alembic to create a migration script that adds the `student_courses` join table and establishes foreign key constraints:
    - Create a new migration file to:
        1. Add `student_courses` table.
        2. Retain integrity of existing data in `students` and `courses` without data loss.
        3. Ensure migrations are reversible when possible.

## 8. Conclusion
This implementation plan outlines the modifications needed to integrate the course relationship into the existing Student entity models effectively while maintaining backward compatibility with current data structures. It emphasizes correct API design, thorough testing, and a clear schema migration strategy to support the enhancement of educational management capabilities in the application.

Existing Code Files:
No code files found from the previous sprint.