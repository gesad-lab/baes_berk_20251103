# Tasks: Add Teacher Relationship to Course Entity

---
### INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `models.py` (Define entities)
- `api.py` (Define API endpoints)
- `tests/test_api.py` (Existing tests)

---

## Task Breakdown

### Task 1: Update Course Model to Include Teacher Relationship
- **File**: `src/models.py`
- **Description**: Modify the `Course` class to add a `teacher_id` attribute that references the `Teacher` entity.
- **Implementation**:
  ```python
  class Course(Base):
      ...
      teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New field
      teacher = relationship("Teacher", back_populates="courses")  # Establish relationship
  ```
- **Testing**: Verify that the model compiles correctly and the relationship is set up.
- [ ] Task 1 Complete

### Task 2: Create Migration Script for Database Update
- **File**: `migrations/add_teacher_relationship.py`
- **Description**: Develop a migration script to add the `teacher_id` column to the `courses` table without losing existing data.
- **Implementation**:
  ```python
  from sqlalchemy import create_engine, Column, Integer, ForeignKey, Table, MetaData
  
  def upgrade(migrate_engine):
      meta = MetaData(bind=migrate_engine)
      courses = Table('courses', meta, autoload=True)
      # Adding new column
      teacher_id_col = Column('teacher_id', Integer, ForeignKey('teachers.id'), nullable=True)
      teacher_id_col.create(courses)

  def downgrade(migrate_engine):
      ...
  ```
- **Testing**: Run the migration script in a sandbox environment to ensure the column is added.
- [ ] Task 2 Complete

### Task 3: Implement Service Functions for Course-Teacher Management
- **File**: `src/course_service.py`
- **Description**: Create functions to assign and unassign teachers, and retrieve course details.
- **Implementation**:
  ```python
  def assign_teacher_to_course(course_id, teacher_id):
      # Logic to assign a teacher to a course
      pass
  
  def unassign_teacher_from_course(course_id):
      # Logic to unassign a teacher from a course
      pass
  
  def get_course_details(course_id):
      # Logic to fetch course details including assigned teacher
      pass
  
  def list_courses_with_teachers():
      # Logic to get all courses with assigned teachers
      pass
  ```
- **Testing**: Unit tests will be created in the next task.
- [ ] Task 3 Complete

### Task 4: Define New API Endpoints for Assigning and Unassigning Teachers
- **File**: `src/api.py`
- **Description**: Implement the endpoints to handle HTTP requests for teacher assignment and retrieval.
- **Implementation**:
  ```python
  @app.route('/courses/<int:course_id>/assign-teacher/<int:teacher_id>', methods=['PUT'])
  def assign_teacher():
      # Logic for assigning a teacher to a course
      pass
  
  @app.route('/courses/<int:course_id>/unassign-teacher', methods=['DELETE'])
  def unassign_teacher():
      # Logic for unassigning a teacher from a course
      pass
  
  @app.route('/courses/<int:course_id>', methods=['GET'])
  def get_course():
      # Logic for retrieving course details
      pass
  
  @app.route('/courses', methods=['GET'])
  def list_courses():
      # Logic for listing all courses with assigned teachers
      pass
  ```
- **Testing**: Verify routes register correctly in the Flask app.
- [ ] Task 4 Complete

### Task 5: Create Test Cases for Course-Teacher API Functionality
- **File**: `tests/test_api.py`
- **Description**: Add test cases to check the functionality of new course-teacher assignments and retrieval logic.
- **Implementation**:
  ```python
  def test_assign_teacher_to_course():
      ...
  
  def test_unassign_teacher_from_course():
      ...
  
  def test_get_course_details():
      ...
  
  def test_list_courses_with_teachers():
      ...
  ```
- **Testing**: Ensure that tests cover valid and invalid scenarios for API interactions.
- [ ] Task 5 Complete

### Task 6: Update Swagger Documentation for New API Endpoints
- **File**: `docs/swagger.yaml`
- **Description**: Modify the API documentation to include details about the new endpoints added for teacher assignments.
- **Implementation**:
  ```yaml
  paths:
    /courses/{course_id}/assign-teacher/{teacher_id}:
      put:
        summary: Assign a teacher to a course
      ...
    /courses/{course_id}/unassign-teacher:
      delete:
        summary: Remove teacher from a course
      ...
  ```
- **Testing**: Check Swagger UI to ensure new endpoints are documented and accessible.
- [ ] Task 6 Complete

---
By following this task breakdown, each action item will contribute to the overall feature implementation with clear dependencies and independent testability.