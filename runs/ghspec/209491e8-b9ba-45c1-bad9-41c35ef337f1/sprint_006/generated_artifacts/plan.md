# Implementation Plan: Add Teacher Relationship to Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
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
This implementation plan outlines the technical design and changes required to establish a relationship between the Course entity and the Teacher entity in the existing application. By implementing this feature, we will enhance data management for educators and improve clarity in course offerings.

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
    │   │   └── teachers.py       # API endpoints for teacher management
    ├── tests/
    │   ├── test_routes.py        # Test cases for API endpoints
    │   ├── test_teachers.py      # Test cases for teacher management
    │   └── test_courses.py        # Test cases for course management
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
- **`routes/courses.py`**: Implement API endpoints for the new course-teacher relationship.

### 3.2 Existing Modules Updates
- **`models.py`**: Update the existing `Course` model to include `teacher_id`.
- **`schemas.py`**: Add new response models for course retrieval with teacher details.
- **`routes/teachers.py`**: (Existing) No changes required here; will continue handling teacher-related endpoints.

## 4. Data Models and API Contracts

### 4.1 Data Model Updates
```python
# models.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))  # Foreign key added

    teacher = relationship("Teacher", back_populates="courses")

Teacher.courses = relationship("Course", order_by=Course.id, back_populates="teacher")
```

### 4.2 API Endpoints
**New Endpoints in `routes/courses.py`:**

- **POST /courses/{course_id}/assign-teacher**
    - **Request**:
    ```json
    {
        "teacher_id": 1  // ID of the teacher to assign
    }
    ```
    - **Response**: 
        - Success: `200 OK` with `{ "message": "Teacher assigned successfully." }`
        - Error: `404 Not Found` for invalid course or teacher IDs.

- **GET /courses/{course_id}**
    - **Response**:
        - Success: `200 OK` with:
        ```json
        {
            "id": 1,
            "title": "Math 101",
            "description": "Introduction to Mathematics",
            "teacher": {
                "id": 1,
                "name": "John Doe",
                "email": "john.doe@example.com"
            }
        }
        ```

### 4.3 Response Format
Responses will follow a standardized format, including error messages:
```json
{
  "error": {
      "code": "E001",
      "message": "Invalid request, teacher or course ID not found",
      "details": {}
  }
}
```

## 5. Implementation Approach

### 5.1 Development Phases
1. **Setup Project Environment**:
    - Ensure `requirements.txt` includes necessary dependencies for the new feature if any.

2. **Database and Model Implementation**:
    - Update the `Course` model in `models.py` to include `teacher_id`.

3. **API Development**:
    - Implement the `/courses/{course_id}/assign-teacher` POST and modify the `/courses/{course_id}` GET endpoints in `routes/courses.py`.

4. **Testing**:
    - Develop new tests in `tests/test_courses.py` for the new assignment functionality.
  
5. **Documentation**:
    - Update `README.md` with descriptions of the new API endpoints and examples.

## 6. Testing Strategy

### 6.1 API Tests
- Test cases should verify:
  - Successful assignment of teachers to courses.
  - Retrieval of course data, including associated teacher information.
  - Validation error responses for invalid IDs.

### 6.2 Example Test Case
```python
# tests/test_courses.py
import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c

# Test assignment of teacher to course
def test_assign_teacher_to_course(client):
    response = client.post("/courses/1/assign-teacher", json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher assigned successfully."}

# Test retrieval of course with teacher information
def test_get_course_with_teacher(client):
    response = client.get("/courses/1")  # assuming this ID exists
    assert response.status_code == 200
    assert "teacher" in response.json()  # Check that teacher info is included

# Test validation handling
def test_assign_teacher_invalid_course(client):
    response = client.post("/courses/999/assign-teacher", json={"teacher_id": 1})  # Invalid course ID
    assert response.status_code == 404
    assert response.json()["error"]["code"] == "E001"
```

## 7. Database Migration Strategy
- Utilize Alembic to create a migration script to:
    1. Add `teacher_id` column to the `courses` table.
    2. Create necessary relationships and indexes to ensure efficient querying.
    3. Ensure migrations are reversible and do not disrupt existing data integrity.

## 8. Conclusion
This implementation plan sets out the necessary modifications to integrate a teacher relationship with course entities in the existing application. By focusing on clear API endpoint definitions, robust data models, and comprehensive test strategies, we will enhance the educational management system while ensuring backward compatibility and functional reliability.

Existing Code Files:
- The existing code from the previous sprint will be updated to reflect these changes without full replacements, ensuring efficient integration of new functionalities.