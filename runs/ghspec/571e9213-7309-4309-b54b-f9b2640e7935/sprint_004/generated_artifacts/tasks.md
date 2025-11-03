# Tasks: Add Course Relationship to Student Entity

---

INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_course_routes.py` (2856 bytes)

---

### Task Breakdown

- [ ] **Task 1**: Create the `student_courses.py` model  
  - **File**: `src/models/student_courses.py`  
  - **Description**: Implement the intermediary table that facilitates the many-to-many relationship between Students and Courses.  
    ```python
    from sqlalchemy import Column, Integer, ForeignKey
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()

    class StudentCourses(Base):
        __tablename__ = 'student_courses'
        
        student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
        course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    ```

- [ ] **Task 2**: Update the `student.py` model to include course relationships  
  - **File**: `src/models/student.py`  
  - **Description**: Add a relationship to the `Student` model for `StudentCourses`.  
    ```python
    from sqlalchemy.orm import relationship

    class Student(Base):
        __tablename__ = 'students'

        id = Column(Integer, primary_key=True, autoincrement=True)
        # Existing fields...
        courses = relationship("StudentCourses", back_populates="student")
    ```

- [ ] **Task 3**: Update the `course.py` model with course fields  
  - **File**: `src/models/course.py`  
  - **Description**: Ensure `Course` model is correctly set up with necessary fields (name, level).  
    ```python
    class Course(Base):
        __tablename__ = 'courses'

        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String, nullable=False)
        level = Column(String, nullable=False)
    ```

- [ ] **Task 4**: Create the Course Association Request Schema  
  - **File**: `src/schemas/course_association_schema.py`  
  - **Description**: Implement Pydantic model for validating requests to associate courses with students.  
    ```python
    from pydantic import BaseModel

    class CourseAssociationRequestSchema(BaseModel):
        course_id: int
    ```

- [ ] **Task 5**: Implement POST route for course association  
  - **File**: `src/routes/student_course_routes.py`  
  - **Description**: Add logic to handle requests that associate a course to a student.
    ```python
    @router.post("/students/{student_id}/courses")
    def associate_course(student_id: int, course: CourseAssociationRequestSchema, db: Session = Depends(get_db)):
        # Logic to associate the course with the student
        pass
    ```

- [ ] **Task 6**: Implement GET route for retrieving a student's courses  
  - **File**: `src/routes/student_course_routes.py`  
  - **Description**: Retrieve all courses associated with a specific student.
    ```python
    @router.get("/students/{student_id}/courses", response_model=List[CourseSchema])
    def get_student_courses(student_id: int, db: Session = Depends(get_db)):
        # Logic to retrieve student's courses
        pass
    ```

- [ ] **Task 7**: Implement DELETE route for removing course association  
  - **File**: `src/routes/student_course_routes.py`  
  - **Description**: Add functionality to remove a course association from a student.
    ```python
    @router.delete("/students/{student_id}/courses/{course_id}")
    def remove_course_association(student_id: int, course_id: int, db: Session = Depends(get_db)):
        # Logic to remove course association from student
        pass
    ```

- [ ] **Task 8**: Create database migration for `student_courses` table  
  - **File**: `migrations/versions/create_student_courses_table.py`  
  - **Description**: Write and execute migration to add the new `student_courses` table. Use Alembic for this process.  
    ```bash
    alembic revision --autogenerate -m "Create student_courses table"
    ```

- [ ] **Task 9**: Implement error handling in route logic  
  - **File**: `src/routes/student_course_routes.py`  
  - **Description**: Add validation logic for student and course associations, ensuring clear error messages are returned for invalid requests.

- [ ] **Task 10**: Write unit tests for course association functionalities  
  - **File**: `tests/test_course_routes.py`  
  - **Description**: Create test cases for the new functionality such as successful associations, retrieval, and deletions, ensuring the codebase meets the minimum coverage requirements.

- [ ] **Task 11**: Update the README.md to document the new API endpoints and usage instructions  
  - **File**: `README.md`  
  - **Description**: Ensure that API documentation reflects the updates made for course associations with students.

---

This structured task breakdown ensures a clear progression through the implementation of the Course relationship feature, allowing for effective testing and independent execution of each task.