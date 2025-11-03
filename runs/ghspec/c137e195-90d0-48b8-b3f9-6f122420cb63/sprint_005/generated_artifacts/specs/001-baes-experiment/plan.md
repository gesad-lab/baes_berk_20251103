# Implementation Plan: Create Teacher Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:  
# Implementation Plan: Add Course Relationship to Student Entity

---

## Version
1.0.0

## Purpose
To introduce a new Teacher entity into the existing system, allowing for the effective management of teacher data, including names and email addresses, which will be used to enhance the educational platform's operations related to educator management and course assignments.

## Technology Stack
- **Backend Framework**: FastAPI (for building the REST API)
- **Database**: SQLite (for data persistence)
- **ORM**: SQLAlchemy (for database interactions)
- **Data Format**: JSON (for API requests and responses)
- **Testing Framework**: pytest (for unit and integration testing)

## Architecture Overview
This implementation will create a new Teacher table to manage teacher data, including attributes such as name and email. The main modules involved will include:
1. **Models**: Defines the Teacher model for managing teacher records.
2. **API**: Implements RESTful endpoints for creating and retrieving teachers.
3. **Database**: Handles database migrations and schema updates to include the new Teacher table.
4. **Error Handling**: Centralizes error responses for API requests.
5. **Testing**: Covers the functionalities with appropriate test cases.

## Module Layout
```
src/
    ├── api/
    │   └── teacher.py              # New endpoint for teacher management
    ├── models/
    │   └── teacher.py               # Teacher model definition
    ├── database/
    │   └── db.py                    # Database connection and schema initialization (modified to include Teacher table)
    ├── error_handlers/
    │   └── error_responses.py       # Centralized error handling
    └── main.py                      # Application entry point (modified)
tests/
    └── test_teacher.py              # Tests for teacher API endpoints (new)
```

## Implementation Approach

### 1. Database Model
- **Teacher Model**:
    ```python
    from sqlalchemy import Column, Integer, String
    from database.db import Base

    class Teacher(Base):
        __tablename__ = 'teachers'
        
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String, nullable=False)
        email = Column(String, unique=True, nullable=False)
    ```

### 2. Database Migration Strategy
- **Automated Schema Update**:
    The application will check for the existence of the new Teacher table at startup and create it if it does not exist, while ensuring existing data remains intact:
    ```python
    from sqlalchemy import inspect

    def init_db():
        Base.metadata.create_all(bind=engine)  # Ensures all necessary tables are created
        
        inspector = inspect(engine)
        if "teachers" not in inspector.get_table_names():  # Check if the Teacher table exists
            with engine.begin() as connection:
                connection.execute('CREATE TABLE teachers (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL)')
    ```

### 3. API Endpoints
- **Create Teacher**:
    ```python
    from fastapi import APIRouter, HTTPException
    from sqlalchemy.orm import Session
    from models.teacher import Teacher
    from database.db import SessionLocal
    from pydantic import BaseModel, EmailStr

    router = APIRouter()

    class TeacherCreate(BaseModel):
        name: str
        email: EmailStr

    @router.post("/teachers", status_code=201)
    def create_teacher(teacher: TeacherCreate):
        db: Session = SessionLocal()
        if db.query(Teacher).filter(Teacher.email == teacher.email).first():
            raise HTTPException(status_code=400, detail="Email already registered")
        
        new_teacher = Teacher(name=teacher.name, email=teacher.email)
        db.add(new_teacher)
        db.commit()
        db.refresh(new_teacher)
        return new_teacher
    ```

- **Retrieve Teacher Information**:
    ```python
    @router.get("/teachers/{teacher_id}", status_code=200)
    def get_teacher(teacher_id: int):
        db: Session = SessionLocal()
        teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
        
        if not teacher:
            raise HTTPException(status_code=404, detail="Teacher not found")

        return {"id": teacher.id, "name": teacher.name, "email": teacher.email}
    ```

### 4. Application Entry Point
- **Main Application** (Updated):
    The entry point will integrate the new teacher routes:
    ```python
    from fastapi import FastAPI
    from database.db import init_db
    from api.teacher import router as teacher_router

    app = FastAPI()

    @app.on_event("startup")
    def startup():
        init_db()

    app.include_router(teacher_router)
    ```

## Testing Strategy
- **Unit and Integration Tests** implemented with pytest will cover the creation and retrieval of teachers, ensuring proper error handling.
- Testing scenarios include:
    - Successful creation of a teacher with valid inputs.
    - Attempting to create a teacher with duplicate email addresses.
    - Retrieving existing teacher data.
    - Handling of invalid teacher requests (e.g., non-existent IDs).

### Testing Structure
- **Unit tests** located in `tests/test_teacher.py`:
    ```python
    import pytest
    from fastapi.testclient import TestClient
    from api.teacher import router as teacher_router
    from database.db import init_db

    app = FastAPI()
    app.include_router(teacher_router)

    @pytest.fixture(scope="module")
    def client():
        """Create a test client for the FastAPI app."""
        init_db()
        yield TestClient(app)

    def test_create_teacher(client):
        response = client.post("/teachers", json={"name": "John Doe", "email": "johndoe@example.com"})
        assert response.status_code == 201
        assert response.json()["name"] == "John Doe"

    def test_create_teacher_duplicate_email(client):
        response = client.post("/teachers", json={"name": "Jane Doe", "email": "johndoe@example.com"})
        assert response.status_code == 400
        assert "Email already registered" in response.json()['detail']

    def test_get_teacher_info(client):
        response = client.get("/teachers/1")  # Assuming the ID of the created teacher is 1
        assert response.status_code == 200
        assert response.json()["name"] == "John Doe"
    ```

## API Contracts
- **POST /teachers**:
    - Request:
        ```json
        {
            "name": "John Doe",
            "email": "johndoe@example.com"
        }
        ```
    - Response:
        ```json
        {
            "id": 1,
            "name": "John Doe",
            "email": "johndoe@example.com"
        }
        ```

- **GET /teachers/{teacher_id}**:
    - Response:
        ```json
        {
            "id": 1,
            "name": "John Doe",
            "email": "johndoe@example.com"
        }
        ```

## Deployment Considerations
- The application will run locally using Uvicorn as the ASGI server.
- Update the `README.md` file to include setup instructions for the new Teacher entity functionality, detailing endpoints and expected data formats.

## Success Criteria
1. Successful creation of a teacher with valid inputs returns status code 201 and includes the teacher data.
2. Successful retrieval of teacher data returns status code 200 and includes the correct teacher information.
3. The application handles errors properly by returning meaningful HTTP status codes and error messages for invalid requests.
4. The database schema is updated automatically without requiring user intervention, maintaining data integrity across all existing models.

This implementation plan outlines a comprehensive approach to adding the Teacher entity to the system, ensuring adherence to technical standards and maintaining backward compatibility with existing data models.