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
- **Layered Architecture**: The existing architecture will be updated to include support for the Course relationship with Students:
  - **Presentation Layer**: Implements the API endpoints for managing both Student and Course operations.
  - **Service Layer**: Contains business logic for Course management and the new relationships.
  - **Data Access Layer (DAL)**: Manages interactions with Student, Course, and StudentCourse tables in the database.

### 1.2 Component Diagram
```plaintext
+--------------------+          +------------------+          +----------------+
|    Client (Web)    | <-----> |   FastAPI App    | <-----> | SQLite Database |
+--------------------+          +------------------+          +----------------+
```

## II. Technology Stack

### 2.1 Backend Framework
- **FastAPI**: The application will continue to utilize FastAPI for managing APIs.

### 2.2 Database
- **SQLite**: Continuation of using SQLite for lightweight database management.

### 2.3 ORM
- **SQLAlchemy**: Utilized to interact with the updated Student and Course data models and manage database interactions.

### 2.4 Testing Framework
- **pytest**: Will be used for creating unit and integration tests for the added functionality.

### 2.5 Dependency Management
- **poetry**: To manage dependencies and ensure consistent development environments.

## III. Module Design

### 3.1 Module Structure
The existing application structure will be updated to include a new module responsible for handling the Course relationship with Students:

```
student_app/
├── src/
│   ├── main.py
│   ├── models/
│   │   ├── student.py
│   │   ├── course.py          # New model for Course
│   │   └── student_course.py   # New model for StudentCourse bridge
│   ├── db/
│   │   ├── database.py
│   │   └── migrations/
│   ├── routes/
│   │   ├── student_routes.py
│   │   └── course_routes.py    # New routes for Course operations
│   ├── services/
│   │   ├── student_service.py
│   │   └── course_service.py    # New service for Course operations
│   ├── schemas/
│   │   ├── student_schemas.py
│   │   ├── course_schemas.py    # New schemas for Course
│   │   └── student_course_schemas.py # New schemas for StudentCourse operations
└── tests/
    ├── test_student.py
    ├── test_routes.py
    └── test_course.py           # New tests for Course operations
```

### 3.2 Module Responsibilities
- **`main.py`**: Integrate the new course routes with existing application routing.
- **`models/course.py`**: Defines the Course data model (SQLAlchemy ORM).
- **`models/student_course.py`**: Defines the StudentCourse relationship model (SQLAlchemy ORM).
- **`routes/course_routes.py`**: Implements API endpoints for managing the Course operations and relationships to Students.
- **`services/course_service.py`**: Contains business logic for enrolling and removing courses from students.
- **`schemas/student_course_schemas.py`**: Defines Pydantic models for input/output related to the student-course relationship.
- **`tests/test_course.py`**: Contains tests for the API endpoints and logic applicable to the Course functionalities.

## IV. API Design

### 4.1 Endpoints
1. **Enroll Student in Course**
   - **Method**: POST
   - **Endpoint**: `/students/enroll`
   - **Request Body**: `{"student_id": 1, "course_id": 1}`
   - **Response**: `200 OK` with updated student details including enrolled courses.

2. **Retrieve Student's Courses**
   - **Method**: GET
   - **Endpoint**: `/students/{student_id}/courses`
   - **Response**: `200 OK` with list of courses or `404 Not Found`.

3. **Remove Course from Student**
   - **Method**: DELETE
   - **Endpoint**: `/students/{student_id}/courses/{course_id}`
   - **Response**: `200 OK` with updated student details upon successful removal or `404 Not Found`.

### 4.2 JSON Response Format
All API responses will adhere to the following structure:
```json
{
  "data": { /* updated student or course data */ },
  "error": { /* error details if any */ }
}
```

## V. Data Model

### 5.1 Course Model Schema
```python
from sqlalchemy import Column, Integer, String
from db.database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
```

### 5.2 StudentCourse Model Schema
```python
from sqlalchemy import Column, Integer, ForeignKey
from db.database import Base

class StudentCourse(Base):
    __tablename__ = 'student_course'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
```

## VI. Database Management

### 6.1 Database Creation
- SQLAlchemy will define and manage the new StudentCourse join table and the Course table.

### 6.2 Migrations
- **Migration Strategy**: Use Alembic for schema migrations.
  - Migrations will create the `courses` and `student_course` tables while ensuring existing data remains intact.

```plaintext
# Alembic migration to create new tables
def upgrade():
    op.create_table('courses',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'))

    op.create_table('student_course',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['students.id']),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id']),
        sa.PrimaryKeyConstraint('student_id', 'course_id'))

def downgrade():
    op.drop_table('student_course')
    op.drop_table('courses')
```

## VII. Testing Plan

### 7.1 Test Coverage
- Aim for at least 70% coverage for the new features.
- Critical paths (enrollment, course retrieval, course removal) should maintain 90% coverage.

### 7.2 Test Types
- Unit tests for course service methods and integration tests for the Course API endpoints.

## VIII. Security Considerations

- API inputs must be validated for the expected format (e.g., proper integer IDs).
- All communication should utilize HTTPS for secure data transfer.

## IX. Deployment Considerations

### 9.1 Production Readiness
- Ensure the application starts successfully and initializes all required tables.
- Implement a health check endpoint for monitoring the application's health status.

### 9.2 Backward Compatibility
- API endpoints for existing Student operations will remain unchanged. The Course relationship will be added without altering current Student data structures.

## X. Logging & Monitoring

- Include structured logging to capture the context of Course and Student requests, including request IDs and error details.

## XI. Fail-Fast Philosophy

- Validate inputs at the start of each request to capture errors early.
- All exceptions should be logged with appropriate context for easier debugging.

## XII. Milestones & Timeline

### 12.1 Project Milestones
- **Week 1**: Define new models (Course, StudentCourse) and update module structure.
- **Week 2**: Implement endpoints for enrolling, retrieving, and removing courses for students.
- **Week 3**: Develop and run tests to ensure functionality and coverage.
- **Week 4**: Code review, finalize documentation, and prepare for deployment.

## XIII. Conclusion
This implementation plan outlines the necessary steps to integrate the Course relationship into the Student entity within the existing student management application. By following the proposed architecture and guidelines, we will enhance the application's capabilities while maintaining performance, scalability, and maintainability. 

### Modifications Needed
- **`main.py`**: Update to import and include `course_routes`.
- **Existing tests**: New tests will be added in `test_course.py` to test the newly created functionalities. Ensure shared database fixtures accommodate relationships.

```python
# Sample addition in tests/test_course.py
def test_enroll_student_in_course(student_service):
    response = client.post("/students/enroll", json={"student_id": 1, "course_id": 1})
    assert response.status_code == 200
    assert "courses" in response.json()["data"]
    ...
```