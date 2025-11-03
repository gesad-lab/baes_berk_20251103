# Implementation Plan: Create Teacher Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
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

## Technical Architecture

### 1. Architecture Overview
The introduction of the Teacher entity into the Student Management Application will extend the current architecture by enabling the management of educational staff data alongside existing Student and Course entities. The system will continue to utilize FastAPI for the RESTful API structure and SQLAlchemy as the ORM for data interactions, ensuring smooth integration and maintainable code structure.

### 2. Technology Stack
- **Programming Language**: Python
- **Web Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Docker**: For containerization
- **Testing Framework**: Pytest
- **Migration Tool**: Alembic

---

## Module Design

### 1. Module Responsibilities
- **Teacher Module**: Responsible for managing Teacher-related functionality such as creating, retrieving, updating, and deleting Teacher data.

### 2. Class/Function Design
- **Teacher Class**:
  Attributes:
  - `id`: Integer (auto-generated, primary key)
  - `name`: String (required)
  - `email`: String (required, unique)

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
```

- **CRUD Operations for Teacher**:
  - `create_teacher(name: str, email: str) -> Teacher`: Method to create a new Teacher.
  - `get_all_teachers() -> List[Teacher]`: Method to retrieve all Teachers.
  - `update_teacher(teacher_id: int, name: Optional[str], email: Optional[str]) -> Teacher`: Method to update Teacher details.
  - `delete_teacher(teacher_id: int) -> None`: Method to delete a Teacher.

### 3. API Endpoints
- **Create Teacher**:
  - **Method**: POST
  - **Endpoint**: `/teachers`
  - **Request Body**:
    ```json
    {
      "name": "Jane Doe",
      "email": "jane.doe@example.com"
    }
    ```
  - **Response**:
    - 201 Created:
      ```json
      {
        "id": 1,
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
      }
      ```

- **Get All Teachers**:
  - **Method**: GET
  - **Endpoint**: `/teachers`
  - **Response**:
    - 200 OK:
      ```json
      [
        {
          "id": 1,
          "name": "Jane Doe",
          "email": "jane.doe@example.com"
        }
      ]
      ```

- **Update Teacher**:
  - **Method**: PUT
  - **Endpoint**: `/teachers/{id}`
  - **Request Body**:
    ```json
    {
      "name": "Jane NewName",
      "email": "jane.new.email@example.com"
    }
    ```
  - **Response**:
    - 200 OK:
      ```json
      {
        "id": 1,
        "name": "Jane NewName",
        "email": "jane.new.email@example.com"
      }
      ```

- **Delete Teacher**:
  - **Method**: DELETE
  - **Endpoint**: `/teachers/{id}`
  - **Response**:
    - 204 No Content: on successful deletion.

---

## Data Model

### 1. Database Schema
- **Teacher Table**:
  - `id`: INTEGER PRIMARY KEY AUTOINCREMENT
  - `name`: TEXT NOT NULL
  - `email`: TEXT NOT NULL UNIQUE

### 2. Database Migration
- A migration script will be created to add the Teacher table. This will use Alembic to ensure the integrity of existing data in Students and Courses.

```python
"""create_teachers_table

Revision ID: xxx_revisions
Revises: previous_revision_id
Create Date: YYYY-MM-DD
"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    # Create the teacher table
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False, unique=True)
    )

def downgrade():
    op.drop_table('teachers')
```

---

## Error Handling & Validation

### 1. Input Validation
- **Request validation** will confirm:
  - Both `name` and `email` fields are required.
  - `email` must be unique and follow valid email format.
- **Responses** for unsuccessful validations:
  - 400 Bad Request for missing fields or validation errors.

### 2. Error Responses
Error responses for invalid requests will follow this format:
```json
{
  "error": {
    "code": "E001",
    "message": "Invalid input: 'email' must be unique and valid."
  }
}
```

---

## Testing Plan

### 1. Test Coverage
- Implement unit tests targeting at least 70% coverage for all Teacher-related functionalities.
- Critical paths (creating, updating, and deleting Teachers) need to have 90%+ coverage.

### 2. Test Scenarios
- Test creating a Teacher with valid details.
- Test retrieving all Teachers from the system.
- Test updating a Teacher's name and email.
- Test deleting a Teacher from the system.
  
```python
def test_create_teacher():
    response = client.post("/teachers", json={"name": "Jane Doe", "email": "jane.doe@example.com"})
    assert response.status_code == 201
    assert "id" in response.json()

def test_get_all_teachers():
    response = client.get("/teachers")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
```

---

## Deployment Considerations

### 1. Containerization
- Update the Dockerfile if necessary to include new dependencies or configurations related to the Teacher entity.

### 2. Documentation & Configuration
- Update the `README.md` to include information about the new Teacher entity endpoints and usage.
- Ensure new RESTful API endpoints and changes to data models are reflected in API documentation.

---

## Conclusion

This implementation plan outlines the introduction of the Teacher entity into the Student Management Application. It defines the responsibilities of the new Teacher module, outlines API endpoints for Teacher management, and ensures thorough validation and testing strategies. By maintaining compatibility with existing structures and documenting all modifications, this plan facilitates a smooth integration process while enhancing application scalability and maintainability.

Existing Code Files:
File: tests/services/test_teacher_service.py
```python
# Sample test structure
def test_delete_teacher():
    """Test removal of a teacher from the system."""
    response = client.delete("/teachers/1")
    assert response.status_code == 204  # No Content
```

Existing Code Files:
File: tests/services/test_teacher_service.py
```python
import pytest
from fastapi.testclient import TestClient
from src.services.teacher_service import app

client = TestClient(app)

@pytest.fixture
def valid_teacher():
    return {
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    }

@pytest.fixture
def create_teacher(valid_teacher):
    """Fixture to create a teacher for testing purposes."""
    response = client.post("/teachers", json=valid_teacher)
    assert response.status_code == 201
    return response.json()
```