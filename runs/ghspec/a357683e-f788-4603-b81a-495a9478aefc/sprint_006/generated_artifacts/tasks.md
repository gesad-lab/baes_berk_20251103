# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/api/test_course.py`
- `tests/models/test_class.py`

## Tasks Breakdown

### Task 1: Update Database Model for Course
- **File**: `src/models/course.py`
- **Description**: Modify the existing Course model to include a new column `teacher_id` as a foreign key referencing the Teacher entity.
- **Code Changes**:
  ```python
  from sqlalchemy import Column, Integer, ForeignKey
  from sqlalchemy.orm import relationship
  
  class Course(Base):
      __tablename__ = 'courses'
      
      id = Column(Integer, primary_key=True, autoincrement=True)
      name = Column(String, nullable=False)
      teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)
  
      teacher = relationship("Teacher", back_populates="courses")
  ```
  
- [ ] Implement the model update

### Task 2: Create Database Migration Script
- **File**: `migrations/versions/xxxx_add_teacher_relationship_to_course.py`
- **Description**: Generate and implement a migration script to alter the Course table and add `teacher_id` column.
- **Command**: Use `Flask-Migrate` to generate the script.
- [ ] Create migration script

### Task 3: Implement API Endpoint to Assign Teacher to Course
- **File**: `src/routes/course.py`
- **Description**: Create a new PATCH endpoint `/courses/{course_id}/assign-teacher` to associate a teacher with a specific course.
- **Code Changes**:
  ```python
  @app.route('/courses/<int:course_id>/assign-teacher', methods=['PATCH'])
  def assign_teacher(course_id):
      # Logic to assign teacher
  ```
  
- [ ] Implement teacher assignment endpoint

### Task 4: Implement API Endpoint to Retrieve Course with Assigned Teacher
- **File**: `src/routes/course.py`
- **Description**: Create a GET endpoint `/courses/{course_id}` to retrieve course information along with assigned teacher details.
- **Code Changes**:
  ```python
  @app.route('/courses/<int:course_id>', methods=['GET'])
  def get_course(course_id):
      # Logic to retrieve course details
  ```
  
- [ ] Implement retrieval endpoint

### Task 5: Implement API Endpoint to Remove Teacher from Course
- **File**: `src/routes/course.py`
- **Description**: Create a new PATCH endpoint `/courses/{course_id}/remove-teacher` for removing a teacher assignment from a course.
- **Code Changes**:
  ```python
  @app.route('/courses/<int:course_id>/remove-teacher', methods=['PATCH'])
  def remove_teacher(course_id):
      # Logic to remove teacher
  ```

- [ ] Implement removal endpoint

### Task 6: Implement API Endpoint to Query Courses by Teacher
- **File**: `src/routes/teacher.py`
- **Description**: Create a new GET endpoint `/teachers/{teacher_id}/courses` that returns all courses assigned to a particular teacher.
- **Code Changes**:
  ```python
  @app.route('/teachers/<int:teacher_id>/courses', methods=['GET'])
  def get_courses_by_teacher(teacher_id):
      # Logic to list courses taught by the teacher
  ```
  
- [ ] Implement query endpoint

### Task 7: Write Tests for Assigning Teacher to Course
- **File**: `tests/api/test_course.py`
- **Description**: Add unit tests for the functionality of assigning a teacher to a course.
- **Test Cases**:
  - Validate successful assignment.
  - Validate failure with an invalid teacher_id.
  
- [ ] Implement assignment tests

### Task 8: Write Tests for Retrieving Course with Teacher
- **File**: `tests/api/test_course.py`
- **Description**: Add unit tests for validating retrieval of course details that include teacher information.
  
- [ ] Implement retrieval tests

### Task 9: Write Tests for Removing Teacher from Course
- **File**: `tests/api/test_course.py`
- **Description**: Add tests to ensure a teacher can be removed from a course correctly without affecting other data.
  
- [ ] Implement removal tests

### Task 10: Write Tests for Querying Courses by Teacher
- **File**: `tests/api/test_teacher.py`
- **Description**: Add tests to ensure that all courses taught by a specific teacher are retrieved correctly.
  
- [ ] Implement querying tests

### Task 11: Update README Documentation
- **File**: `README.md`
- **Description**: Add documentation to describe the new endpoints and their usage regarding teacher-course assignment.
  
- [ ] Update documentation

### Task 12: Review and Refactor Code for Consistency
- **Files**: All modified files
- **Description**: Review code for consistency with existing coding standards and ensure all new functions and models are documented.
  
- [ ] Perform code review and refactor

--- 

This task breakdown organizes the implementation plan into actionable tasks that maintain focus on individual files, ensuring each task is independent and testable.