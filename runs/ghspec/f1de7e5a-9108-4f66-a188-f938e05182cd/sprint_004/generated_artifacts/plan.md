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

## Version
1.1.0  

## Overview
This implementation plan outlines the technical approach for integrating a relationship between the `Student` entity and the newly introduced `Course` entity within the Student Management Web Application. This feature enables students to enroll in various courses, significantly enhancing their educational engagement and administrative oversight. The plan discusses modifications to the database schema, API endpoints for enrollment management, data models, and testing strategies necessary for successful implementation.

## Architecture
The architecture will adhere to the existing RESTful API structure, integrating the new features seamlessly. The technical stack remains consistent with prior iterations:
- **Framework**: FastAPI (Python)
- **Database**: SQLite
- **ORM**: SQLAlchemy for database interaction
- **Data Validation**: Pydantic for request validation

### Module Boundaries
1. **API Module**: Extends current functionality to manage enrollment requests and course retrievals.
2. **Service Module**: Contains business logic for handling enrollment operations.
3. **Data Access Module**: Facilitates database operations related to student-course relationships.
4. **Model Module**: Defines the `StudentCourses` junction model for associating students with courses.

## Technology Stack
- **Programming Language**: Python 3.11+
- **Web Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Data Validation**: Pydantic
- **Testing Framework**: pytest
- **Dependency Management**: pip, with a `requirements.txt` file for lockable dependency installations.

## Data Models
### StudentCourses Model
Using SQLAlchemy to define the new `student_courses` junction model for the many-to-many relationship:
```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class StudentCourses(Base):
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")
```

### Modifications to Student and Course Models
In the `Student` model, add a relationship to the `Course` model:
```python
class Student(Base):
    # Existing fields...

    courses = relationship("StudentCourses", back_populates="student")
```

In the `Course` model, similar changes should be made:
```python
class Course(Base):
    # Existing fields...

    students = relationship("StudentCourses", back_populates="course")
```

## API Contracts
### Enroll Student in Course Endpoint
- **Endpoint**: `/students/{student_id}/enroll`
- **Method**: POST
- **Request Body**:
    ```json
    {
        "course_id": "<integer>"
    }
    ```
- **Response**:
    - **Status Code**: 201 (Created)
    - **Body**:
    ```json
    {
        "student_id": "<integer>",
        "course_id": "<integer>"
    }
    ```

### Retrieve Courses for Student Endpoint
- **Endpoint**: `/students/{student_id}/courses`
- **Method**: GET
- **Response**:
    - **Status Code**: 200 (OK)
    - **Body**:
    ```json
    [
        {
            "course_id": "<integer>",
            "name": "Intro to Programming",
            "level": "Beginner"
        },
        {
            "course_id": "<integer>",
            "name": "Advanced Algorithms",
            "level": "Advanced"
        }
    ]
    ```

## Input Validation
- Validate that `course_id` corresponds to an existing course:
    - Return status code 400 if the course does not exist.
    - Error Response:
    ```json
    {
        "error": {
            "code": "E002",
            "message": "The specified course does not exist."
        }
    }
    ```

## Database Migration Management
- Create a migration script to introduce the `student_courses` table:
```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True),
    )

def downgrade():
    op.drop_table('student_courses')
```

## Testing Strategy
1. **Unit Tests**: 
   - Test the `enroll` functionality for students, ensuring correct associations are created in the database.
   - Validate error responses when invalid course IDs are provided.
   
2. **Integration Tests**:
   - Comprehensive flow tests for both enrollment and course retrieval endpoints, confirming correct interactions with the database.

3. **Contract Tests**:
   - Validate API responses against defined schemas using tools like `pytest`.

Maintain the minimum test coverage target of 70% for business logic and at least 90% for critical paths (e.g., enrollment and retrieval).

## Error Handling
- Implement global error handling within FastAPI to standardize error responses and ensure critical information is logged without exposing sensitive details.

## Scalability Considerations
- Continue leveraging a stateless approach.
- Ensure that module boundaries remain clear, allowing for enhancements and new features without impacting existing functionalities.

## Security Considerations
- Store sensitive configurations as environment variables to avoid hardcoding.
- Rigorously validate all user inputs to guard against vulnerabilities like SQL injection.

## Deployment Plan
- Set up the FastAPI application to include new endpoints.
- Ensure the database migration script is run to reflect changes.
- Update the deployment documentation to include instructions for testing new functionalities.

## Documentation
- Update the `README.md` with:
  - The new `StudentCourses` model specifications.
  - Instructions for using the newly established API endpoints.
  - Guidelines for running unit and integration tests.

## Conclusion
This implementation plan provides a structured approach to creating a relationship between `Student` and `Course` entities within the application, ensuring backward compatibility, maintaining data integrity, and safeguarding best practices in software development.

### Existing Code Files Modifications Needed:
- **models.py**
  - Add code for the `StudentCourses` model.
  - Update the `Student` and `Course` classes with relationship attributes.

- **api.py**
  - Implement the `/students/{student_id}/enroll` and `/students/{student_id}/courses` endpoints.

- **database_migrations.py**
  - Create a migration file to set up the `student_courses` junction table.

### Tests Code Files Modifications Needed:
- **tests/test_api.py**
  - Add test cases for enrolling a student in a course and retrieving courses for a student.

- **tests/test_integration.py**
  - Include integration tests for the enrollment and retrieval functionalities.

This structured approach guarantees that existing functionalities remain intact while enhancing the application's capabilities in a cohesive manner.