# Tasks: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `models.py`
- `api.py`
- `database_migrations.py`
- `tests/test_api.py`
- `tests/test_integration.py`

---

## Task Breakdown

### 1. Update Models

- [ ] **Task: Create StudentCourses Model**
    - **File**: `src/models.py`
    - **Description**: Define the `StudentCourses` model to establish a many-to-many relationship between `Student` and `Course`.
    - **Code**:
    ```python
    from sqlalchemy import Column, Integer, ForeignKey
    from sqlalchemy.orm import relationship
    from database import Base

    class StudentCourses(Base):
        __tablename__ = 'student_courses'

        student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
        course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

        student = relationship("Student", back_populates="courses")
        course = relationship("Course", back_populates="students")
    ```

- [ ] **Task: Update Student Model**
    - **File**: `src/models.py`
    - **Description**: Add a relationship attribute to the `Student` model that connects it to the `StudentCourses` model.
    - **Code**:
    ```python
    class Student(Base):
        # Existing fields...
        
        courses = relationship("StudentCourses", back_populates="student")
    ```

- [ ] **Task: Update Course Model**
    - **File**: `src/models.py`
    - **Description**: Add a relationship attribute to the `Course` model that connects it to the `StudentCourses` model.
    - **Code**:
    ```python
    class Course(Base):
        # Existing fields...
        
        students = relationship("StudentCourses", back_populates="course")
    ```

### 2. Implement API Endpoints

- [ ] **Task: Implement Enroll Student Endpoint**
    - **File**: `src/api.py`
    - **Description**: Create the POST endpoint that allows enrolling students in a course.
    - **Endpoint**: `/students/{student_id}/enroll`
    - **Code**:
    ```python
    @app.post("/students/{student_id}/enroll", status_code=201)
    async def enroll_student(student_id: int, course_data: CourseData):
        # Logic to enroll the student goes here
    ```

- [ ] **Task: Implement Retrieve Courses for Student Endpoint**
    - **File**: `src/api.py`
    - **Description**: Create the GET endpoint that retrieves a list of courses for a particular student.
    - **Endpoint**: `/students/{student_id}/courses`
    - **Code**:
    ```python
    @app.get("/students/{student_id}/courses")
    async def get_courses_for_student(student_id: int):
        # Logic to retrieve courses for the student goes here
    ```

### 3. Database Migration 

- [ ] **Task: Create Migration for StudentCourses Table**
    - **File**: `src/database_migrations.py`
    - **Description**: Write a migration script to create the `student_courses` junction table.
    - **Code**:
    ```python
    from alembic import op
    import sqlalchemy as sa

    def upgrade():
        op.create_table(
            'student_courses',
            sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
            sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True),
        )

    def downgrade():
        op.drop_table('student_courses')
    ```

### 4. Implement Input Validation

- [ ] **Task: Validate Course ID Input**
    - **File**: `src/api.py`
    - **Description**: Ensure the course ID provided for enrollment is valid and exists.
    - **Code**:
    ```python
    if not course_exists(course_data.course_id):
        raise HTTPException(status_code=400, detail="The specified course does not exist.")
    ```

### 5. Testing

- [ ] **Task: Add Unit Tests for API Endpoints**
    - **File**: `tests/test_api.py`
    - **Description**: Create tests for the new enrollment and course retrieval endpoints.
    - **Checks**:
      - Test successful enrollment
      - Test enrollment with invalid course ID
   
- [ ] **Task: Add Integration Tests for Complete Functionality**
    - **File**: `tests/test_integration.py`
    - **Description**: Verify the end-to-end functionality of both new API endpoints.
    - **Checks**:
      - Enrollment and retrieval process works as expected in full integration.

### 6. Documentation Updates

- [ ] **Task: Update README.md**
    - **File**: `README.md`
    - **Description**: Document new functionalities regarding course enrollment and course retrieval.
    - **Sections**:
      - API endpoint specifications
      - Instructions for running unit and integration tests

---

This task breakdown provides a clear path for the implementation of adding a course relationship to the student entity, ensuring it is modular and meets all requirements specified in the original feature specification. Each task is independent, ensuring the team can work on different tasks in parallel if necessary.