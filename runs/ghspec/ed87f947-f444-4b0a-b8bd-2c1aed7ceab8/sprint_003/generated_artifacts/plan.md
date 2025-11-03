# Implementation Plan: Create Course Entity

---

INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---

INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Entity Web Application

## I. Overview

The purpose of this implementation plan is to outline the steps required to create a new Course entity in the existing system. This new entity will facilitate the organization and management of courses, allowing for efficient categorization and retrieval of course details. The implementation will enhance the educational offerings of the application while maintaining compatibility with the existing architecture and technology stack.

## II. Architecture

### 2.1 Architectural Overview
The application will continue using a RESTful architecture, allowing clients to interact with the new Course entity through well-defined API endpoints. The Course entity will be introduced without disrupting existing functionalities such as the Student entity, ensuring a seamless integration.

### 2.2 Components
1. **API Layer**: New endpoints will handle the creation, retrieval, and updating of Course entities.
2. **Service Layer**: Logic for course validation and business rules related to courses.
3. **Data Access Layer (DAL)**: Responsible for managing database operations, including CRUD for Course entities.
4. **Database**: The existing SQLite database will be modified with a migration to include a new Course table.

## III. Technology Stack

- **Programming Language**: Python 3.11+
- **Web Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing Framework**: Pytest
- **Environment Management**: `pip`
- **Logging**: Python's built-in logging module

## IV. Module Boundaries and Responsibilities

### 4.1 API Module
- Endpoint Definitions:
  - `POST /courses`: Create a new Course (requires `name` and `level`)
  - `GET /courses/{id}`: Retrieve a Course by ID
  - `PUT /courses/{id}`: Update an existing Course by ID

### 4.2 Service Layer
- Business logic will include:
  - Validation for the `name` and `level` fields during creation and updates.
  
### 4.3 Data Access Layer
- Responsible for database interactions, including:
  - Implementation of CRUD operations for Course entities.
  - Migration handling for the Course entity addition.

## V. Data Models

### 5.1 Course Entity Model
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
```

## VI. API Contracts

### 6.1 Request/Response Format

1. **Create Course** (`POST /courses`)
   - **Request**: 
     ```json
     {
         "name": "Data Science 101",
         "level": "Beginner"
     }
     ```
   - **Response** (201 Created):
     ```json
     {
         "id": 1,
         "name": "Data Science 101",
         "level": "Beginner"
     }
     ```

2. **Retrieve Course** (`GET /courses/{id}`)
   - **Response** (200 OK):
     ```json
     {
         "id": 1,
         "name": "Data Science 101",
         "level": "Beginner"
     }
     ```

3. **Update Course** (`PUT /courses/{id}`)
   - **Request**:
     ```json
     {
         "name": "Advanced Data Science",
         "level": "Intermediate"
     }
     ```
   - **Response** (200 OK):
     ```json
     {
         "id": 1,
         "name": "Advanced Data Science",
         "level": "Intermediate"
     }
     ```

### 6.2 Error Responses
- **Missing Course Fields**:
```json
{
    "error": {
        "code": "E001",
        "message": "Both 'name' and 'level' fields are required."
    }
}
```

## VII. Error Handling

- Validate that both `name` and `level` are provided. These validations will be done in the service layer during the course creation and update operations.
- Provide detailed error messages for invalid inputs to facilitate debugging and enhance user experience.

## VIII. Implementation Steps

1. **Database Migration**:
   - Create a migration script to add the `courses` table to the existing database.
   - Utilize Alembic or a similar tool for schema migrations.
   ```sql
   CREATE TABLE courses (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT NOT NULL,
       level TEXT NOT NULL
   );
   ```

2. **Update Data Access Layer**:
   - Create a new Course model to support CRUD operations.
   - Implement methods to interact with the Course entity in the database.

3. **Modify API Endpoints**:
   - Implement the `POST /courses` endpoint to create a new Course.
   - Implement the `GET /courses/{id}` endpoint to retrieve Course details.
   - Implement the `PUT /courses/{id}` endpoint to allow updates on existing Courses.

4. **Enhance Service Layer**:
   - Create services to handle business logic for Course creation and validation.
   - Leverage existing logging and error-handling practices.

5. **Write Tests**:
   - Create unit tests for Course creation, retrieval, and updating functionalities.
   - Ensure applicable error cases are also tested.
   - Aim for a minimum of 70% test coverage for the new Course features.

6. **Documentation**:
   - Update API documentation to include new endpoints for the Course entity.
   - Provide a changelog in the README detailing the database migration steps.

7. **End-to-End Testing**:
   - Conduct integration tests to ensure API endpoints work as expected with valid and invalid data.

8. **Deployment**:
   - Validate all updates in a staging environment, ensuring that existing functionalities remain intact.

## IX. Testing Strategy

- Implement automated tests aligned with the current testing framework for:
  - Unit tests of the service methods to validate course validations and business logic. 
  - Integration tests that cover new API functionality and validate correct interaction with the database layer.

## X. Deployment Considerations

- Confirm the environment configurations include variables necessary for database operation.
- Document the migration strategies with specific rollbacks and testing requirements to ensure safety in production.

## XI. Conclusion

This implementation plan provides a detailed and structured approach to introducing the Course entity into the existing system. The design leverages the current architecture and technology stack while ensuring backward compatibility and a smooth integration of new functionalities for managing courses effectively.

Existing Code Modifications:
- **Course Entity Model**: New model to represent the Course entity.
- **API endpoints**: New endpoints for creating, retrieving, and updating courses.
- **Testing**: New tests aligned with the creation and handling of Course data.

```python
# Migration script example
# migration.py
"""Create courses table

Revision ID: <unique_id>
"""
from sqlalchemy import Column, String, Integer
from alembic import op

def upgrade():
    op.create_table('courses',
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('name', String, nullable=False),
        Column('level', String, nullable=False)
    )

def downgrade():
    op.drop_table('courses')
```

Existing Code Files:
File: tests/test_course_api.py
```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assume your FastAPI app is instantiated in src/main.py


@pytest.fixture(scope="module")
def client():
    """Setup the test client for the FastAPI application."""
    with TestClient(app) as client:
        yield client


def test_create_course(client):
    """Test creating a new course with valid data."""
    response = client.post("/api/v1/courses", json={"name": "Data Science 101", "level": "Beginner"})
    assert response.status_code == 201
    assert "id" in response.json()


def test_get_course(client):
    """Test retrieving an existing course by ID."""
    response = client.get("/api/v1/courses/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Data Science 101"
```

File: tests/test_integration.py
```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assume your FastAPI app is instantiated in src/main.py


@pytest.fixture(scope="module")
def client():
    """Setup the test client for the FastAPI application."""
    with TestClient(app) as client:
        yield client


def test_update_course(client):
    """Test updating an existing course."""
    response = client.put("/api/v1/courses/1", json={"name": "Advanced Data Science", "level": "Intermediate"})
    assert response.status_code == 200
    assert response.json()["name"] == "Advanced Data Science"

def test_create_course_with_missing_fields(client):
    """Test creating a new course with missing fields."""
    response = client.post("/api/v1/courses", json={"name": ""})
    assert response.status_code == 400
    assert response.json()["error"]["code"] == "E001"
```

With this structured plan, the implementation of the Course entity will enrich the existing educational management system while adhering to best practices in software development.