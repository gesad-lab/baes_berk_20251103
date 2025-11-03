# Implementation Plan: Add Email Field to Student Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:  
# Implementation Plan: Student Entity Management Web Application

## I. Architecture Overview

The application will continue to utilize a microservices architecture with clear boundaries between modules. The core components remain the same:

1. **Web Server**: FastAPI will manage HTTP requests and serve API endpoints.
2. **Database**: SQLite will persist student records efficiently.

### Tech Stack
- **Web Framework**: FastAPI (Python 3.11+)
- **Database**: SQLite
- **Data Serialization**: Pydantic (for request and response validation)
- **Testing Framework**: pytest

## II. Module Boundaries

1. **API Module**:
   - Extend routes and HTTP request handling for managing students to include the email field.
   - Implement updated CRUD operations to support the new functionality outlined in the specification.

2. **Database Module**:
   - Extend the data model to add the email field.
   - Update schema management to ensure the database structure reflects changes without losing existing data.

3. **Error Handling Module**: (Basic level)
   - Update to handle validation for the email field input.

4. **Testing Module**:
   - Implement tests reflecting the new scenarios associated with the email field.

## III. Data Models

### Updated Student Model
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New email field added
```

### Updated API Request and Response Models
```python
from pydantic import BaseModel, EmailStr  # Import EmailStr for email validation

class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Update to include email as a required field

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str  # Include email in response model
```

## IV. API Endpoints

### 1. Create a Student
- **Endpoint**: `/students`
- **Method**: POST
- **Request Body**: 
```json
{
    "name": "John Doe",
    "email": "john.doe@example.com"
}
```
- **Response (201 Created)**:
```json
{
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
}
```

### 2. Retrieve a Single Student by ID
- **Endpoint**: `/students/{id}`
- **Method**: GET
- **Response (200 OK)**:
```json
{
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
}
```

### 3. Update a Student's Email
- **Endpoint**: `/students/{id}`
- **Method**: PUT
- **Request Body**: 
```json
{
    "email": "new.email@example.com"
}
```
- **Response (200 OK)**:
```json
{
    "id": 1,
    "name": "John Doe",
    "email": "new.email@example.com"
}
```

## V. Implementation Approach

1. **Set Up Environment**:
   - Verify that Python 3.11+ and SQLite are available.
   - No change in the project structure, existing organization is sufficient.

2. **Implement API Logic**:
   - Extend FastAPI routes in `student_api.py` to include new `POST` and `PUT` endpoints for email management.

3. **Set Up Database**:
   - Update `db_setup.py` to modify the SQLite schema, adding the `email` column with appropriate validations.

4. **Database Migration Strategy**:
   - Create a new migration script that adds the email column to the existing `students` table without data loss.
   - Use SQLite's `ALTER TABLE` command to ensure the existing data remains intact.

## VI. Error Handling

- Update error handling in the API to check for valid inputs for email and handle errors appropriately by returning meaningful messages in case of invalid data provided during creation or updates.

## VII. Success Criteria Verification

- Validate that creating a student works as expected with valid name and email, returning both fields in response.
- Ensure that retrieving students includes their email.
- Confirm that updating a student's email correctly modifies the record and reflects changes on retrieval.

## VIII. Testing Strategy

1. **Unit Tests**: Cover new functionality, including the added email field.
2. **Integration Tests**: Validate endpoint functionality by ensuring that correctly formatted requests/updates can be processed and that students can be created, retrieved, and updated without issues:
   - Implement tests for creation, retrieval, and update of student records.

## IX. Documentation

- Update the `README.md` to reflect new API endpoints, request and response formats, and example payloads.
- Include migration instructions if necessary.

## X. Version Control Practices

- Follow best practices by committing changes in small increments, focusing on logical unit changes.
- Update documentation alongside code changes.

## XI. Deployment Considerations

- Ensure appropriate database migrations are ready to apply during deployment.
- Validate that the application can start successfully with the new feature included, with no manual intervention required during startup.

By following this implementation plan, the enhancement of the Student entity to include an email field can be achieved effectively while ensuring adherence to the architectural principles and code quality guidelines established in previous sprints.