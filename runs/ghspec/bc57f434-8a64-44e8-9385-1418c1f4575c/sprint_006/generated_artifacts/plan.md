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
# Implementation Plan: Add Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Entity Management Web Application

## Version: 1.0.0  
**Date**: 2023-10-10  
**Prepared by**: [Your Name]  

---

## I. Overview

This implementation plan outlines the technical architecture and strategies for establishing a relationship between the Course and Teacher entities within the existing educational management application. This feature will facilitate better tracking of which teachers are responsible for which courses, enhancing the organization and retrieval of course information.

---

## II. Architecture

### 1. Architecture Overview
- **Client-Server Model**: The application will continue to utilize a RESTful API server that interfaces with an existing SQLite database.
- **Microservices**: An established microservices architecture focusing on API development will continue to serve teacher and course management functionalities.

### 2. Technology Stack
- **Web Framework**: FastAPI (for API development)
- **Database**: SQLite (for data persistence)
- **Data Validation**: Pydantic (for request/response validation)
- **Testing Framework**: pytest (for unit and integration testing)
- **ORM**: SQLAlchemy (for database interactions)

### 3. Deployment
- **Environment**: The deployment will occur locally with a later transition to a production environment using Docker.

---

## III. Module Boundaries and Responsibilities 

### 1. Modules Overview
- **API Module**: Introduces new API endpoints for course-teacher relationships.
- **Database Module**: Modifies the existing Course table, introducing the foreign key to refer to the Teacher entity.
- **Validation Module**: Utilizes Pydantic models for validating course-teacher relationship input data.
- **Error Handling Module**: Implements consistent error responses across API operations related to course updates and teacher assignments.

### 2. Module Responsibilities
- **API Module**
  - New Endpoints to Manage Teacher-Course Relationships:
    - `PUT /courses/{id}`: Update existing course to include `teacher_id`.
    - `GET /courses/{id}`: Retrieve course details including associated teacher’s information.

- **Database Module**
  - Modify the existing `Course` table schema to add `teacher_id` as a foreign key referencing the `Teacher` entity.

- **Validation Module**
  - Implement validations for the existence of the `teacher_id`.

- **Error Handling Module**
  - Structured error responses for invalid teacher assignment requests.

---

## IV. Data Models

### 1. Course Entity Data Model Modifications
```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    teacher_id = Column(Integer, ForeignKey('teacher.id'), nullable=True)  # New field added

    teacher = relationship("Teacher", back_populates="courses")  # Add relationship to Teacher
```

### 2. Pydantic Models for Validation
```python
from pydantic import BaseModel, Field
from typing import Optional

class CourseUpdateRequest(BaseModel):
    teacher_id: Optional[int] = Field(None, title="Teacher ID", description="The ID of the teacher to associate with the course.")

class CourseResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    teacher_id: Optional[int]
    teacher_name: Optional[str]
    teacher_email: Optional[str]
```

### 3. Database Migration Strategy
- Use Alembic to create a migration script that would alter the existing `Course` table to add the `teacher_id` field as a foreign key referencing `Teacher.id`.
- Ensure existing data integrity and validate that the migration script can be applied without loss of existing Course data.

---

## V. API Contracts

### 1. Endpoint Definitions

- **PUT /courses/{id}**
  - **Description**: Update a course to associate it with a teacher by modifying the `teacher_id`.
  - **Request Body**: 
    ```json
    {
      "teacher_id": 1
    }
    ```
  - **Responses**:
    - 200 OK:
      ```json
      {
        "id": 1,
        "name": "Mathematics",
        "description": "Advanced algebra course.",
        "teacher_id": 1,
        "teacher_name": "Jane Smith",
        "teacher_email": "jane.smith@example.com"
      }
      ```
    - 400 Bad Request:
      ```json
      {
        "error": {"code": "E001", "message": "Invalid teacher ID provided."}
      }
      ```
    - 404 Not Found (when course ID does not exist):
      ```json
      {
        "error": {"code": "E002", "message": "Course not found."}
      }
      ```

- **GET /courses/{id}**
  - **Description**: Retrieve details of a specific course, including the associated teacher’s information.
  - **Responses**:
    - 200 OK:
      ```json
      {
        "id": 1,
        "name": "Mathematics",
        "description": "Advanced algebra course.",
        "teacher_id": 1,
        "teacher_name": "Jane Smith",
        "teacher_email": "jane.smith@example.com"
      }
      ```
    - 404 Not Found:
      ```json
      {
        "error": {"code": "E003", "message": "Course not found."}
      }
      ```

---

## VI. Error Handling

### Error Handling Strategy
- Implement centralized error handling middleware that captures and manages errors related to course updates and retrievals.
- Ensure all errors follow the defined JSON structure for clarity and consistency.

---

## VII. Testing Strategy

### 1. Test Coverage Goals
- All updates must meet a minimum test coverage of 70%, with critical paths for updating courses to include teacher details exceeding 90%.

### 2. Types of Tests
- **Unit Tests**: Validate individual functions for updating course-teacher assignments and retrieving course details.
- **Integration Tests**: Test the end-to-end functionality of API requests and database interactions involving courses and teachers.
- **Contract Tests**: Ensure API response formats meet the specifications for updating and retrieving course details.

### 3. Testing Framework
- Follow the existing structure with `pytest`, ensuring the tests are organized to reflect the source code organization within `src/`.

---

## VIII. Deployment Considerations

### 1. Initial Deployment Steps
- Extend the Docker configuration to accommodate changes to the Course entity.
- Prepare the environment file (`.env`) if necessary, detailing configurations for new API endpoints.
- Ensure automated test coverage is thorough for all new functionalities.

### 2. Production Readiness
- Make sure that the application starts successfully and can handle requests for both courses and teacher relationships without manual interventions after deployment.
- Health check endpoints should accurately reflect the state of the `Course` and `Teacher` API operations.

---

## IX. Conclusion

This implementation plan is designed to add a Teacher relationship to the Course entity, enhancing the educational management application. It clearly outlines the architecture changes, technology choices, migration strategies, and testing frameworks required to implement the new feature successfully while meeting functional requirements and maintaining backward compatibility.

### Existing Code Files Modifications:
1. **Migration Script**: Create a new Alembic migration file for altering the Course table to add the `teacher_id` field.
2. **Update Course Model**: Modify the existing `Course` entity model to include the new `teacher_id` field.
3. **Implement API routes** in `api.py` to handle new relationships for `/courses/{id}` endpoint for both updating and retrieving course information.
4. **Add new test cases** in `tests/test_api_courses.py` to cover functionality regarding associations between courses and teachers, handling valid and invalid relationships.

---

### Example of Updated Test File: `tests/test_api_courses.py`
```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming the FastAPI app is in src/main.py

@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client

def test_update_course_with_teacher(test_client):
    """Test updating a course with a valid teacher ID."""
    response = test_client.put("/courses/1", json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json()["teacher_id"] == 1

def test_update_course_invalid_teacher(test_client):
    """Test updating a course with an invalid teacher ID."""
    response = test_client.put("/courses/1", json={"teacher_id": 999})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Invalid teacher ID provided."}}

def test_get_course_with_teacher(test_client):
    """Test retrieving course details including teacher information."""
    response = test_client.get("/courses/1")
    assert response.status_code == 200
    assert response.json()["teacher_id"] is not None

def test_get_course_not_found(test_client):
    """Test retrieving a course that does not exist."""
    response = test_client.get("/courses/999")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E003", "message": "Course not found."}}
```

This implementation plan provides a comprehensive guide for integrating the Teacher relationship with Courses in the educational management application, ensuring minimal disruption and maintaining functional integrity.