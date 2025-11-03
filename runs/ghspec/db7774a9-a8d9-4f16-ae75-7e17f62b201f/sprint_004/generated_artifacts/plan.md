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
# Implementation Plan: Student Management Web Application

## I. Project Overview
This implementation plan is focused on extending the existing Student Management Web Application to establish a relationship between the `Student` and `Course` entities. This relationship allows for multiple course enrollments per student, which enhances educational management and tracking. The integration will ensure proper functionality while preserving existing data integrity within the system.

## II. Technology Stack
- **Backend Framework**: FastAPI (Python)
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Data Validation**: Pydantic
- **Environment Management**: Poetry
- **API Documentation**: FastAPI's built-in OpenAPI support
- **Testing Framework**: pytest

## III. Module Structure
```
.
├── src/
│   ├── main.py             
│   ├── models/             
│   │   ├── student.py      # Existing Student model
│   │   ├── course.py       # New Course model
│   │   └── student_course.py # New StudentCourse junction model
│   ├── schemas/            
│   │   ├── student.py      # Existing Student schema
│   │   ├── course.py       # New Course schema for validation
│   │   └── student_course.py # New StudentCourse schema for validation
│   ├── services/           
│   │   ├── student_service.py  # Existing service logic
│   │   └── course_service.py   # New service logic for courses
│   ├── database/           
│   │   └── database.py     
│   ├── routes/             
│   │   ├── student_routes.py # Existing student routes
│   │   ├── course_routes.py  # New routes for course management
│   │   └── student_course_routes.py # New routes for student-course relationships
└── tests/                 
    ├── test_student.py     # Existing student tests
    ├── test_course.py      # New tests for course features
    └── test_student_course.py # New tests for student-course features
```

## IV. API Contracts

### 1. Assign Course to Student
- **Endpoint**: `POST /students/{student_id}/courses`
- **Request Body**:
    ```json
    {
      "course_ids": [1, 2, 3]
    }
    ```
- **Response**:
    - Status: `200 OK`
    - Body:
    ```json
    {
      "id": "student_id",
      "name": "Student Name",
      "course_ids": [1, 2, 3]
    }
    ```

### 2. Retrieve Student with Courses
- **Endpoint**: `GET /students/{id}`
- **Response**:
    - Status: `200 OK` (if found)
    - Body:
    ```json
    {
      "id": "student_id",
      "name": "Student Name",
      "courses": [1, 2, 3]
    }
    ```
    - Status: `404 Not Found` (if not found)

### 3. List All Students with Courses
- **Endpoint**: `GET /students`
- **Response**:
    - Status: `200 OK`
    - Body:
    ```json
    [
      {
        "id": "student_id",
        "name": "Student Name",
        "courses": [1, 2]
      }
    ]
    ```

## V. Data Models

### 1. Course Model
#### New File: `models/course.py`
```python
from sqlalchemy import Column, Integer, String
from database import Base

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    level = Column(String, index=True, nullable=False)
```

### 2. StudentCourse Junction Model
#### New File: `models/student_course.py`
```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class StudentCourse(Base):
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")
```

### 3. Pydantic Models for Validation
#### New File: `schemas/student_course.py`
```python
from pydantic import BaseModel
from typing import List

class StudentCourseAssign(BaseModel):
    course_ids: List[int]

class StudentCourseResponse(BaseModel):
    id: int
    name: str
    course_ids: List[int]

    class Config:
        orm_mode = True
```

## VI. Implementation Approach

1. **Database Schema Migration**:
   - Create a new junction table `student_courses` in the existing SQLite database to establish a many-to-many relationship between `students` and `courses`.
   - The migration can be achieved using SQLAlchemy migrations or manual scripts, depending on whether complex migrations are anticipated in the future.

2. **API Endpoints Update**:
   - Implement new routes in `student_course_routes.py` for assigning courses to students and handling retrieval.
   - Utilize Pydantic models for input validation and structured responses to ensure data integrity.

3. **Error Handling**:
   - Validate that `course_ids` are provided and contain valid integer values when assigning courses to a student.
   - Return meaningful error messages for invalid requests, such as "Missing student ID" or "Invalid course IDs".

4. **Testing**:
   - Create `test_student_course.py` to validate endpoints for assigning courses and retrieving students with their courses.
   - Test scenarios include successful course assignments, retrieval of student details, and error handling.

## VII. Scalability, Security, and Maintainability Considerations
- **Scalability**: As the user base grows, plan for eventual migration from SQLite to a more robust database like PostgreSQL to handle larger datasets.
- **Security**: Input validations are applied using Pydantic to prevent injection attacks and ensure correct data types.
- **Maintainability**: Backup existing data models, and ensure that new code adheres to the project's coding standards for smooth maintenance.

## VIII. Technical Trade-offs
- **Migration Compression**: Leveraging SQLAlchemy for automatic migrations aids in maintaining clarity and reduces manual intervention costs.
- **Model Relationships**: Establishing many-to-many relationships requires additional models but allows for flexible course enrollment scenarios.

## IX. Deployment Considerations
- **Local Development**: Ensure developers are set up to run and validate the API with the new functionality being tested locally.
- **Production Review**: Evaluate the existing database and ensure that backup and recovery plans are in place before applying migrations for a seamless transition.

## X. Documentation
- Update the project README to include details on the new API endpoints for course assignments and student/course relationships.
- Ensure that any new data models or API contract changes are documented for future reference.

## XI. Conclusion
This implementation plan outlines the steps necessary to establish a course-student relationship within the existing Student Management Web Application. By ensuring the new functionality integrates well with existing structures, we aim to provide enhanced educational management capabilities while maintaining data integrity and robustness in application performance.