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

## I. Architecture Overview

### 1.1 Architecture Style
- **Microservices**: The application will continue to utilize FastAPI to build RESTful services.
- **Layered Architecture**: The existing architecture will be supplemented with capabilities to manage the Course-Teacher relationship:
  - **Presentation Layer**: Implements the API endpoints for managing course-teacher relationships.
  - **Service Layer**: Contains business logic for teacher management relative to courses.
  - **Data Access Layer (DAL)**: Manages interactions with the updated Course table in the database.

### 1.2 Component Diagram
```plaintext
+--------------------+          +------------------+          +----------------+
|    Client (Web)    | <-----> |   FastAPI App    | <-----> | SQLite Database |
+--------------------+          +------------------+          +----------------+
```

## II. Technology Stack

### 2.1 Backend Framework
- **FastAPI**: The application will continue to use FastAPI for managing APIs.

### 2.2 Database
- **SQLite**: Continuation of using SQLite for lightweight database management.

### 2.3 ORM
- **SQLAlchemy**: Utilized to interact with the Course and Teacher data model and manage database interactions.

### 2.4 Testing Framework
- **pytest**: Will be used for creating unit and integration tests for the added functionality.

### 2.5 Dependency Management
- **poetry**: To manage dependencies and ensure consistent development environments.

## III. Module Design

### 3.1 Module Structure
The existing application structure will be updated to include new endpoints and logic for handling Course-Teacher relationships:

```
student_app/
├── src/
│   ├── main.py
│   ├── models/
│   │   ├── student.py
│   │   ├── teacher.py
│   │   ├── course.py          # Updated model for Course to include teacher_id
│   ├── db/
│   │   ├── database.py
│   │   └── migrations/
│   ├── routes/
│   │   ├── student_routes.py
│   │   ├── teacher_routes.py
│   │   └── course_routes.py    # New routes for managing Course-Teacher relationship
│   ├── services/
│   │   ├── student_service.py
│   │   ├── teacher_service.py
│   │   └── course_service.py    # New service logic for Course-Teacher relationship
│   ├── schemas/
│   │   ├── student_schemas.py
│   │   ├── teacher_schemas.py
│   │   └── course_schemas.py     # New schemas for Course-Teacher associations
└── tests/
    ├── test_student.py
    ├── test_routes.py
    ├── test_teacher.py
    └── test_course.py             # New tests for Course-Teacher associations
```

### 3.2 Module Responsibilities
- **`main.py`**: Integrate the new course routes with teacher relationships.
- **`models/course.py`**: Update the Course model to include the `teacher_id` foreign key field.
- **`routes/course_routes.py`**: Implements API endpoints for managing the Course-Teacher relationships.
- **`services/course_service.py`**: Contains business logic for associating and managing teachers within courses.
- **`schemas/course_schemas.py`**: Defines Pydantic models for input/output related to Course-Teacher operations.
- **`tests/test_course.py`**: Contains tests for the API endpoints and logic applicable to Course-Teacher functionalities.

## IV. API Design

### 4.1 Endpoints
1. **Associate Teacher to Course**
   - **Method**: POST
   - **Endpoint**: `/courses/{course_id}/teachers`
   - **Request Body**: `{"teacher_id": 1}`
   - **Response**: `200 OK` with the updated course details including teacher information.

2. **Retrieve Course with Teacher Details**
   - **Method**: GET
   - **Endpoint**: `/courses/{course_id}`
   - **Response**: `200 OK` with the course details including associated Teacher or `404 Not Found` if the course does not exist.

3. **Update Teacher for Course**
   - **Method**: PUT or PATCH
   - **Endpoint**: `/courses/{course_id}/teachers`
   - **Request Body**: `{"teacher_id": 2}`
   - **Response**: `200 OK` with the updated course details including the newly associated teacher.

4. **Remove Teacher from Course**
   - **Method**: DELETE
   - **Endpoint**: `/courses/{course_id}/teachers`
   - **Response**: `200 OK` with confirmation of removal or `404 Not Found` if the course does not exist.

### 4.2 JSON Response Format
All API responses will adhere to the following structure:
```json
{
  "data": { /* updated course data */ },
  "error": { /* error details if any */ }
}
```

## V. Data Model

### 5.1 Course Model Schema Update
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))  # New Foreign Key
    teacher = relationship("Teacher", back_populates="courses")  # Bi-directional relationship

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    courses = relationship("Course", back_populates="teacher")  # Bi-directional relationship
```

### 5.2 Database Migration Strategy
- **Migration Strategy**: Use Alembic for schema migrations.
  - Migrations will add the `teacher_id` column to the existing Course table while preserving existing data.

```python
# Alembic migration to add the teacher_id column to courses table
def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))

def downgrade():
    op.drop_column('courses', 'teacher_id')
```

## VI. Testing Plan

### 6.1 Test Coverage
- Aim for at least 70% coverage for the new features.
- Critical paths (associate, retrieve, update, and remove teacher from course operations) should maintain 90% coverage.

### 6.2 Test Types
- Unit tests for course service methods and integration tests for the Course-Teacher API endpoints.

## VII. Security Considerations

- API inputs must be validated for the expected format (e.g., proper integer values for `teacher_id`).
- All communications should utilize HTTPS for secure data transfer.
- Proper sanitation of inputs to avoid injection and similar attacks.

## VIII. Deployment Considerations

### 8.1 Production Readiness
- Ensure that the application starts successfully and initializes all required tables.
- Implement a health check endpoint for monitoring the application's health status.

### 8.2 Backward Compatibility
- API endpoints for existing operations will remain unchanged, allowing current students and courses to remain unaffected.

## IX. Logging & Monitoring

- Include structured logging to capture the context of Course-Teacher requests, including request IDs and error details.

## X. Fail-Fast Philosophy

- Validate inputs at the beginning of each request to catch errors early.
- All exceptions should be logged with sufficient context for easier debugging.

## XI. Milestones & Timeline

### 11.1 Project Milestones
- **Week 1**: Define new models (Course updates) and update module structure.
- **Week 2**: Implement endpoints for associating, retrieving, updating, and removing teachers from courses.
- **Week 3**: Develop and run tests to ensure functionality and coverage.
- **Week 4**: Code review, finalize documentation, and prepare for deployment.

## XII. Conclusion
This implementation plan outlines the necessary steps to integrate the Teacher relationship into the existing Course entity within the student management application. By following the proposed architecture and guidelines, we will enhance the application's capabilities while maintaining performance, scalability, and maintainability.

### Modifications Needed
- **`main.py`**: Update to import and include `course_routes`.
- **Existing code updates**: Modify `models/course.py` to include the `teacher_id` field and relationships.
- **Existing tests**: New tests will be added in `test_course.py` to test the newly created functionalities. Ensure shared database fixtures accommodate for both Course and Teacher data.

```python
# Sample addition in tests/test_course.py
def test_associate_teacher_to_course(test_client):
    response = test_client.post("/courses/1/teachers", json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json()["data"]["teacher_id"] == 1
    ...
```

Existing Code Files:
File: tests/test_course.py
```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models.course import Course
from src.db.database import get_db
from sqlalchemy.orm import Session

@pytest.fixture(scope="module")
def test_client():
    client = TestClient(app)
    yield client

@pytest.fixture(scope="module")
def test_db():
    # Setup code for initializing the database
    # Ideally, this would include population with dummy data for testing...
```

In this implementation plan, we have outlined necessary modules, their responsibilities, API designs, and testing plans according to existing technology stacks and structures while providing backward compatibility. The focus on security, logging, and deployment readiness reinforces a quality implementation that meets the specified requirements.