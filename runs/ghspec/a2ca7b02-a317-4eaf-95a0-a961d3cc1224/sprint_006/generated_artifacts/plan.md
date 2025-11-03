# Implementation Plan: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Entity Management

**Version**: 1.0.0  
**Purpose**: Implement the Add Teacher Relationship to Course Entity feature, enhancing the connection between Courses and Teachers within the educational platform.

---

## I. Architecture Overview

### 1.1 Technology Stack
- **Backend Framework**: FastAPI (Python)
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing Framework**: Pytest
- **Environment Management**: Poetry for dependency management

### 1.2 Module Boundaries and Responsibilities

- **Course Model (`models/course.py`)**
  - Extend existing Course entity to include a relation to the Teacher entity.

- **Database Management (`db/database.py`)**
  - Update schema to support a foreign key relationship between Course and Teacher.

- **Course Service (`services/course_service.py`)**
  - Business logic for assigning teachers to courses and retrieving course details.

- **API Endpoints (`api/course.py`)**
  - Enhance existing routes for courses to include teacher assignment functionality.

- **Input Validation (`validators/course_validator.py`)**
  - Validate incoming requests to ensure that the teacher exists before assignment.

- **Testing (`tests/test_course.py`)**
  - Define unit and integration tests for the new features surrounding course and teacher relationships.

---

## II. Data Models

### 2.1 Modify Course Entity
Extend the existing `models/course.py` to include a relationship with the Teacher entity.

```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New relationship field
    teacher = relationship("Teacher", back_populates="courses")  # Establish relationship

class Teacher(Base):
    __tablename__ = 'teachers'
    
    # Add existing fields here...
    courses = relationship("Course", back_populates="teacher")  # Reverse relationship for teacher
```

### 2.2 API Contracts

- **Assign Teacher to Course (POST /courses/{course_id}/assign-teacher)**
  - **Request Body**: 
    ```json
    {
      "teacher_id": "1"
    }
    ```
  - **Response**:
    - **200 OK**:
    ```json
    {
      "message": "Teacher assigned successfully",
      "course": {
        "id": 1,
        "title": "Math 101",
        "teacher_id": 1
      }
    }
    ```

- **Retrieve Course with Teacher (GET /courses/{course_id})**
  - **Response**:
    - **200 OK**:
    ```json
    {
      "id": 1,
      "title": "Math 101",
      "teacher": {
        "id": 1,
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
      }
    }
    ```

---

## III. Implementation Approach

### 3.1 Database Migration
Create a new migration script to alter the existing `courses` table and set up the foreign key to link the `teachers` table.

```sql
ALTER TABLE courses
ADD COLUMN teacher_id INTEGER,
ADD FOREIGN KEY (teacher_id) REFERENCES teachers(id);
```

### 3.2 Database Initialization
Update the existing `db/database.py` to ensure schema alterations are handled gracefully while enabling backward compatibility.

```python
from models.course import Course
from models.teacher import Teacher  # Ensure Teacher model is imported

# Table creation logic remains as it is.
# Ensure to check for existing tables to avoid duplicates.
```

### 3.3 API Development
- **API Endpoints**:
  Create or update FastAPI routers in `api/course.py` to define endpoints for assigning a teacher to a course and retrieving details.

```python
from fastapi import APIRouter, HTTPException
from services.course_service import CourseService

router = APIRouter()

@router.post("/courses/{course_id}/assign-teacher")
async def assign_teacher(course_id: int, teacher_data: dict):
    return await CourseService.assign_teacher(course_id, teacher_data)

@router.get("/courses/{course_id}")
async def retrieve_course(course_id: int):
    return await CourseService.get_course(course_id)
```

### 3.4 Service Layer Logic
Implement `course_service.py` to handle the logic related to assigning a teacher to a course and fetching course details.

```python
from models.course import Course
from models.teacher import Teacher
from db.database import Session
from fastapi import HTTPException

class CourseService:
    
    @staticmethod
    async def assign_teacher(course_id: int, data: dict):
        async with Session() as session:
            teacher = await session.get(Teacher, data['teacher_id'])
            if not teacher:
                raise HTTPException(status_code=404, detail="Teacher not found")

            course = await session.get(Course, course_id)
            if not course:
                raise HTTPException(status_code=404, detail="Course not found")

            course.teacher_id = teacher.id
            await session.commit()
            return {"message": "Teacher assigned successfully", "course": course}

    @staticmethod
    async def get_course(course_id: int):
        async with Session() as session:
            course = await session.get(Course, course_id)
            if not course:
                raise HTTPException(status_code=404, detail="Course not found")
            return course
```

### 3.5 Input Validation
Create `validators/course_validator.py` to ensure validations are in place for the inputs related to teacher assignment.

```python
def validate_teacher_id(teacher_id: int):
    if not teacher_id:
        raise ValueError("Teacher ID is required.")
    # Additional checks can be performed to ensure teacher exists
```

### 3.6 Error Handling
Extend the error handling logic to ensure appropriate errors are raised and logged, especially for linking a teacher that does not exist or is already assigned.

---

## IV. Testing Plan

### 4.1 Test Coverage
Include tests for the following scenarios:
- Successful assignment of a teacher to a valid course.
- Error responses for non-existent teacher or course.
- Validation for attempting to assign a teacher when the course already has one assigned.

### 4.2 Testing Structure
Implement tests within `tests/test_course.py` to cover all scenarios clearly.

```python
import pytest
from services.course_service import CourseService

@pytest.fixture
def setup_database():
    # Setup an in-memory SQLite database for testing
    pass  # Implement database setup as per project structure

def test_assign_teacher_valid_data(setup_database):
    # Arrange
    course_id = 1
    teacher_data = {"teacher_id": 1}
    
    # Act
    response = CourseService.assign_teacher(course_id, teacher_data)
    
    # Assert
    assert response['message'] == "Teacher assigned successfully"

def test_assign_teacher_invalid_teacher(setup_database):
    # Act & Assert
    with pytest.raises(HTTPException):
        CourseService.assign_teacher(course_id, {"teacher_id": 999})  # Non-existent teacher
```

---

## V. Deployment Considerations

### 5.1 Environment Variables
Ensure sensitivity remains maintained by using the appropriate `.env` configuration file for database connections and settings.

### 5.2 Documentation
Update the `README.md` to document new API endpoints with examples for the Course and Teacher relationship management.

---

## VI. Security Considerations
- Implement input validation to prevent SQL injection attacks through user inputs.
- Protect against unique constraint violations when allowing teacher assignments.

---

## VII. Error Handling and Logging
Ensure structured error logging is in place, following JSON formats to easily parse and monitor issues.

---

## VIII. Performance and Scalability
Monitor the performance of teacher assignment and retrieval of courses. As system use grows, consider caching strategies for retrieved data.

---

## IX. Trade-offs and Decisions
- Maintaining SQLite allows for a straightforward development process. Future migrations to a more robust database can be considered as the platform scales.
- FastAPI's performance and asynchronous capabilities maintain efficiency and robustness for the added functionalities.

---

## Success Metrics
1. Target a success rate of 95% or higher for valid teacher assignment requests.
2. Ensure retrieval of course data is dependable, successfully accessed 90% of the time.
3. Provide clear error messaging for invalid submissions or teacher assignments consistently.
4. Execute the migration script successfully, maintaining backward compatibility without risking data loss or corruption.

---

This implementation plan outlines a comprehensive strategy for integrating the Teacher relationship into the Course entity within the existing educational platform, adhering to best practices and ensuring a smooth developmental process.