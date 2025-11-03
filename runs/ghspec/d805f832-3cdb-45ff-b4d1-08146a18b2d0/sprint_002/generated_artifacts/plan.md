# Implementation Plan: Add Email Field to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## Version
**Version**: 1.1.0  

## Purpose
This implementation plan details the enhancements to the Student Management Web Application, focusing on adding an `email` field to the existing Student entity. This feature enhances data collection and communication effectiveness.

## Architecture Overview
The architecture will remain a microservices pattern using FastAPI and SQLAlchemy, with the addition of the `email` field in the `students` table while ensuring existing data is preserved. The modifications will require API changes for creating and retrieving students, along with validation requirements for the new email field.

## Technology Stack
- **Programming Language**: Python 3.11+
- **Web Framework**: FastAPI
- **ORM**: SQLAlchemy
- **Database**: SQLite
- **API Testing Tool**: Postman / cURL

## Module Boundaries and Responsibilities
1. **API Layer**:
   - New Endpoint:
     - `POST /students`: Create a new Student with the newly required email field.
     - `GET /students/{id}`: Retrieve a Student by ID (no changes needed).
   
2. **Business Logic Layer**:
   - Extend existing logic to validate and process the `email` field during student creation.
   - Implement email format validation.
   
3. **Data Access Layer**:
   - Update the Student model to include the `email` field.
   - Handle database migrations to ensure the new schema reflects the additional field.

## Data Models
### Student Model
Modification to include the `email` field in the `Student` model:
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import re

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New field
    
    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', email='{self.email}')>"

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate email format."""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None
```

## API Contracts
### 1. Create a Student
No longer just requires `name`. Must also validate for `email`.
- **Endpoint**: `POST /students`
- **Request Body**:
  ```json
  {
    "name": "string",
    "email": "string"
  }
  ```
- **Response**:
  - **Success (201)**:
    ```json
    {
      "id": 1,
      "name": "string",
      "email": "string"
    }
    ```
  - **Error (400)**:
    For missing `email`:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "The email field is required."
      }
    }
    ```
    For invalid email format:
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Invalid email format."
      }
    }
    ```

### 2. Retrieve a Student
No changes; returns existing fields including the new `email`.

## Implementation Approach
1. **Environment Setup**:
   - Ensure Python 3.11+ is installed.
   - Create a virtual environment.
   - Install dependencies: 
     ```bash
     pip install fastapi[all] sqlalchemy
     ```

2. **Database Migration**:
   - Update the `students` table to include the `email` field. Use Alembic for migrations or direct SQLAlchemy commands to add the new column without losing existing data:
   ```python
   from sqlalchemy import create_engine, Column, String
   from sqlalchemy.orm import sessionmaker
   from models import Base
   
   engine = create_engine('sqlite:///./database.db')
   Base.metadata.bind = engine
   with engine.connect() as connection:
       connection.execute('ALTER TABLE students ADD email STRING NOT NULL DEFAULT "";')

3. **Endpoint Implementation**:
   - Modify the `main.py` file to add functionality for validating and creating a Student with the new `email` field.
   - Implement request validation using Pydantic models:
   ```python
   from pydantic import BaseModel, EmailStr
   
   class StudentCreateModel(BaseModel):
       name: str
       email: EmailStr  # Automatically validates email
   
   @app.post("/students", response_model=Student)
   async def create_student(student: StudentCreateModel):
       # Logic to save to the database
   ```

4. **Error Handling**:
   - Implement exception handling for validation and database-related errors.
   - Ensure new error response formats are consistent with previous implementations.

5. **Testing**:
   - Use Postman or cURL to test the API endpoints, focusing on:
     - Creating students with valid and invalid email formats.
     - Ensuring users cannot create a student without providing email.

## Scalability and Security Considerations
- **Scalability**: 
  - The application is designed stateless and can be easily deployed across multiple instances.
- **Security**: 
  - Validate and sanitize inputs to prevent injection attacks; ensure email addresses are validated properly.

## Implementation Timeline
- **Week 1**: 
  - Environment setup and initial project skeleton update.
- **Week 2**: 
  - Implement API endpoint modifications and business logic for email handling.
- **Week 3**: 
  - Complete schema migration and error handling.
  - Finalize initial testing and debugging.
- **Week 4**: 
  - Conduct comprehensive tests, update documentation, and prepare for deployment.

## Documentation and References
- **Code Documentation**: 
  - Each module, class, and function will have docstrings explaining the purpose and usage.
- **README.md**: 
  - Update to reflect new requirements for creating students with an email address and testing instructions.

## Trade-offs and Decisions
- **Database Migration**: 
  - Direct SQL command for `ALTER TABLE` chosen for simplicity; however, be cautious to ensure support in production environments.
- **New Validation Logic**: 
  - Built-in email validation from Pydantic saves development time and reduces the chance of manual errors.

This implementation plan addresses the requirements set forth in the specification, enhancing the Student Management Web Application with a critical field while preserving existing functionalities and data integrity.