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
# Implementation Plan: Student Management Web Application

## I. Architecture Overview

### 1.1 Components
- **API Layer**: A RESTful API to manage teacher assignments within the existing student management system, responding in JSON format.
- **Database Layer**: SQLite will be utilized to manage Course and Teacher records, and ensure referential integrity.
- **Business Logic Layer**: Handle the validation and processing logic concerning teacher-course assignments.

### 1.2 Technology Stack
- **Programming Language**: Python (version 3.11 or higher)
- **Web Framework**: FastAPI (for ease of API development)
- **Database**: SQLite (for lightweight and reliable storage)
- **ORM**: SQLAlchemy (for managing database interactions)
- **Testing Framework**: pytest (to ensure robust unit and integration tests)
- **Environment Management**: Poetry (for managing dependencies)
- **Migration Tool**: Alembic (to handle database schema updates)

---

## II. Module Boundaries and Responsibilities

### 2.1 API Layer
- **Module**: `app/api/course.py`
  - **Responsibilities**:
    - Handle HTTP requests for assigning teachers to courses and retrieving course information (`PATCH /courses/{id}/assign-teacher`, `GET /courses/{id}`).
    - Validate incoming requests and format JSON responses.

### 2.2 Database Layer
- **Module**: `app/models/course.py`
  - **Responsibilities**:
    - Update the `Course` entity to include a foreign key relationship with the `Teacher` entity.

### 2.3 Business Logic Layer
- **Module**: `app/services/course_service.py`
  - **Responsibilities**:
    - Handle the logic of assigning teachers to courses.
    - Validate course and teacher existence before the assignment and manage data interactions.

---

## III. Data Models and API Contracts

### 3.1 Data Model
#### Course
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New Foreign Key

    teacher = relationship("Teacher", back_populates="courses")  # Relationship with Teacher

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    courses = relationship("Course", back_populates="teacher")
```

### 3.2 API Contract
#### Assign Teacher to Course
- **Endpoint**: `PATCH /courses/{id}/assign-teacher`
- **Request Body**:
  ```json
  {
      "teacher_id": "1"
  }
  ```
- **Responses**:
  - **200 OK**:
    ```json
    {
        "message": "Teacher assigned to course successfully."
    }
    ```
  - **404 Not Found (Course)**:
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Course not found."
        }
    }
    ```
  - **404 Not Found (Teacher)**:
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Teacher not found."
        }
    }
    ```

#### Retrieve Course with Teacher Details
- **Endpoint**: `GET /courses/{id}`
- **Responses**:
  - **200 OK**:
    ```json
    {
        "id": 1,
        "name": "Biology 101",
        "level": "Beginner",
        "teacher": {
            "name": "Jane Doe",
            "email": "jane@example.com"
        }
    }
    ```
  - **404 Not Found**:
    ```json
    {
        "error": {
            "code": "E003",
            "message": "Course not found."
        }
    }
    ```

---

## IV. Implementation Approach

### 4.1 Initial Setup
- **Update Course Module**:
  - Modify `app/models/course.py` to include the new `teacher_id` field and set up relationships with the `Teacher` entity.
  - Create `app/api/course.py` for handling teacher assignment and course retrieval API endpoints.

### 4.2 Database Migration
1. **Using Alembic for migrations**:
   - Ensure Alembic is installed via Poetry:
     ```bash
     poetry add alembic
     ```
   - Generate a migration script to add a foreign key to the `courses` table and create the `teachers` table:
     ```bash
     alembic revision --autogenerate -m "Add Teacher relationship to Course"
     ```
   - The migration script must include:
     ```python
     def upgrade():
         op.add_column('courses', sa.Column('teacher_id', sa.Integer(), sa.ForeignKey('teachers.id'), nullable=True))
         op.create_table(
             'teachers',
             sa.Column('id', sa.Integer(), primary_key=True),
             sa.Column('name', sa.String(), nullable=False),
             sa.Column('email', sa.String(), nullable=False)
         )

     def downgrade():
         op.drop_column('courses', 'teacher_id')
         op.drop_table('teachers')
     ```

### 4.3 Implementing API Endpoints
- **PATCH /courses/{id}/assign-teacher**:
  - Implement logic in `app/api/course.py` to manage teacher assignment, including checks for course and teacher existence.
  
- **GET /courses/{id}**:
  - Implement retrieval logic that returns the course details along with teacher information.

### 4.4 Input Validation and Response Generation
- Input validation will be handled within `app/services/course_service.py` to ensure correct assignment of teachers to courses.
- Format JSON responses appropriately based on the outcomes.

### 4.5 Testing
- Write test cases in `tests/test_course.py`:
  - Example tests:
    - Test successful assignment of a teacher to a course.
    - Test retrieving a course by ID.
    - Test error handling for assigning to non-existing course or teacher.

Example test file structure:
```python
import pytest

def test_assign_teacher_to_course(client):
    response = client.patch("/courses/1/assign-teacher", json={"teacher_id": "1"})
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher assigned to course successfully."}

def test_assign_teacher_to_non_existing_course(client):
    response = client.patch("/courses/999/assign-teacher", json={"teacher_id": "1"})
    assert response.status_code == 404
    assert response.json() == {
        "error": {
            "code": "E001",
            "message": "Course not found."
        }
    }

def test_retrieve_course_with_teacher(client):
    response = client.get("/courses/1")
    assert response.status_code == 200
    assert "teacher" in response.json()

def test_retrieve_non_existing_course(client):
    response = client.get("/courses/999")
    assert response.status_code == 404
    assert response.json() == {
        "error": {
            "code": "E003",
            "message": "Course not found."
        }
    }
```

---

## V. Security Considerations
- Implement input validation to guard against injection attacks.
- Ensure sensitive data is not logged and error responses do not expose internal details.

---

## VI. Deployment Considerations
- Ensure database migrations are executed automatically at application startup to integrate the new relationships without losing existing data.

---

## VII. Development Workflow
1. Implement the updates to the Course model and API endpoints in the respective modules.
2. Run database migrations to adjust table structures.
3. Execute unit and integration tests to verify that all functionality meets specifications.
4. Update README.md with guidelines on how to interact with the new endpoints.

---

## VIII. Monitoring and Logging
- Implement structured logging within the existing logging framework to capture teacher assignment events and possible errors.

---

## IX. Future Considerations
- Future iterations could include user interface enhancements to allow non-technical users to manage teacher assignments more effectively.
- Integrate authentication and authorization for teacher assignments to enhance security and provide role-specific access control. 

This implementation plan outlines the steps necessary to establish a teacher relationship within the course entity, ensuring coherence with the existing functionality of the student management system while preserving data integrity.