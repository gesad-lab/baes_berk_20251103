# Implementation Plan: Add Teacher Relationship to Course Entity

---

## I. Overview

The purpose of this implementation plan is to define the technical architecture and implementation strategy for establishing a relationship between the `Course` entity and the newly created `Teacher` entity within the existing educational database system. This feature will enable the application to associate courses with designated teachers, thus enhancing the management of teaching assignments and improving the user experience for administrators.

## II. Architecture

### 1. System Components

- **Web Framework**: FastAPI (Python) for building the asynchronous API.
- **Database**: SQLite, for lightweight, file-based data storage, continuing from the previous implementation.
- **ORM**: SQLAlchemy to connect and interact with the SQLite database.
- **API Documentation**: Swagger UI provided by FastAPI enabled for automatic API documentation.

### 2. Module Structure

- **src/**
  - **api/**: Contains API endpoints.
    - `courses.py`: Update to manage requests related to course operations.
    - `teachers.py`: New module to manage requests related to teacher operations.
  - **models/**: Defines data models.
    - `course.py`: Update to include the `teacher_id` relationship.
    - `teacher.py`: New SQLAlchemy model for the `Teacher` entity.
  - **db/**: Responsible for database interactions.
    - `database.py`: Update to manage the schema change for the `Course` and `Teacher` tables.
  - **main.py**: Entry point for the application; will initialize the new `Teacher` entity logic.

- **tests/**: Contains test files.
  - `test_courses.py`: Update to include tests covering course-teacher relationships.
  - `test_teachers.py`: New test suite for testing teacher creation and retrieval operations.

---

## III. Technology Stack

- **Programming Language**: Python 3.9+
- **Web Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing Framework**: pytest
- **Dependency Management**: pip with requirements.txt

---

## IV. Implementation Details

### 1. Data Models

#### 1.1 Update `Course` Model

Add `teacher_id` to the existing `Course` model to establish the new relationship:

```python
# src/models/course.py
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    teacher_id = Column(String, ForeignKey('teachers.id'), nullable=True)  # New foreign key to Teacher

    teacher = relationship("Teacher", back_populates="courses")  # Define relationship for ORM access
```

#### 1.2 New `Teacher` Model

Create the `Teacher` model:

```python
# src/models/teacher.py
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(String, primary_key=True, index=True)  # Auto-generated ID
    name = Column(String, nullable=False)  # Required teacher name
    email = Column(String, nullable=False, unique=True)  # Required teacher email (must be unique)

```

### 2. Database Setup

#### Migration Strategy

The migration strategy will involve updating the existing database schema to include the new `teacher_id` in the `courses` table without losing data. The application will create the required relationships on startup as part of schema initialization.

```python
# src/db/database.py
from sqlalchemy import create_engine, ForeignKeyConstraint
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from models.course import Base as CourseBase
from models.teacher import Base as TeacherBase

DATABASE_URL = "sqlite:///./education.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    CourseBase.metadata.create_all(bind=engine)  # Existing tables
    TeacherBase.metadata.create_all(bind=engine) # Create Teacher table
    # To maintain transactional integrity, consider wrapping in try-except for migrations
```

### 3. API Endpoints

#### Update Endpoint for Assigning Teacher to Course

Create or update API endpoints to assign a teacher to a course and retrieve course details including the assigned teacher.

```python
# src/api/courses.py
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from db.database import SessionLocal
from models.course import Course
from models.teacher import Teacher

router = APIRouter()

class AssignTeacher(BaseModel):
    teacher_id: str

@router.post("/courses/{course_id}/assign_teacher")
def assign_teacher(course_id: str, assign_teacher: AssignTeacher):
    db = SessionLocal()
    course = db.query(Course).filter(Course.id == course_id).first()
    teacher = db.query(Teacher).filter(Teacher.id == assign_teacher.teacher_id).first()

    if not course:
        raise HTTPException(status_code=404, detail={"error": {"code": "E002", "message": "Course does not exist"}})
    if not teacher:
        raise HTTPException(status_code=404, detail={"error": {"code": "E003", "message": "Teacher does not exist"}})

    course.teacher_id = assign_teacher.teacher_id
    db.commit()
    db.refresh(course)

    return {"message": "Teacher assigned to course successfully"}

@router.get("/courses/{course_id}")
def get_course_details(course_id: str):
    db = SessionLocal()
    course = db.query(Course).filter(Course.id == course_id).first()
    
    if not course:
        raise HTTPException(status_code=404, detail={"error": {"code": "E002", "message": "Course does not exist"}})

    return {
        "course": {
            "name": course.name,
            "teacher": {
                "name": course.teacher.name if course.teacher else None,
                "email": course.teacher.email if course.teacher else None
            }
        }
    }
```

### 4. Application Entry Point

Update the main application entry point to include the new course teaching assignments.

```python
# src/main.py
from fastapi import FastAPI
from db.database import init_db
import api.courses
import api.teachers

app = FastAPI()

@app.on_event("startup")
def startup_event():
    init_db()

app.include_router(api.courses.router)  # Include updated courses routes
app.include_router(api.teachers.router)  # Include new teachers routes
```

---

## V. Testing Strategy

### 1. Test Coverage

Unit tests will be updated for the course-teacher relationship, ensuring each functional scenario is covered:

- **Assign Teacher to Course**
- **Retrieve Course Details with Assigned Teacher**
- **Error Handling for Non-existent Course/Teacher**

### 2. Test Structure

Update `test_courses.py` and create new tests where necessary:

```python
# tests/test_courses.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_assign_teacher_to_course():
    """Test assigning a teacher to a course."""
    response = client.post("/courses/course1/assign_teacher", json={"teacher_id": "teacher123"})
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher assigned to course successfully"}

def test_assign_teacher_to_non_existent_course():
    """Test assigning a teacher to a non-existent course."""
    response = client.post("/courses/invalid_course_id/assign_teacher", json={"teacher_id": "teacher123"})
    assert response.status_code == 404
    assert response.json() == {"error": {"code": "E002", "message": "Course does not exist"}}

def test_get_course_details_with_teacher():
    """Test retrieving course details including assigned teacher."""
    response = client.get("/courses/course1")
    assert response.status_code == 200
    assert "teacher" in response.json()["course"]
```

---

## VI. Deployment Considerations

### 1. Environment Setup

- Ensure Python (version 3.9+) is installed alongside dependencies specified in `requirements.txt`.

### 2. Configuration Management

- Environment-specific configurations should be managed through environment variables if needed. The `.env.example` should reflect required configurations.

---

## VII. Security Considerations

- All incoming data will be validated to ensure compliant types and formats to mitigate risks such as injection attacks.
- Sensitive information (e.g., teacher email) will not be logged or unnecessarily exposed.

---

## VIII. Performance Considerations

- Leveraging SQLite’s lightweight design will allow the application to maintain expected performance levels, especially with proper indexing and query strategies for teacher assignment operations.

---

## IX. Additional Notes

- The implementation maintains backward compatibility with existing models, ensuring that changes are additive rather than disruptive. The integration of the `Teacher` entity into the `Course` model will enable expanded management functionalities while adhering to established coding standards.

This implementation plan provides a comprehensive pathway for implementing the relationship between the `Course` and `Teacher` entities in the educational database system, ensuring all aspects of the specification are covered.