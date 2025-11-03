# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Entity Management

## Version
1.1.0

## Purpose
To extend the existing `Student` entity functionality by adding a new required `email` field to improve data collection and communication capabilities without disrupting current functionalities.

## Architecture Overview
The application maintains a microservices architecture focusing on RESTful APIs. The backend is developed using Python with FastAPI, and SQLite remains the chosen database. The enhancement will be seamlessly integrated into the existing structure while maintaining the extensibility of the application.

## Technology Stack
- **Backend Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing**: pytest

## Module Boundaries and Responsibilities
1. **API Layer**:
   - Updates current endpoints for CRUD operations related to `Student` to include the new `email` field.

2. **Service Layer**:
   - Enhances business logic to support email validation and management in conjunction with existing operations.

3. **Persistence Layer**:
   - Facilitates schema updates in conjunction with SQLAlchemy to maintain data integrity.

## Data Models and API Contracts

### Data Model: Student
```python
from sqlalchemy import Column, Integer, String

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New field added here
```

### API Endpoints
1. **Create Student**
   - **Endpoint**: `POST /students`
   - **Request Body**: `{ "name": "string", "email": "string" }`
   - **Response**: 
     - 201 Created: `{ "id": integer, "name": "string", "email": "string" }`
     - 400 Bad Request if `name` or `email` is missing or invalid.

2. **Retrieve Student**
   - **Endpoint**: `GET /students/{student_id}`
   - **Response**: 
     - 200 OK: `{ "id": integer, "name": "string", "email": "string" }`
     - 404 Not Found if `student_id` does not exist.

3. **Update Student**
   - **Endpoint**: `PUT /students/{student_id}`
   - **Request Body**: `{ "name": "string", "email": "string" }`
   - **Response**: 
     - 200 OK: `{ "id": integer, "name": "string", "email": "string" }`
     - 404 Not Found if `student_id` does not exist.
     - 400 Bad Request if `name` or `email` is invalid.

## Implementation Approach

### 1. Project Initialization
- Update existing FastAPI project structure as follows:
  ```
  src/
  ├── main.py
  ├── models.py       # Updated to include the email field
  ├── services.py     # Updated to handle email logic
  ├── api.py          # Updated to reflect new endpoints
  ├── database.py     # Schema updates handled here
  tests/
  ├── test_api.py     # Updated tests for API endpoints including email
  ├── test_services.py # Updated tests for email-related logic
  ```

### 2. Database Migration
- **Alembic**: Implement database migrations using Alembic to add the `email` column to the `students` table while preserving existing data:
  ```python
  from alembic import op
  import sqlalchemy as sa

  def upgrade():
      op.add_column('students', sa.Column('email', sa.String(), nullable=False))

  def downgrade():
      op.drop_column('students', 'email')
  ```

### 3. API Implementation
- Modify existing API endpoints in `api.py` to handle the `email` field.
- Ensure proper validation of email format in the `POST` and `PUT` endpoints.

### 4. Business Logic Update
- Modify service functions in `services.py` to incorporate email handling, validation logic (using regex for format validation), and appropriate return values upon success or failure of operations.

### 5. Input Validation
- Use Pydantic models for input validation in FastAPI to ensure that the newly introduced email adheres to required formats:
```python
from pydantic import BaseModel, EmailStr

class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Use EmailStr for email validation

class StudentUpdate(BaseModel):
    name: str = None
    email: EmailStr = None  # Optional update
```

### 6. Testing
- Write unit tests in `test_services.py` to validate email handling (including creation with valid/invalid emails).
- Update `test_api.py` to include scenarios ensuring correct responses for endpoints concerning email functionalities.

### 7. Docker Setup
- Ensure that Dockerfile and Docker Compose configurations support new database migrations upon startup. Maintain seamless integration into the existing deployment pipeline.

## Scalability, Security, and Maintainability Considerations
- Continue using environment variables for configuration management.
- Implement robust error handling for invalid email input.
- Maintain modularity and clear function responsibilities to facilitate future enhancements.

## Trade-Offs and Decisions
- **Mandatory Email Field**: As a critical user requirement, the email field is made mandatory to enhance communication capabilities, thus increasing complexity in input validation.
- **No External Libraries for Email Validation**: Built-in Pydantic types are used for email validation instead of third-party libraries to maintain simplicity and reduce dependencies.

### Success Criteria
- Ensure response times for endpoints regarding the email functionality meet the 500 ms threshold.
- Total coverage for business logic concerning emails reaches at least 70% through proper unit and integration testing.

## Deployment Considerations
- Review Docker configurations to ensure smooth deployments with updated migrations.
- Maintain backward compatibility with existing student data while safely handling schema modifications in migrations.

## Conclusion
This implementation plan outlines the necessary steps for integrating the email field into the Student entity while maintaining existing functionalities. The detailed approach ensures compliance with best practices for future maintainability and scalability.