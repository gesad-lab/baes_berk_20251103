# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Entity Management Application

## Overview

This implementation plan outlines the technical specifications for adding an email field to the existing Student entity. This enhancement will facilitate better communication by allowing email addresses to be stored with student information, preparing for future functionalities such as notifications.

---

## I. Architecture Overview

### 1.1 Technology Stack
- **Language**: Python
- **Framework**: Flask
- **Database**: SQLite (with SQLAlchemy as the ORM)
- **API Testing Tool**: Postman or curl (for manual testing)
- **Development Environment**: Virtual environment using `venv`

### 1.2 Application Structure Update
```
student-management-app/
    ├── src/
    │   ├── app.py          # Main application entry point
    │   ├── models.py       # Database models (updated to include email)
    │   ├── services.py      # Business logic and API functionalities (updated for validation)
    │   ├── config.py       # Configuration settings
    │   └── database.py     # Database initialization (no changes)
    ├── tests/
    │   ├── test_services.py # Unit tests for service functions (updated for new scenarios)
    ├── requirements.txt     # List of dependencies (no changes)
    ├── .env.example         # Environment variable example
    └── README.md            # Documentation (update to reflect new feature)
```

---

## II. Module Boundaries and Responsibilities

### 2.1 Modules and Responsibilities

- `app.py`: 
  - Define new routes for handling email input in student creation.
  
- `models.py`: 
  - Update the `Student` model to include an `email` field.
  
- `services.py`: 
  - Implement validation checks for email and modify the creation logic to include email handling.
  
- `database.py`: 
  - Unchanged, but will facilitate the migration process for adding new fields.

- `tests/test_services.py`: 
  - Update unit tests to include scenarios for email validation, including proper handling of missing and invalid email fields.

---

## III. Data Models

### 3.1 Updated Student Model

```python
from sqlalchemy import Column, Integer, String
from database import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New email field required

    def __repr__(self):
        return f"<Student(id={self.id}, name={self.name}, email={self.email})>"
```

### 3.2 Migration Strategy

To accommodate the new `email` field while preserving existing data, we'll use SQLAlchemy's migration tools:

```bash
alembic revision --autogenerate -m "Add email field to Student entity"
alembic upgrade head
```

Ensure the migration script is generated correctly to add a non-nullable email column, incorporating a default value or allowing it to be nullable initially.

---

## IV. API Contracts

### 4.1 Create Student Endpoint

- **Endpoint**: `POST /students`
- **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
- **Response**: 
    - **Success (201 Created)**:
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  
    - **Error (400 Bad Request)**:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Email field is required."
      }
    }
    ```

### 4.2 Retrieve Students Endpoint

- **Endpoint**: `GET /students`
- **Response**:
  - **Success (200 OK)**:
    ```json
    [
      {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
    ]
    ```

---

## V. Implementation Approach

### 5.1 Steps for Development

1. Update `models.py` to include the `email` attribute in the Student model.
  
2. Create a migration script using Alembic to modify the database schema without losing existing data.
  
3. Modify `services.py` to include validation logic:
   - Ensure the email is provided and is in a valid format (regular expression can be employed).
  
4. Update `app.py` for the new `POST /students` route that handles emails alongside names.
  
5. Extend unit tests in `tests/test_services.py` to include scenarios for:
   - Successful creation with email.
   - Failure when email is missing.
   - Failure when email is improperly formatted.

6. Conduct manual end-to-end tests to validate all API endpoints.

---

## VI. Validation and Testing

### 6.1 Automated Testing Strategy

- Ensure at least **70% test coverage** on business logic across the services, including new validation logic for the email.
- Implement unit tests to validate edge cases of email formats.

### 6.2 Testing Scenarios

1. **POST /students**
   - Test with valid name and email -> Expect successful creation with correct response.
   - Test without email -> Expect error indicating the email field is required.
   - Test with invalid email format -> Expect an error about invalid email.

2. **GET /students**
   - Test retrieval when the database includes multiple entries -> Confirm that data includes names and emails correctly.

---

## VII. Error Handling and Validation

### 7.1 Input Validation

- Email validation using regex must ensure correct email structure.
- Implement logic in `services.py` that fails fast when validation checks do not pass.

### 7.2 Error Messages

- Standardize error messages, using codes for common issues such as missing fields or invalid formats.

---

## VIII. Security Considerations

The modifications must still adhere to existing security practices:
- Input sanitization to prevent vulnerabilities.
- Proper logging of failures without exposing sensitive information.

---

## IX. Deployment Considerations

This local application environment allows automatic schema modification. Ensure that any migration scripts produced are correctly placed within the application deployment lifecycle for integration into future versions.

---

## X. Conclusion

This implementation plan provides a structured approach to expand the Student Entity by adding an email field. It emphasizes backward compatibility, maintains existing functionality, and introduces necessary validation and error handling. Following these guidelines will strengthen the application's ability to manage student data more efficiently.

Existing Code Files:
File: `tests/test_services.py`
```python
import unittest
from src.services import create_student, get_all_students
from src.models import Student
from src.database import db, init_db

class TestStudentServices(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the testing database and create necessary tables."""
        init_db()
        cls.app_context = db.app.app_context()
        cls.app_context.push()

    @classmethod
    def tearDownClass(cls):
        """Teardown app context."""
        cls.app_context.pop()

    def test_create_student_with_email(self):
        response = create_student(name="John Doe", email="john.doe@example.com")
        self.assertEqual(response["name"], "John Doe")
        self.assertEqual(response["email"], "john.doe@example.com")

    def test_create_student_without_email(self):
        with self.assertRaises(ValueError):  # Expect a ValueError for missing email
            create_student(name="Jane Doe")

    def test_create_student_with_invalid_email(self):
        with self.assertRaises(ValueError):  # Expect validation error for invalid email
            create_student(name="Jane Doe", email="invalid-email-format")
```

This concludes the comprehensive implementation of the feature extending the Student entity.