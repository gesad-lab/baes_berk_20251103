# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## I. Overview

The purpose of this implementation plan is to define the technical architecture and implementation strategy for adding an `email` field to the existing `Student` entity in the Student Management Web Application. This feature will enhance the management of student records by allowing educational institutions to capture and store students' email addresses for improved communication.

## II. Architecture

### 1. System Components

- **Web Framework**: FastAPI (Python) for building the API with asynchronous capabilities.
- **Database**: SQLite for storing student records, providing a lightweight, file-based approach.
- **ORM**: SQLAlchemy to interact with the SQLite database, establishing an easy interface for database operations.
- **API Documentation**: Swagger UI provided by FastAPI for automatic API documentation.

### 2. Module Structure

- **src/**
  - **api/**: Contains API endpoints.
    - `student.py`: Handles requests related to student management (create and retrieve).
  - **models/**: Defines data models.
    - `student.py`: Updates the `Student` SQLAlchemy model to include the `email` field.
  - **db/**: Responsible for database interactions.
    - `database.py`: Modifications to migrate the database schema to include the `email` field.
  - **main.py**: Entry point for the application; slight modifications to call initialization logic.
- **tests/**: Contains test files.
  - `test_student.py`: Updates to include tests for new email functionality.

## III. Technology Stack

- **Programming Language**: Python 3.9+
- **Web Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing Framework**: pytest
- **Dependency Management**: pip with requirements.txt

## IV. Implementation Details

### 1. Data Models

```python
# src/models/student.py
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New email field for storing student emails
```

### 2. Database Setup

#### Migration Strategy

On application startup, the code will check if the `email` field already exists and, if not, will create a new column. This can be accomplished using a lightweight migration library (like Alembic) or by managing the schema directly without losing existing data.

```python
# src/db/database.py
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from models.student import Base

DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    # Create tables if not present
    Base.metadata.create_all(bind=engine)

    # Check for existing students, and perform migration if needed
    with engine.connect() as connection:
        result = connection.execute("PRAGMA table_info(students);")
        columns = [row[1] for row in result]
        if 'email' not in columns:
            connection.execute("ALTER TABLE students ADD COLUMN email TEXT NOT NULL;")
        # Note: This may require additional handling for existing students and migration context.
```

### 3. API Endpoints

#### Updated Create a Student Endpoint

The API needs to validate the email format and include it in the student creation request.

```python
# src/api/student.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from db.database import SessionLocal, init_db
from models.student import Student

app = FastAPI()

class StudentCreate(BaseModel):
    name: str
    email: EmailStr  # Updated to require email field

@app.post("/students")
def create_student(student: StudentCreate):
    if not student.name:
        raise HTTPException(status_code=400, detail={"error": {"code": "E001", "message": "Name is required"}})
    
    db = SessionLocal()
    db_student = Student(name=student.name, email=student.email)  # Save email
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return {"message": "Student created successfully", "student": {"name": db_student.name, "email": db_student.email}}

@app.get("/students")
def get_students():
    db = SessionLocal()
    students = db.query(Student).all()
    return {"students": [{"name": student.name, "email": student.email} for student in students]}
```

### 4. Application Entry Point

Minor modifications to ensure the updated database initialization takes place during startup.

```python
# src/main.py
from fastapi import FastAPI
from db.database import init_db

app = FastAPI()

@app.on_event("startup")
def startup_event():
    init_db()

# Import API routes
import api.student
```

## V. Testing Strategy

### 1. Test Coverage

- Implement unit tests for the new `create_student` functionality with email.
- Ensure a minimum of 70% test coverage for this added business logic.

### 2. Test Structure

```python
# tests/test_student.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_student_valid():
    """Test creating a student with a valid name and email."""
    response = client.post("/students", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 200
    assert response.json() == {"message": "Student created successfully", "student": {"name": "John Doe", "email": "john.doe@example.com"}}

def test_create_student_empty_name():
    """Test creating a student with an empty name."""
    response = client.post("/students", json={"name": "", "email": "john.doe@example.com"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Name is required"}}

def test_create_student_invalid_email():
    """Test creating a student with an invalid email."""
    response = client.post("/students", json={"name": "Jane Doe", "email": "invalid-email"})
    assert response.status_code == 422  # Unprocessable Entity for email validation

def test_get_students():
    """Test retrieving all students."""
    response = client.get("/students")
    assert response.status_code == 200
    assert "students" in response.json()
```

## VI. Deployment Considerations

### 1. Environment Setup

- Ensure Python is installed with package manager `pip`.
- Requirements to be listed in `requirements.txt`.

### 2. Configuration Management

- Use environment variables for any sensitive configuration, although none are specified in this case. An example `.env.example` can be created for reference.

## VII. Security Considerations

- Since no complex user authentication is implemented, access to the API must be limited to trusted environments only.
- Request validation in place to ensure errors are handled gracefully with informative messages.

## VIII. Performance Considerations

- With SQLite's lightweight nature, this application will handle the expected number of records efficiently.
- Properly indexed database schema will ensure efficient data retrieval.

## IX. Additional Notes

- The API will automatically create the database schema on startup without manual intervention.
- New functionality will maintain backward compatibility with existing student records, which will remain intact following the email field addition.

---

This implementation plan provides a clear outline for integrating the new email field into the existing Student entity while complying with existing coding standards and architectural guidelines. The approach prioritizes maintainability and scalability in line with the business specifications.