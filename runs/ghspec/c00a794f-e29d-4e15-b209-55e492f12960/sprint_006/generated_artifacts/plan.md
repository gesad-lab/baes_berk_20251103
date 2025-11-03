# Implementation Plan: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Course Relationship to Student Entity

---

## Version
**Version**: 1.1.0  
**Date**: 2023-10-10

---

## 1. Project Overview
The purpose of this feature is to establish a relationship between the Course and Teacher entities in the existing system. This will allow each Course to have an assigned Teacher, enhancing course management functionality by clearly defining course responsibilities. The feature aims to improve reporting, tracking, and overall organization of course assignments.

---

## 2. Technical Architecture

### 2.1 Overall Architecture
- **Architecture Pattern**: Continue leveraging a microservices architecture.
- **Tech Stack**:
  - **Web Framework**: FastAPI (asynchronous capabilities)
  - **Database**: SQLite
  - **ORM**: SQLAlchemy
  - **Testing**: pytest
  - **Dependency Management**: Poetry
  - **API Documentation**: OpenAPI (via FastAPI)

### 2.2 Module Boundaries
- **Course Service Module**:
  - Extend this module to include management capabilities for the Teacher-Course relationship.
  
- **Teacher Service Module**:
  - Existing functionality remains unaffected.

---

## 3. Implementation Approach

### 3.1 Directory Structure
```plaintext
teacher_entity_app/
│
├── src/
│   ├── __init__.py
│   ├── main.py                     # Entry point for the application
│   ├── models.py                   # Database models (SQLAlchemy)
│   ├── schemas.py                  # Data validation schemas (Pydantic)
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── teacher_routes.py        # API routes for teacher endpoints (remains unchanged)
│   │   ├── student_routes.py        # API routes for student endpoints (remains unchanged)
│   │   └── course_routes.py         # Updated API routes for course endpoints for teacher assignment
│   └── database.py                  # Database connection and initialization
│
├── tests/
│   ├── __init__.py
│   ├── test_teacher.py              # Test cases for teacher features (remains unchanged)
│   ├── test_student.py              # Test cases for student features (remains unchanged)
│   └── test_course.py               # Test cases updated to validate course and teacher relationships
│
├── config/
│   └── .env                         # Environment variables
│
├── requirements.txt                 # Dependencies file
└── README.md                        # Project documentation
```

### 3.2 Database Models
#### Update Course Model
Modify the existing `Course` model to include a `teacher_id` foreign key, establishing the relationship to the `Teacher`.

```python
# models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    teacher = relationship("Teacher", back_populates="courses")

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    courses = relationship("Course", back_populates="teacher")
```

### 3.3 API Endpoints
- **POST /courses/{course_id}/assign_teacher**
  - **Request**: JSON body with `teacher_id`.
  - **Response**: JSON indicating success or failure.

- **GET /courses/{course_id}**
  - **Response**: JSON containing course details, including teacher information.
  
### 3.4 Application Startup
Implement database migration to add the `teacher_id` column to the `courses` table. Ensure existing data integrity is maintained.

### 3.5 Error Handling
- Implement validation for course-related API calls to ensure a teacher is specified when assigning.

```json
{
  "error": {
    "code": "E001",
    "message": "A teacher must be selected."
  }
}
```

---

## 4. Testing Approach

### 4.1 Test Coverage
Maintain a minimum of 70% test coverage, with 90% coverage for critical paths involving course and teacher assignments.

### 4.2 Test Types
- **Unit Tests**: Validate methods for the course service, especially those modifying course-teacher relationships.
- **Integration Tests**: Ensure the entire process of assigning a teacher to a course works as intended with the database.
- **Contract Tests**: Verify API response structures for success and error cases.

### 4.3 Testing Structure
Add new tests to `test_course.py` to cover the newly established teacher-course relationships.

```python
# tests/test_course.py
import pytest
from fastapi import status
from src.models import Course, Teacher
from src.database import SessionLocal

@pytest.fixture
def client():
    from fastapi.testclient import TestClient
    from src.main import app
    return TestClient(app)

def test_assign_teacher_to_course(client):
    # Assuming a course with ID 1 exists and a teacher with ID 1 exists
    response = client.post("/courses/1/assign_teacher", json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher assigned successfully."}

def test_assign_teacher_without_teacher(client):
    response = client.post("/courses/1/assign_teacher", json={})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "A teacher must be selected."}}

def test_get_course_with_teacher(client):
    response = client.get("/courses/1")
    assert response.status_code == 200
    assert "teacher" in response.json()
```

---

## 5. Error Handling & Validation
- Validate incoming requests for teacher assignments. Return structured JSON error responses when inputs are invalid.

---

## 6. API Design Considerations
Ensure all endpoints adhere to RESTful standards, maintaining structured error responses and effective use of HTTP status codes.

---

## 7. Database Migration Strategy
Utilize Alembic to manage any changes in the `courses` table schema, ensuring `teacher_id` is added while preserving existing course data.

### Migration Script Example
```python
# migrations/versions/xxxx_add_teacher_id_to_courses.py
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_teacher_course', 'courses', 'teachers', ['teacher_id'], ['id'])

def downgrade():
    op.drop_constraint('fk_teacher_course', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')
```

---

## 8. Logging & Monitoring
Implement logging for significant operations involving teacher and course assignments. Ensure that all operations are well-documented for easier monitoring.

---

## 9. Documentation
Update `README.md` to include new API endpoint documentation for assigning teachers to courses and retrieving course details with teacher information.

---

## 10. Success Criteria Check
1. **Teacher Assignment**: Admins can assign teachers to courses without errors.
2. **Retrieval**: The API returns accurate course details with teacher information.
3. **Error Handling**: Appropriate error messages are returned for invalid assignments.
4. **Data Integrity**: The database migration should succeed without impacting existing course data.
5. **Backward Compatibility**: Existing features remain intact and operational.

---

This implementation plan outlines the critical steps to establish a relationship between the Course and Teacher entities, maintaining existing structures while enhancing the academic management capabilities. The plan emphasizes resilience, thorough testing, and adherence to previous coding standards and practices.