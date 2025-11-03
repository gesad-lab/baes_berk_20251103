# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## 1. Overview
This document outlines the technical implementation plan for introducing the Course entity in the Student Management Web Application. The Course entity will facilitate the management of courses offered by the institution, capturing necessary attributes that will support future features such as course enrollment and tracking.

## 2. Technology Stack
### 2.1 Frameworks & Libraries
- **FastAPI**: For building the web API.
- **SQLAlchemy**: For ORM to interact with the SQLite database.
- **SQLite**: As the database for storing course records.
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
│   ├── main.py                   # Entry point of the application
│   ├── models/
│   │   ├── student.py            # Pydantic model and SQLAlchemy ORM model for Student
│   │   └── course.py             # Pydantic model and SQLAlchemy ORM model for Course
│   ├── routes/
│   │   ├── student_routes.py      # API endpoints for Student management
│   │   └── course_routes.py       # API endpoints for Course management
│   └── database/
│       └── db.py                 # Database connection and initialization
│
├── migrations/                    # Directory for database migration scripts
│   └── 001_create_courses_table.py # Migration script to create courses table
│
├── tests/
│   ├── test_student.py            # Unit tests for the student management
│   └── test_course.py             # Unit tests for the course management
│
├── requirements.txt               # Dependencies for the project
└── README.md                      # Documentation for setup and usage
```

### 3.2 Module Responsibilities
- **models/course.py**: Define the Course entity and its Pydantic model.
- **routes/course_routes.py**: Implement API endpoints for creating and retrieving courses.
- **database/db.py**: Maintain database connection and initialization.
- **migrations/001_create_courses_table.py**: Implement schema migration to create the Course table.

## 4. Data Models
### 4.1 Course Model
The Course entity will be implemented with the following fields:
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
```

### 4.2 Pydantic Schema
```python
from pydantic import BaseModel, constr

class CourseCreate(BaseModel):
    name: constr(min_length=1)  # Name must not be empty
    level: constr(min_length=1) # Level must not be empty

class CourseResponse(BaseModel):
    id: int
    name: str
    level: str

    class Config:
        orm_mode = True
```

## 5. API Contract
### 5.1 Endpoints
- **POST /courses**: Create a new course.
  - Request Body: `{"name": "Mathematics", "level": "Beginner"}`
  - Response: 
    - Status Code: 201
    - Body: `{"id": 1, "name": "Mathematics", "level": "Beginner"}`

- **GET /courses**: Retrieve a list of all courses.
  - Response:
    - Status Code: 200
    - Body: `[{"id": 1, "name": "Mathematics", "level": "Beginner"}, {"id": 2, "name": "Science", "level": "Intermediate"}]`

### 5.2 Error Handling
- If the name or level fields are empty during creation:
  - Response:
    - Status Code: 400
    - Body: `{"error": {"code": "E001", "message": "Course name is required."}}`
    
## 6. Implementation Steps
### 6.1 Setup Environment
- Ensure the setup from the previous sprint is intact and correctly configured.

### 6.2 Install Dependencies
- Verify that the dependencies in `requirements.txt` remain applicable, with no additions necessary for this feature.

### 6.3 Implement Database Migration (001_create_courses_table.py)
- Create a migration script to establish the new `courses` table without downtime.

```python
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from models.course import Course

def upgrade():
    engine = create_engine("sqlite:///./students.db")
    with engine.connect() as connection:
        connection.execute('''
            CREATE TABLE courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                level TEXT NOT NULL
            );
        ''')

def downgrade():
    engine = create_engine("sqlite:///./students.db")
    with engine.connect() as connection:
        connection.execute('DROP TABLE IF EXISTS courses;')

if __name__ == "__main__":
    upgrade()
```

### 6.4 Update API Endpoints (course_routes.py)
- Implement the POST endpoint to create a new course, checking for valid name and level fields.
- Implement the GET endpoint to retrieve all courses and return their details.

```python
from fastapi import APIRouter, HTTPException
from models.course import Course
from database.db import SessionLocal
from schemas.course import CourseCreate, CourseResponse

router = APIRouter()

@router.post("/courses", response_model=CourseResponse, status_code=201)
def create_course(course: CourseCreate):
    db = SessionLocal()
    db_course = Course(name=course.name, level=course.level)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

@router.get("/courses", response_model=list[CourseResponse])
def get_courses():
    db = SessionLocal()
    return db.query(Course).all()
```

### 6.5 Update Tests
- Implement unit tests in `test_course.py` for the Course creation and retrieval functionality.

```python
import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_create_course():
    response = client.post("/courses", json={"name": "Mathematics", "level": "Beginner"})
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["name"] == "Mathematics"
    assert response.json()["level"] == "Beginner"

def test_create_course_with_empty_name():
    response = client.post("/courses", json={"name": "", "level": "Advanced"})
    assert response.status_code == 400
    assert response.json()["error"]["message"] == "Course name is required."

def test_create_course_with_empty_level():
    response = client.post("/courses", json={"name": "History", "level": ""})
    assert response.status_code == 400
    assert response.json()["error"]["message"] == "Course level is required."

def test_get_courses():
    response = client.get("/courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
```

## 7. Testing Strategy
- Ensure that all user scenarios are covered:
  - **Successful creation of a course with valid name and level.**
  - **Validation failure when name or level is empty.**
  - **Successful retrieval of the course list.**
- Ensure a minimum of 70% test coverage for business logic.

## 8. Deployment Considerations
- The application must start correctly and run the migration script that creates the courses table on startup.
- Document explicit setup instructions in `README.md`.
- Avoid hardcoding configurations; use environment variables.

## 9. Documentation
- Update `README.md` to reflect:
  - Newly added API endpoints and examples for course creation and retrieval.
  - Migration guidelines and any relevant environment variable settings.

## 10. Conclusion
This implementation plan details a structured approach to enhancing the Student Management Web Application by integrating a new Course entity. Following this plan will ensure a consistent development process, preserve backward compatibility, and reinforce system integrity. The use of clearly defined tests will enhance the reliability of the course management functionality.

Existing Code Files Modifications:
- **models/course.py**: Create a new model for the Course entity.
- **routes/course_routes.py**: Implement new API endpoints for course management.
- **tests/test_course.py**: Create new test cases to validate course functionality. 

Existing Code Files:
File: tests/test_course.py
```python
```python
import pytest
from fastapi.testclient import TestClient
from src.main import app

# Initialize the TestClient for testing the API
client = TestClient(app)

def test_create_course():
    """Test for creating a course with a valid name and level."""
    response = client.post("/courses", json={"name": "Mathematics", "level": "Beginner"})
    assert response.status_code == 201  # Check for successful creation
    assert "id" in response.json()       # Check if the response contains the course id
    assert response.json()["name"] == "Mathematics"  # Ensure the name is correct

def test_create_course_with_invalid_name():
    """Test for creating a course with invalid (empty) name."""
    response = client.post("/courses", json={"name": "", "level": "Advanced"})
    assert response.status_code == 400  # Should return a bad request error
    assert response.json()["error"]["message"] == "Course name is required."
```
