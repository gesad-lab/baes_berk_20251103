# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## I. Architecture Overview

The architecture remains unchanged. The application will continue to use a microservices architecture with a RESTful API allowing CRUD operations on the Student entity. However, modifications will be made to accommodate the new email field in both the API and database schema.

## II. Technology Stack

- **Programming Language**: Python 3.11
- **Web Framework**: Flask
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing Framework**: pytest
- **Environment Management**: pip

## III. Module Boundaries and Responsibilities

### 1. API Layer
- Extend API endpoints to manage the email field in the Student entity.

### 2. Service Layer
- Update service functions to include email handling during creation and updates.

### 3. Data Access Layer
- Modify the SQLAlchemy model and implement a migration strategy for adding the email field.

### 4. Validation Layer
- Update validation logic for newly added email inputs.

## IV. Data Models

### 1. Updated Student Model
The Student model will be updated to include the email field:
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New email field, required
```

### 2. Database Initialization
- The initialization code in existing files will be augmented to handle the new column during migrations.

## V. API Contracts

### 1. Create a Student
- **Endpoint**: `POST /students`
- **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"  // Added email field
    }
    ```
- **Response**:
    - **Status**: 201 Created
    - **Body**:
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"  // Included in response
    }
    ```

### 2. Retrieve All Students
- **Endpoint**: `GET /students`
- **Response**:
    - **Status**: 200 OK
    - **Body**:
    ```json
    [
      {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"  // Included in response
      }
    ]
    ```

### 3. Update Existing Student Email
- **Endpoint**: `PUT /students/{id}`
- **Request Body**:
    ```json
    {
      "email": "john.newemail@example.com"  // Updated email
    }
    ```
- **Response**:
    - **Status**: 200 OK
    - **Body**:
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.newemail@example.com"  // Updated in response
    }
    ```

## VI. Implementation Approach

### 1. Development Steps
1. **Modify Project Structure**:
   - Ensure existing directory structure under `src/` remains compatible.
   - Update the model to include the new email field; this requires schema migration.

2. **API Layer Update**:
   - Extend the `POST /students` endpoint to include email handling.
   - Update the `PUT /students/{id}` endpoint to modify student emails.

3. **Service Layer Implementation**:
   - Modify service functions (`create_student`, `update_student`) to handle email inputs:
     - Ensure email is correctly saved and retrieved.
     - Validate email format.

4. **Validation Layer**:
   - Update validation logic to include email format checks (basic regex for email validation).

5. **Database Migration**:
   - Create migration script using Alembic for database schema update:
   - Ideally, the migration will look like this:
     ```python
     from sqlalchemy import Column, String, Integer
     from alembic import op

     def upgrade():
         op.add_column('students', Column('email', String, nullable=False))

     def downgrade():
         op.drop_column('students', 'email')
     ```

### 2. Testing Strategy
- **Unit Tests**: Include tests for email validation, both for creating and updating students.
- **Integration Tests**: Ensure the API's functionality works correctly with the new email field:
  - Use existing test structures in `tests/test_student_api.py` and `tests/test_student_service.py`.

## VII. Error Handling & Validation

- Input validation will ensure email is present and formatted correctly.
- Respond with clear error messages for invalid email formats.
- Implement logging of unexpected errors with context while avoiding sensitive information in logs.

## VIII. Security Considerations

- Confirm that email addresses are not subjected to SQL injection via ORM.
- As before, no sensitive data will be logged, and response errors will not reveal internal details.

## IX. Deployment Considerations

- Ensure migrations run as part of the deployment steps.
- Document how to run migrations in `README.md`.
- Include environment variable instructions for database connection strings.

## X. Documentation

- Update Docstrings: Ensure that all API functions are well-documented, especially around the new email handling.
- Update `README.md` to reflect changes in API contracts and usage examples.
- Ensure migration strategies are documented clearly for future reference.

With this plan, we aim to enhance the Student Management Web Application by adding email management capabilities while following best practices and maintaining backwards compatibility with existing functionalities.