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
# Implementation Plan: Student Management Application

## Technical Architecture

### 1. Architecture Overview
This implementation introduces a relationship between the Course and Teacher entities, enabling each Course to have a designated Teacher. The existing architecture using FastAPI for the RESTful API structure and SQLAlchemy as the ORM will continue to be leveraged, ensuring maintainability and ease of integration.

### 2. Technology Stack
- **Programming Language**: Python
- **Web Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Docker**: For containerization
- **Testing Framework**: Pytest
- **Migration Tool**: Alembic

---

## Module Design

### 1. Module Responsibilities
- **Teacher Module**: Manages Teacher-related functions (creating, retrieving, updating, and deleting Teacher data).
- **Course Module**: Extended to manage Teacher assignments, including methods for assigning, updating, and removing the Teacher associated with a Course.

### 2. Class/Function Design
**Course Class Updates:**
- Extend the existing Course data model to include a foreign key reference to the Teacher entity.

```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New relationship

    teacher = relationship("Teacher")  # Establish relationship with Teacher
```

### 3. API Endpoints
- **Assign Teacher to Course**:
  - **Method**: POST
  - **Endpoint**: `/courses/{course_id}/assign-teacher`
  - **Request Body**:
    ```json
    {
      "teacher_id": "1"
    }
    ```
  - **Response**:
    - 201 Created:
      ```json
      {
        "message": "Teacher assigned to Course successfully."
      }
      ```

- **Get Course Details**:
  - **Method**: GET
  - **Endpoint**: `/courses/{course_id}`
  - **Response**:
    - 200 OK:
      ```json
      {
        "id": 1,
        "name": "Mathematics 101",
        "teacher": {
          "id": 1,
          "name": "Jane Doe",
          "email": "jane.doe@example.com"
        }
      }
      ```

- **Update Teacher Assignment**:
  - **Method**: PUT
  - **Endpoint**: `/courses/{course_id}/update-teacher`
  - **Request Body**:
    ```json
    {
      "teacher_id": "2"
    }
    ```
  - **Response**:
    - 200 OK:
      ```json
      {
        "message": "Teacher assignment updated successfully."
      }
      ```

- **Remove Teacher from Course**:
  - **Method**: DELETE
  - **Endpoint**: `/courses/{course_id}/remove-teacher`
  - **Response**:
    - 204 No Content: on successful removal.

---

## Data Model

### 1. Database Schema
- **Course Table Update**:
  - New column `teacher_id` added as a foreign key referencing the `Teacher` entity.

### 2. Database Migration
- A new migration script will be created to add the `teacher_id` column to the Course table and ensure referential integrity without data loss.

```python
"""add_teacher_id_to_courses

Revision ID: xxx_revisions
Revises: previous_revision_id
Create Date: YYYY-MM-DD
"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    # Add teacher_id column to courses
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_courses_teachers', 'courses', 'teachers', ['teacher_id'], ['id'])

def downgrade():
    op.drop_constraint('fk_courses_teachers', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')
```

---

## Error Handling & Validation

### 1. Input Validation
- **Request validation** will ensure:
  - `teacher_id` is required in requests.
  - The specified `teacher_id` exists in the Teachers table.
  - Responses for unsuccessful validations:
    - 400 Bad Request for missing required fields or non-existent Teachers.

### 2. Error Responses
Error responses for invalid requests will follow this format:
```json
{
  "error": {
    "code": "E002",
    "message": "Teacher with ID '1' does not exist."
  }
}
```

---

## Testing Plan

### 1. Test Coverage
- Implement unit tests targeting at least 70% coverage for all Course-related functionalities involving Teacher assignments.
- Critical paths (assigning, updating, and removing Teachers from Courses) need to ensure 90%+ coverage.

### 2. Test Scenarios
- Test assigning a Teacher to a Course.
- Test retrieving Course details along with Teacher information.
- Test updating the assigned Teacher for a Course.
- Test removing a Teacher from a Course.

```python
def test_assign_teacher_to_course(create_teacher, create_course):
    response = client.post(f"/courses/{create_course['id']}/assign-teacher", json={"teacher_id": create_teacher["id"]})
    assert response.status_code == 201
    assert response.json() == {"message": "Teacher assigned to Course successfully."}

def test_get_course_details_with_teacher(create_teacher, create_course):
    client.post(f"/courses/{create_course['id']}/assign-teacher", json={"teacher_id": create_teacher["id"]})
    response = client.get(f"/courses/{create_course['id']}")
    assert response.status_code == 200
    assert response.json()["teacher"]["id"] == create_teacher["id"]
```

---

## Deployment Considerations

### 1. Containerization
- Update the Dockerfile to include any new dependencies or configurations required for the Course and Teacher relationship.

### 2. Documentation & Configuration
- Update the `README.md` to include new API endpoints and their usage related to teacher assignments on courses.
- Ensure that the API documentation reflects changes in data models and new functionalities.

---

## Conclusion

This implementation plan details the establishment of a relationship between Courses and Teachers in the Student Management Application. It highlights the necessary API endpoints, validation rules, and data integrity measures necessary for successful Teacher assignments. By maintaining compatibility with existing data models and documenting all changes, this plan aims to ensure a smooth integration process while enhancing the application's functionality.

Existing Code Files:
- Update `src/services/course_service.py` to implement the new API endpoints for managing Teacher assignments, integrating with the Teacher module.

Existing Code Example:
File: `src/services/course_service.py`
```python
# New API endpoint additions
@app.post("/courses/{course_id}/assign-teacher")
async def assign_teacher_to_course(course_id: int, request: AssignTeacherRequest):
    ...
```

Existing Code Files:
- Update `tests/services/test_course_service.py` to include tests for the new Teacher assignment functionality.

```python
# Sample test structure for new functionality
def test_assign_teacher_to_course(create_teacher, create_course):
    response = client.post(f"/courses/{create_course['id']}/assign-teacher", json={"teacher_id": create_teacher["id"]})
    assert response.status_code == 201
```
