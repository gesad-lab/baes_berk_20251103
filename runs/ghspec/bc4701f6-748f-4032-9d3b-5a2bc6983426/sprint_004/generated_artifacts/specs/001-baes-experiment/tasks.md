# Tasks: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- src/models/student.py (1350 bytes)
- src/models/course.py (1200 bytes)
- src/api/enrollment.py (0 bytes)
- tests/api/test_course.py (2363 bytes)

---

### Tasks

- [ ] **Create Enrollment Model**
  - **File**: `src/models/enrollment.py`
  - **Description**: Implement the `Enrollment` model with foreign keys for `student_id` and `course_id`. 
  ```python
  from sqlalchemy import Column, Integer, ForeignKey
  from sqlalchemy.orm import relationship
  from sqlalchemy.ext.declarative import declarative_base

  Base = declarative_base()

  class Enrollment(Base):
      __tablename__ = 'enrollments'
      student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
      course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
      student = relationship("Student", back_populates="enrollments")
      course = relationship("Course", back_populates="enrollments")
  ```

- [ ] **Update Student Model to Include Enrollments**
  - **File**: `src/models/student.py`
  - **Description**: Add a relationship to the existing `Student` model to access associated enrollments.
  ```python
  class Student(Base):
      # Existing fields...
      enrollments = relationship("Enrollment", back_populates="student")
  ```

- [ ] **Update Course Model to Include Enrollments**
  - **File**: `src/models/course.py`
  - **Description**: Add a relationship to the existing `Course` model to access associated enrollments.
  ```python
  class Course(Base):
      # Existing fields...
      enrollments = relationship("Enrollment", back_populates="course")
  ```

- [ ] **Implement Enrollment API Endpoints**
  - **File**: `src/api/enrollment.py`
  - **Description**: Create POST and GET endpoints for enrolling students and retrieving their courses respectively.
  - **POST** `/enrollments`
  - **GET** `/students/{student_id}/courses`
  
- [ ] **Validate Input for Enrollment Endpoint**
  - **File**: `src/api/enrollment.py`
  - **Description**: Add validation logic to ensure valid `student_id` and `course_id` are provided. Return appropriate error messages for invalid requests.

- [ ] **Implement Database Initialization and Migration Logic**
  - **File**: `src/database/init.py`
  - **Description**: Create the logic that initializes the database and includes the new `enrollment` table while preserving existing data.
  ```python
  from sqlalchemy import create_engine
  from sqlalchemy.orm import sessionmaker

  def initialize_database():
      engine = create_engine('sqlite:///app.db')
      Base.metadata.create_all(engine)
  ```

- [ ] **Create Unit Tests for Enrollment API**
  - **File**: `tests/api/test_enrollment.py`
  - **Description**: Implement tests to cover the following scenarios:
    - `test_enroll_student_succeeds_when_valid_ids_provided`
    - `test_enroll_student_fails_when_student_or_course_invalid`
    - `test_retrieve_courses_for_student_returns_correct_data`

- [ ] **Update README with New API Details**
  - **File**: `README.md`
  - **Description**: Add a section to document the new enrollment endpoints, including request/response formats and error handling information.

- [ ] **Review & Validate Changes**
  - **File**: NA (all changes)
  - **Description**: Conduct a code review to ensure all tasks comply with project coding standards and integrate well with existing code.

- [ ] **Perform Integration Testing**
  - **File**: NA (all changes)
  - **Description**: Run integration tests to check the interaction between the new enrollment functionality and existing components in the application.

--- 

This task breakdown ensures a structured implementation of the feature, maintaining proper organization while allowing for independent testing and integration of functionality. Each change has been scoped to specific files to ease the development and review processes.