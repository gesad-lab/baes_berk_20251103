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
# Implementation Plan: Student Management Application

---

## I. Project Overview

The purpose of this implementation plan is to define the approach for adding a relationship between the Course entity and the Teacher entity in the Student Management Application. This modification will enable effective management of educational resources by associating courses with their respective instructors, thereby providing enhanced visibility and organization of teaching assignments.

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
│   ├── models.py              # Database models (updated for Course and Teacher relationship)
│   ├── routes.py              # API routes and endpoints (updated for course management)
│   ├── database.py            # Database setup and initialization (migration logic)
│   └── config.py              # Configuration settings
│
├── migrations/                # Database migration files
│   └── 003_add_teacher_to_courses.py
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
   - Implement new endpoint for updating a course to assign a teacher using a PATCH request.
   - Include input validation for teacher assignment.

2. **Database Module** (`database.py`):
   - Update initialization logic to include the new `teacher_id` foreign key reference in the Courses table.
   - Handle migrations to ensure backward compatibility and data integrity.

3. **Models Module** (`models.py`):
   - Update the existing Course model to include a `teacher_id` field that references the Teacher entity.

4. **Migrations** (`migrations/`):
   - Create migration scripts to add the `teacher_id` field in the Courses table while preserving existing data.

---

## V. API Endpoints

1. **PATCH /courses/{id}**
   - **Description**: Update an existing Course entity to assign a teacher.
   - **Request**: JSON body must contain `{ "teacher_id": <integer> }`.
   - **Response**:
     - 200 OK on success with the updated course details.
     - 404 Not Found if the course ID does not exist.
     - 400 Bad Request if the teacher ID does not exist or is invalid.

2. **GET /courses/{id}**
   - **Description**: Retrieve details of a specific Course including the assigned Teacher.
   - **Response**:
     - 200 OK with a JSON object representing the course details along with the assigned teacher.
     - 404 Not Found if the course ID does not exist.

---

## VI. Data Models

```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Updated with foreign key reference
    # Other existing fields...

    teacher = relationship("Teacher", back_populates="courses")  # Establishing relationship

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    courses = relationship("Course", back_populates="teacher")  # Establish reverse relationship
```

---

## VII. Database Setup

1. **Initialization and Migration**:
   - Create a migration script to add the `teacher_id` field to the `courses` table:

```python
# migrations/003_add_teacher_to_courses.py

from sqlalchemy import create_engine, Column, Integer, ForeignKey
from alembic import op

def upgrade():
    op.add_column('courses', Column('teacher_id', Integer, ForeignKey('teachers.id'), nullable=True))

def downgrade():
    op.drop_column('courses', 'teacher_id')
```

2. **Database Connection**: Ensure that the application startup script initializes migrations to incorporate the new relationship:

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
    "message": "Teacher does not exist."
  }
}
```

---

## IX. Testing Strategy

1. **Unit Tests**: Utilize pytest to validate new API endpoints for course assignments.
   - Test successful assignment of a teacher to a course.
   - Validate cases for non-existent courses and teachers.
   - Validate responses to ensure all expected JSON structures are returned.
  
2. **Integration Tests**: Assess the interaction between the course assignment API, data models, and the database to ensure complete data integrity.

3. **Coverage Target**: Aim to have at least 70% test coverage for the newly implemented logic, with 90% coverage for critical paths regarding assignments and retrievals.

---

## X. Security Considerations

- Validate foreign key references to ensure assigned teachers exist before updating courses.
- Implement comprehensive error handling to avoid exposing sensitive data or internal state.
- Protect against SQL injection by using SQLAlchemy's ORM capabilities for all database interactions.

---

## XI. Deployment Considerations

- Ensure that the application starts seamlessly with automated migrations for the new `teacher_id` field.
- Document necessary environment variables in `.env.example`.
- Include a health check endpoint to monitor the application status.

---

## XII. Documentation

- Update `README.md` to include new features related to course management and teacher assignments.
- Ensure that Swagger/OpenAPI documentation reflects the added course assignment endpoints.

---

## XIII. Conclusion

This implementation plan details the necessary steps and changes needed to add a Teacher relationship to the Course entity in the Student Management Application. By adhering to established data handling practices and ensuring backward compatibility, this feature aims to enhance the application's functionality while maintaining data integrity and performance.

Existing Code Files:
Filename: `src/routes.py`
```python
from flask import Flask, request, jsonify
from models import Course, Teacher, session

app = Flask(__name__)

@app.route('/courses/<int:id>', methods=['PATCH'])
def update_course(id):
    data = request.json
    course = session.query(Course).get(id)
    if course is None:
        return jsonify({'error': {'code': 'E001', 'message': 'Course not found'}}), 404
    if 'teacher_id' not in data:
        return jsonify({'error': {'code': 'E002', 'message': 'Missing teacher_id'}}), 400
    # Validate teacher existence
    teacher = session.query(Teacher).get(data['teacher_id'])
    if teacher is None:
        return jsonify({'error': {'code': 'E003', 'message': 'Teacher does not exist'}}), 400
    
    course.teacher_id = data['teacher_id']
    session.commit()
    return jsonify(course), 200

@app.route('/courses/<int:id>', methods=['GET'])
def get_course(id):
    course = session.query(Course).get(id)
    if course is None:
        return jsonify({'error': {'code': 'E001', 'message': 'Course not found'}}), 404
    return jsonify(course), 200
```

Existing Code Files:
File: `tests/test_routes.py`
```python
import pytest
from fastapi.testclient import TestClient
from src.app import app
from src.models import Course, Teacher

client = TestClient(app)

@pytest.fixture(scope="module")
def test_courses():
    """Setup test courses and teachers in the database before any tests run."""
    clear_and_seed_database_with_courses_and_teachers()
    yield
    # Tear down test database cleanup
    clear_test_database()

def test_update_course_assign_teacher_success(test_courses):
    """Test successful assignment of a teacher to a course."""
    response = client.patch('/courses/1', json={"teacher_id": 2})
    assert response.status_code == 200
    assert response.json()["teacher_id"] == 2

def test_update_course_invalid_id():
    """Test updating course that does not exist returns 404."""
    response = client.patch('/courses/999', json={"teacher_id": 2})
    assert response.status_code == 404

def test_update_course_nonexistent_teacher(test_courses):
    """Test assignment of a non-existent teacher to a course returns 400."""
    response = client.patch('/courses/1', json={"teacher_id": 999})
    assert response.status_code == 400
```

This implementation will ensure that the system maintains existing functionality while successfully integrating new features that enhance the management capability of the Student Management Application.