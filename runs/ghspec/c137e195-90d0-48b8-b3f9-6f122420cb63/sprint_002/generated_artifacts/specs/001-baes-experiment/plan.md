# Implementation Plan: Add Email Field to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Entity Management Web Application

## Version
1.1.0

## Purpose
To enhance the existing Student entity by adding a new required email field, allowing for the storage and management of each student's email address, which will facilitate communication and notifications.

## Technology Stack
- **Backend Framework**: FastAPI (for building the REST API)
- **Database**: SQLite (for data persistence)
- **ORM**: SQLAlchemy (for database interactions)
- **Data Format**: JSON (for API requests and responses)
- **Testing Framework**: pytest (for unit and integration testing)

## Architecture Overview
The application will maintain its modular structure while incorporating the new email field. The primary modules will include:
1. **Models**: Defines the updated database schema for the Student entity.
2. **API**: Updates the existing RESTful endpoints for student management.
3. **Database**: Handles database migration and schema updates.
4. **Error Handling**: Centralizes error responses for invalid requests.
5. **Testing**: Extends tests to cover new scenarios involving email.

## Module Layout
```
src/
    ├── api/
    │   └── students.py           # Updated endpoint for student management
    ├── models/
    │   └── student.py            # Updated Student model to include email
    ├── database/
    │   └── db.py                 # Database connection and schema initialization
    ├── error_handlers/
    │   └── error_responses.py     # Centralized error handling
    └── main.py                   # Application entry point
tests/
    ├── test_students.py           # Tests for student API endpoints
```

## Implementation Approach

### 1. Database Model
- **Updated Student Model**:
    ```python
    from sqlalchemy import Column, Integer, String
    from database.db import Base

    class Student(Base):
        __tablename__ = 'students'
        
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String, nullable=False)
        email = Column(String, nullable=False)  # New email field
    ```

### 2. Database Migration Strategy
- **Automated Schema Update**:
    The application will check for the existence of the new email field in the Student table at startup. If it does not exist, the application will automatically apply a migration:
    ```python
    from sqlalchemy import inspect

    def init_db():
        # Create tables if not exist
        Base.metadata.create_all(bind=engine)
        
        # Inspect the existing database for the Student table
        inspector = inspect(engine)
        if "students" in inspector.get_table_names():
            columns = [col['name'] for col in inspector.get_columns("students")]
            if "email" not in columns:
                with engine.begin() as connection:
                    # Adding the email column to the existing table
                    connection.execute('ALTER TABLE students ADD COLUMN email VARCHAR NOT NULL')
    ```

### 3. API Endpoints
- **Create Student Endpoint** (Updated):
    ```python
    from fastapi import APIRouter, HTTPException
    from models.student import Student
    from database.db import SessionLocal
    from pydantic import BaseModel, EmailStr

    router = APIRouter()

    class StudentCreate(BaseModel):
        name: str
        email: EmailStr  # Use Pydantic for email validation

    @router.post("/students", response_model=StudentCreate, status_code=201)
    def create_student(student: StudentCreate):
        db = SessionLocal()
        new_student = Student(name=student.name, email=student.email)
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
        return new_student
    ```

- **Retrieve Students Endpoint** (Updated):
    ```python
    from typing import List

    @router.get("/students", response_model=List[StudentCreate], status_code=200)
    def get_students():
        db = SessionLocal()
        students = db.query(Student).all()
        return students
    ```

### 4. Error Handling
- **Error Responses**:
    Returns clear error messages for missing or invalid email formats:
    ```python
    @router.post("/students", response_model=StudentCreate, status_code=201)
    def create_student(student: StudentCreate):
        if not student.name:
            raise HTTPException(status_code=400, detail="Name is required")
        if not student.email:
            raise HTTPException(status_code=400, detail="Email is required")
        # Note: Validation handled by EmailStr from Pydantic

        db = SessionLocal()
        # ... (creation logic as before)
    ```

### 5. Application Entry Point
- **Main Application** (No Changes):
    ```python
    from fastapi import FastAPI
    from database.db import init_db
    from api.students import router as student_router

    app = FastAPI()

    @app.on_event("startup")
    def startup():
        init_db()

    app.include_router(student_router)
    ```

## Testing Strategy
- **Unit and Integration Tests** using pytest to verify individual components, covering new email field functionality.
- Testing scenarios will include:
    - Creating a student with valid/invalid name and email data.
    - Retrieving all students and verifying the email output format.
    - Error handling for missing name/email fields.

### Testing Structure
- **Unit tests** located in `tests/test_students.py`:
    ```python
    def test_create_student_with_email(client):
        response = client.post("/students", json={"name": "Alice", "email": "alice@example.com"})
        assert response.status_code == 201
        assert response.json()['name'] == "Alice"
        assert response.json()['email'] == "alice@example.com"

    def test_create_student_without_email(client):
        response = client.post("/students", json={"name": "Alice"})
        assert response.status_code == 400
        assert "Email is required" in response.json()['error']['message']

    def test_get_students(client):
        response = client.get("/students")
        assert response.status_code == 200
        # Additional checks on the students body response...
    ```

## API Contracts
- **POST /students**:
    - Request:
        ```json
        {
            "name": "Alice",
            "email": "alice@example.com"
        }
        ```
    - Response:
        ```json
        {
            "id": 1,
            "name": "Alice",
            "email": "alice@example.com"
        }
        ```

- **GET /students**:
    - Response:
        ```json
        [
            {
                "id": 1,
                "name": "Alice",
                "email": "alice@example.com"
            },
            {
                "id": 2,
                "name": "Bob",
                "email": "bob@example.com"
            }
        ]
        ```

## Deployment Considerations
- The application will run locally using Uvicorn as the ASGI server.
- Documentation will be updated in the `README.md` file with setup instructions and API usage, including the new email field details.

## Success Criteria
1. Students can be created and retrieved successfully, including names and emails, with appropriate status codes and JSON responses.
2. Error handling provides actionable feedback for invalid input related to email fields.
3. The database schema is properly updated on startup without user intervention.

This implementation plan outlines a clear and structured approach to adding the email field to the Student entity while maintaining compliance with existing application standards and practices.