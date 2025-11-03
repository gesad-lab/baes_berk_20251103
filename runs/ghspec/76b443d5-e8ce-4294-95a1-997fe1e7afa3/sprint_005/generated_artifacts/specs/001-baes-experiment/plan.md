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
This implementation plan outlines the architecture, technologies, and approach for adding a new `Teacher` entity to the educational management system. This feature will enhance the management of teacher data, enabling better organization and future functionalities related to teachers in the system.

## 2. Architecture

### 2.1 Application Structure
- **Frontend**: Not included in this scope (API only).
- **Backend**: RESTful API developed using Python and FastAPI, expanding the existing functionality to include Teacher management.
- **Database**: SQLite for development and testing, with migrations to introduce a new `Teachers` table.

### 2.2 Components
- **API Endpoints**:
  - **POST /teachers**: Create a new Teacher.
  - **GET /teachers/{teacherId}**: Retrieve details of a specific Teacher.

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
- **New Teacher Entity**:
  - `id`: Integer (Primary Key, auto-increment)
  - `name`: String (Required)
  - `email`: String (Required, Unique)

#### 4.1.1 Database Schema Creation
Create a new `Teacher` model:
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

### 4.2 Database Migration Strategy
Use Alembic migrations to create the new `teachers` table.
1. **Create Migration Script**:
   ```bash
   alembic revision --autogenerate -m "Add teachers table"
   ```

2. **Migrations will include**:
   - Creating the `teachers` table to store teacher information.

#### Migration Example
```python
def upgrade():
    op.create_table(
        'teachers',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('email', sa.String, nullable=False, unique=True)
    )

def downgrade():
    op.drop_table('teachers')
```

### 4.3 API Contract

#### 4.3.1 Create Teacher Endpoint
- **Endpoint**: `/teachers`
- **Method**: POST
- **Request Body**:
   ```json
   {
       "name": "string" (required),
       "email": "string" (required)
   }
   ```

- **Response** (201 Created): 
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

- **Error Response** (400 Bad Request - Missing Name):
```json
{
  "error": {
    "code": "E001",
    "message": "Name field is required."
  }
}
```

- **Error Response** (400 Bad Request - Invalid Email):
```json
{
  "error": {
    "code": "E002",
    "message": "Email format is invalid."
  }
}
```

#### 4.3.2 Retrieve Teacher Details Endpoint
- **Endpoint**: `/teachers/{teacherId}`
- **Method**: GET
- **Response** (200 OK):
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

- **Error Response** (404 Not Found - Teacher not found):
```json
{
  "error": {
    "code": "E003",
    "message": "Teacher not found."
  }
}
```

### 4.4 Error Handling & Validation
- Validate the presence of `name` and `email` fields during Teacher creation and return structured error messages as per the API contract.
- Use Pydantic models in FastAPI for automatic validation:
```python
from pydantic import BaseModel, EmailStr, validator

class TeacherCreateRequest(BaseModel):
    name: str
    email: EmailStr

    @validator('name')
    def check_name(cls, v):
        if not v:
            raise ValueError('Name field is required.')
        return v
```

### 4.5 Testing Strategy
- **Unit Tests**:
  - Create tests for the Teacher creation functionality and validation of the request body.

- **Integration Tests**:
  - Test `/teachers` and `/teachers/{teacherId}` endpoints to ensure correct behavior with valid and invalid input.

### 4.6 Startup Procedures
- Update FastAPI's startup procedure to apply migrations during startup:
```python
@app.on_event("startup")
async def startup():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")  # Ensure latest migrations run on startup
```

## 5. Scalability, Security, and Maintainability Considerations
- **Scalability**: While SQLite suffices for development, consider transitioning to PostgreSQL for production scalability.
- **Security**: Implement input validation rigorously alongside access controls to prevent unauthorized modifications.
- **Maintainability**: Maintain clean code practices, document API changes, and ensure unit tests are updated with each new endpoint or feature addition.

## 6. Documentation
- Automatic API documentation via FastAPI will be available at `/docs`.
- Update the `README.md` to provide directions regarding the new Teacher management functionality and how to utilize the endpoints.

## 7. Milestones
1. **Setup Migration**: Create and apply migrations to establish the `teachers` table.
2. **Create Teacher Model**: Implement the Teacher data model.
3. **Implement API Endpoints**: Develop the `/teachers` and `/teachers/{teacherId}` endpoints.
4. **Testing**: Create and run unit tests and integration tests for the new functionality.
5. **Documentation**: Ensure the `README.md` and API documentation reflect the changes made.

## 8. Trade-offs and Decisions
- Utilized SQLite for development to keep the setup straightforward. Note that a move to a more robust database like PostgreSQL is warranted for production.
- Engaged in direct validation of `name` and `email` at the API level for immediate user feedback.
- Focused solely on creating RESTful API endpoints without changes to UI or advanced features, limiting the scope solely to the API enhancements required for Teacher management.

## Conclusion
This implementation plan provides a comprehensive strategy for incorporating a Teacher entity into the educational management system following established coding practices. The outlined approach ensures maintainability and scalability while adding essential functionality to manage educators effectively.

### Existing Code Files
- **File**: `tests/test_teachers.py` (New Test File)
```python
import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

def test_create_teacher(client):
    response = client.post("/teachers", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john.doe@example.com"

def test_create_teacher_missing_name(client):
    response = client.post("/teachers", json={"email": "john.doe@example.com"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name field is required."}}

def test_create_teacher_invalid_email(client):
    response = client.post("/teachers", json={"name": "John Doe", "email": "invalid-email"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Email format is invalid."}}

def test_get_teacher_details(client):
    # Assume we have created a Teacher with ID 1
    response = client.get("/teachers/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_get_teacher_not_found(client):
    response = client.get("/teachers/9999")
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E003", "message": "Teacher not found."}}
``` 

This test suite ensures the success and error cases for the Teacher creation and retrieval functionality are covered comprehensively.