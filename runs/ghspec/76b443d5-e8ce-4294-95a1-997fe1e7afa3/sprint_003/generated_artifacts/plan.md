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
This implementation plan outlines the architecture, technologies, and approach for adding a new Course entity to the existing Student Management Web Application. The Course entity will allow the system to manage courses effectively, enabling features such as course management and student enrollment.

## 2. Architecture

### 2.1 Application Structure
- **Frontend**: Not included in this scope (API only).
- **Backend**: RESTful API developed using Python and FastAPI, expanding the existing functionality to include courses.
- **Database**: SQLite for development and testing, with migrations to add the new Course table.

### 2.2 Components
- **API Endpoints**:
  - **POST /courses**: Create a new Course with name and level.
  - **GET /courses/{id}**: Retrieve a Course's details including name and level.

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
- **New Course Entity**:
  - ID (auto-generated integer)
  - name (string, required)
  - level (string, required)

#### 4.1.1 Database Schema Creation
Create a new `Course` model to represent courses in the database:
```python
from sqlalchemy import Column, Integer, String
from database import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
```

### 4.2 Database Migration Strategy
Use Alembic migrations to add the Course table and ensure that existing Student data is preserved.
1. **Create Migration Script**:
   ```bash
   alembic revision --autogenerate -m "Add courses table"
   ```

2. **Migrations will include**:
   - Creating the `courses` table so that existing data models remain intact.

#### Migration Example
```python
def upgrade():
    op.create_table(
        'courses',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('level', sa.String(), nullable=False)
    )

def downgrade():
    op.drop_table('courses')
```

### 4.3 API Contract

#### 4.3.1 Create Course Endpoint
- **Endpoint**: `/courses`
- **Method**: POST
- **Request Body**:
  ```json
  {
    "name": "string" (required),
    "level": "string" (required)
  }
  ```

- **Response** (201 Created):
```json
{
  "id": "integer",
  "name": "string",
  "level": "string"
}
```

- **Error Response** (400 Bad Request - missing name):
```json
{
  "error": {
    "code": "E001",
    "message": "Name is required."
  }
}
```

- **Error Response** (400 Bad Request - missing level):
```json
{
  "error": {
    "code": "E002",
    "message": "Level is required."
  }
}
```

#### 4.3.2 Retrieve Course Endpoint
- **Endpoint**: `/courses/{id}`
- **Method**: GET
- **Response** (200 OK):
```json
{
  "id": "integer",
  "name": "string",
  "level": "string"
}
```

- **Error Response** (404 Not Found):
```json
{
  "error": {
    "code": "E003",
    "message": "Course not found."
  }
}
```

### 4.4 Error Handling & Validation
- Validate presence of `name` and `level` fields during Course creation. Return structured error messages as per the API contract.
- Use type hints and Pydantic models in FastAPI to handle validation easily.

### 4.5 Testing Strategy
- **Unit Tests**:
  - Test cases for creating a Course with both valid and invalid input.
  
- **Integration Tests**:
  - Verify the functionality of both creating and retrieving Course entities.

### 4.6 Startup Procedures
- Update FastAPI's startup event for database migrations:
```python
from fastapi import FastAPI
from alembic import command
from alembic.config import Config
from database import engine

app = FastAPI()

@app.on_event("startup")
async def startup():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")  # Apply migration during startup
    Base.metadata.create_all(bind=engine)
```

## 5. Scalability, Security, and Maintainability Considerations
- **Scalability**: SQLite is suitable for initial development. Migration to PostgreSQL or another robust database should be considered for production.
- **Security**: Implement input validation to prevent SQL injection and other forms of attacks. Use environment variables for sensitive configuration.
- **Maintainability**: Follow clean coding principles, keep documentation updated, and ensure that the integration of the new Course entity does not disrupt existing functionalities.

## 6. Documentation
- Automatic API documentation via FastAPI will be available at `/docs`.
- Update the `README.md` to include instructions on using the new API endpoints for Courses.

## 7. Milestones
1. **Setup Migration**: Prepare and run migrations to establish the `courses` table.
2. **Create Course Model**: Implement the Course model in the SQLAlchemy ORM.
3. **Implement API Endpoints**: Develop the `/courses` POST and `/courses/{id}` GET endpoints.
4. **Testing**: Design and execute unit and integration tests for the Course functionality.
5. **Documentation**: Update API documentation showcasing new course features.

## 8. Trade-offs and Decisions
- SQLite was maintained for development to simplify setup, with awareness that a more scalable database may be required in production scenarios.
- Direct validation in API endpoints allows for clear and immediate feedback to users, streamlining the development of a secure and functional course management feature.
- Avoided UI changes or complex integrations due to project scope restrictions, focusing solely on API functionality for course management.

## Conclusion
This implementation plan provides comprehensive guidance on enhancing the Student Management Web Application by introducing a new Course entity. By following established coding standards, maintaining a focus on testing and documentation, and adhering to best practices, this feature will enhance the application's capabilities for course management.

Existing Code Files:  
File: tests/test_courses.py (New Test File)
```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Assuming your FastAPI app is in src/main.py
from src.models import Course  # Assuming your SQLAlchemy model is defined in src/models.py
from sqlalchemy.orm import Session
from src.database import get_db  # Dependency that provides a database session

@pytest.fixture
def client():
    """Fixture for the test client."""
    with TestClient(app) as client:
        yield client

@pytest.fixture
def course_data():
    """Sample data for Course creation."""
    return {
        "name": "Introduction to Programming",
        "level": "Beginner"
    }

def test_create_course(client, course_data):
    """Test creating a course with valid data."""
    response = client.post("/courses", json=course_data)
    assert response.status_code == 201
    assert 'id' in response.json()
    assert response.json()["name"] == course_data["name"]
    assert response.json()["level"] == course_data["level"]

def test_create_course_missing_name(client):
    """Test creating a course without a name."""
    response = client.post("/courses", json={"level": "Intermediate"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name is required."}}

def test_create_course_missing_level(client):
    """Test creating a course without a level."""
    response = client.post("/courses", json={"name": "Advanced Algorithms"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Level is required."}}

def test_get_course(client):
    """Test retrieving a course by ID."""
    course_response = client.post("/courses", json={"name": "Data Structures", "level": "Intermediate"})
    course_id = course_response.json()["id"]
    
    response = client.get(f"/courses/{course_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Data Structures"
    assert response.json()["level"] == "Intermediate"

def test_get_course_not_found(client):
    """Test retrieving a non-existent course."""
    response = client.get("/courses/9999")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E003", "message": "Course not found."}}
```

This test suite includes basic tests for creating and retrieving course entities. Adjust the model imports based on your actual project structure.