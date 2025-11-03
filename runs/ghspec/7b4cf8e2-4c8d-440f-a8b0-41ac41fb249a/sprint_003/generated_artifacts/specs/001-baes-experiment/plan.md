# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## Version
1.1.0

## Overview
This implementation plan outlines the technical design for enhancing the Student Management Web Application by introducing a Course entity. This feature will enable users to define and manage courses, allowing for improved curriculum organization and further student management capabilities.

## Technology Stack
- **Programming Language**: Python
- **Web Framework**: Flask
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **HTTP Client**: Requests (for potential testing/interaction)
- **Testing Framework**: pytest
- **API Documentation**: Swagger (Flasgger)

## Architecture Overview
1. **API Layer**: Handles HTTP requests and responses, integrating with the Course service layer.
2. **Service Layer**: Business logic for managing course operations, including creation, retrieval, and updating course details.
3. **Data Access Layer**: Interacts with the SQLite database via SQLAlchemy for the Course entity.
4. **Model Layer**: Defines the Course data model and schema, including properties for name and level.

## Module Breakdown
### 1. API Layer (`api.py`)
- New endpoint definitions for:
  - `POST /courses`: Create a new course record with a provided name and level.
  - `GET /courses/{id}`: Retrieve details of a specific course by ID.
  - `PUT /courses/{id}`: Update an existing course's name or level by ID.

### 2. Service Layer (`course_service.py`)
- Implement CRUD operations for courses:
  - A function to create a new course.
  - A function to retrieve course details by ID.
  - A function to update course details based on the course ID.

### 3. Data Access Layer (`models.py`)
- Define a new Course entity with fields for ID, name, and level.
- Implement necessary changes in the database initialization and schema for Course management.

### 4. Utility Functions (`utils.py`)
- Reuse existing utility functions where applicable and add any new utilities needed for course validation.

### 5. Testing Suite (`tests/test_api.py`)
- Additional test cases for course-related functionalities and validation scenarios for course CRUD operations.

## Data Models
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
```

## API Contracts
### Endpoint: `POST /courses`
- **Request Body**:
  ```json
  {
    "name": "Introduction to Programming",
    "level": "Beginner"
  }
  ```
- **Response** (201 Created):
  ```json
  {
    "id": 1,
    "name": "Introduction to Programming",
    "level": "Beginner"
  }
  ```

### Endpoint: `GET /courses/{id}`
- **Response** (200 OK):
  ```json
  {
    "id": 1,
    "name": "Introduction to Programming",
    "level": "Beginner"
  }
  ```

### Endpoint: `PUT /courses/{id}`
- **Request Body**:
  ```json
  {
    "name": "Advanced Programming",
    "level": "Intermediate"
  }
  ```
- **Response** (200 OK):
  ```json
  {
    "id": 1,
    "name": "Advanced Programming",
    "level": "Intermediate"
  }
  ```

### Error Responses
- **Missing Required Fields**:
  ```json
  {
    "error": {
      "code": "E001",
      "message": "Course name and level are required."
    }
  }
  ```

## Implementation Approach
1. **Setup Application Structure**:
   - Create a new `Course` model in `models.py`.
   - Extend the existing schema migration to handle the new Course table.

2. **Define API Endpoints**:
   - Update `api.py` to include handling for the new Course endpoints (POST, GET, PUT).

3. **Implement Service Logic**:
   - Create `course_service.py` for handling business logic related to courses, incorporating necessary validation for inputs.

4. **Database Migration**:
   - Create a migration script to establish the Course table in the existing database without affecting current Student data.

5. **Testing**:
   - Augment `tests/test_api.py` to include new test cases for Course functionalities, ensuring the same level of test coverage as previous implementations.

6. **Documentation**:
   - Update Swagger documentation to reflect new API endpoints and the modifications to the API contracts.

## Scalability, Security, and Maintainability Considerations
- The Course entity is distinctly defined, allowing for future expansions such as course prerequisites or associations with students without impacting current system functions.
- Implement input validation to prevent SQL injection and invalid data entries for the Course creation and update processes.
- Maintain backward compatibility with existing models, ensuring student data handling remains unaffected.

## Logging & Monitoring
- Integrate logging functionality that records API calls and actions taken with courses, facilitating debugging and monitoring of the Course management operations.

## Deployment Considerations
- Update the `Dockerfile` as necessary to ensure all new dependencies and migration tools are present.
- Provide updated documentation for new API endpoints, including necessary configurations for database migrations.

## Conclusion
This implementation plan outlines a systematic and thorough approach to introducing a Course entity to the Student Management Web Application. By following this plan, we can ensure a seamless integration that satisfies all outlined specifications, enhances current capabilities, and maintains consistency with the existing codebase. The outlined steps will facilitate a successful deployment while adhering to best practices in software development.

Existing Code Files:
File: `src/tests/test_api.py`
```python
import pytest
from fastapi.testclient import TestClient
from src.api import app
from src.course_service import create_course, get_course, update_course 

client = TestClient(app)

@pytest.fixture
def setup_course():
    """Fixture to create a sample course for tests."""
    response = client.post("/courses", json={"name": "Math 101", "level": "Beginner"})
    course_data = response.json()
    yield course_data["id"]  # Return course ID for tests
    client.delete(f"/courses/{course_data['id']}")  # Clean up after tests

def test_create_course(setup_course):
    course_id = setup_course
    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Math 101"

def test_update_course(setup_course):
    course_id = setup_course
    response = client.put(f"/courses/{course_id}", json={"name": "Math 201", "level": "Intermediate"})
    assert response.status_code == 200
    assert response.json()["name"] == "Math 201"

def test_create_course_invalid_input():
    response = client.post("/courses", json={"name": "", "level": ""})
    assert response.status_code == 400
    assert response.json()["error"]["code"] == "E001"
    assert "Course name and level are required." in response.json()["error"]["message"]
```
