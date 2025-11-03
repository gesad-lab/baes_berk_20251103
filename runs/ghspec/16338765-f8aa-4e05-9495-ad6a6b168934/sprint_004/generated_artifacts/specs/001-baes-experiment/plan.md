# Implementation Plan: Add Course Relationship to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:  
# Implementation Plan: Create Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:  
# Implementation Plan: Add Email Field to Student Entity

---

## I. Architecture Overview

The application will continue to utilize a microservices architecture with clear boundaries between modules. The core components remain the same:

1. **Web Server**: FastAPI will manage HTTP requests and serve API endpoints.
2. **Database**: SQLite will persist course and student records efficiently, enabling tracking of enrollments.

### Tech Stack
- **Web Framework**: FastAPI (Python 3.11+)
- **Database**: SQLite
- **Data Serialization**: Pydantic (for request and response validation)
- **Testing Framework**: pytest

## II. Module Boundaries

1. **API Module**:
   - Extend existing routes to include HTTP request handling for course enrollment management in addition to student functionalities.

2. **Database Module**:
   - Introduce a `StudentCourse` data model to manage the many-to-many relationship between Students and Courses and handle schema management.

3. **Error Handling Module**:
   - Implement enhanced error handling to validate inputs for enrollments and return appropriate error messages when validation fails.

4. **Testing Module**:
   - Implement tests reflecting new scenarios associated with course enrollments and relationships with students.

## III. Data Models

### StudentCourse Model

```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StudentCourse(Base):
    __tablename__ = "StudentCourse"
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
```

### Update Existing Course and Student Models

The existing models for Course and Student may not require changes, but they should ensure their relationships are properly defined in the ORM if not already done.

### API Request and Response Models
```python
from pydantic import BaseModel
from typing import List

class CourseEnrollment(BaseModel):
    course_id: int  # Required field for enrollment

class CourseEnrollmentsUpdate(BaseModel):
    course_ids: List[int]  # Required for updating enrollments

class EnrollmentResponse(BaseModel):
    student_id: int
    course_id: int
```

## IV. API Endpoints

### 1. Enroll a Student in a Course
- **Endpoint**: `/students/{student_id}/courses`
- **Method**: POST
- **Request Body**: 
```json
{
    "course_id": 1
}
```
- **Response (201 Created)**:
```json
{
    "student_id": 1,
    "course_id": 1
}
```

### 2. Retrieve Student's Courses
- **Endpoint**: `/students/{student_id}/courses`
- **Method**: GET
- **Response (200 OK)**:
```json
{
    "courses": [
        {
            "id": 1,
            "name": "Introduction to Python",
            "level": "Beginner"
        },
        {
            "id": 2,
            "name": "Mathematics 101",
            "level": "Beginner"
        }
    ]
}
```

### 3. Update Course Enrollment
- **Endpoint**: `/students/{student_id}/courses`
- **Method**: PUT
- **Request Body**: 
```json
{
    "course_ids": [1, 2, 3]
}
```
- **Response (200 OK)**:
```json
{
    "student_id": 1,
    "course_ids": [1, 2, 3]
}
```

## V. Implementation Approach

1. **Set Up Environment**:
   - Ensure existing project environment supports the addition of new modules.
   - Confirm dependencies are properly installed and configured in FastAPI.

2. **Implement API Logic**:
   - Extend FastAPI routes in a new file `enrollment_api.py` to include new `POST`, `GET`, and `PUT` endpoints for course enrollment management.

3. **Set Up Database**:
   - Update existing `db_setup.py` to modify the SQLite schema, creating the new `StudentCourse` table with appropriate constraints.

4. **Database Migration Strategy**:
   - Create a new migration script that sets up the `StudentCourse` table, ensuring referential integrity without disrupting existing student and course data.

## VI. Error Handling

- Implement error handling in the new API to validate existing student and course IDs during enrollments/updates.
- Return clear error messages for invalid requests.

## VII. Success Criteria Verification

1. Validate that creating a course enrollment works with valid `student_id` and `course_id`, returning the correct enrollment response.
2. Ensure retrieving courses for a student works as expected.
3. Confirm updates to a student’s list of enrolled courses reflect changes appropriately and accurately when re-fetched.

