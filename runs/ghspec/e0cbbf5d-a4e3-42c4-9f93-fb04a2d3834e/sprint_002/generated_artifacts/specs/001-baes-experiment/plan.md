# Implementation Plan: Add Email Field to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Entity Web Application

## 1. Overview

This implementation plan outlines the architecture, technology stack, module boundaries, data models, and API contracts for extending the Student Entity Web Application by adding an `email` field to the existing "Student" entity. The goal of this enhancement is to improve student record management by allowing email addresses to be stored alongside student names, thereby facilitating better communication and record-keeping.

## 2. Technology Stack

- **Programming Language**: Python
- **Web Framework**: Flask
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing Framework**: pytest
- **Dependency Management**: pip (with requirements.txt)
- **Environment Management**: python-dotenv for environment variables

## 3. Architecture

### 3.1 Module Boundaries

- **API Layer**: Handles incoming HTTP requests and responses related to student records, including email.
- **Service Layer**: Contains business logic for creating and retrieving student records, including email validation.
- **Data Access Layer**: Utilizes SQLAlchemy for CRUD operations on the SQLite database.

### 3.2 Directory Structure
```
student_app/
├── src/
│   ├── controllers/
│   │   └── student_controller.py
│   ├── models/
│   │   └── student.py
│   ├── services/
│   │   └── student_service.py
│   ├── database/
│   │   └── db.py
│   ├── main.py
├── tests/
│   ├── test_student.py
└── requirements.txt
```

## 4. Data Models

The application will manage the following data model:

### 4.1 Student Model
```python
from sqlalchemy import Column, Integer, String
from database.db import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New column for email

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, email={self.email})>"
```

## 5. API Contracts

The application will provide the following updated API endpoints:

### 5.1 Create Student
- **Endpoint**: `POST /students`
- **Request Body**:
    ```json
    {
      "name": "string",
      "email": "string"
    }
    ```
- **Responses**:
    - **201 Created**:
      ```json
      {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com"
      }
      ```
    - **400 Bad Request**:
      ```json
      {
        "error": {
          "code": "E001",
          "message": "Name is required."
        }
      }
      ```

### 5.2 Retrieve Students
- **Endpoint**: `GET /students`
- **Responses**:
    - **200 OK**:
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

## 6. Implementation Approach

### 6.1 Database Initialization
- Modify the existing database schema to include the new `email` field. Ensure this is done through a migration.

### 6.2 Database Migration Strategy
- Create a migration script that alters the existing `students` table to add the `email` column. This script should preserve existing records and ensure that new records include an email value.

Sample migration code using Alembic (assuming Alembic is already set up):
```python
def upgrade():
    op.add_column('students', sa.Column('email', sa.String(), nullable=False))

def downgrade():
    op.drop_column('students', 'email')
```

### 6.3 Validation Logic
- Implement email validation logic in the service layer when creating a student to ensure that the email is in a valid format.

### 6.4 API Implementation Steps
1. **Create Flask App**:
   - Initialize the Flask application and configure necessary settings.
2. **Define Routes**:
   - Update routes for creating and retrieving Student records to handle email information.
3. **Implement Logic**:
   - In the service layer, implement logic to create and retrieve students with email, including validation of inputs.

Example `student_service.py` update:
```python
from email_validator import validate_email, EmailNotValidError

def create_student(name: str, email: str):
    try:
        # Validate email format
        validate_email(email)
    except EmailNotValidError as e:
        raise ValueError(f"Invalid email: {str(e)}")
    # Create student logic, including saving to the database
```

## 7. Testing Requirements

### 7.1 Unit Tests
- Implement tests for both updated endpoints:
  - `test_create_student`: Test successful student creation with valid name and email, and various invalid inputs (e.g., invalid email).
  - `test_retrieve_students`: Test retrieval of all students ensuring email is included.

```python
def test_create_student(client):
    response = client.post('/students', json={'name': 'John Doe', 'email': 'john@example.com'})
    assert response.status_code == 201
    assert 'id' in response.get_json()
    assert 'email' in response.get_json()

def test_create_student_with_invalid_email(client):
    response = client.post('/students', json={'name': 'John Doe', 'email': 'invalid-email'})
    assert response.status_code == 400
    assert response.get_json()['error']['message'] == "Invalid email format."
```

### 7.2 Integration Tests
- Implement integration tests to ensure the create and retrieve endpoints work together as expected, including checking the database state after operations.

## 8. Security Considerations
- Validate all user inputs to prevent SQL injection or data integrity issues.
- Sensitive data should never be logged, and error messages should not expose implementation details.

## 9. Deployment Considerations
- Use environment variables for configuration (database path, application settings).
- Provide a `.env.example` file to document necessary environment configurations.
- Ensure migration scripts run during deployment to update the database schema.

## 10. Success Criteria
- All specified endpoints must work correctly, returning the appropriate status codes and data formats as outlined in the API contracts.
- The application must handle invalid inputs gracefully with clear error messages.
- The database must be updated to include the `email` field without losing any existing data.

---

This implementation plan provides a comprehensive approach to enhancing the Student Entity Web Application by adding an `email` field, ensuring robustness, maintainability, and adherence to best practices in software development, while maintaining backward compatibility with existing features.