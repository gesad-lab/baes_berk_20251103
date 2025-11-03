# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Entity Web Application

## I. Overview

The purpose of this implementation plan is to outline the steps required to enhance the Student entity by adding an email field as a required string attribute. This change will improve student management capabilities and support future communication functionalities. The existing architecture and technology stack will be reused to ensure consistency and maintainability of the application.

## II. Architecture

### 2.1 Architectural Overview
The application will continue to use a RESTful architecture, allowing clients to interact with the extended Student entity through well-defined API endpoints. The email field will be introduced without disrupting existing functionalities.

### 2.2 Components
1. **API Layer**: Updates to handle the email field for creation and updates to Student records.
2. **Service Layer**: Extended to include email validation and interaction logic.
3. **Data Access Layer (DAL)**: Updated to include the email field in database operations.
4. **Database**: SQLite will be modified with a migration to include the email field.

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
  - `POST /students`: Create a new Student (now requires `name` and `email`)
  - `GET /students/{id}`: Retrieve a Student by ID (includes email)
  - `PUT /students/{id}`: Update a Student by ID (includes email field)

### 4.2 Service Layer
- Business logic will include:
  - Validation for the email format during creation and updates.
  
### 4.3 Data Access Layer
- Responsible for database interactions, including:
  - Schema migrations for the email field addition.
  - CRUD operations for both the existing and new fields.

## V. Data Models

### 5.1 Student Entity Model
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New Field
```

## VI. API Contracts

### 6.1 Request/Response Format

1. **Create Student** (`POST /students`)
   - **Request**: 
     ```json
     {
         "name": "John Doe",
         "email": "john.doe@example.com"
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

2. **Retrieve Student** (`GET /students/{id}`)
   - **Response** (200 OK):
     ```json
     {
         "id": 1,
         "name": "John Doe",
         "email": "john.doe@example.com"
     }
     ```

3. **Update Student** (`PUT /students/{id}`)
   - **Request**:
     ```json
     {
         "name": "Jane Doe",
         "email": "jane.doe@example.com"
     }
     ```
   - **Response** (200 OK):
     ```json
     {
         "id": 1,
         "name": "Jane Doe",
         "email": "jane.doe@example.com"
     }
     ```

### 6.2 Error Responses
- **Validation Error for Email**:
```json
{
    "error": {
        "code": "E002",
        "message": "Invalid email format."
    }
}
```

## VII. Error Handling

- Validate email format using regex in the service layer during create and update operations.
- Provide detailed error messages for invalid inputs to enhance user experience and aid debugging.

## VIII. Implementation Steps

1. **Database Migration**:
   - Create a migration script to add the `email` column to the existing Student table.
   - Use Alembic or a similar tool for managing schema changes.
   ```sql
   ALTER TABLE students ADD COLUMN email VARCHAR NOT NULL;
   ```

2. **Update Data Access Layer**:
   - Modify the Student model to include the `email` field.
   - Ensure the email field is not nullable.

3. **Modify API Endpoints**:
   - Update the `POST /students` endpoint to require both `name` and `email`.
   - Update the `PUT /students/{id}` endpoint to allow updates for `email`.

4. **Enhance Service Layer**:
   - Implement email validation logic using regular expressions.
   - Integrate enhancements in the create and update methods.

5. **Write Tests**:
   - Create unit tests for email validation and new API endpoint behavior.
   - Ensure coverage meets or exceeds 70% for new features.

6. **Documentation**:
   - Update API documentation to reflect changes, including the new email field.
   - Document the database migration process in the README.

7. **End-to-End Testing**:
   - Ensure existing and new functionality works seamlessly together.

8. **Deployment**:
   - Implement the modifications and validate in a staging environment before promoting to production.

## IX. Testing Strategy

- Implement automated tests in line with existing test structure for:
  - Unit tests of service methods to validate email formatting and business logic.
  - Integration tests for new API endpoints handling.

## X. Deployment Considerations

- Confirm all environment configurations include variables for database connectivity.
- Clearly document migration strategies and test thoroughly to avoid disruptions.

## XI. Conclusion

This implementation plan provides a structured approach to extend the Student entity by adding an email field without interfering with existing functionality. By utilizing the established architecture and technology stack, we ensure a consistent and reliable application with improved capabilities for managing student data. 

Existing Code Modifications:
- **Student Entity Model**: Update to include the `email` attribute.
- **API endpoints**: Adjustments in request payloads and response formats to include `email`.
- **Testing**: New tests must be implemented to cover scenarios related to email input.

```python
# Migration script example
# migration.py
"""Add email column to students

Revision ID: <unique_id>
"""
from sqlalchemy import Column, String
from alembic import op

def upgrade():
    op.add_column('students', Column('email', String, nullable=False))

def downgrade():
    op.drop_column('students', 'email')
```