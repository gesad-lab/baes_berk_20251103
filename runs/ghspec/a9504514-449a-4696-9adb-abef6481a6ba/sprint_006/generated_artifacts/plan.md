# Implementation Plan: Add Teacher Relationship to Course Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

### Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---

## Overview

This implementation plan outlines the technical specifications for establishing a relationship between the existing `Course` entity and the newly created `Teacher` entity within the educational management system. This relationship facilitates course management and accountability for teaching staff. The plan includes necessary updates to existing endpoints, database schema, and testing requirements to ensure a seamless integration of functionality while preserving current operations.

---

## I. Architecture Overview

### 1.1 Technology Stack
- **Language**: Python
- **Framework**: Flask
- **Database**: SQLite (using SQLAlchemy as the ORM)
- **API Testing Tool**: Postman or curl (for manual testing)
- **Development Environment**: Virtual environment using `venv`

### 1.2 Application Structure Update
```
teacher-management-app/
    ├── src/
    │   ├── app.py                # Main application entry point (updated for new routes)
    │   ├── models.py             # Database models (update to include course-teacher relationship)
    │   ├── services.py           # Business logic including course-teacher management
    │   ├── config.py             # Configuration settings
    │   └── database.py           # Database initialization (updates for migrations)
    ├── tests/
    │   ├── test_services.py      # Unit tests (updated to include course-teacher functionalities)
    ├── requirements.txt           # List of dependencies (no changes)
    ├── .env.example               # Environment variable example
    └── README.md                  # Documentation (update to reflect new feature)
```

---

## II. Module Boundaries and Responsibilities

### 2.1 Modules and Responsibilities
- `app.py`: 
  - Define new routes for assigning a teacher to a course and retrieving course details (e.g., `POST /courses/{course_id}/assign-teacher`, `GET /courses/{course_id}`).

- `models.py`: 
  - Update the `Course` model to include `teacher_id`, and define the relationship through SQLAlchemy.

- `services.py`: 
  - Implement business logic for assigning a teacher to a course and retrieving course details, including necessary validations for teacher existence.

- `database.py`: 
  - Manage database connections and migrations, including updating the `Course` table schema to include the `teacher_id` foreign key.

- `tests/test_services.py`: 
  - Extend unit tests to cover the assignment of teachers to courses and retrieval of course details.

---

## III. Data Models

### 3.1 Updates to Course Model

```python
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
import uuid

class Course(Base):
    __tablename__ = 'courses'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    teacher_id = Column(String, ForeignKey('teachers.id'), nullable=True)

    teacher = relationship("Teacher", backref="courses")

    def __init__(self, title, description, teacher_id=None):
        self.title = title
        self.description = description
        self.teacher_id = teacher_id
```

### 3.2 Migration Strategy

To include the `teacher_id` foreign key in the existing `courses` table, the following Alembic migration command will be executed:

```bash
alembic revision --autogenerate -m "Add teacher_id to courses table"
alembic upgrade head
```

The migration will ensure that the existing course data remains intact while adding the new relationship attribute.

---

## IV. API Contracts

### 4.1 Assign Teacher to Course Endpoint

- **Endpoint**: `POST /courses/{course_id}/assign-teacher`
- **Request Body**:
    ```json
    {
      "teacher_id": "123e4567-e89b-12d3-a456-426614174000"
    }
    ```
- **Response**: 
    - **Success (200 OK)**:
    ```json
    {
      "message": "Teacher assigned successfully.",
      "course": {
        "id": "course_id",
        "title": "Course Title",
        "description": "Course Description",
        "teacher": {
          "id": "123e4567-e89b-12d3-a456-426614174000",
          "name": "John Doe"
        }
      }
    }
    ```

    - **Error (400 Bad Request)**:
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Teacher does not exist."
      }
    }
    ```

### 4.2 Retrieve Course with Teacher Information Endpoint

- **Endpoint**: `GET /courses/{course_id}`
- **Response**:
  - **Success (200 OK)**:
    ```json
    {
      "id": "course_id",
      "title": "Course Title",
      "description": "Course Description",
      "teacher": {
        "id": "123e4567-e89b-12d3-a456-426614174000",
        "name": "John Doe"
      }
    }
    ```

---

## V. Implementation Approach

### 5.1 Steps for Development

1. Update the `Course` model in `models.py` to include `teacher_id` and define the relationship with the `Teacher` entity.
  
2. Generate and apply a migration script to update the `courses` table schema in the database.

3. Implement the logic for the `POST /courses/{course_id}/assign-teacher` and `GET /courses/{course_id}` endpoints in `services.py`.

4. Update `app.py` to handle routing for the new course-teacher relationship endpoints.

5. Extend the tests in `tests/test_services.py` to cover:
   - Successful assignment of a teacher to a course.
   - Retrieving a course with assigned teacher details.
   - Validation for nonexistent teacher assignments.

6. Conduct comprehensive manual testing with tools like Postman to validate the functionality.

---

## VI. Validation and Testing

### 6.1 Automated Testing Strategy

- Ensure at least **70% overall test coverage** on the business logic related to course-teacher management.
- Implement unit and integration tests covering all newly created functionalities.

### 6.2 Testing Scenarios

1. **POST /courses/{course_id}/assign-teacher**
   - Test with valid `teacher_id` -> Expect success response confirming the assignment.
   - Test with invalid `teacher_id` -> Expect error indicating the teacher does not exist.

2. **GET /courses/{course_id}**
   - Test with valid `course_id` -> Confirm the returned data includes teacher details correctly.
   - Test with nonexistent `course_id` -> Expect error indicating the course does not exist.

---

## VII. Error Handling and Validation

### 7.1 Input Validation

- Validate incoming requests to ensure required fields (like `teacher_id`) are present and correct.
- Use SQLAlchemy and custom validations to confirm the existence of the specified teacher before assignment.

### 7.2 Error Messages

- Standardize error responses as specified in the API contract section.

---

## VIII. Security Considerations

- Ensure user inputs are sanitized to avoid SQL injection vulnerabilities.
- Log errors and validation feedback appropriately without exposing sensitive information.

---

## IX. Deployment Considerations

Ensure that migrations for adding the `teacher_id` field in the `courses` table are applied successfully during the deployment process, verifying there are no adverse effects on existing data.

---

## X. Conclusion

This implementation plan provides a clear path for adding a teacher relationship to the course entity in the educational management system. It emphasizes robust API design and includes validation and error handling mechanisms to ensure system integrity while maintaining backward compatibility. By adhering to this plan, the application can effectively enhance its capabilities in managing course assignments and associated teaching resources.

Existing Code Files:
File: tests/test_services.py
```python
import unittest
from src.services import create_course, get_course_by_id, assign_teacher_to_course
from src.models import Course, Teacher
from src.database import db, init_db

class TestCourseServices(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the testing database and create necessary tables."""
        init_db()
        cls.app_context = db.app.app_context()
        cls.app_context.push()
        
    def test_assign_teacher_to_course(self):
        # Create a course and a teacher for testing
        course = create_course("Course Title", "Course Description")
        teacher = Teacher(name="John Doe", email="john.doe@example.com")
        db.session.add(teacher)
        db.session.commit()
        
        # Assign the teacher to the course
        response = assign_teacher_to_course(course.id, teacher.id)
        self.assertEqual(response.status_code, 200)
        self.assertIn('teacher', response.json)
        
    def test_get_course_details(self):
        # Assume a course has been created and teacher assigned
        course = get_course_by_id(course_id)
        self.assertIn('teacher', course)

    @classmethod
    def tearDownClass(cls):
        """Clean up the testing database."""
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()
```