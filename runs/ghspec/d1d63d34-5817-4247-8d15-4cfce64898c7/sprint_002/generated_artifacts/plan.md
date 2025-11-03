# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Application

## Technical Architecture

### 1. Architecture Overview
The Student Management Application expansion maintains its previously established architecture. This will remain a RESTful API using FastAPI and SQLAlchemy to manage student data. The core addition is the integration of an `email` field into the Student entity and updating related operations without disrupting existing functionalities.

### 2. Technology Stack
- **Programming Language**: Python
- **Web Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Deployment**: Docker
- **Testing Framework**: Pytest

---

## Module Design

### 1. Module Responsibilities
- **Student Module**: Enhanced to manage the new `email` property alongside the existing `name` property.
- **Database Module**: To handle database connections and migrations, ensuring existing data integrity during schema updates.

### 2. Class/Function Design
- **Student Class**:
  Attributes:
  - `id`: Integer (auto-generated, primary key)
  - `name`: String (required)
  - `email`: String (required, valid email format)

```python
from pydantic import BaseModel, EmailStr

class Student(BaseModel):
    id: int
    name: str
    email: EmailStr
```

- **CRUD Operations**:
  - `create_student(name: str, email: str) -> Student`
  - `get_student(student_id: int) -> Student`
  - `update_student(student_id: int, name: Optional[str], email: Optional[str]) -> Student`
  - `delete_student(student_id: int) -> None`
  - `list_students() -> List[Student]`

### 3. API Endpoints
- **Create Student**:
  - **Method**: POST
  - **Endpoint**: `/students`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **Response**:
    - 201 Created:
      ```json
      {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
      ```

- **Get Student**:
  - **Method**: GET
  - **Endpoint**: `/students/{id}`
  - **Response**:
    - 200 OK:
      ```json
      {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
      ```
    - 404 Not Found: if the student does not exist.

- **Update Student**:
  - **Method**: PUT
  - **Endpoint**: `/students/{id}`
  - **Request Body**:
    ```json
    {
      "name": "Jane Doe",
      "email": "jane.doe@example.com"
    }
    ```
  - **Response**:
    - 200 OK:
      ```json
      {
        "id": 1,
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
      }
      ```

- **List Students**:
  - **Method**: GET
  - **Endpoint**: `/students`
  - **Response**:
    - 200 OK:
      ```json
      [
        {
          "id": 1,
          "name": "John Doe",
          "email": "john.doe@example.com"
        },
        {
          "id": 2,
          "name": "Jane Smith",
          "email": "jane.smith@example.com"
        }
      ]
      ```

---

## Data Model

### 1. Database Schema
- **Student Table**:
  - Fields:
  - `id`: INTEGER PRIMARY KEY AUTOINCREMENT
  - `name`: TEXT NOT NULL
  - `email`: TEXT NOT NULL UNIQUE

### 2. Database Migration
- To implement the email field in the Student table without losing existing data, a migration script will be executed using Alembic or a similar migration library.
- Migration script will:
  - Add a new column `email` to the existing Student table.
  - Preserve existing records by setting a default value for emails initially (e.g., empty strings), ensuring no null values.

```python
"""add_email_to_student_table

Revision ID: xxx
Revises: previous_revision_id
Create Date: YYYY-MM-DD
"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column('student', sa.Column('email', sa.String(), nullable=False, server_default=''))

def downgrade():
    op.drop_column('student', 'email')
```

---

## Error Handling & Validation

### 1. Input Validation
- The `name` field will validate as a non-empty string.
- The `email` field will validate against standard email formats using Pydantic's `EmailStr`.
- Responses for unsuccessful validations will be:
  - 400 Bad Request for invalid email formats and empty names.

### 2. Error Responses
Error responses will be structured as follows:
```json
{
  "error": {
    "code": "E001",
    "message": "Invalid input: email must be a valid email format"
  }
}
```

---

## Testing Plan

### 1. Test Coverage
- Unit tests will be developed for each new feature covering at least 70% of business logic.
- Critical paths will feature tests ensuring 90%+ coverage.

### 2. Test Scenarios
- Test creating a Student with a valid name and email returns the correct Student data.
- Test retrieving a Student by ID returns accurate data including the email.
- Test updating a Student's email reflects the change in the response.
- Test listing all Students returns a proper list with emails.

```python
def test_create_student_with_email():
    response = client.post("/students/", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john.doe@example.com"
```

---

## Deployment Considerations

### 1. Containerization
- Continue using Docker to ensure consistency in the deployment pipeline.
- Update the `Dockerfile` if new dependencies are added for email validation or migrations.

### 2. Documentation & Configuration
- Update the `README.md` file to describe new fields and endpoints.
- Ensure the `.env.example` file reflects any new environment variables required for the email feature.

---

## Conclusion

This implementation plan details the approach for integrating an email field into the Student entity within the Student Management Application. The plan emphasizes scalability, maintainability, and backward compatibility while setting clear boundaries for module responsibilities, API contracts, and testing strategies. Following these standards will ensure successful implementation while maintaining existing functionality.