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
# Implementation Plan: Student Management Web Application

## 1. Overview 
This implementation plan outlines the architecture, technologies, and approach for establishing a relationship between the `Course` entity and the newly created `Teacher` entity in the educational management system. This feature will enable better tracking of which teacher is responsible for each course and improve overall educational management.

## 2. Architecture

### 2.1 Application Structure
- **Frontend**: Not included in this scope (API only).
- **Backend**: RESTful API developed using Python and FastAPI, enhancing existing functionality to manage the inclusion of teacher relationships to courses.
- **Database**: SQLite for development and testing, involving migrations to update the `Course` table to include a `teacher_id` reference.

### 2.2 Components
- **API Endpoints**:
  - **PATCH /courses/{course_id}/assign-teacher**: Assign a teacher to a course.
  - **GET /courses/{course_id}**: Retrieve course details including assigned teacher information.
  - **PATCH /courses/{course_id}/remove-teacher**: Remove a teacher from a course.

## 3. Technology Stack
- **Programming Language**: Python
- **Web Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy for database interactions
- **Testing Framework**: pytest for unit and integration testing
- **Environment Management**: Poetry for dependency management
- **API Documentation**: OpenAPI provided automatically by FastAPI

## 4. Implementation Approach

### 4.1 Database Design
#### Modify the Existing Course Entity
Add a new foreign key column to the `Course` table:
- `teacher_id`: Integer (foreign key referencing the `Teacher` table).

### 4.1.1 Update Course Model
Extend the existing `Course` model to include:
```python
class Course(Base):
    __tablename__ = 'courses'

    # Existing fields...
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)
    teacher = relationship("Teacher", back_populates="courses")
```

### 4.1.2 Teacher Relationship in Teacher Model
Ensure the reverse relationship is defined in the `Teacher` model:
```python
class Teacher(Base):
    __tablename__ = 'teachers'

    # Existing fields...
    courses = relationship("Course", back_populates="teacher")
```

### 4.2 Database Migration Strategy
Utilize Alembic to create a migration script that will add the `teacher_id` column to the existing `Course` table without affecting existing data.

1. **Create Migration Script**:
   ```bash
   alembic revision --autogenerate -m "Add teacher_id to courses"
   ```

2. **Implement Migration Logic**:
```python
def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id'), nullable=True))

def downgrade():
    op.drop_column('courses', 'teacher_id')
```

### 4.3 API Contract

#### 4.3.1 Assign Teacher to Course Endpoint
- **Endpoint**: `/courses/{course_id}/assign-teacher`
- **Method**: PATCH
- **Request Body**:
   ```json
   {
       "teacher_id": 1  // Required
   }
   ```

- **Response** (200 OK): 
```json
{
  "message": "Teacher assigned successfully.",
  "course_id": 1,
  "teacher_id": 1
}
```

- **Error Response** (404 Not Found - Course does not exist):
```json
{
  "error": {
    "code": "E001",
    "message": "Course not found."
  }
}
```

#### 4.3.2 Retrieve Course Details Endpoint
- **Endpoint**: `/courses/{course_id}`
- **Method**: GET
- **Response** (200 OK):
```json
{
  "course_id": 1,
  "course_name": "Mathematics",
  "teacher": {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
}
```

#### 4.3.3 Remove Teacher from Course Endpoint
- **Endpoint**: `/courses/{course_id}/remove-teacher`
- **Method**: PATCH
- **Response** (200 OK):
```json
{
  "message": "Teacher removed successfully from the course."
}
```

- **Error Response** (404 Not Found - Course does not exist):
```json
{
  "error": {
    "code": "E002",
    "message": "Course not found."
  }
}
```

### 4.4 Error Handling & Validation
- Validate that the `course_id` and `teacher_id` are valid before assignment.
- Use Pydantic models in FastAPI to automate validation for the request body.

### 4.5 Testing Strategy
- **Unit Tests**:
  - Develop tests for course assignments and retrieval of course details.

- **Integration Tests**:
  - Validate the `/courses/{course_id}/assign-teacher`, `/courses/{course_id}`, and `/courses/{course_id}/remove-teacher` endpoints for expected functionality and error cases.

### 4.6 Startup Procedures
Ensuring the migration runs on application startup:
```python
@app.on_event("startup")
async def startup():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")  # Run latest migrations on startup
```

## 5. Scalability, Security, and Maintainability Considerations
- **Scalability**: Although SQLite is sufficient for development, migrate to PostgreSQL for production workloads.
- **Security**: Implement role-based access controls, only allowing admins to assign or remove teachers.
- **Maintainability**: Ensure thorough documentation, well-structured code, and unit tests to facilitate future changes.

## 6. Documentation
- FastAPI's automatically generated API documentation will be available at `/docs`.
- Update `README.md` with new instructions for assigning teachers to courses and the available endpoints.

## 7. Milestones
1. **Setup Migration**: Create and apply migrations to update the `Course` table.
2. **Modify Course Model**: Extend the `Course` model to include the `teacher_id` relationship.
3. **Implement API Endpoints**: Develop the `/courses/{course_id}/assign-teacher`, `/courses/{course_id}`, and `/courses/{course_id}/remove-teacher` endpoints.
4. **Testing**: Create and run unit tests and integration tests for the new functionality.
5. **Documentation**: Ensure `README.md` and API documentation are updated.

## 8. Trade-offs and Decisions
- Utilized SQLite for local development but consider PostgreSQL for production to address scalability and performance.
- Focused on ensuring the integration of the `Teacher` relationship into the existing `Course` entity without disrupting current functionality or existing data integrity.

## Conclusion
This implementation plan provides a structured framework for adding a teacher relationship to the course entity in the educational management system. It ensures adherence to coding standards and principles and considers scalability, security, maintainability, and efficient testing practices.

### Existing Code Files
- **File**: `tests/test_courses.py` (New Test File)
```python
import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

def test_assign_teacher_to_course(client):
    response = client.patch("/courses/1/assign-teacher", json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json() == {
        "message": "Teacher assigned successfully.",
        "course_id": 1,
        "teacher_id": 1
    }

def test_assign_teacher_to_nonexistent_course(client):
    response = client.patch("/courses/9999/assign-teacher", json={"teacher_id": 1})
    assert response.status_code == 404
    assert response.json() == {
        "error": {"code": "E001", "message": "Course not found."}
    }

def test_get_course_details(client):
    response = client.get("/courses/1")
    assert response.status_code == 200
    # Assuming teacher details are available
    assert "teacher" in response.json()

def test_remove_teacher_from_course(client):
    response = client.patch("/courses/1/remove-teacher")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Teacher removed successfully from the course."
    }
```

These tests ensure the success and error cases for course-teacher management functionality are adequately covered.