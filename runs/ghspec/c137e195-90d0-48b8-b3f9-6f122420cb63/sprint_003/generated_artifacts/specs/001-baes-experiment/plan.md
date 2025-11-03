# Implementation Plan: Create Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:  
# Implementation Plan: Add Email Field to Student Entity

---

## Version
1.0.0

## Purpose
To introduce a new Course entity into the existing system, enriching educational functionalities by managing course information (name and level) for academic offerings and future educational features.

## Technology Stack
- **Backend Framework**: FastAPI (for building the REST API)
- **Database**: SQLite (for data persistence)
- **ORM**: SQLAlchemy (for database interactions)
- **Data Format**: JSON (for API requests and responses)
- **Testing Framework**: pytest (for unit and integration testing)

## Architecture Overview
This implementation will follow a modular approach similar to previous sprints while integrating the new Course entity. The primary modules will include:
1. **Models**: Defines the Course database schema.
2. **API**: Implements RESTful endpoints for course management.
3. **Database**: Handles database migration and schema updates.
4. **Error Handling**: Centralizes error responses for API requests.
5. **Testing**: Extends tests to cover scenarios related to Course entity interactions.

## Module Layout
```
src/
    ├── api/
    │   └── courses.py            # New endpoint for course management
    ├── models/
    │   └── course.py             # Course model definition
    ├── database/
    │   └── db.py                 # Database connection and schema initialization (modified)
    ├── error_handlers/
    │   └── error_responses.py     # Centralized error handling
    └── main.py                   # Application entry point (modified)
tests/
    ├── test_courses.py            # Tests for course API endpoints (new)
```

## Implementation Approach

### 1. Database Model
- **Course Model**:
    ```python
    from sqlalchemy import Column, Integer, String
    from database.db import Base

    class Course(Base):
        __tablename__ = 'courses'
        
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String, nullable=False)
        level = Column(String, nullable=False)  # New level field
    ```

### 2. Database Migration Strategy
- **Automated Schema Update**:
    The application will check for the existence of the new Course table at startup and create it if it does not exist. The existing functionality for the Student table will remain unaffected:
    ```python
    from sqlalchemy import inspect

    def init_db():
        # Create all tables if they do not exist
        Base.metadata.create_all(bind=engine)  # Ensures courses table is created
        
        inspector = inspect(engine)
        if "courses" not in inspector.get_table_names():  # Check if courses table exists
            with engine.begin() as connection:
                connection.execute('CREATE TABLE courses (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, level TEXT NOT NULL)')
    ```

### 3. API Endpoints
- **Create Course Endpoint**:
    ```python
    from fastapi import APIRouter, HTTPException
    from models.course import Course
    from database.db import SessionLocal
    from pydantic import BaseModel

    router = APIRouter()

    class CourseCreate(BaseModel):
        name: str
        level: str

    @router.post("/courses", response_model=CourseCreate, status_code=201)
    def create_course(course: CourseCreate):
        if not course.name or not course.level:
            raise HTTPException(status_code=400, detail="Name and level are required")

        db = SessionLocal()
        new_course = Course(name=course.name, level=course.level)
        db.add(new_course)
        db.commit()
        db.refresh(new_course)
        return new_course
    ```

- **Retrieve Courses Endpoint**:
    ```python
    from typing import List

    @router.get("/courses", response_model=List[CourseCreate], status_code=200)
    def get_courses():
        db = SessionLocal()
        courses = db.query(Course).all()
        return courses
    ```

### 4. Error Handling
- **Error Responses**:
    For missing fields, the application will return helpful error messages:
    ```python
    @router.post("/courses", response_model=CourseCreate, status_code=201)
    def create_course(course: CourseCreate):
        if not course.name:
            raise HTTPException(status_code=400, detail="Course name is required")
        if not course.level:
            raise HTTPException(status_code=400, detail="Course level is required")
        
        db = SessionLocal()
        # ... (creation logic as before)
    ```

### 5. Application Entry Point
- **Main Application** (Updated):
    The entry point will integrate the newly created course routes:
    ```python
    from fastapi import FastAPI
    from database.db import init_db
    from api.courses import router as course_router

    app = FastAPI()

    @app.on_event("startup")
    def startup():
        init_db()

    app.include_router(course_router)
    ```

## Testing Strategy
- **Unit and Integration Tests** implemented with pytest will validate the Course API functionalities, ensuring creation and retrieval work as expected and handle errors correctly.
- Testing scenarios will include:
    - Creating a course with valid/invalid name and level data.
    - Retrieving all courses and verifying the response structure.
    - Testing error handling for missing fields in the requests.

### Testing Structure
- **Unit tests** located in `tests/test_courses.py`:
    ```python
    def test_create_course_with_valid_data(client):
        response = client.post("/courses", json={"name": "Mathematics", "level": "Advanced"})
        assert response.status_code == 201
        assert response.json()['name'] == "Mathematics"
        assert response.json()['level'] == "Advanced"

    def test_create_course_without_level(client):
        response = client.post("/courses", json={"name": "Mathematics"})
        assert response.status_code == 400
        assert "Course level is required" in response.json()['detail']

    def test_get_courses(client):
        response = client.get("/courses")
        assert response.status_code == 200
        # Additional checks on the courses body response...
    ```

## API Contracts
- **POST /courses**:
    - Request:
        ```json
        {
            "name": "Mathematics",
            "level": "Advanced"
        }
        ```
    - Response:
        ```json
        {
            "id": 1,
            "name": "Mathematics",
            "level": "Advanced"
        }
        ```

- **GET /courses**:
    - Response:
        ```json
        [
            {
                "id": 1,
                "name": "Mathematics",
                "level": "Advanced"
            },
            {
                "id": 2,
                "name": "History",
                "level": "Intermediate"
            }
        ]
        ```

## Deployment Considerations
- The application will run locally using Uvicorn as the ASGI server.
- Update the `README.md` file to include setup instructions for the new Course functionality, including endpoints and data requirements.

## Success Criteria
1. Courses can be created and retrieved successfully with appropriate status codes and JSON responses.
2. Error handling delivers actionable feedback for missing input fields.
3. The database schema is automatically updated upon application startup without requiring user intervention, while retaining the Student data model previously created.

This implementation plan provides a structured approach to introducing the Course entity while ensuring minimal disruption to existing code and maintaining compliance with outlined technical standards and practices.