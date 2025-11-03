# Tasks: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models.py`
- `src/schemas.py`
- `src/routes/enrollments.py`
- `tests/test_enrollments.py`
- `tests/test_students.py`
- `src/database.py`
- `src/main.py`

Instructions for Task Breakdown:
1. Identify which existing files need modifications.
2. Create new files for new functionality.
3. Ensure integration tasks are included.
4. Maintain consistency with existing code style and patterns.

---

## Task List

- [ ] **Task 1**: Create `StudentCourse` Join Model  
  **File**: `src/models.py`  
  **Description**: Add the `StudentCourse` model to handle the relationship between students and courses, including necessary SQLAlchemy relationships.  
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

- [ ] **Task 2**: Update Student and Course Models  
  **File**: `src/models.py`  
  **Description**: Modify the existing `Student` and `Course` models to include relationships for courses and students via the `StudentCourse` model.  

- [ ] **Task 3**: Implement Database Migration Script  
  **File**: `migrations/add_student_courses.sql`  
  **Description**: Write a migration script to create the `student_courses` table, including foreign keys and primary key constraints.

- [ ] **Task 4**: Create Enrollment Request Schema  
  **File**: `src/schemas.py`  
  **Description**: Define a Pydantic schema for handling course enrollment requests with validation.  
  ```python
  from pydantic import BaseModel
  from typing import List

  class EnrollmentRequest(BaseModel):
      course_ids: List[int]
  ```

- [ ] **Task 5**: Create Course Info Schema  
  **File**: `src/schemas.py`  
  **Description**: Define a Pydantic schema for the response of enrolled course information.

- [ ] **Task 6**: Implement Enrollments API Routes  
  **File**: `src/routes/enrollments.py`  
  **Description**: Create routes to handle POST requests for enrolling students in courses and GET requests for retrieving courses for a student.  
  - Endpoint: `POST /students/{student_id}/enroll`  
  - Endpoint: `GET /students/{student_id}/courses`

- [ ] **Task 7**: Write Unit Tests for Enrollment Functionality  
  **File**: `tests/test_enrollments.py`  
  **Description**: Create tests including successful enrollment cases and validation for invalid course IDs.  
  - Test Functions: `test_student_enrollment_success()`, `test_student_enrollment_invalid_course()`, `test_retrieve_student_courses()`

- [ ] **Task 8**: Update README File with API Documentation  
  **File**: `README.md`  
  **Description**: Document new API endpoints and provide example requests/responses for the enrollment functionality.

- [ ] **Task 9**: Integrate Database Initialization with Migration  
  **File**: `src/database.py`  
  **Description**: Ensure that the database is initialized with the capability to run migrations to add the new `student_courses` table upon starting the application.

- [ ] **Task 10**: Test Migration to Ensure Data Integrity  
  **File**: N/A  
  **Description**: Execute migration in a staging environment to ensure that the existing data remains intact and the new `student_courses` table is created successfully.

- [ ] **Task 11**: Review and Refactor Code for Consistency  
  **File**: All modified files  
  **Description**: Go through the modified files to ensure consistent styling, comments, and adherence to the project constitution.

--- 

With these tasks, the integration of the course relationship to the student entity can be done incrementally while ensuring system integrity and functionality. Each task is designed to be independently testable and maintains a focus on MVP features.