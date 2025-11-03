# Implementation Plan: Add Email Field to Student Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

**Previous Sprint Plan:**  
# Implementation Plan: Student Management Web Application

## I. Architecture Overview

The Student Management Web Application will continue following the previously established microservice architecture. The addition of the email field to the Student entity requires modifications in the API layer and the database layer while maintaining the existing structure.

## II. Technology Stack

- **Programming Language:** Python 3.11+
- **Web Framework:** FastAPI
- **Data Persistence:** SQLite
- **Data Access Library:** SQLAlchemy
- **Testing Framework:** Pytest
- **Dependency Management:** Poetry
- **Configuration Management:** Environment variables and a `.env` file

## III. Module Boundaries and Responsibilities

### 1. API Layer
- **Routes**:
  - `POST /students`: Create a new student (now with email).
  - `GET /students/{id}`: Retrieve a student by ID (with email included).

### 2. Service Layer
- **StudentService**: 
  - `create_student(name: str, email: str)`: Validates input (including email) and saves a new student to the database.
  - `get_student_by_id(student_id: int)`: Retrieves a student’s details (including email) from the database.

### 3. Data Layer
- **Database Configuration and Models**:
  - Modify the **Student model** to include the email field:
    ```python
    class Student(Base):
        __tablename__ = 'students'

        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String, nullable=False)
        email = Column(String, nullable=False)  # New field
    ```

## IV. API Contracts

### 1. Create Student Endpoint
- **Endpoint:** `POST /students`
- **Request**: 
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```
- **Response**:
  - **Success** (201 Created):
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **Error** (400 Bad Request):
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Email field is required."
      }
    }
    ```

### 2. Retrieve Student Endpoint
- **Endpoint:** `GET /students/{id}`
- **Response**:
  - **Success** (200 OK):
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **Error** (404 Not Found):
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Student not found."
      }
    }
    ```

## V. Database Schema

The application will require a migration to add the email field to the Student entity. The migration strategy includes:
1. Create a new migration file to add the `email` column:
   ```python
   from sqlalchemy import Column, String, Integer
   from ..model import Base

   class Migration_AddEmailToStudent(Base):
       __tablename__ = "migrations"
      
       id = Column(Integer, primary_key=True)
       # Migration to add email field
       def upgrade():
           op.add_column('students', sa.Column('email', sa.String(), nullable=False))
   
       def downgrade():
           op.drop_column('students', 'email')
   ```

## VI. Implementation Approach

1. **Setup Development Environment**:
   - Ensure the environment is set up with the necessary dependencies from Poetry.
   - Update the `.env` file as necessary.

2. **Modify API Endpoints**:
   - Update the `POST` route in FastAPI to accept the email field in requests.
   - Ensure correct handling of HTTP status codes and error responses for missing fields.

3. **Implement Service Logic**:
   - Update the `StudentService` class to validate the email input and handle errors.
   ```python
   def create_student(name: str, email: str):
       if not email:
           raise ValueError("Email field is required.")
   ```

4. **Database Layer with SQLAlchemy Modifications**:
   - Update the SQLite `students` table schema to include the `email` field.
   - Implement retrieval and creation methods that now include handling the email field.

5. **Create Tests**:
   - Update existing tests in `tests/api/test_routes.py` and `tests/services/test_student_service.py` to validate the email functionality:
     - Test creating a student with valid name and email.
     - Test error handling when the email is missing.

6. **Documentation**:
   - Update the API documentation to reflect changes in the request and response structures.
   - Document all modifications within the codebase.

7. **Run Migrations**:
   - Ensure that the application starts without errors and runs the migration to add the email field.
   - Validate that the updates reflect on the SQLite database without losing existing data.

## VII. Security & Error Handling

- **Input Validation**: Ensure that the email format is valid (simple regex check can be implemented in `create_student`).
- **Error Messages**: Define structured error responses for both missing name and email fields without revealing internal structure.

## VIII. Testing Strategies

- Implement unit tests for the `StudentService` class to cover:
  - Valid student creation.
  - Handling missing name and email inputs.
  - Successful retrieval of student data.
- Implement integration tests to validate the API behavior and responses.

## IX. Monitoring & Logging

- Implement structured logging with requests and error details in JSON format to track API usage patterns and issues.
- Establish basic monitoring for application health checks, ensuring the API is responsive.

## X. Success Criteria

1. The application must successfully respond to valid requests for creating and retrieving students, including the email field.
2. It must handle errors gracefully and return meaningful messages for missing inputs.
3. The implementation should maintain backward compatibility and be easy to manage for future changes.

## Existing Code Files Modifications

- **`src/models.py`:** Modify the Student model to include the `email` field.
- **`src/services/student_service.py`:** Update `create_student` method to handle email validations.
- **`src/main.py`:** Ensure routes are properly handling new request fields.
- **`tests/api/test_routes.py`:** Add tests for new email field scenarios.
- **`tests/services/test_student_service.py`:** Update tests to validate email handling.

By following this implementation plan, we can ensure a smooth transition to incorporating the email field into the existing Student entity while adhering to our established coding standards and policies.