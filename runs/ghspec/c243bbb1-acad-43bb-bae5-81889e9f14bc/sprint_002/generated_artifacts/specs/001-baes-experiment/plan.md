# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Entity Web Application

## I. Project Overview
This implementation plan details the architectural modifications, technology stack, module boundaries, and technical specifications required to enhance the existing Student entity by adding an email field. This will allow for comprehensive management of student information, and lay the groundwork for future functionalities such as communication systems.

---

## II. Technology Stack

- **Backend Framework**: FastAPI (Python) - For building the RESTful API.
- **Database**: SQLite - A lightweight database for data persistence.
- **HTTP Client for Testing**: HTTPX - For making API calls in testing.
- **Asynchronous Support**: Uvicorn - ASGI server to run the FastAPI application.

---

## III. Architecture & Modules

### 3.1 High-Level Architecture
- **API Layer**: Handles all incoming HTTP requests and routes them to the appropriate service.
- **Service Layer**: Contains the business logic for adding and retrieving student records.
- **Data Access Layer**: Interacts with the SQLite database to perform CRUD operations on student data.

### 3.2 Module Responsibilities

1. **API Module (`api/`)**:
   - Endpoint definitions for creating and retrieving students, including email handling.
   - Input validation and crafting of JSON responses.

2. **Service Module (`services/`)**:
   - Business logic for creating a student, including validation for email.
   - Logic for retrieving all students.

3. **Data Access Module (`db/`)**:
   - Database model for the Student entity, now including the email field.
   - Functions for database interactions (e.g., schema creation, CRUD operations).

---

## IV. Data Models

### SQLite Database Model

```python
from sqlalchemy import Column, Integer, String
from database import Base
import re

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate email format."""
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None
```

---

## V. API Endpoints

### 5.1 API Design

1. **POST `/students`**:
   - **Request Body**:
     - `name` (string, required)
     - `email` (string, required, must be a valid email format)
   - **Response**:
     ```json
     {
       "message": "Student created successfully",
       "student": {
         "id": 1,
         "name": "John Doe",
         "email": "john@example.com"
       }
     }
     ```
   - **Error Handling**:
     - Status 400: Missing name or email field.
     ```json
     {
       "error": {
         "code": "E001",
         "message": "Name field is required."
       }
     }
     ```
     - Status 400: Invalid email format.
     ```json
     {
       "error": {
         "code": "E002",
         "message": "Email field must be a valid email address."
       }
     }
     ```

2. **GET `/students`**:
   - **Response**:
   ```json
   [
     {
       "id": 1,
       "name": "John Doe",
       "email": "john@example.com"
     },
     {
       "id": 2,
       "name": "Jane Smith",
       "email": "jane@example.com"
     }
   ]
   ```

---

## VI. Implementation Steps

1. **Project Update**:
   - Maintain the existing project structure:
     ```
     student-management/
     ├── api/
     ├── db/
     ├── services/
     ├── main.py
     ├── requirements.txt
     └── README.md
     ```

2. **Update Requirements**:
   - Above dependencies remain as is, ensuring no modifications required in `requirements.txt`.

3. **Database Schema Migration**:
   - Create a migration script to alter the existing database schema to add the `email` field to the `students` table:
   ```python
   from sqlalchemy import create_engine, MetaData, Table, Column, String

   engine = create_engine('sqlite:///students.db')
   metadata = MetaData(bind=engine)

   students = Table('students', metadata, autoload_with=engine)
   with engine.begin() as connection:
       connection.execute(f'ALTER TABLE {students.name} ADD COLUMN email VARCHAR NOT NULL')
   ```

4. **Implement API Endpoints**:
   - Define API endpoints in the `api` module, implementing validation with Pydantic models for requests that include email validation.

5. **Implement Business Logic**:
   - Create service functions for the creation and retrieval of student records, ensuring email validation is enforced during these operations.

6. **Testing**:
   - Write unit tests for service functions to ensure email validation and data integrity.
   - Implement integration tests for API endpoints using `httpx` to validate responses for both successful and erroneous requests involving email fields.

---

## VII. Testing Strategy

### 7.1 Test Coverage
- Aim for at least 70% coverage on business logic.
- Validate critical paths (student creation with email and retrieval) with 90%+ coverage.

### 7.2 Types of Tests
- **Unit Tests**: Ensure individual functions (particularly validation) function as expected.
- **Integration Tests**: Validate API endpoints to ensure functionality and error handling work correctly.

---

## VIII. Error Handling and Input Validation

### 8.1 Input Validation
- Validate that both name and email fields are provided when creating a student.
- Implement responses for invalid or missing input, returning consistent JSON error responses.

### 8.2 Error Responses
- Structure error responses to match JSON format outlined in API Design.

---

## IX. Security Considerations

### 9.1 Data Protection
- Input sanitization and validation strategies to prevent SQL injection risks.
- While not implemented in this phase, set up a `.env` structure for future configuration of secrets and sensitive data.

---

## X. Deployment Considerations

### 10.1 Local Development
- Verify that the application starts without configuration errors, generates the updated database schema, and successfully completes migrations.

---

## XI. Logging & Monitoring

### 11.1 Basic Logging
- Implement basic logging for API interactions to track requests and responses, focusing on error handling, although extensive logging is out of scope for this phase.

---

## XII. Conclusion

This implementation plan outlines the necessary steps to enhance the Student entity by adding an email field. By adhering to the structured approach detailed in this plan, we will effectively implement the feature while maintaining existing system functionalities, ensuring a robust, user-friendly API for managing student records.

Existing Code Files:
No code files found from the previous sprint.

Instructions for Technical Plan:
1. Utilize the same tech stack as the previous sprint.
2. Define integration points and modifications necessary to existing files without replacing them.
3. Ensure that all changes remain backward compatible with existing models.
4. Outline a database migration strategy to accommodate the new data structure.
