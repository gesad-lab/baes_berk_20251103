# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## 1. Overview
This document outlines the technical implementation plan for adding an email field to the existing Student entity in the Student Management Web Application. This enhancement will enable the capture of students' email addresses, thereby improving communication capabilities for educational institutions.

## 2. Technology Stack
### 2.1 Frameworks & Libraries
- **FastAPI**: For building the web API.
- **SQLAlchemy**: For ORM to interact with the SQLite database.
- **SQLite**: As the database for storing student records.
- **Pydantic**: For data validation and serialization.

### 2.2 Environment
- Development environment: Local machine.
- Language: Python 3.x.

## 3. Module Architecture
### 3.1 Module Structure
```
student_management/
│
├── src/
│   ├── main.py               # Entry point of the application
│   ├── models/
│   │   └── student.py        # Pydantic model and SQLAlchemy ORM model for Student
│   ├── routes/
│   │   └── student_routes.py  # API endpoints for Student management
│   └── database/
│       └── db.py             # Database connection and initialization
│
├── migrations/                # Directory for database migration scripts
│   └── 001_add_email_field.py # Migration script to add email field
│
├── tests/
│   └── test_student.py        # Unit tests for the student management
│
├── requirements.txt           # Dependencies for the project
└── README.md                  # Documentation for setup and usage
```

### 3.2 Module Responsibilities
- **models/student.py**: Update the Student entity with the new `email` field.
- **routes/student_routes.py**: Update API endpoints to handle the email field in student creation and retrieval.
- **database/db.py**: Maintain database connection and initialization.
- **migrations/001_add_email_field.py**: Implement schema migration to add the email field.

## 4. Data Models
The Student entity will be updated to include the new `email` field as follows:
### 4.1 Student Model Update
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

### 4.2 Pydantic Schema Update
```python
from pydantic import BaseModel, constr, EmailStr

class StudentCreate(BaseModel):
    name: constr(min_length=1)  # Name must not be empty
    email: EmailStr             # Email must be valid

class StudentResponse(BaseModel):
    id: int
    name: str
    email: str                  # Include email in the response

    class Config:
        orm_mode = True
```

## 5. API Contract
### 5.1 Endpoints
- **POST /students**: Create a new student.
  - Request Body: `{"name": "John Doe", "email": "john.doe@example.com"}`
  - Response: 
    - Status Code: 201
    - Body: `{"id": 1, "name": "John Doe", "email": "john.doe@example.com"}`

- **GET /students**: Retrieve a list of all students.
  - Response:
    - Status Code: 200
    - Body: `[{"id": 1, "name": "John Doe", "email": "john.doe@example.com"}, {"id": 2, "name": "Jane Doe", "email": "jane.doe@example.com"}]`

### 5.2 Error Handling
- If the email field is empty or improperly formatted during creation:
  - Response:
    - Status Code: 400
    - Body: `{"error": {"code": "E001", "message": "Invalid email format."}}`

## 6. Implementation Steps
### 6.1 Setup Environment
- Ensure the environment is ready based on the previous sprint setup.

### 6.2 Install Dependencies
- The previously defined dependencies in `requirements.txt` remain the same, requiring no changes.

### 6.3 Implement Database Migration (001_add_email_field.py)
- Create a migration script to add the `email` field to the Student table without requiring downtime.

```python
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker
from src.models.student import Student

def upgrade():
    engine = create_engine("sqlite:///./students.db")
    with engine.connect() as connection:
        connection.execute('ALTER TABLE students ADD COLUMN email TEXT NOT NULL DEFAULT "";')

def downgrade():
    # Logic to be defined if needing a rollback.
    pass

if __name__ == "__main__":
    upgrade()
```

### 6.4 Update API Endpoints (student_routes.py)
- Modify the POST endpoint to include the email field during student creation.
- Ensure GET requests retrieve all relevant student information including email.

### 6.5 Update Tests
- Implement additional unit tests to verify the functionality of student creation with the new email field.
```python
def test_create_student_with_email():
    response = client.post("/students", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["email"] == "john.doe@example.com"

def test_create_student_with_invalid_email():
    response = client.post("/students", json={"name": "John Doe", "email": "invalid-email"})
    assert response.status_code == 400
```

## 7. Testing Strategy
- Ensure that all user scenarios are covered:
  - **Successful creation with valid data (name and email).**
  - **Validation failure with empty or improperly formatted email.**
  - **Successful retrieval of students records including their emails.**
- Ensure a minimum of 70% test coverage for business logic.

## 8. Deployment Considerations
- The application must successfully start and implement the migration on startup.
- Clearly document necessary environment setup in `README.md`.
- Ensure that no sensitive configuration information is hardcoded.

## 9. Documentation
- Update `README.md` to include:
  - Updated API usage examples (including email field).
  - Migration guidelines if applicable.

## 10. Conclusion
This implementation plan provides a comprehensive roadmap for enhancing the Student entity by adding an email field. Following this plan ensures integration with existing modules, maintains backward compatibility, and meets specified functional requirements. The structured testing and migration strategy enhances application robustness and reliability.

Existing Code Files Modifications:
- **models/student.py**: Add a new `email` field to the Student model.
- **routes/student_routes.py**: Update the POST route to handle the new email parameter and adjust the response and validation accordingly.
- **tests/test_student.py**: Add new test cases to cover the email creation and validation scenarios.