# Implementation Plan: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## I. Overview

The purpose of this implementation plan is to define the technical architecture and implementation strategy for adding a many-to-many relationship between the `Student` and `Course` entities in the existing educational database system. This feature will enable students to enroll in multiple courses, enhancing the school’s ability to track student participation and improve academic tracking and reporting.

## II. Architecture

### 1. System Components

- **Web Framework**: FastAPI (Python) for building the asynchronous API.
- **Database**: SQLite, for lightweight, file-based data storage.
- **ORM**: SQLAlchemy to connect and interact with the SQLite database.
- **API Documentation**: Swagger UI provided by FastAPI enabled for automatic API documentation.

### 2. Module Structure

- **src/**
  - **api/**: Contains API endpoints.
    - `student.py`: Updates to manage course enrollments.
    - `courses.py`: New module to handle requests related to course management (enrollment and retrieval).
  - **models/**: Defines data models.
    - `student.py`: Updates to include the new many-to-many relationship.
    - `student_courses.py`: New SQLAlchemy model representing the join table for `Student` and `Course` enrollments.
  - **db/**: Responsible for database interactions.
    - `database.py`: Adjustments to manage the new schema updates for the join table.
  - **main.py**: Entry point for the application; will initialize the new relationship logic.

- **tests/**: Contains test files.
  - `test_student.py`: Updates for testing student enrollments and error handling.
  - `test_courses.py`: New test suite for managing course enrollment operations.

## III. Technology Stack

- **Programming Language**: Python 3.9+
- **Web Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing Framework**: pytest
- **Dependency Management**: pip with requirements.txt

## IV. Implementation Details

### 1. Data Models

#### 1.1 Existing `Student` Model Update

```python
# src/models/student.py
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(String, primary_key=True, index=True)
    # Existing fields...

    # New relationship declaration
    courses = relationship("StudentCourse", back_populates="student")
```

#### 1.2 New `Course` Model

```python
# src/models/course.py
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(String, primary_key=True, index=True)  # Primary key for the course
    name = Column(String, nullable=False)  # Required course title
    level = Column(String, nullable=False)  # Required course level
```

#### 1.3 New `StudentCourse` Join Table

```python
# src/models/student_courses.py
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class StudentCourse(Base):
    __tablename__ = 'student_courses'

    student_id = Column(String, ForeignKey('students.id'), primary_key=True)
    course_id = Column(String, ForeignKey('courses.id'), primary_key=True)

    # Define relationships
    student = relationship("Student", back_populates="courses")
    course = relationship("Course")
```

### 2. Database Setup

#### Migration Strategy

On application startup, the code will check if the `student_courses` table exists, along with the `courses` table, and create them if not. This can be accomplished using SQLAlchemy's `create_all` method.

```python
# src/db/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.student import Base as StudentBase
from models.course import Base as CourseBase
from models.student_courses import Base as StudentCourseBase

DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    # Create tables if they do not exist
    StudentBase.metadata.create_all(bind=engine)  # Ensure Student table exists
    CourseBase.metadata.create_all(bind=engine)   # Ensure Course table exists
    StudentCourseBase.metadata.create_all(bind=engine)  # Ensure join table exists
```

### 3. API Endpoints

#### New Endpoints for Enrollment Management

Two API endpoints will be added for enrolling a student and retrieving enrolled courses.

```python
# src/api/student.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from db.database import SessionLocal
from models.student_courses import StudentCourse
from models.student import Student
from models.course import Course

router = APIRouter()

class Enrollment(BaseModel):
    course_id: str

@router.post("/students/{student_id}/courses")
def enroll_student(student_id: str, enrollment: Enrollment):
    db = SessionLocal()
    
    # Validate student and course existence
    student = db.query(Student).filter(Student.id == student_id).first()
    course = db.query(Course).filter(Course.id == enrollment.course_id).first()

    if not student or not course:
        raise HTTPException(status_code=400, detail={"error": {"code": "E002", "message": "Invalid student ID or course ID"}})

    # Create enrollment record
    new_enrollment = StudentCourse(student_id=student_id, course_id=enrollment.course_id)
    db.add(new_enrollment)
    db.commit()

    return {"message": "Student enrolled successfully", "studentId": student_id, "courseId": enrollment.course_id}

@router.get("/students/{student_id}/courses")
def get_student_courses(student_id: str):
    db = SessionLocal()
    enrolled_courses = db.query(StudentCourse).filter(StudentCourse.student_id == student_id).all()

    courses = [{"name": course.course.name, "level": course.course.level} for course in enrolled_courses]
    
    return {"courses": courses}
```

### 4. Application Entry Point

The main application entry point will need to import and include the new student routes.

```python
# src/main.py
from fastapi import FastAPI
from db.database import init_db

app = FastAPI()

@app.on_event("startup")
def startup_event():
    init_db()

# Import API routes
import api.student  # Existing student routes
app.include_router(api.student.router)  # Register student routes 
```

## V. Testing Strategy

### 1. Test Coverage

- Unit tests for enrolling a student and retrieving courses should be implemented to ensure all functional scenarios are covered, focusing on successful operations as well as error handling for incorrect inputs.

### 2. Test Structure

```python
# tests/test_student.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_enroll_student_valid():
    """Test enrolling a student with valid student and course IDs."""
    response = client.post("/students/123/courses", json={"course_id": "C001"})
    assert response.status_code == 200
    assert response.json() == {"message": "Student enrolled successfully", "studentId": "123", "courseId": "C001"}

def test_enroll_student_invalid_course():
    """Test enrolling a student with an invalid course ID."""
    response = client.post("/students/123/courses", json={"course_id": "INVALID_COURSE"})
    assert response.status_code == 400
    assert response.json() == {"error": {"code": "E002", "message": "Invalid student ID or course ID"}}

def test_get_student_courses():
    """Test retrieving all courses a student is enrolled in."""
    response = client.get("/students/123/courses")
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

- SQLite’s lightweight nature will ensure the application can handle expected workloads. Proper indexing and efficient querying will maximize performance, especially when fetching enrolled courses.

## IX. Additional Notes

- The API will create the `student_courses` join table on startup as part of schema migration, ensuring seamless integration within the database without losing existing data related to students or other entities. The addition of the `StudentCourse` entity does not interfere with existing data integrity.