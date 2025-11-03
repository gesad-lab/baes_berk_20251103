# Implementation Plan: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---

## I. Project Overview
This implementation plan focuses on enhancing the existing Student Management Web Application by establishing a relationship between the `Course` and `Teacher` entities. By integrating this relationship, the application will enable better tracking of course management and facilitate reporting on course offerings alongside their responsible educators. The implementation ensures that existing data related to `Student`, `Course`, and `Teacher` remains intact and functional.

## II. Technology Stack
- **Backend Framework**: FastAPI (Python)
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Data Validation**: Pydantic
- **Environment Management**: Poetry
- **API Documentation**: FastAPI's built-in OpenAPI support
- **Testing Framework**: pytest

## III. Module Structure
Here’s the updated module structure reflecting the introduction of the `teacher_id` field in the `Course` model.

```
.
├── src/
│   ├── main.py              
│   ├── models/             
│   │   ├── student.py      # Existing Student model
│   │   ├── course.py       # Existing Course model (to be modified)
│   │   ├── teacher.py      # Existing Teacher model
│   ├── schemas/            
│   │   ├── student.py      # Existing Student schema
│   │   ├── course.py       # Existing Course schema (to be modified)
│   │   └── teacher.py      # Existing Teacher schema
│   ├── services/           
│   │   ├── student_service.py  # Existing student service logic
│   │   ├── course_service.py   # Existing course service logic (to be modified)
│   │   └── teacher_service.py   # Existing service logic for teachers
│   ├── database/           
│   │   └── database.py     
│   ├── routes/             
│   │   ├── student_routes.py # Existing student routes
│   │   ├── course_routes.py  # Existing course routes (to be modified)
│   │   └── teacher_routes.py  # Existing routes for teacher management
└── tests/                 
    ├── test_student.py     # Existing student tests
    ├── test_course.py      # Existing course tests (to be modified)
    └── test_teacher.py      # Tests for teacher features
```

## IV. API Contracts

### 1. Assign a Teacher to a Course
- **Endpoint**: `PATCH /courses/{id}`
- **Request Body**:
    ```json
    {
      "teacher_id": "integer (required)"
    }
    ```
- **Response**:
    - Status: `200 OK`
    - Body:
    ```json
    {
      "id": "course_id",
      "name": "Course Name",
      "teacher_id": 1,
      "teacher_name": "Teacher Name"
    }
    ```

### 2. Retrieve Course Information
- **Endpoint**: `GET /courses/{id}`
- **Response**:
    - Status: `200 OK` (if found)
    - Body:
    ```json
    {
      "id": "course_id",
      "name": "Course Name",
      "teacher_id": 1,
      "teacher_name": "Teacher Name"
    }
    ```
    - Status: `404 Not Found` (if not found)

### 3. List All Courses with Teachers
- **Endpoint**: `GET /courses`
- **Response**:
    - Status: `200 OK`
    - Body:
    ```json
    [
      {
        "id": "course_id",
        "name": "Course Name",
        "teacher_name": "Teacher Name"
      }
    ]
    ```

## V. Data Models

### 1. Modify `Course` Model
#### File: `models/course.py`
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)
    
    teacher = relationship("Teacher", back_populates="courses")
```

### 2. Update Pydantic Models for Validation
#### File: `schemas/course.py`
```python
from pydantic import BaseModel, Field
from typing import Optional

class CourseBase(BaseModel):
    name: str = Field(..., example="Mathematics")

class CourseResponse(CourseBase):
    id: int
    teacher_id: Optional[int]
    teacher_name: Optional[str]

    class Config:
        orm_mode = True
```

## VI. Implementation Approach

1. **Database Schema Migration**:
   - Update the existing `courses` table to add the `teacher_id` foreign key relationship to the `teachers` table.
   - Use SQLAlchemy migrations to handle this update ensuring existing course data is preserved.

2. **API Endpoints Update**:
   - Implement new route in `course_routes.py` to handle PATCH requests for assigning a teacher to a course.
   - Utilize updated Pydantic models (`CourseResponse`) for structured responses containing teacher information.

3. **Error Handling**:
   - Implement input validation to ensure that when a teacher is assigned to a course, the `teacher_id` must reference an existing teacher in the database.
   - Returns meaningful error messages for requests with invalid `teacher_id`.

4. **Testing**:
   - Update `test_course.py` to include:
     - Tests for successfully assigning a teacher to a course.
     - Tests for retrieving course details including the teacher.
     - Tests to ensure appropriate error handling when invalid `teacher_id` is provided.

## VII. Scalability, Security, and Maintainability Considerations
- **Scalability**: The course-teacher relationship is designed for future enhancements, allowing for functionalities like filtering courses by teacher.
- **Security**: Ensure proper input validation to mitigate risks such as CSRF or SQL injection.
- **Maintainability**: Follow best coding practices to keep the code organized and easily understandable for future developers.

## VIII. Technical Trade-offs
- **Data Integrity**: Adding a foreign key constraint enhances data integrity but requires careful migration to avoid issues with existing course records.
- **Feature Complexity**: While integrating the teacher assignment has increased the complexity of the course model, it provides necessary functionality for better management of educational offerings.

## IX. Deployment Considerations
- **Local Development**: Provide documentation on how to set up the migration steps locally to reflect the new schema changes.
- **Production Review**: Mark the updated database schema changes and ensure backup processes are in place before deployment.

## X. Documentation
- Update the project README.md to include new API endpoints for assigning teachers to courses, including example requests and responses.
- Document the updates made to the `Course` model, as well as new validation rules.

## XI. Conclusion
This implementation plan outlines the steps necessary to integrate the `Teacher` relationship into the `Course` entity within the Student Management Web Application. By defining API contracts, updating data models, and ensuring stringent validation practices, this plan aims to enhance the application’s capability to manage teacher-course relationships while preserving existing data integrity and facilitating ease of future development.

**Existing Code File Modifications:**
- **models/course.py**: Add `teacher_id` field and relationship.
- **schemas/course.py**: Add fields for teacher details to Pydantic model.
- **routes/course_routes.py**: Implement PATCH endpoint for updating course with teacher.
- **tests/test_course.py**: Include new tests for teacher assignment scenarios.