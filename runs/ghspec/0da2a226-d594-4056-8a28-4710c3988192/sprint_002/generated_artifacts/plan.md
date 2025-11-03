# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Entity Web Application

## Version
1.0.1

## Overview
This implementation plan outlines the steps to enhance the existing Student Entity Web Application by adding an email field to the Student entity. The new feature will allow for improved data management and retrieval of student records, ensuring that each student's email address is stored and returned alongside their name.

## Architecture Overview
- **Architecture Pattern**: RESTful microservice (as per previous design)
- **Components**:
  - API Layer: Updated to include email handling in CRUD operations.
  - Service Layer: Business logic adjusted to manage email in student entities.
  - Data Layer: SQLite database schema to be modified to include the email field.
- **Deployment**: Remains unchanged, using a lightweight server with the existing web framework.

## Technology Stack
- **Backend Framework**: FastAPI (Python)
- **Database**: SQLite
- **ORM**: SQLAlchemy (for database interactions)
- **Data Format**: JSON
- **Testing Framework**: pytest
- **Containerization**: Docker (optional for deployment)
- **Version Control**: Git

## Module Boundaries and Responsibilities

### 1. API Layer
- **Module Name**: `api`
- **Responsibilities**:
  - Update routes for CRUD operations to handle the email field.
  - Validate incoming requests for the email field in addition to the name.

### 2. Service Layer
- **Module Name**: `services`
- **Responsibilities**:
  - Implement updated business logic in `student_service.py` to manage email along with names during create, retrieve, and update operations.

### 3. Data Layer
- **Module Name**: `models`
- **Responsibilities**:
  - Modify the existing Student entity schema to include the new email field using SQLAlchemy.
  - Handle migrations to ensure the new schema maintains data integrity.

## Implementation Approach

### Project Structure
```
student_entity_app/
│
├── src/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py          # Update API endpoints
│   │   └── dependencies.py     # Dependency functions
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── student_service.py  # Update business logic for students
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── models.py           # Update Student model
│   │
│   ├── main.py                 # Application entry point
│   └── config.py               # Configuration settings
│
├── tests/
│   ├── __init__.py
│   ├── test_routes.py          # Unit tests for API endpoints
│   └── test_services.py        # Unit tests for business logic
│
├── .env.example                 # Sample environment variables
├── requirements.txt             # Project dependencies
└── README.md                    # Documentation
```

### Step-by-Step Implementation

1. **Update Data Models**
   - Modify `models.py` to define the `Student` entity, adding an `email` field:
   ```python
   from sqlalchemy import Column, Integer, String
   from sqlalchemy.ext.declarative import declarative_base

   Base = declarative_base()

   class Student(Base):
       __tablename__ = 'students'

       id = Column(Integer, primary_key=True, autoincrement=True)
       name = Column(String, nullable=False)
       email = Column(String, nullable=False)  # New email field
   ```

2. **Database Migration Strategy**
   - Use Alembic for handling database migrations. Create a migration script that:
     - Adds the email column to the existing Student table without losing data.
   ```bash
   alembic revision --autogenerate -m "Add email field to Student"
   ```

3. **Implement Services Logic**
   - Update functions in `student_service.py`:
     - `create_student(name: str, email: str)`: to accept and store the email.
     - `get_student(student_id: int)`: to retrieve email along with name.
     - `update_student(student_id: int, new_email: str)`: to update email.
   ```python
   def create_student(name: str, email: str):
       # Create student with both name and email
       new_student = Student(name=name, email=email)
       # Add to session and commit...
   ```

4. **Define API Endpoints**
   - In `routes.py`, update POST, GET, and PUT endpoints to handle email:
   - **POST** `/students`:
     - Request body should include both `name` and `email`.
     ```json
     {
       "name": "John Doe",
       "email": "john@example.com"
     }
     ```
   - **GET** `/students/{id}`: Update response JSON structure to include email:
     ```json
     {
       "id": 1,
       "name": "John Doe",
       "email": "john@example.com"
     }
     ```
   - **PUT** `/students/{id}`: Update to allow email modification:
     ```json
     {
       "email": "john.doe@example.com"
     }
     ```

5. **Implement Input Validation**
   - Update Pydantic models to validate the email field alongside the name.

6. **Error Handling**
   - Enhance error handling to include validation for the email field (required, proper format).

7. **Testing**
   - Expand `test_services.py` and `test_routes.py` to cover scenarios for creating, retrieving, and updating students with the new email field.
   - Implement tests for handling missing email scenarios:
   ```python
   def test_create_student_without_email():
       response = client.post("/students", json={"name": "John Doe"})
       assert response.status_code == 422  # Unprocessable Entity
       assert "email" in response.json()["detail"][0]["loc"]
   ```

8. **Documentation**
   - Update `README.md` to include instructions about the new email feature and examples of how to use the updated API endpoints.

## Data Models

### Updated Student Entity
```json
{
  "id": "integer (primary key, automatically generated)",
  "name": "string (required)",
  "email": "string (required)"
}
```

## API Contracts

### Create Student
- **Endpoint**: POST `/students`
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  }
  ```

### Retrieve Student
- **Endpoint**: GET `/students/{id}`
- **Response**:
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  }
  ```

### Update Student
- **Endpoint**: PUT `/students/{id}`
- **Request Body**:
  ```json
  {
    "email": "john.doe@example.com"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

### Error Response for Missing Email
- **Response (400)**:
  ```json
  {
    "error": {
      "code": "E001",
      "message": "Email is required.",
      "details": {}
    }
  }
  ```

## Success Criteria
- All API endpoints must now respond with valid JSON including the email field.
- Full pass for all specified user scenarios with added email functionalities.
- Proper error handling for cases where the email field is missing.
- Successful confirmation of data migration with both names and emails present in SQLite database.

## Final Considerations
### Scalability
- While SQLite suffices for early stages, consider PostgreSQL for future scalability as user data grows.

### Security
- Ensure appropriate validation and sanitization steps are taken for both name and email inputs to avoid injection vulnerabilities.

### Maintainability
- Adhering to clean code practices and the defined project structure promotes maintainability throughout future implementations.

### Logging and Monitoring
- Integrate structured logging mechanisms for tracking critical events in the application life cycle. 

---

This plan outlines a clear path to implement the requested feature while ensuring continuity with existing code, maintaining backward compatibility, and adhering to previous coding standards.