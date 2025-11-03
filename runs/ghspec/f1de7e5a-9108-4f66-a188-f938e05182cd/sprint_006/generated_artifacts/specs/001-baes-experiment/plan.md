# Implementation Plan: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---

## Version
1.1.0  

## Overview
This implementation plan details the approach for establishing a relationship between the `Course` and `Teacher` entities within the educational management system. The feature allows each course to have an assigned teacher, enhancing course organization and administration. It covers modifications to the database schema, new API endpoints for course management, data models, input validation, error handling, and testing strategies.

## Architecture
The architecture will extend the existing RESTful API structure to integrate the new course-teacher relationship. The technology stack remains consistent with previous iterations:
- **Framework**: FastAPI (Python)
- **Database**: SQLite
- **ORM**: SQLAlchemy for database interaction
- **Data Validation**: Pydantic for request validation

### Module Boundaries
1. **API Module**: Extends current course functionality to include assigning teachers to courses.
2. **Service Module**: Implements business logic for assigning a teacher to a course and retrieving course details.
3. **Data Access Module**: Manages database operations related to courses and teachers.
4. **Model Module**: Defines the course model and updates to include the teacher relationship.

## Technology Stack
- **Programming Language**: Python 3.11+
- **Web Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Data Validation**: Pydantic
- **Testing Framework**: pytest
- **Dependency Management**: pip, with a `requirements.txt` file for lockable dependency installations.

## Data Models
### Course Model Update
In `models.py`, the `Course` model needs to be updated to include the new `teacher_id` field:

```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=True)

    teacher = relationship("Teacher", back_populates="courses")

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    
    courses = relationship("Course", back_populates="teacher")
```

## API Contracts
### Assign Teacher to Course Endpoint
- **Endpoint**: `/courses/{courseId}/assign-teacher`
- **Method**: POST
- **Request Body**:
    ```json
    {
        "teacherId": "<integer>"
    }
    ```
- **Response**:
    - **Status Code**: 200 (OK)
    - **Body**:
    ```json
    {
        "message": "Teacher assigned successfully."
    }
    ```

### Retrieve Course with Teacher Information Endpoint
- **Endpoint**: `/courses/{courseId}`
- **Method**: GET
- **Response**:
    - **Status Code**: 200 (OK)
    - **Body**:
    ```json
    {
        "id": "<integer>",
        "name": "<string>",
        "teacher": {
            "id": "<integer>",
            "name": "<string>"
        }
    }
    ```

## Input Validation
- Validate that `teacherId` is provided when assigning a teacher to a course:
    - Return status code 400 if `teacherId` is missing.
    - Return status code 404 if `teacherId` does not correspond to an existing teacher.
    - Error Response:
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Teacher ID is required."
        }
    }
    ```

## Database Migration Management
- Create a migration script to modify the `courses` table to add the `teacher_id` column using Alembic:

```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'), nullable=True))

def downgrade():
    op.drop_column('courses', 'teacher_id')
```

## Testing Strategy
1. **Unit Tests**: 
   - Test the functionality of assigning a teacher to a course, ensuring that the correct database record is made.
   - Validate error handling when a non-existent teacher ID is provided.

2. **Integration Tests**:
   - Confirm end-to-end flows for the `/courses/{courseId}/assign-teacher` and `/courses/{courseId}` endpoints, ensuring proper database interactions and valid responses.

3. **Contract Tests**:
   - Utilize testing tools to confirm API responses match the defined schemas.

Maintain minimum test coverage target of 70% for business logic and at least 90% for critical paths (e.g., teacher assignment to course).

## Error Handling
- Implement centralized error handling within FastAPI to deliver standardized error responses while logging relevant information without leaking sensitive data.

## Scalability Considerations
- Adhere to a stateless service architecture.
- Maintain clearly defined module boundaries for easier feature expansion in subsequent iterations.

## Security Considerations
- Utilize environment variables for sensitive configurations and avoid hardcoding secrets in the codebase.
- Rigorously validate all user inputs to prevent SQL injection and ensure compliance with security best practices.

## Deployment Plan
- Update the FastAPI application to include new endpoints and functionality for teacher assignment.
- Run the database migration script to ensure the schema is updated accordingly.
- Refresh deployment documentation with information on the new API functionalities.

## Documentation
- Update `README.md` with:
  - Method specifications for assigning teachers to courses.
  - Guidelines for invoking new endpoints.
  - Updated instructions for running unit and integration tests.
  
## Conclusion
This implementation plan provides a comprehensive strategy for adding a teacher relationship to courses in the educational management application, preserving existing functionalities while facilitating future extensions.

### Existing Code Files Modifications Needed:
- **models.py**
  - Update the `Course` model to include `teacher_id` as a foreign key and define the relationship with `Teacher`.

- **api.py**
  - Implement the `/courses/{courseId}/assign-teacher` endpoint for assigning a teacher to a course.
  - Implement the `/courses/{courseId}` endpoint to retrieve course and teacher details.

- **database_migrations.py**
  - Create a migration file to adjust the `courses` table to accommodate the new `teacher_id` foreign key.

### Tests Code Files Modifications Needed:
- **tests/test_api.py**
  - Add test cases for the new assignment functionality, verifying successful assignments and error handling.

- **tests/test_integration.py**
  - Include integration tests to verify that the new endpoints function as expected for assignments and retrieval of course details.

This meticulous plan ensures that the existing infrastructures remain intact while implementing a vital new feature for managing educators within the educational system.