# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Entity Management

## I. Overview

This implementation plan outlines the architecture, technologies, and approach for enhancing the existing "Student" entity by adding an email field. The addition will improve data management capabilities by allowing users to maintain important contact information.

## II. Technology Stack

- **Backend Framework**: FastAPI (Python)
- **Database**: SQLite
- **Data Model**: SQLAlchemy ORM (to handle database interactions)
- **API Documentation**: Swagger UI (integrated with FastAPI)
- **Testing Framework**: pytest
- **Dependency Management**: Poetry

## III. Architecture

### 1. High-Level Architecture
- **Web Server**: FastAPI will handle HTTP requests.
- **Database Layer**: SQLite for data persistence, accessed via SQLAlchemy models.
- **Business Logic Layer**: Handlers for student management operations.
- **Error Handling and Validation**: Middleware for error responses.

### 2. Module Breakdown
- **Models**: Update existing Student model to include email.
- **Routes**: Add new routes to handle email-related functionalities.
- **Services**: Update business logic to accommodate email field operations (create, retrieve, update, delete).
- **Database Initialization**: Modify database initialization to accommodate new schema and migration strategy.
- **Error Handling**: Middleware to handle validation errors and other issues.

## IV. Data Models

### Updated Student Model

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New field added

# Database setup
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
```

## V. API Endpoints

### 1. Create Student

- **HTTP Method**: POST
- **Endpoint**: `/students`
- **Request Body**:
    ```json
    {
      "name": "string",
      "email": "string"  // New field added
    }
    ```
- **Response**: 
    - Success (201 Created):
    ```json
    {
      "id": "integer", 
      "name": "string",
      "email": "string"  // Return email in response
    }
    ```

### 2. Retrieve Student

- **HTTP Method**: GET
- **Endpoint**: `/students/{id}`
- **Response**:
    - Success (200 OK):
    ```json
    {
      "id": "integer", 
      "name": "string",
      "email": "string"  // Return email in response
    }
    ```

### 3. Update Student

- **HTTP Method**: PUT
- **Endpoint**: `/students/{id}`
- **Request Body**:
    ```json
    {
      "name": "string",
      "email": "string"  // New field added
    }
    ```
- **Response**:
    - Success (200 OK):
    ```json
    {
      "id": "integer", 
      "name": "string",
      "email": "string"  // Return updated email in response
    }
    ```

### 4. Delete Student

- **HTTP Method**: DELETE
- **Endpoint**: `/students/{id}`
- **Response**:
    - Success (204 No Content)
    - Error (404 Not Found):
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Student not found."
        }
    }
    ```

## VI. Implementation Steps

1. **Setup Environment**:
   - Ensure the project structure remains consistent:
     ```
     student-management/
     ├── src/
     │   ├── main.py
     │   ├── models.py        # Update this file
     │   ├── routes.py        # Update this file
     │   └── services.py      # Update this file
     ├── tests/               # Add tests to this directory
     ├── requirements.txt
     ├── README.md
     └── .env.example
     ```

   - Initialize with Poetry for dependency management or ensure existing setup is intact:
     ```bash
     poetry add fastapi[all] sqlalchemy pytest
     ```

2. **Modify the Student Model** in `models.py` to include the new email field.

3. **Update CRUD operations** in `services.py`:
   - Implement input validation for the new email field:
   ```python
   import re

   def validate_email(email: str) -> bool:
       pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
       return re.match(pattern, email) is not None
   ```

4. **Update API routes** in `routes.py` to include email parameters for the POST and PUT methods.

5. **Handle Validation Errors**: Validate email format when creating or updating a student in `services.py` and respond with meaningful error messages.

6. **Modify the Database Initialization** in `main.py`:
   - Create and execute a migration that alters the existing `students` table to add the email column while preserving existing data.
   ```python
   def upgrade():
       op.add_column('students', sa.Column('email', sa.String(), nullable=False))
   ```

7. **Write Unit Tests** using pytest to cover all functionalities, including edge cases revolving around email input validation.

8. **Documentation**:
   - Update `README.md` with changes to the API endpoints and new data models.

## VII. Testing Strategy

- Ensure a minimum of 90% test coverage on the business logic, especially for the new email-related functionalities.
- Include unit tests for creating and updating students while validating emails.

## VIII. Deployment Considerations

- Ensure that sensitive configurations are stored in environment variables and not hardcoded.
- Perform database backups prior to deploying the migration.
- Conduct smoke tests post-deployment to verify API endpoints return expected results.

## IX. Success Criteria

1. At least 90% successful CRUD operations with students, including handling of the email field.
2. All responses continue to be in JSON format and return the correct HTTP status codes.
3. The application must correctly handle invalid requests gracefully with informative error messages.
4. Database schema must update without data loss upon application startup.

## X. Technical Trade-offs

- **Migration Strategy**: Implementing a migration strategy allows for safe alterations to the database schema while avoiding disruptions to existing functionality.
- **Input Validation**: Simple regular expression-based validation for emails can prevent errors caused by malformed inputs. If scaling beyond this feature is warranted in the future, we may consider integrating more robust validation libraries.

This implementation plan sets a clear and structured path for enhancing the Student Entity with an email field while ensuring adherence to existing specifications and maintaining a focus on code quality and data integrity.