# Implementation Plan: Add Course Relationship to Student Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Relationship to Student Entity

---

## Version: 1.0.0

### I. Architecture Overview
This plan focuses on establishing a relationship between the `Student` and `Course` entities within the existing Student Entity Management Web Application built with FastAPI. By enabling students to enroll in multiple courses, we aim to enhance tracking of academic progress and curriculum management. This feature is designed to improve usability for academic coordination and reporting.

### II. Technology Stack
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: SQLite (as per the existing setup)
- **ORM**: SQLAlchemy for ORM management
- **Data Validation**: Pydantic for request/response validation
- **Testing**: Pytest for unit and integration tests
- **Environment**: Python 3.11+

### III. Module Design

#### 1. Project Structure
```
student_management/
├── src/
│   ├── main.py             # Entry point of FastAPI application
│   ├── models.py           # SQLAlchemy models (add StudentCourse join model)
│   ├── schemas.py          # Pydantic schemas for Course and enrollment requests
│   ├── database.py         # Database connection and initialization
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── students.py      # Existing API routes for student endpoints
│   │   ├── enrollments.py    # New API routes for student enrollments
├── tests/
│   ├── __init__.py
│   ├── test_enrollments.py  # Tests for enrollment functionality
│   ├── test_students.py     # Existing tests for students API
├── README.md                # Project documentation
└── requirements.txt         # Dependency management
```

#### 2. Components Breakdown
- **models.py**: Add a `StudentCourse` join model that relates students to the courses they are enrolled in.
- **schemas.py**: Create Pydantic schemas for request and response payloads for course enrollment.
- **routes/enrollments.py**: Implement API routes for enrolling students in courses and retrieving their courses.
- **tests/test_enrollments.py**: Create tests for enrollment functionalities.

### IV. Data Models

#### 1. StudentCourse Model 
New addition in `models.py`:
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

**Updates to existing `Student` and `Course` models**:
Ensure that the `Student` and `Course` models support relationships:
```python
# In Student model
courses = relationship("StudentCourse", back_populates="student")

# In Course model
students = relationship("StudentCourse", back_populates="course")
```

### V. API Contracts

#### 1. Enroll Student in Courses Endpoint
- **Endpoint**: `POST /students/{student_id}/enroll`
- **Request Body**:
  ```json
  {
      "course_ids": [1, 2]
  }
  ```
- **Response**:
  - **Success**:
    ```json
    {
        "message": "Enrolled in courses successfully",
        "enrolled_courses": [
            {"course_id": 1},
            {"course_id": 2}
        ]
    }
    ```
  - **Error (Invalid Course)**:
    ```json
    {
        "error": {
            "code": "E002",
            "message": "One or more courses not found"
        }
    }
    ```

#### 2. Retrieve Student Courses Endpoint
- **Endpoint**: `GET /students/{student_id}/courses`
- **Response**:
  ```json
  [
      {
          "name": "Introduction to Programming",
          "level": "Beginner"
      },
      {
          "name": "Advanced Mathematics",
          "level": "Intermediate"
      }
  ]
  ```

### VI. Implementation Steps

1. **Initialize Project**:
   - Ensure the project environment is set up with the required dependencies specified in `requirements.txt`.

2. **Database Update**:
   - Implement migration scripts to create the `student_courses` join table:
     ```sql
     CREATE TABLE student_courses (
         student_id INTEGER,
         course_id INTEGER,
         PRIMARY KEY (student_id, course_id),
         FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
         FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
     );
     ```

3. **Update API Endpoints**:
   - In `routes/enrollments.py`, create endpoints for the enrollments:
     - Enrollment endpoint for students to enroll in courses.
     - Endpoint to retrieve a student's enrolled courses.

4. **Input Validation**:
   - Create Pydantic schemas in `schemas.py` for validating enrollment requests:
     ```python
     from pydantic import BaseModel
     from typing import List

     class EnrollmentRequest(BaseModel):
         course_ids: List[int]

     class CourseInfo(BaseModel):
         name: str
         level: str
     ```

5. **Testing**:
   - Implement test cases in `tests/test_enrollments.py` for:
     - Enrolling a student in valid courses.
     - Attempting enrollment in non-existent courses and verifying the error response.
     - Retrieving courses for a given student.

6. **Documentation**:
   - Update `README.md` to include new enrollment endpoints and their example usage.

### VII. Success Criteria
- The API successfully allows students to enroll in multiple courses and retrieves their enrolled courses.
- JSON responses for all requests conform to prescribed specifications.
- All tests pass without errors, validating both successful and error scenarios.
- Database migration correctly establishes the `student_courses` table linking students and courses.

### VIII. Deployment Considerations
- Ensure that the application is available in a production-ready environment complete with appropriate configurations.
- Run migrations in staging before pushing to production to verify integrity and correct behavior.

### IX. Future Enhancements (Out of Scope for v1.0.0)
- User authentication for securing enrollment endpoints.
- Handling course capacities and prerequisites for enrollment, which can be incorporated in future iterations.
- UI updates for managing course relationships.

### X. Conclusion
This implementation plan outlines the necessary steps for integrating the course relationship into the existing Student Entity Management Web Application, enhancing its capabilities while maintaining integrity and usability. By adhering to specified structures, the plan lays a foundation not only for initial implementation but also for future developments and improvements.

**Existing Code Files**:
The implementation modifies/includes `models.py`, `schemas.py`, `routes/enrollments.py`, and `tests/test_enrollments.py`. 

**Instructions for Technical Plan**:
1. Use the established tech stack from previous sprints.
2. Integrate existing modules while adding new ones.
3. Document modifications needed to existing files (not replacements).
4. Maintain backward compatibility with existing data models.
5. Specify database migration strategy if data model changes.