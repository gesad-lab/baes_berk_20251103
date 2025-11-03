# Implementation Plan: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

## I. Overview
This document outlines the technical implementation plan for establishing a relationship between the existing Student entity and the newly created Course entity within the Student Management Web Application. This feature aims to facilitate the association of students with specific courses, enriching the application's handling of student records.

## II. Architecture
- **Type**: Microservices architecture
- **Components**:
  - **API Service**: Extends current functionalities to manage student-course associations.
  - **Database**: SQLite for storing both Student and Course data.

### Component Interaction
1. The API service will interact with the SQLite database to manage the relationship between students and courses.
2. New RESTful endpoints will be added to the existing API for enrolling and unenrolling students from courses, as well as retrieving student course details.

## III. Tech Stack
- **Backend Framework**: FastAPI (Python 3.11+)
- **Database**: SQLite (via SQLAlchemy ORM)
- **Serialization**: Pydantic for data validation and serialization
- **Testing Framework**: Pytest for unit and integration testing
- **Environment Management**: Poetry (to manage dependencies)

## IV. Module Boundaries and Responsibilities
### API Service (`api` module)
- Responsible for:
  - Enrolling a student in a course.
  - Retrieving a student's courses.
  - Unenrolling a student from a course.
  - Validating the existence of courses and students before performing actions.

### Database Model (`models` module)
- Extend the Student model to include relationships with the Course entity.
- Define new association models if required (e.g., many-to-many relationship).

### Validation (`schemas` module)
- Create Pydantic schemas for request validation and response serialization for student-course relationships.

## V. Data Models
### Updated Student Model
To reflect the relationship with the Course entity, the Student model is updated to include a many-to-many relationship. It should also support a new association table if required.

```python
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

student_course_association = Table(
    'student_courses',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True),
)

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    courses = relationship('Course', secondary=student_course_association, back_populates='students')

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    students = relationship('Student', secondary=student_course_association, back_populates='courses')
```

### Pydantic Schemas
#### Enroll and Unenroll Student
```python
from pydantic import BaseModel

class StudentEnroll(BaseModel):
    student_id: int
    course_id: int

class StudentUnenroll(BaseModel):
    student_id: int
    course_id: int
```

#### Student Courses Response Schema
```python
class StudentCoursesResponse(BaseModel):
    student_id: int
    courses: list[CourseResponse]
```

### Course Response Schema
```python
class CourseResponse(BaseModel):
    id: int
    name: str
    level: str
```

## VI. API Contracts
### Endpoints Specification
- **POST /students/enroll**: Enroll a student in a course
  - **Request Body**: `{"student_id": 1, "course_id": 1}`
  - **Response**: `201 Created` on success or `404 Not Found` if the student or course does not exist.

- **GET /students/{student_id}/courses**: Retrieve student's enrolled courses.
  - **Response**: `200 OK` with the list of courses or `404 Not Found` if no such student exists.

- **DELETE /students/unenroll**: Unenroll a student from a course
  - **Request Body**: `{"student_id": 1, "course_id": 1}`
  - **Response**: `204 No Content` on success or `404 Not Found`.

## VII. Implementation Approach
1. **Environment Setup**: Ensure Python 3.11+ and Poetry are configured as before.
2. **Update FastAPI Application**:
   - Add `student_courses.py` for the new enrollment and unenrollment endpoints.
   - Modify `models.py` to include relationships in existing Student and Course models.
   - Create `schemas.py` for new validation and serialization schemas.
3. **Database Migration**:
   - Use Alembic to create migration scripts that establish the `student_courses` association table, maintaining data integrity and ensuring backward compatibility.
4. **CRUD Logic Implementation**:
   - Implement necessary logic in the controller file for handling enrollments, unenrollments, and course retrieval.
5. **Input Validation Logic**:
   - Utilize Pydantic for input validation on enrollment, unenrollment, and student retrieval requests.
6. **Testing**:
   - Write new tests in the `tests/test_student_course.py` file to validate the features and ensure proper functionality.

## VIII. Testing Strategy
### Coverage Goals
- Achieve at least 80% test coverage for new student-course relationship functionalities.
- Implement tests based on specified user scenarios:
  - Successful enrollments and unenrollments.
  - Validation error checks for incorrect requests.

### Test Organization
- Directory Structure:
```
.
├── src/
│   ├── api/
│   │   ├── student_courses.py    # New endpoints for student-course associations
│   ├── models.py                 # Updated models
│   ├── schemas.py                # Updated schemas
│   └── main.py
├── tests/
│   ├── test_student_course.py     # Tests for student-course functionalities
└── README.md
```

## IX. Security Considerations
- Implement input validation to prevent SQL injection or malformed data submissions.
- Ensure that no sensitive data is disclosed in API responses.

## X. Deployment Considerations
- Use environment variables for database URL and sensitive application settings.
- Ensure that the deployment pipeline incorporates tests for new features.

## XI. Documentation
- Update the README.md file to include setup instructions for the new functionality.
- Provide API usage instructions for new endpoints related to student-course management.

## XII. Future Enhancements
- Additional features may include managing student attendance in courses or advanced reporting on course enrollment.
- Possible enhancements for user permissions and role management concerning course registration.

## XIII. Trade-offs and Decisions
- **Migration Strategy**: Careful migration scripts will ensure that both data integrity and backward compatibility are maintained.
- **FastAPI**: This framework enables efficient API management while offering built-in support for validation requirements.
- **Testing Focus**: Priority on covering core functionalities now, with plans to expand test coverage and scenarios in future sprints.

### Existing Code Files Modifications:
1. **models.py**: Extend the `Student` class to include relationships with courses through a join table for many-to-many associations.
2. **schemas.py**: Add new Pydantic schemas for managing student-course associations.
3. **student_courses.py**: Introduce links to new endpoints for enrolling and unenrolling students from courses and fetching their course lists.

### Database Migration Strategy:
Alembic migration script to create the association table `student_courses`:
```python
"""Create student_courses table

Revision ID: xxxxxxxx
Revises: previous_revision_id
Create Date: YYYY-MM-DD HH:MM:SS

"""
from alembic import op
import sqlalchemy as sa

revision = 'xxxxxxxx'
down_revision = 'previous_revision_id'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), primary_key=True),
    )

def downgrade():
    op.drop_table('student_courses')
```

### Testing Example:
File: `tests/test_student_course.py`
```python
import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    # Setup logic for creating necessary records or test database goes here
    ...

def test_enroll_student_in_course():
    response = client.post("/students/enroll", json={"student_id": 1, "course_id": 1})
    assert response.status_code == 201

def test_retrieve_student_courses():
    response = client.get("/students/1/courses")
    assert response.status_code == 200
    assert len(response.json()['courses']) > 0

def test_unenroll_student_from_course():
    response = client.delete("/students/unenroll", json={"student_id": 1, "course_id": 1})
    assert response.status_code == 204
```

This technical implementation plan is developed to fully integrate a new relationship between students and courses into the existing Student Management Web Application while adhering strictly to the project’s coding standards, architecture, and incremental development philosophy.