## VIII. Testing Strategy

1. **Unit Tests**: Cover functionality for enrolling, retrieving, and updating student courses.
2. **Integration Tests**: Validate endpoint functionality for enrolling a student, retrieving their courses, and modifying enrollments:
   - Implement tests for POST, GET, and PUT endpoints.

## IX. Documentation

- Update the `README.md` to include new API endpoints, request/response formats, and example payloads for course enrollments.
- Document the database migration process to ensure deployment readiness.

## X. Version Control Practices

- Commit changes with clear messages indicating the feature addition.
- Organize commits into logical increments, ensuring documentation stays up-to-date with code.

## XI. Deployment Considerations 

- Verify that the database migration for adding the `StudentCourse` table has been thoroughly tested.
- Ensure that upon application startup, the feature can be fully tested and verified without downtime or disruption in existing functionalities.

### Existing Code Modifications:

**File**: `src/db_setup.py`
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Course, StudentCourse  # Ensure to import the new StudentCourse model
...

def setup_database():
    ...
    Base.metadata.create_all(engine)  # This will now create all necessary tables
```

**File**: `src/enrollment_api.py` (new file for managing student course enrollments)
```python
from fastapi import APIRouter, HTTPException
from models import StudentCourse, Course, CourseEnrollment, CourseEnrollmentsUpdate, EnrollmentResponse
from db_setup import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/students/{student_id}/courses", response_model=EnrollmentResponse, status_code=201)
def enroll_student_in_course(student_id: int, enrollment: CourseEnrollment):
    session = SessionLocal()
    course = session.query(Course).filter(Course.id == enrollment.course_id).first()
    if not course:
        session.close()
        raise HTTPException(status_code=404, detail="Course not found")

    enrollment_entry = StudentCourse(student_id=student_id, course_id=enrollment.course_id)
    session.add(enrollment_entry)
    session.commit()
    session.refresh(enrollment_entry)
    session.close()
    return EnrollmentResponse(student_id=enrollment_entry.student_id, course_id=enrollment_entry.course_id)

@router.get("/students/{student_id}/courses")
def get_courses_for_student(student_id: int):
    session = SessionLocal()
    courses = session.query(Course).join(StudentCourse).filter(StudentCourse.student_id == student_id).all()
    session.close()
    return {"courses": [{"id": course.id, "name": course.name, "level": course.level} for course in courses]}

@router.put("/students/{student_id}/courses", response_model=EnrollmentResponse)
def update_courses_for_student(student_id: int, enrollment_update: CourseEnrollmentsUpdate):
    session = SessionLocal()
    session.query(StudentCourse).filter(StudentCourse.student_id == student_id).delete()
    
    # Add new courses
    for course_id in enrollment_update.course_ids:
        if session.query(Course).filter(Course.id == course_id).first() is None:
            session.close()
            raise HTTPException(status_code=404, detail="One or more courses not found")
        session.add(StudentCourse(student_id=student_id, course_id=course_id))

    session.commit()
    session.close()
    return EnrollmentResponse(student_id=student_id, course_ids=enrollment_update.course_ids)
```

### Testing Files

**File**: `tests/test_enrollment_api.py`
```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Adjust the import based on your actual project structure
from src.models import Course, Student, StudentCourse  # Import necessary data models

client = TestClient(app)

# Test enrollment of a student in a course
def test_enroll_student_in_course():
    response = client.post("/students/1/courses", json={"course_id": 1})
    assert response.status_code == 201
    data = response.json()
    assert data["student_id"] == 1
    assert data["course_id"] == 1

# Test retrieval of courses for a student
def test_get_courses_for_student():
    response = client.get("/students/1/courses")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["courses"], list)  # Ensure we get a list back

# Test updating courses for a student
def test_update_courses_for_student():
    response = client.put("/students/1/courses", json={"course_ids": [1, 2]})
    assert response.status_code == 200
    data = response.json()
    assert data["student_id"] == 1
    assert sorted(data["course_ids"]) == sorted([1, 2])
```

By adhering to the outlined implementation plan, the enhancement to manage student-course relationships can be achieved effectively, enriching the application's functionalities while ensuring integration with existing modules and code adherence.