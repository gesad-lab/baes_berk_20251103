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
**Purpose**: Implement the Add Course Relationship to Student Entity feature to enhance student enrollment management and tracking in the web application.

---

## I. Architecture Overview

### 1.1 Technology Stack
- **Backend Framework**: FastAPI (Python)
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing Framework**: Pytest
- **Environment Management**: Poetry for dependency management

### 1.2 Module Boundaries and Responsibilities

- **Student Model (`models/student.py`)**
  - Update the existing Student entity to include a relationship to the Course entity.

- **Course Model (`models/course.py`)**
  - Ensure that the Course entity is defined to allow for relations with the Student model.

- **Database Management (`db/database.py`)**
  - Perform relevant updates to facilitate the Student-Course relationship through a join table.

- **Student Service (`services/student_service.py`)**
  - Business logic for enrolling students in courses and retrieving student data with courses.

- **API Endpoints (`api/student.py`)**
  - Expose RESTful routes for enrolling students in courses and retrieving a student's enrolled courses.

- **Input Validation (`validators/student_validator.py`)**
  - Validate incoming requests for required fields when enrolling in courses.

- **Testing (`tests/test_student.py`)**
  - Define unit and integration tests for the student-course relationship functionality.

---

## II. Data Models

### 2.1 Updated Student Entity
Update `models/student.py` to represent the relationship between students and courses. This will typically include a many-to-many relationship via an association table.

```python
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

association_table = Table('student_courses', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    
    # Relationship to represent enrolled courses
    courses = relationship("Course", secondary=association_table, back_populates="students")
```

### 2.2 Updated Course Entity
Ensure the Course model can represent its relationship back to students.

```python
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    # Relationship to represent students enrolled in the course
    students = relationship("Student", secondary=association_table, back_populates="courses")
```

### 2.3 API Contracts

- **Enroll Student in Course (POST /students/{student_id}/courses)**
  - **Request Body**: 
    ```json
    {
      "course_id": "1"
    }
    ```
  - **Response**:
    - **200 OK**:
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "courses": [
        {
          "id": 1,
          "name": "Course Name",
          "level": "Beginner"
        }
      ]
    }
    ```

- **Retrieve Student with Courses (GET /students/{student_id})**
  - **Response**:
    - **200 OK**:
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "courses": [
        {
          "id": 1,
          "name": "Course Name",
          "level": "Beginner"
        }
      ]
    }
    ```

---

## III. Implementation Approach

### 3.1 Database Migration
Create a new migration script to set up the association table (`student_courses`) to establish a many-to-many relationship.

```sql
CREATE TABLE student_courses (
    student_id INTEGER,
    course_id INTEGER,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);
```
Ensure the migration script runs at application startup if the database schema is outdated.

### 3.2 Database Initialization
Update `db/database.py` accordingly to incorporate the new association table:

```python
from models.student import Student
from models.course import Course  # Maintain import for relationship configuration

# In the section that creates tables
Base.metadata.create_all(bind=engine)  # This will include the new association table.
```

### 3.3 API Development
- **API Endpoints**:
  Create a new FastAPI router in `api/student.py` to define endpoints for enrolling students and retrieving student data alongside courses.

```python
from fastapi import APIRouter, HTTPException
from services.student_service import StudentService

router = APIRouter()

@router.post("/students/{student_id}/courses")
async def enroll_student_in_course(student_id: int, course_data: dict):
    return await StudentService.enroll_student_in_course(student_id, course_data['course_id'])

@router.get("/students/{student_id}")
async def retrieve_student_with_courses(student_id: int):
    return await StudentService.get_student_with_courses(student_id)
```

### 3.4 Service Layer Logic
Implement the `student_service.py` to handle the students' enrollment logic and retrieving student details with their courses.

```python
class StudentService:
    @staticmethod
    async def enroll_student_in_course(student_id: int, course_id: int):
        # Validate student and course existence
        # Handle enrollment logic
        pass

    @staticmethod
    async def get_student_with_courses(student_id: int):
        # Fetch the student along with their enrolled courses from the database
        pass
```

### 3.5 Input Validation
Create a new `validators/student_validator.py` to ensure input validation for both student and course IDs during enrollment. 

```python
def validate_student_course_enrollment(student_id: int, course_id: int):
    # Ensure both student_id and course_id are valid
    pass
```

### 3.6 Error Handling
Extend the error handling to ensure appropriate HTTP exceptions are raised in case of invalid inputs and enrollment failures.

---

## IV. Testing Plan

### 4.1 Test Coverage
Include tests for the following scenarios:
- Successful enrollment of a student in a valid course.
- Error responses for invalid student or course IDs.
- Successful retrieval of a student alongside their enrolled courses.

### 4.2 Testing Structure
Implement tests within `tests/test_student.py` to cover all scenarios clearly.

```python
import pytest
from services.student_service import StudentService

@pytest.fixture
def setup_database():
    # Setup an in-memory SQLite database for testing
    yield setup_database

def test_enroll_student_in_course_valid_data(setup_database):
    # Arrange
    # Mock requests for successful student enrollment in a course
    pass

# Additional tests for error cases
```

---

## V. Deployment Considerations

### 5.1 Environment Variables
Utilize the existing `.env` file for configuration, ensuring the database URL accurately reflects the testing and production databases.

### 5.2 Documentation
Update the `README.md` to document the new API endpoints, data structures, and instructions for student enrollment in courses.

---

## VI. Security Considerations
- Ensure inputs are properly sanitized to avoid SQL injection vulnerabilities.
- Maintain validation to reject invalid student or course IDs.

---

## VII. Error Handling and Logging
Implement structured error logging using JSON format to enhance error tracking. Ensure users receive contextual error messages without sensitive data exposure.

---

## VIII. Performance and Scalability
Monitor the performance of the student enrollment process and course retrieval. Anticipate implementing performance optimizations and indexing as usage grows.

---

## IX. Trade-offs and Decisions
- Remain with SQLite as the development database for simplicity, planning for future migration to a more robust database system.
- FastAPI continues to be employed for its performance and ease of API development.

---

## Success Metrics
1. Achieve a success rate of 90% or more for valid student enrollment requests.
2. Ensure successful retrieval of student data along with enrolled courses without errors 100% of the time.
3. Provide clear error messages for incorrect enrollments or invalid IDs, consistently across all failure scenarios.

--- 

This implementation plan provides a detailed strategy for integrating Course relationships into the Student entity, maintaining backward compatibility, and enhancing the overall system functionality while following best practice development standards.