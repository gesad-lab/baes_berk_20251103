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
The integration of the Course relationship within the Student Management Application will enhance the existing architecture while adhering to best practices in API design. We will continue to use FastAPI for the RESTful API structure and SQLAlchemy as the Object Relational Mapping (ORM) tool for data manipulation. The architecture accommodates many-to-many relationships, ensuring seamless tracking of student enrollments in multiple courses.

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
- **Student Module**: Update to maintain the list of Course IDs for each Student.
- **Course Module**: Newly integrated module managing course-related functionalities, including assignment to Students.
  
### 2. Class/Function Design
- **Updated Student Class**:
  Attributes:
  - `id`: Integer (auto-generated, primary key)
  - `name`: String (required)
  - `courses`: List of Course IDs (relation to Course entity)

```python
class Student(BaseModel):
    id: int
    name: str
    courses: List[int]
```

- **Updated CRUD Operations** for Student:
  - `assign_courses_to_student(student_id: int, course_ids: List[int]) -> List[str]`
  - `get_student_courses(student_id: int) -> List[Course]`
  - `remove_course_from_student(student_id: int, course_id: int) -> None`

### 3. API Endpoints
- **Assign Courses to Student**:
  - **Method**: POST
  - **Endpoint**: `/students/{id}/courses`
  - **Request Body**:
    ```json
    {
      "course_ids": ["course_id_1", "course_id_2"]
    }
    ```
  - **Response**:
    - 201 Created:
      ```json
      {
        "message": "Courses assigned successfully."
      }
      ```
      
- **Get Courses of Student**:
  - **Method**: GET
  - **Endpoint**: `/students/{id}/courses`
  - **Response**:
    - 200 OK:
      ```json
      [
        {
          "id": "course_id_1",
          "name": "Mathematics 101",
          "level": "Beginner"
        }
      ]
      ```
      
- **Remove Course from Student**:
  - **Method**: DELETE
  - **Endpoint**: `/students/{student_id}/courses/{course_id}`
  - **Response**:
    - 204 No Content: on successful removal.

---

## Data Model

### 1. Database Schema
- **Student Table Modification**:
  Now includes relation to courses. 
  - `id`: INTEGER PRIMARY KEY AUTOINCREMENT
  - `name`: TEXT NOT NULL
  - `courses`: TEXT (comma-separated Course IDs)

### 2. Database Migration
- A migration script will be written to modify the Student table and manage relationships.
- Alembic will manage migrations to ensure the integrity of existing data.

```python
"""Add_courses_to_student

Revision ID: xxx_revisions
Revises: previous_revision_id
Create Date: YYYY-MM-DD
"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    # Altering the 'student' table to add a 'courses' field
    op.add_column('student', sa.Column('courses', sa.Text(), nullable=True))

def downgrade():
    op.drop_column('student', 'courses')
```

---

## Error Handling & Validation

### 1. Input Validation
- **Request validation** will confirm:
  - Course IDs must exist and be valid integers.
- **Responses** for unsuccessful validations: 
  - 400 Bad Request for invalid student/courses input.

### 2. Error Responses
Error responses for invalid requests will follow this format:
```json
{
  "error": {
    "code": "E001",
    "message": "Invalid input: 'course_ids' must be present and valid."
  }
}
```

---

## Testing Plan

### 1. Test Coverage
- Implement unit tests targeting at least 70% coverage for all course-related features.
- Critical paths (assigning/removing courses) need to have 90%+ coverage.

### 2. Test Scenarios
- Test assigning courses using a valid Student ID and Course IDs.
- Test retrieving courses for a specific Student ID.
- Test removing a course from a Student ensures the Course ID is removed.

```python
def test_assign_courses_to_student():
    response = client.post("/students/1/courses", json={"course_ids": ["course_id_1", "course_id_2"]})
    assert response.status_code == 201
    assert response.json()["message"] == "Courses assigned successfully."
```

---

## Deployment Considerations

### 1. Containerization
- Use Docker for deployment, utilizing the existing Dockerfile unless new dependencies emerge.
  
### 2. Documentation & Configuration
- Update the `README.md` to include new functionalities for course assignment.
- Ensure new RESTful endpoints and the data model are documented conformance with existing API documentation standards.

---

## Conclusion

This implementation plan outlines the required adaptations necessary for linking Courses to Students in the Student Management Application. By clearly defining modules and endpoints, validating input, and ensuring existing functionality remains unaffected, the plan facilitates the seamless integration of Course relationships. All modifications maintain backward compatibility, ensuring a smooth transition for end-users while reinforcing scalability and maintainability in the application architecture.

Existing Code Files:
File: tests/services/test_student_service.py
```python
# Sample test structure
def test_remove_course_from_student():
    """Test successful course removal from student."""
    response = client.delete("/students/1/courses/course_id_1")
    assert response.status_code == 204  # No Content
```