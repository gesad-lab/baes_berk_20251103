# Implementation Plan: Add Course Relationship to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

### Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

### Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

### Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## I. Architecture Overview
The architecture for the Student Management Web Application remains predominantly unchanged. The addition of the Course relationship involves modifying existing data models and adding corresponding API endpoints. The architecture consists of the following components:

1. **FastAPI Server**: Continues to manage API requests and responses for both Student and Course entities.
2. **SQLite Database**: The schema will be updated to accommodate a many-to-many relationship between Student and Course entities via a join table while ensuring existing records remain unaffected.
3. **Data Models**: Update to include a relationship in the Student model to reference the Course model.
4. **API Endpoints**: Addition of new endpoints for associating and retrieving courses for students.
5. **Automatic Schema Creation**: Updates on application startup will handle the new relationship schema migrations.

## II. Technology Stack
- **Backend Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy (for database interaction)
- **ASGI Server**: Uvicorn (for serving the FastAPI app)
- **Dependency Management**: Poetry or Pip for package handling
- **Testing Framework**: pytest for unit and integration tests

## III. Module Boundaries and Responsibilities
- **Main Application Module**: Entry point for the FastAPI application, managing initial imports and route definitions.
- **Database Module**: Additions to manage connections, schema changes, and migrations for both Student and Course entities.
- **Models Module**: Updates to include a new join table for Course-Student relationships while maintaining existing model integrity.
- **API Module**: New routes for Course associations and validation.
- **Errors Module**: Centralized error handling to include responses for course-related association validations.

## IV. Data Models and API Contracts

### Data Model Updates
```python
# In models/student.py
class Student(Base):
    __tablename__ = 'students'
    
    # Existing fields...
    courses = relationship("Course", secondary="student_courses", back_populates="students")

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # Required
    level = Column(String, nullable=False)  # Required
    students = relationship("Student", secondary="student_courses", back_populates="courses")

class StudentCourse(Base):
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
```

### API Contracts
- **Endpoint: POST `/students/{id}/courses`**
  - **Request Body**:
    ```json
    {
      "course_ids": [1, 2, 3]  # List of course identifiers
    }
    ```
  - **Response** (Upon Successful Association):
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "courses": [
        {"id": 1, "name": "Introduction to Python", "level": "Beginner"},
        ...
      ]
    }
    ```
  - **Error Response** (When a course ID does not exist):
    ```json
    {
      "error": {
        "code": "E001",
        "message": "One or more specified courses cannot be found."
      }
    }
    ```

- **Endpoint: GET `/students/{id}/courses`**
  - **Response** (On Successful Retrieval):
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "courses": [
        {"id": 1, "name": "Introduction to Python", "level": "Beginner"},
        ...
      ]
    }
    ```

## V. Implementation Steps

1. **Project Update**
   - Confirm the existing FastAPI project structure is intact. Ensure integration points are clear, and no additional directories are necessary for the new feature.

2. **Dependency Installation**
   - All required dependencies (FastAPI, SQLAlchemy, Alembic) are already present in the project framework. No new installations required.

3. **Model Creation**
   - **Modify the Student model** in `src/models/student.py` to include a relationship with courses via a join table.
   - **Create the StudentCourse join table** in `src/models/student.py`.

4. **Database Migration**
   - Use Alembic for managing database schema changes to implement the join table.
     1. Generate a migration using Alembic:
        ```bash
        alembic revision --autogenerate -m "Add StudentCourse join table"
        ```
     2. Edit the generated migration script to create the `student_courses` table:
        ```python
        def upgrade():
            op.create_table(
                'student_courses',
                sa.Column('student_id', sa.Integer(), nullable=False),
                sa.Column('course_id', sa.Integer(), nullable=False),
                sa.PrimaryKeyConstraint('student_id', 'course_id'),
                sa.ForeignKeyConstraint(['student_id'], ['students.id']),
                sa.ForeignKeyConstraint(['course_id'], ['courses.id'])
            )
        
        def downgrade():
            op.drop_table('student_courses')
        ```
     3. Apply the migration:
        ```bash
        alembic upgrade head
        ```

5. **API Endpoints Implementation**
   - Modify existing `api.py` to include new endpoints for associating courses with students and retrieving associated courses. Ensure validation for course existence.

6. **Error Handling Module**
   - Extend existing centralized error handling in `errors.py` to include potential error responses when specifying invalid course IDs during associations.

7. **Application Entry Point**
   - Ensure `app.py` is updated to include the new routes for handling course associations. Confirm necessary changes to include middleware for request validation are in place.

8. **Testing**
   - Extend `tests/test_api.py` to ensure existing functionality remains intact while adding a new `tests/test_student_courses.py` for:
     - Successfully associating courses with a student.
     - Checking responses for missing course IDs.
     - Validating retrieval of associated courses.
     - Ensuring all tests maintain at least 70% coverage.

9. **Documentation**
   - Update FastAPI’s auto-generated OpenAPI documentation to reflect new endpoints.
   - Modify `README.md` to provide guidance on the course association endpoints, ensuring there's clarity on input and output specifications.

## VI. Scalability, Security, and Maintainability Considerations
- **Scalability**: Design is flexible to allow for more complex relationships or features in the future, such as course prerequisites or enrollment limits.
- **Security**: Input validation and error handling must enforce integrity checks on course associations and protect against injection vulnerabilities.
- **Maintainability**: All new code adheres to existing project standards for readability, documentation, and logic separation.

## VII. Trade-offs and Decisions
- **SQLite**: Using SQLite remains practical for simplicity and existing integration, though the design anticipates scaling to more robust databases in the future.
- **Join Table**: Adopting a many-to-many relationship allows for greater flexibility in course assignments, adhering to relational database best practices.

## VIII. Conclusion
This comprehensive implementation plan outlines a structured approach to adding a Course entity relationship to the Student Management Web Application while ensuring backward compatibility with existing models. By thoughtfully integrating new features, this effort will enhance student course management capabilities within the application.

### Existing Code References
- **File: tests/test_api.py**
```python
# test_api.py remains unchanged except for additional import statements.
from src.models import Course  # Add this import to use Course in tests
```

- **File: tests/test_models.py**
```python
# Additional logic only for setup if needed.
```

- **File: tests/test_student_courses.py**
```python
# This file will be newly created for course association tests covering both endpoints and any edge cases.
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.app import app
from src.models import Base, Student, Course

# Setting up the testing...

@pytest.fixture(scope="module")
def test_db():
    # Setup test database and model fixtures...
```

---

This implementation plan provides a thorough roadmap for successfully adding a new course relationship to students, maintaining the integrity of existing systems, and ensuring clarity in the integration of new functionality.