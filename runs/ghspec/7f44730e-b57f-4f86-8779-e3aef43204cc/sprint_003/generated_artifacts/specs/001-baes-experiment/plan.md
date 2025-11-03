# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## I. Overview

The purpose of this implementation plan is to define the technical architecture and implementation strategy for adding a new `Course` entity to the existing educational database system. This feature will allow educational institutions to manage and categorize courses effectively, enriching the overall system by facilitating student-course associations in the future.

## II. Architecture

### 1. System Components

- **Web Framework**: FastAPI (Python) for building the asynchronous API.
- **Database**: SQLite, for lightweight, file-based data storage.
- **ORM**: SQLAlchemy to connect and interact with the SQLite database.
- **API Documentation**: Swagger UI provided by FastAPI enabled for automatic API documentation.

### 2. Module Structure

- **src/**
  - **api/**: Contains API endpoints.
    - `course.py`: New module to handle requests related to course management (create and retrieve).
  - **models/**: Defines data models.
    - `course.py`: New file for the SQLAlchemy model representing the `Course` entity with `name` and `level` attributes.
  - **db/**: Responsible for database interactions.
    - `database.py`: Adjustments to migrate the database schema to include the new `Course` entity.
  - **main.py**: Entry point for the application; will initialize the new course logic.
- **tests/**: Contains test files.
  - `test_course.py`: New test suite for the `Course` functionality.

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
# src/models/course.py
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)  # Primary key for the course
    name = Column(String, nullable=False)  # Course title (required)
    level = Column(String, nullable=False)  # Course difficulty level (required)
```

### 2. Database Setup

#### Migration Strategy

On application startup, the code will check if the `courses` table exists and create it if not. This can be accomplished using SQLAlchemy's `create_all` method.

```python
# src/db/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.course import Base as CourseBase
from models.student import Base as StudentBase

DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    # Create tables if they do not exist
    StudentBase.metadata.create_all(bind=engine)  # Ensure Student table exists
    CourseBase.metadata.create_all(bind=engine)   # Ensure Course table exists
```

### 3. API Endpoints

#### New Endpoints for Course Management

Two API endpoints will be added for creating and retrieving course records.

```python
# src/api/course.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.database import SessionLocal
from models.course import Course

router = APIRouter()

class CourseCreate(BaseModel):
    name: str
    level: str

@router.post("/courses")
def create_course(course: CourseCreate):
    if not course.name or not course.level:
        raise HTTPException(status_code=400, detail={"error": {"code": "E001", "message": "Both name and level are required"}})

    db = SessionLocal()
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    
    return {"message": "Course created successfully", "course": {"name": db_course.name, "level": db_course.level}}

@router.get("/courses")
def get_courses():
    db = SessionLocal()
    courses = db.query(Course).all()
    return {"courses": [{"name": course.name, "level": course.level} for course in courses]}
```

### 4. Application Entry Point

The main application entry point will need to import and include the new course routes.

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
import api.course  # Import new course module routes
app.include_router(api.course.router)  # Register course routes
```

## V. Testing Strategy

### 1. Test Coverage

- Unit tests for creating and retrieving courses should be implemented to ensure all functional scenarios are covered, focusing on successful operations as well as error handling.

### 2. Test Structure

```python
# tests/test_course.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_course_valid():
    """Test creating a course with a valid name and level."""
    response = client.post("/courses", json={"name": "Math 101", "level": "beginner"})
    assert response.status_code == 200
    assert response.json() == {"message": "Course created successfully", "course": {"name": "Math 101", "level": "beginner"}}

def test_create_course_empty_fields():
    """Test creating a course with empty fields."""
    response = client.post("/courses", json={"name": "", "level": ""})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E001", "message": "Both name and level are required"}}

def test_get_courses():
    """Test retrieving all courses after creation."""
    response = client.get("/courses")
    assert response.status_code == 200
    assert "courses" in response.json()
```

## VI. Deployment Considerations

### 1. Environment Setup

- Ensure Python is installed with package manager `pip`.
- The requirements including FastAPI, SQLAlchemy, and other dependencies will be listed in a `requirements.txt`.

### 2. Configuration Management

- Use environment variables for configuration if required, while keeping the `.env.example` for reference on the needed variables.

## VII. Security Considerations

- Validate all incoming data to ensure adherence to the expected types and formats, guarding against injection attacks.
- No authentication mechanisms are included in this implementation; access should be safeguarded through secure environments.

## VIII. Performance Considerations

- SQLite’s lightweight nature will ensure the application can handle expected workloads. Proper indexing and efficient querying will maximize performance, especially when fetching course data.

## IX. Additional Notes

- The API will create the `Course` table on startup as part of schema migration, ensuring seamless integration within the database without losing existing data related to students or other entities. The addition of the `Course` entity does not interfere with existing data integrity.
  
---

This implementation plan provides a comprehensive strategy for adding the `Course` entity to the educational database system, detailing clear paths for integration with existing functionalities, along with future-focused approaches for validation, testing, and deployment.