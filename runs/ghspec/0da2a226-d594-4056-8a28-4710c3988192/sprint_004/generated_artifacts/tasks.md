# Tasks: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_course.py` (2068 bytes)

---

## Tasks Breakdown

### 1. Update Data Models

- [ ] **Modify the `models.py` to Define Enrollment Relationship**
    - **File**: `src/models/models.py`
    - Description: Update the existing `Student` and `Course` schemas to include a new `Enrollment` table for associating students with courses.
    - Code Changes:
    ```python
    from sqlalchemy import Column, Integer, String, ForeignKey
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import relationship

    Base = declarative_base()

    class Student(Base):
        __tablename__ = 'students'
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String, nullable=False)
        enrolled_courses = relationship("Course", secondary="enrollments")

    class Course(Base):
        __tablename__ = 'courses'
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String, nullable=False)
        level = Column(String, nullable=False)

    class Enrollment(Base):
        __tablename__ = 'enrollments'
        student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
        course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    ```

### 2. Implement Database Migration

- [ ] **Create Database Migration for Enrollment Relationship**
    - **File**: Migration script (to be generated)
    - Description: Use Alembic to generate a migration that creates the `enrollments` table ensuring data preservation.
    - Command:
    ```bash
    alembic revision --autogenerate -m "Add enrollment relationship between Student and Course"
    ```

### 3. Implement Services Logic

- [ ] **Create Logic for Enrolling Students in Courses**
    - **File**: `src/services/enrollment_service.py`
    - Description: Implement business logic for enrolling a student in a course and retrieving courses for a student.
    - Function to implement:
    ```python
    def enroll_student(student_id: int, course_id: int):
        # Logic to enroll student in a course
        # Check if the course exists and if the student is already enrolled
    ```

### 4. Define API Endpoints

- [ ] **Create Enrollment Endpoints in Routes**
    - **File**: `src/api/routes.py`
    - Description: Define new API endpoints for enrolling students in courses and retrieving courses for a student.
    - New Endpoints to Implement:
    - **POST** `/students/{student_id}/courses` for enrollment
    - **GET** `/students/{student_id}/courses` for retrieval

### 5. Input Validation

- [ ] **Implement Input Validation for Enrollments**
    - **File**: `src/api/dependencies.py`
    - Description: Use Pydantic to create schemas for validating the input during student enrollment.

### 6. Error Handling

- [ ] **Enhance Error Handling Mechanism**
    - **File**: `src/services/enrollment_service.py`
    - Description: Ensure handling of errors for invalid course IDs or duplicate enrollments, returning meaningful messages.

### 7. Testing

- [ ] **Write Unit Tests for Enrollment Feature**
    - **File**: `tests/test_enrollment.py`
    - Description: Create tests covering all scenarios related to course enrollment.
    - Example Test Case Implementation:
    ```python
    def test_enroll_student_in_valid_course():
        response = client.post("/students/1/courses", json={"course_id": 1})
        assert response.status_code == 201  # Created
    ```

### 8. Documentation

- [ ] **Update README to Include New API Instructions**
    - **File**: `README.md`
    - Description: Document the new course enrollment API endpoints, including request and response examples.

---

This task breakdown ensures each part of the implementation plan is distributed into actionable items, maintaining focus on specific files and their responsibilities, facilitating easier tracking and testing.