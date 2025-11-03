# Implementation Plan: Add Course Relationship to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---
## Overview
The purpose of this implementation plan is to outline the technical architecture, technology stack, module responsibilities, data models, API contracts, and key considerations for adding a relationship between Student and Course entities within the existing application. This feature will enhance the application's capability to manage educational enrollment by allowing students to associate with multiple courses while preserving existing functionality and data integrity.

## Technology Stack
- **Programming Language**: Python 3.11+
- **Web Framework**: FastAPI
- **Database**: SQLite (using SQLAlchemy for ORM)
- **Testing Framework**: pytest
- **API Documentation**: Swagger UI (integrated with FastAPI)
- **Environment Management**: Poetry (for dependency management)
- **Type Checking**: MyPy (for static type checking)

## Module Structure
The existing application structure will be updated as follows:
- **src/**
  - **main.py**: 
    - **Modifications**: Include new routes for associating courses with students.
  - **models/**
    - `student.py`:
      - **Modifications**: Update the Student model to establish a relationship with Course through a StudentCourse link.
    - `course.py`:
      - **Modifications**: Ensure the Course model is ready to be used in relationship mappings.
    - `student_course.py`: 
      - **New File**: Define the StudentCourse relationship entity to link students and courses.
  - **schemas/**:
    - `student_course_schema.py`:
      - **New File**: Define Pydantic schemas for associating courses with students.
  - **routes/**:
    - `student_course_routes.py`:
      - **New File**: Create endpoints to handle student-course associations.
  - **database/**:
    - `database.py`: 
      - **Modifications**: Include migration scripts for the new StudentCourse relationship table.
- **migrations/**: Modify migration directory to support updates for the StudentCourse relationship.
- **tests/**:
  - `test_student_course.py`: 
      - **New File**: Create tests for associating courses with students.

## Data Model
### New StudentCourse Relationship Model
The StudentCourse relationship entity will be defined using SQLAlchemy as follows:
```python
from sqlalchemy import Column, Integer, ForeignKey
from database.database import Base

class StudentCourse(Base):
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
```

### Modifications to Existing Models
1. **Student Model**: Add a relationship to access `courses`.
```python
from sqlalchemy.orm import relationship
# Assuming this is within the existing Student model
class Student(Base):
    __tablename__ = 'students'
  
    # Existing columns...
  
    courses = relationship("Course", secondary="student_courses", back_populates="students")
```
2. **Course Model**: Add a relationship to access `students`.
```python
class Course(Base):
    __tablename__ = 'courses'
  
    # Existing columns...
  
    students = relationship("Student", secondary="student_courses", back_populates="courses")
```

### Pydantic Schema
Request and response validations for the Student-Course relationship will be handled using Pydantic as follows:
```python
from pydantic import BaseModel
from typing import List

class CourseAssociation(BaseModel):
    course_ids: List[int]  # List of Course IDs to associate

class StudentResponse(BaseModel):
    id: int
    name: str
    courses: List[int]  # List of associated Course IDs
```

## API Contracts
### Endpoints
1. **Associate Student with Courses**
   - **POST** `/students/{id}/courses`
   - Request Body: `{"course_ids": [1, 2, 3]}`
   - Response: `200 OK` with updated student details in JSON format, including the list of associated Course IDs.
  
2. **Retrieve a Student's Courses**
   - **GET** `/students/{id}/courses`
   - Response: `200 OK` with student details and associated Course IDs.

### Error Handling
- Returning a 400 for non-existent Course IDs should have a response format like: 
```json
{"error": {"code": "E001", "message": "Invalid Course ID."}}
```
  
## Implementation Approach
1. **Setup Environment**
   - Use Poetry to install required dependencies related to new modules.

2. **Database Migration**
   - Create a migration script in the `migrations/` folder to add the `student_courses` table.
   ```python
   from sqlalchemy import create_engine
   from database.database import Base
   from models.student_course import StudentCourse

   engine = create_engine('sqlite:///./test.db')  # Use the appropriate database URL
   Base.metadata.create_all(bind=engine)
   ```

3. **CRUD Functionality**
   - Implement `student_course_routes.py` to handle associating courses with students.
   - Use the StudentCourse model for establishing relationships and handle validations through schemas.

4. **Testing**
   - Develop unit tests in `test_student_course.py` to ensure coverage and correct behavior of the new feature, targeting at least 70% coverage.

5. **Documentation**
   - Update FastAPI documentation to include the new student-course association endpoints.

## Scalability and Security Considerations
- The SQLite database is adequate for this stage; transition to a more capable DB (e.g., PostgreSQL) may be necessary as usage grows.
- Ensure input sanitization on course associations to mitigate injection risks.

## Trade-offs and Decisions
- **Framework Choice**: Continuing with FastAPI capitalizes on previously established design and functionality.
- **Aggregation of Related Entities**: Utilizing many-to-many relationships (through the StudentCourse model) maintains extensibility for future features such as performance tracking.

---
## Conclusion
This implementation plan outlines the steps to integrate a relationship between students and courses within the existing application, following predefined coding standards and functional requirements. It enhances educational management capabilities while ensuring data integrity and backward compatibility.

Existing Code Files:
File: tests/test_student_course.py
```python
import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models.student import Student
from src.models.course import Course
from src.models.student_course import StudentCourse  # New import for the relationship model
from src.database.database import get_db, Base, engine

# Create the FastAPI test client
client = TestClient(app)

# Setup the test database
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)  # Create the database tables
    yield
    Base.metadata.drop_all(bind=engine)  # Clean up after tests
```