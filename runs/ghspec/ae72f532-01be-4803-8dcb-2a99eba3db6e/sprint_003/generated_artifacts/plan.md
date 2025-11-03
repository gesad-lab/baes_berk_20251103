# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## 1. Overview
This implementation plan outlines the approach for introducing a new Course entity within the existing Student Management Web Application. The addition of the Course entity will facilitate the storage and management of educational courses associated with students, enhancing the organization and record-keeping capabilities of the application.

## 2. Architecture
The architecture will remain largely unchanged but will include modifications to accommodate the new Course entity. The following layers are present:
- **Presentation Layer**: Flask (for creating the API endpoints)
- **Service Layer**: Business logic to handle course operations
- **Data Access Layer (DAL)**: SQLite for database interactions
- **Model Layer**: Represents the Course entity alongside the existing Student entity.

### Diagram

```
[Client] <---> [API (Flask)] <---> [Service Layer] <---> [Data Access Layer (SQLite)]
```

## 3. Technology Stack
- **Framework**: Flask (Python web framework)
- **Database**: SQLite (lightweight disk-based database)
- **ORM**: SQLAlchemy (to facilitate database operations)
- **Validation**: Marshmallow (for request validation and serialization)
- **Testing Framework**: pytest (for unit and integration testing)
- **Environment**: Python 3.11+
- **Deployment**: Docker (for containerization)

## 4. Module Boundaries and Responsibilities

### 4.1 Modules
1. **API Module**
   - Introduce new endpoints for creating and retrieving courses.

2. **Service Module**
   - Implement business logic to handle course creation and retrieval.

3. **Data Access Layer Module**
   - Implement CRUD operations for the Course entity in the database.

4. **Model Module**
   - Define the Course entity, including necessary validations.

### 4.2 Responsibilities
- **API Module**: Routes, handles requests, and sends responses for Course operations.
- **Service Module**: Implements functions for creating and retrieving courses, including validation.
- **Data Access Layer Module**: Manages database connections, schema creation, and queries for the Course entity.
- **Model Module**: Defines data structures and validations for the Course entity.

## 5. Data Models

### Course Entity
```python
class Course(Base):  # SQLAlchemy model
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    def __repr__(self):
        return f"<Course(id={self.id}, name={self.name}, level={self.level})>"
```

### API Contracts
#### Create Course
- **Endpoint**: `POST /api/v1/courses`
- **Request**: 
  ```json
  {
      "name": "Mathematics 101",
      "level": "Beginner"
  }
  ```
- **Response**:
  - Success (201 Created):
    ```json
    {
        "id": 1,
        "name": "Mathematics 101",
        "level": "Beginner"
    }
    ```
  - Error (400 Bad Request):
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Name and level are required."
        }
    }
    ```

#### Retrieve Courses
- **Endpoint**: `GET /api/v1/courses`
- **Response**:
  - Success (200 OK):
    ```json
    [
        {
            "id": 1,
            "name": "Mathematics 101",
            "level": "Beginner"
        },
        {
            "id": 2,
            "name": "Physics 101",
            "level": "Beginner"
        }
    ]
    ```

## 6. Implementation Plan

### 6.1 Project Structure Modifications
```plaintext
student_management/
│
├── src/
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py         # New routes for courses
│   ├── models/
│   │   ├── __init__.py
│   │   ├── student.py        # No modifications necessary here
│   │   └── course.py         # New model for Course entity
│   ├── services/
│   │   ├── __init__.py
│   │   └── course_service.py  # New service logic for Course
│   ├── dal/
│   │   ├── __init__.py
│   │   └── course_dal.py     # New data access methods for Course
│   ├── app.py
│   └── config.py
│
├── migrations/
│   └── 002_add_courses_table.py # New migration file for Course table
│
├── tests/
│   ├── __init__.py
│   ├── test_student_routes.py  # No modifications necessary here
│   ├── test_student_service.py  # No modifications necessary here
│   ├── test_course_routes.py    # New tests for Course endpoints
│   └── test_course_service.py    # New tests for Course business logic
│
├── .env.example
├── requirements.txt
└── README.md
```

### 6.2 Environment Configuration
- A database migration strategy will be implemented for adding the `courses` table, ensuring it integrates smoothly with existing student data.

### Migration Strategy
1. Create a migration script that creates the new `courses` table with the required fields (id, name, level).
2. Ensure that existing schema and data remain unaffected.

Example migration script outline:
```python
def upgrade():
    # Create courses table
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )

def downgrade():
    # Drop courses table on downgrade
    op.drop_table('courses')
```

## 7. Testing Strategy
- **Unit Tests**: Create tests for course creation and validation within `test_course_service.py`.
- **Integration Tests**: Create tests within `test_course_routes.py` to ensure API endpoints work as expected.
- **Contract Tests**: Ensure that API responses match expectations for both successful and error conditions.

### 7.1 Coverage Requirement
- Maintain a minimum 70% coverage overall, with critical paths achieving 90% coverage.

### 7.2 Continuous Improvement
- Utilize pytest to run tests, ensuring no breaking changes are introduced to existing functionality.

## 8. Security Considerations
- Validate all user input for creating courses to ensure that name and level are provided and correctly formatted.
- Avoid exposing any sensitive information in logs or error messages related to course operations.

## 9. Deployment Considerations
- Continue to utilize Docker for containerization of the application, ensuring that migrations are executed correctly on deployment.
- Make sure that the application starts successfully without manual intervention post-migration.

## 10. Conclusion
This implementation plan focuses on introducing a Course entity, enhancing the educational management capabilities of the Student Management Web Application. By adhering to specifications and following established coding standards, we ensure that the application can effectively manage courses alongside students without compromising functionality or integrity.

Existing Code Files:
No significant modifications are needed for existing files. New files for the Course entity will be added, and migration scripts will be created to accommodate the new database schema. 

This plan provides a clear pathway for implementing the Course feature while adhering to all principles outlined in the initial project constitution. 

Existing Code Files:
File: tests/test_course_routes.py
```
```python
import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

@pytest.mark.parametrize("name, level, expected_status, expected_response", [
    ("Mathematics 101", "Beginner", 201, {"id": 1, "name": "Mathematics 101", "level": "Beginner"}),
    ("Physics 101", "Intermediate", 201, {"id": 2, "name": "Physics 101", "level": "Intermediate"}),
    ("Invalid Course", None, 400, {"error": {"code": "E001", "message": "Name and level are required."}})
])
def test_create_course(name, level, expected_status, expected_response):
    response = client.post("/api/v1/courses", json={"name": name, "level": level})
    assert response.status_code == expected_status
    assert response.json() == expected_response

def test_get_courses():
    response = client.get("/api/v1/courses")
    assert response.status_code == 200
    # Verify response structure is as expected
```

File: tests/test_course_service.py
```
```python
# This file will contain tests for the course creation and retrieval logic.
``` 

Create the tests and implementations based on the established patterns in existing code files from `tests/test_student_routes.py` and `tests/test_student_service.py`.