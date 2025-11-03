# Implementation Plan: Add Teacher Relationship to Course Entity

---

INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:  
# Implementation Plan: Create Teacher Entity

---

## I. Architecture Overview

The application will continue leveraging its microservices architecture principles, enhancing it by establishing the relationship between the Course entity and the Teacher entity:

1. **Web Server**: FastAPI will be used to manage HTTP requests and serve API endpoints for handling Course-Teacher assignments.
2. **Database**: SQLite will be utilized to persist the relationships without impacting existing structures or data integrity.

### Tech Stack
- **Web Framework**: FastAPI (Python 3.11+)
- **Database**: SQLite
- **Data Serialization**: Pydantic (for request and response validation)
- **Testing Framework**: pytest
- **ORM**: SQLAlchemy

## II. Module Boundaries

1. **API Module**:
   - Extend existing API routes to include Course-Teacher relationship handling (assignment and removal).

2. **Database Module**:
   - Modify the existing Course model to include a new `teacher_id` field as a Foreign Key.

3. **Error Handling Module**:
   - Verify validation for course and teacher data inputs, providing accurate error messages when invalid data is submitted.

4. **Testing Module**:
   - Create tests to validate scenarios for assigning, viewing, and removing teachers from courses.

## III. Data Models

### Course Model Update

To establish the relationship between `Course` and `Teacher`, we will modify the existing `Course` data model:

```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = "courses"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    # ... other existing fields ...
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New relationship field

    # Establish relationship with Teacher
    teacher = relationship("Teacher", back_populates="courses")
```

### Teacher Model 

Assuming the `Teacher` model has been previously defined, we will ensure it maintains a back-reference to the `Course` model for integrity:

```python
class Teacher(Base):
    __tablename__ = "teachers"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    courses = relationship("Course", back_populates="teacher")  # Added back-reference
```

### API Request and Response Models

Request and response models for managing the Course-Teacher relationship:

```python
from pydantic import BaseModel

class AssignTeacherRequest(BaseModel):
    teacher_id: int  # Required field for assigning a teacher to a course

class CourseDetailsResponse(BaseModel):
    id: int
    teacher_id: int = None  # Assigned teacher's ID; None if unassigned
    # ... other existing course fields ...
```

## IV. API Endpoints

### 1. Assign a Teacher to a Course
- **Endpoint**: `/courses/{course_id}/assign-teacher`  
- **Method**: POST 
- **Request Body**: 
```json
{
    "teacher_id": 1
}
```
- **Response (200 OK)**:
```json
{
    "message": "Teacher assigned successfully to course."
}
```

### 2. View Course with Teacher Information
- **Endpoint**: `/courses/{course_id}`  
- **Method**: GET
- **Response (200 OK)**:
```json
{
    "id": 1,
    "teacher_id": 1,
    // ... additional course details ...
}
```

### 3. Remove Teacher from Course
- **Endpoint**: `/courses/{course_id}/remove-teacher`  
- **Method**: DELETE
- **Response (200 OK)**:
```json
{
    "message": "Teacher removed successfully from the course."
}
```

## V. Implementation Approach

1. **Set Up Environment**:
   - Upgrade dependencies if necessary to ensure compatibility with existing modules.

2. **Modify API Logic**:
   - Extend current routes in `course_api.py` to include methods for assigning and removing the teacher from courses.

3. **Set Up Database**:
   - Modify the `db_setup.py` to include the `teacher_id` field in the existing Course schema.

4. **Database Migration Strategy**:
   - Use Alembic to create a migration script that will:
     - Alter the `Course` table to add the `teacher_id` column without impacting existing data.

## VI. Error Handling

- Implement validation on incoming requests for `teacher_id` to ensure it corresponds to an existing Teacher record.
- Return appropriate error messages if the course cannot be found or if invalid inputs are submitted.

## VII. Success Criteria Verification

1. Admin can successfully assign a teacher to a course and will receive confirmation in the response.
2. Users can view course details correctly, which includes the teacher's information.
3. Admin can remove a teacher from a course successfully, and fetching the course details afterward reflects this change.

## VIII. Testing Strategy

1. **Unit Tests**: Create tests for the functionality of assigning and removing teachers from courses.
2. **Integration Tests**: Validate the API endpoints:
   - Implement tests for POST, DELETE, and GET requests related to teacher assignments.

## IX. Documentation

- Update `README.md` to include the new API endpoints for managing Course-Teacher relationships, detailing request formats and examples.
- Document the migration process for the `Course` table modifications to ensure deployment can proceed smoothly.

## X. Version Control Practices

- Commit changes with clear messages detailing the addition of Course-Teacher relationship management.
- Structure commits logically to facilitate easier review and documentation alignment.

## XI. Deployment Considerations 

- Implement the database migration regarding the `Course` table carefully and test thoroughly in a staging environment before deployment to production.
- Validate that the application starts successfully and all functionalities work, ensuring no existing data integrity issues arise.

### Existing Code Modifications:

**File**: `src/db_setup.py`
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student, Course, Teacher  # Ensure Teacher model is imported

def setup_database():
    ...
    # Ensure the teacher_id column added to the Course table
    Base.metadata.create_all(engine)  # This will create all necessary tables including modifications.
```

**File**: `src/course_api.py` (extend existing file)
```python
from fastapi import APIRouter, HTTPException
from models import Course, AssignTeacherRequest, CourseDetailsResponse
from db_setup import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/courses/{course_id}/assign-teacher", response_model=dict)
def assign_teacher(course_id: int, request: AssignTeacherRequest):
    session = SessionLocal()
    course = session.query(Course).filter(Course.id == course_id).first()
    if not course:
        session.close()
        raise HTTPException(status_code=404, detail="Course not found")
    
    course.teacher_id = request.teacher_id
    session.commit()
    session.close()
    return {"message": "Teacher assigned successfully to course."}

@router.delete("/courses/{course_id}/remove-teacher", response_model=dict)
def remove_teacher(course_id: int):
    session = SessionLocal()
    course = session.query(Course).filter(Course.id == course_id).first()
    if not course:
        session.close()
        raise HTTPException(status_code=404, detail="Course not found")
    
    course.teacher_id = None  # Setting to None to reflect removal
    session.commit()
    session.close()
    return {"message": "Teacher removed successfully from the course."}
```

### Testing Files

**File**: `tests/test_course_api.py`
```python
import pytest
from fastapi.testclient import TestClient
from src.main import app  # Adjust based on your project structure
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db_setup import Base

client = TestClient(app)

# Test assigning a teacher to a course
def test_assign_teacher():
    response = client.post("/courses/1/assign-teacher", json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json()["message"] == "Teacher assigned successfully to course."

# Test removing a teacher from a course
def test_remove_teacher():
    response = client.delete("/courses/1/remove-teacher")
    assert response.status_code == 200
    assert response.json()["message"] == "Teacher removed successfully from the course."

# Test viewing course with teacher information
def test_view_course_with_teacher():
    response = client.get("/courses/1")  # Adjust ID as necessary
    assert response.status_code == 200
    # Add assertions to check teacher_id in response
```

By implementing this plan, we will effectively enhance the existing application, integrating Teacher-Course relationships while ensuring code quality and backward compatibility are maintained.