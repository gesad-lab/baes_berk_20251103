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

---

## I. Project Overview

The purpose of this implementation plan is to define the approach for establishing a relationship between the `Student` and `Course` entities within the Student Management Application. This enhancement allows multiple course enrollments per student, enabling improved tracking and reporting of academic progress while maintaining compatibility with existing data models.

---

## II. Technology Stack

- **Programming Language**: Python 3.11+
- **Web Framework**: Flask
- **Database**: SQLite
- **Database ORM**: SQLAlchemy
- **Testing Framework**: pytest
- **Environment Management**: Poetry for dependency management
- **API Documentation**: Swagger/OpenAPI (using Flask-RESTPlus or Flask-Swagger)

---

## III. Project Structure

```
student_management_app/
│
├── src/
│   ├── app.py                 # Main application entry point
│   ├── models.py              # Database models (updated for Course relationship)
│   ├── routes.py              # API routes and endpoints (updated for enrollment)
│   ├── database.py            # Database setup and initialization (migration logic)
│   └── config.py              # Configuration settings
│
├── migrations/                # Database migration files for student_courses
│   └── 001_create_student_courses_table.py
│
├── tests/                     # Test suite
│   ├── test_routes.py         # Tests for API functionality (updated)
│   └── conftest.py            # Fixtures for tests
│
├── .env.example               # Example environment configuration
├── README.md                  # Project documentation
└── pyproject.toml             # Dependency management with Poetry
```

---

## IV. Module Responsibilities

1. **API Module** (`routes.py`):
   - Implement new endpoints for enrolling students in courses and retrieving a student's course list.
   - Include validation for course enrollments.

2. **Database Module** (`database.py`):
   - Update initialization logic to reflect the new relationship through a linking table.

3. **Models Module** (`models.py`):
   - Extend the existing `Student` model and define the `student_courses` linking table for the many-to-many relationship.

4. **Migrations** (`migrations/`):
   - Create migration scripts that enable the addition of the `student_courses` table.

---

## V. API Endpoints

1. **POST /students/{id}/enroll**
   - **Description**: Enroll a student in a specific course.
   - **Request**:
     - JSON body must contain `{ "course_id": <valid_course_id> }`.
   - **Response**:
     - 201 Created on success with the student's updated enrollment data.
     - 404 Not Found if `course_id` does not exist.
     - 400 Bad Request if the student is already enrolled in that course.

2. **GET /students/{id}/courses**
   - **Description**: Retrieve a list of courses a student is enrolled in.
   - **Response**:
     - 200 OK with a JSON array of courses associated with the student.

---

## VI. Data Models

```python
from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Linking table for many-to-many relationship
student_courses = Table('student_courses', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    # existing fields...

    # Establishing relationship
    courses = relationship('Course', secondary=student_courses, back_populates='students')


class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    # Establish Back-relationship
    students = relationship('Student', secondary=student_courses, back_populates='courses')
```

---

## VII. Database Setup

1. **Initialization and Migration**:
   - Create a migration script to implement the `student_courses` table that captures the many-to-many relationship between students and courses:

```python
# migrations/001_create_student_courses_table.py

from sqlalchemy import create_engine, Column, Integer, ForeignKey, Table
from alembic import op

def upgrade():
    op.create_table(
        'student_courses',
        Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
        Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
    )

def downgrade():
    op.drop_table('student_courses')
```

2. **Database Connection**: Ensure that the application startup script initializes the migration for the new linking table.

```python
def init_db():
    """Initialize the database and run migrations."""
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)

    # Running migrations
    alembic_cfg = Config("alembic.ini")
    with engine.begin() as connection:
        command.upgrade(alembic_cfg, "head")

    Session = sessionmaker(bind=engine)
    return Session()
```

---

## VIII. API Response Format

All responses will be in JSON format. Valid error responses will contain the following structured format:

```json
{
  "error": {
    "code": "E001",
    "message": "Course ID does not exist."
  }
}
```

---

## IX. Testing Strategy

1. **Unit Tests**: Utilize pytest to validate new API endpoints for course enrollment.
   - Test successful enrollments and course fetching.
   - Validate cases with non-existent course IDs and duplicate enrollments.

2. **Integration Tests**: Assess the interaction between the API, data models, and the database to ensure data integrity and relationship functionality.

3. **Coverage Target**: Aim to have at least 70% test coverage for the newly implemented logic, targeting 90% for critical enrollment paths.

---

## X. Security Considerations

- Validate course enrollment requests for proper ID formats.
- Implement careful error-handling mechanisms to avoid sensitive data exposure.
- Protect against SQL injection by using parameterized queries through ORM.

---

## XI. Deployment Considerations

- Ensure the application starts seamlessly with automated migrations.
- Document required environment variables in `.env.example`.
- Include a health check endpoint to monitor the application status.

---

## XII. Documentation

- Update `README.md` to include new features related to course relationships and relevant API usage.
- Use Swagger/OpenAPI to comprehensively document the API endpoints introduced.

---

## XIII. Conclusion

This implementation plan details the necessary steps and modifications to add a course relationship to the student entity in the Student Management Application. By maintaining rigorous data handling practices and ensuring backward compatibility, this feature will enhance the application’s functionality while preserving the integrity of existing user data.

Existing Code Files:
Filename: `tests/test_routes.py`
```python
import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_db():
    """Setup and teardown the database for testing."""
    clear_and_seed_database()
    yield
    clear_test_database()

def test_enroll_student_success(setup_db):
    response = client.post("/students/1/enroll", json={"course_id": 1})
    assert response.status_code == 201
    # Further checks can include verifying course enrollment in the database.

def test_enroll_student_invalid_course(setup_db):
    response = client.post("/students/1/enroll", json={"course_id": 999})
    assert response.status_code == 404  
    assert response.json()['error']['code'] == "E001"
```

This approach ensures seamless integration of the new feature while preserving existing functionality and performance.