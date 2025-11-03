# Tasks: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_api.py` (2428 bytes)

Instructions for Task Breakdown:
1. Identify which existing files need modifications
2. Create new files for new functionality
3. Ensure integration tasks are included
4. Maintain consistency with existing code style and patterns

---

## Tasks

- [ ] **Task 1**: Update `models.py` to add the `StudentCourse` model  
  **File**: `src/models.py`  
  **Description**: Implement the `StudentCourse` model to establish the many-to-many relationship between students and courses.  
    ```python
    from sqlalchemy import Column, ForeignKey, Integer
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()

    class StudentCourse(Base):
        __tablename__ = 'student_courses'

        id = Column(Integer, primary_key=True, index=True, autoincrement=True)
        student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
        course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
    ```

- [ ] **Task 2**: Create `schemas.py` for Pydantic models  
  **File**: `src/schemas.py`  
  **Description**: Define Pydantic validation models for the course enrollment requests to ensure course IDs are valid.  
    ```python
    from pydantic import BaseModel
    from typing import List

    class CourseEnrollment(BaseModel):
        course_ids: List[int]
    ```

- [ ] **Task 3**: Implement enrolling endpoint in `api.py`  
  **File**: `src/api.py`  
  **Description**: Handle POST requests to `/students/{id}/courses` for enrolling students in courses. Include validation logic for course IDs.  
    ```python
    @app.post("/students/{id}/courses")
    async def enroll_student(id: int, enrollment: CourseEnrollment):
        # Logic to validate IDs and enroll students
    ```

- [ ] **Task 4**: Implement unenrolling endpoint in `api.py`  
  **File**: `src/api.py`  
  **Description**: Handle DELETE requests to `/students/{id}/courses/{course_id}` for unenrolling students from specific courses.  
    ```python
    @app.delete("/students/{id}/courses/{course_id}")
    async def unenroll_student(id: int, course_id: int):
        # Logic to unenroll student
    ```

- [ ] **Task 5**: Implement listing courses endpoint in `api.py`  
  **File**: `src/api.py`  
  **Description**: Handle GET requests to `/students/{id}/courses` to retrieve a list of courses for a student.  
    ```python
    @app.get("/students/{id}/courses")
    async def get_student_courses(id: int):
        # Logic to retrieve courses
    ```

- [ ] **Task 6**: Implement fetching student details endpoint in `api.py`  
  **File**: `src/api.py`  
  **Description**: Handle GET requests to `/students/{id}` to include enrolled course details in the student response.  
    ```python
    @app.get("/students/{id}")
    async def get_student_details(id: int):
        # Logic to fetch student with courses
    ```

- [ ] **Task 7**: Create Alembic migration script for `student_courses` table  
  **File**: `migrations/versions/*_create_student_courses_table.py`  
  **Description**: Define and create a migration script to establish the `student_courses` junction table in the database.  
    ```sql
    CREATE TABLE student_courses (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      student_id INTEGER NOT NULL,
      course_id INTEGER NOT NULL,
      FOREIGN KEY (student_id) REFERENCES students(id),
      FOREIGN KEY (course_id) REFERENCES courses(id)
    );
    ```

- [ ] **Task 8**: Write unit tests for API in `test_api.py`  
  **File**: `tests/test_api.py`  
  **Description**: Implement unit tests for student enrollment and unenrollment, verify the expected behavior and responses from the API.  
    ```python
    def test_enroll_student_in_courses():
        # Complete test implementation

    def test_unenroll_student_from_course():
        # Complete test implementation
    ```

- [ ] **Task 9**: Write integration tests in `test_api.py`  
  **File**: `tests/test_api.py`  
  **Description**: Write integration tests to cover the complete flow of student course enrollments and validation of associated data retrieval.  

- [ ] **Task 10**: Update `README.md` with new API details  
  **File**: `README.md`  
  **Description**: Update project documentation to include new API endpoints for course enrollments and the structure of responses.  

---

Each task is designed to be independently testable, ensuring a clear path toward incremental development and integration of the new functionality.