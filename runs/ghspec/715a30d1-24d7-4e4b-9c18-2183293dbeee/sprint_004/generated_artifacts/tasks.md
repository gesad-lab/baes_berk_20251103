# Tasks: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `models.py`  
- `repository.py`  
- `service.py`  
- `main.py`  
- `README.md`  

## Task Breakdown

- [ ] **1. Create New Relationship Model**
  - **Description**: Add a new class definition for the `StudentCourse` relationship model in `models.py`.
  - **File**: `src/models.py`
  - ```python
    class StudentCourse(Base):
        __tablename__ = 'student_courses'
    
        student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
        course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    ```

- [ ] **2. Extend Repository for Enrollment Logic**
  - **Description**: Implement `enroll_student_in_courses` method in `repository.py` to associate students with courses.
  - **File**: `src/repository.py`
  - ```python
    def enroll_student_in_courses(student_id: int, course_ids: List[int]):
        # Logic to associate student with the listed courses
    ```

- [ ] **3. Add Enrollment Handling in Service Layer**
  - **Description**: Create a new method `add_enrollment` in `service.py` to validate course IDs and interact with the repository.
  - **File**: `src/service.py`
  - ```python
    def add_enrollment(student_id: int, course_ids: List[int]):
        # Validate course IDs and call repository to create associations
    ```

- [ ] **4. Define API Routes for Enrollment Actions**
  - **Description**: Extend `main.py` to register new API routes for enrolling students and retrieving student data.
  - **File**: `src/main.py`
  - ```python
  @app.post("/students/enroll", response_model=StudentEnrollmentResponse)
  def enroll_student(enrollment: StudentEnrollmentRequest):
      # Call service to enroll a student in courses
  
  @app.get("/students/{id}", response_model=StudentResponse)
  def get_student(id: int):
      # Call service to retrieve student data along with courses
  ```

- [ ] **5. Implement Input Validation with Pydantic**
  - **Description**: Define Pydantic schemas in a new file to validate incoming enrollment requests and student responses.
  - **File**: `src/schemas.py`
  - ```python
  from pydantic import BaseModel
  from typing import List
  
  class StudentEnrollmentRequest(BaseModel):
      student_id: int
      course_ids: List[int]
    
  class StudentEnrollmentResponse(BaseModel):
      student_id: int
      enrolled_courses: List[dict]
  ```

- [ ] **6. Create Migration Script for Database**
  - **Description**: Generate a new Alembic migration script to create the `student_courses` table.
  - **File**: `migrations/versions/create_student_courses_table.py`
  - ```python
  def upgrade():
      op.create_table(
          'student_courses',
          sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
          sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True)
      )
  ```

- [ ] **7. Document New API Endpoints in README**
  - **Description**: Update the `README.md` to include documentation on the new endpoints and their expected inputs/outputs.
  - **File**: `README.md`

- [ ] **8. Write Unit Tests for New Functionality**
  - **Description**: Implement unit and integration tests targeting the new service methods and API routes in `tests/test_service.py`.
  - **File**: `tests/test_service.py`

- [ ] **9. Validate Error Handling for Enrollment**
  - **Description**: Ensure that error handling is implemented in the service and API layers for invalid course IDs and non-existent students.
  - **File**: `src/service.py`, `src/main.py`

- [ ] **10. Execute Database Migration**
  - **Description**: Run Alembic to apply the migration and create the `student_courses` table.
  - **Command**: 
  ```bash
  alembic upgrade head
  ```

---

This task breakdown prepares a clear path for implementing the feature while ensuring modularity and ease of testing for each component involved. Each task is defined to maintain focus, facilitate integration, and adhere to the established coding standards.