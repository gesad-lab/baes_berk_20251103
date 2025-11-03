# Implementation Plan: Add Email Field to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Web Application

## Overview
The purpose of this implementation plan is to outline the technical architecture, technology stack, module responsibilities, data models, API contracts, and key considerations for extending the existing Student entity by adding an email field. This addition aims to enhance data management capabilities and overall functionality of the Student Web Application.

## Technology Stack
- **Programming Language**: Python 3.11+
- **Web Framework**: FastAPI
- **Database**: SQLite (using SQLAlchemy for ORM)
- **Testing Framework**: pytest
- **API Documentation**: Swagger UI (integrated with FastAPI)
- **Environment Management**: Poetry (for dependency management)
- **Type Checking**: MyPy (for static type checking)

## Module Structure
The existing application structure will be updated as follows:
- **src/**
  - **main.py**: No changes required.
  - **models/**
    - `student.py`: 
        - **Modifications**: Extend `Student` entity to include the new `email` field.
  - **schemas/**:
    - `student_schema.py`:
        - **Modifications**: Update existing schemas to include `email` validation.
  - **routes/**:
    - `student_routes.py`:
        - **Modifications**: Update endpoints to handle the `email` field in POST and PUT requests.
  - **database/**:
    - `database.py`: 
        - **Modifications**: Include a new migration script to add the email column to the students table.
- **migrations/**: New directory for database migration scripts.
- **tests/**:
  - `test_student.py`: 
        - **Modifications**: Add tests for email validation and the new functionalities.

## Data Model
### Student Model
The updated Student entity will be defined using SQLAlchemy to include the `email` field:
```python
from sqlalchemy import Column, Integer, String
from database.database import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New field
```

### Pydantic Schema
Request and response validations will be updated in Pydantic to include email:
```python
from pydantic import BaseModel, constr, EmailStr

class StudentCreate(BaseModel):
    name: constr(min_length=1, max_length=100)
    email: EmailStr  # New field with Email validation

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Include email in response
```

## API Contracts
### Endpoints
1. **Create a Student**
   - **POST** `/students`
   - Request Body: `{"name": "John Doe", "email": "john@example.com"}`
   - Response: `201 Created` with student details in JSON.
  
2. **Retrieve a Student**
   - **GET** `/students/{id}`
   - Response: `200 OK` with student details in JSON including email or `404 Not Found` if student doesn't exist.
  
3. **Update a Student**
   - **PUT** `/students/{id}`
   - Request Body: `{"name": "Jane Smith", "email": "jane@example.com"}`
   - Response: `200 OK` with updated student details in JSON or `400 Bad Request` if invalid.
  
4. **Error Handling**
   - Handle invalid email scenarios and return `400 Bad Request` with a structured error message.

### Error Responses
- Must include the email-related error response: `{"error": {"code": "E002", "message": "Invalid email format"}}`

## Implementation Approach
1. **Setup Environment**
   - Use Poetry to install additional dependencies if needed.

2. **Database Migration**
   - Create a migration script in the `migrations/` folder to add an `email` column to the existing `students` table while retaining all existing data.
   ```python
   from sqlalchemy import create_engine, Column, String
   from sqlalchemy.sql import Table, MetaData

   engine = create_engine('sqlite:///./test.db')  # Use the appropriate database URL
   metadata = MetaData(bind=engine)
   students_table = Table('students', metadata, autoload_with=engine)

   with engine.connect() as conn:
       conn.execute(students_table.insert().values(email=''))  # Ensure column is added properly
   ```

3. **CRUD Functionality**
   - Modify `student_routes.py` to handle the new email field and maintain the API contract.

4. **Update Validations**
   - Update validations in the request schemas to include email checks.

5. **Testing**
   - Write new unit tests for email handling and enhanced functionality in `tests/test_student.py`.

6. **Documentation**
   - Update FastAPI automatic documentation to reflect the changes in API contracts.

## Scalability and Security Considerations
- The SQLite database will suffice for initial deployments; however, future migrations to a more robust database should be planned.
- Ensure that inputs, particularly the email field, are sanitized to prevent injection attacks.
- Use environment variables to manage sensitive data in production.

## Trade-offs and Decisions
- **框架选择**: FastAPI remains the framework of choice for its speed and automatic documentation.
- **数据迁移**: We leverage SQLAlchemy for column updates, ensuring existing data persist through migrations without data loss.
- **错误处理**: Explicit error messages are paramount to enhance user experience during validation failures.

## Conclusion
This implementation plan outlines the steps and considerations for integrating an email field into the existing Student Web Application. It aims to uphold code quality, maintainability, and best practices while enhancing functionality and data accuracy through RESTful API operations.

Existing Code Files:
File: `tests/test_student.py`
```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models.student import Student
from src.database.database import get_db, Base, engine

client = TestClient(app)

@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)  # Create the database tables
    yield
    Base.metadata.drop_all(bind=engine)    # Drop the database tables after tests

# New test cases for email functionality should be added here
def test_create_student_with_email():
    response = client.post("/students", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 201
    assert response.json()["email"] == "john@example.com"

def test_create_student_with_invalid_email():
    response = client.post("/students", json={"name": "John Doe", "email": "invalid-email"})
    assert response.status_code == 400
    assert response.json()["error"]["message"] == "Invalid email format"
```