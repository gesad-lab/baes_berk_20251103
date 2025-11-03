# Tasks: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/api/test_courses.py` (3161 bytes)

---

## Task Breakdown

### 1. Database Migration

- [ ] Create a new migration script to add the `student_courses` junction table.
  - **File**: `migrations/versions/2023_10_01_create_student_courses_table.py`
  
  ```python
  """Create student_courses table for relationships

  Revision ID: abc123
  Revises: 
  Create Date: 2023-10-01 12:00:00
  """
  
  from alembic import op
  import sqlalchemy as sa
  
  def upgrade():
      op.create_table(
          'student_courses',
          sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
          sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True)
      )
  
  def downgrade():
      op.drop_table('student_courses')
  ```

- [ ] Apply migration to the database.
  - **File**: `migrations/upgrade_script.sh`
  
  ```bash
  #!/bin/bash
  flask db upgrade
  ```

### 2. Model Implementation

- [ ] Create a new model for `StudentCourse` to define relationships.
  - **File**: `models/student_course.py`
  
  ```python
  from sqlalchemy import Column, Integer, ForeignKey
  from base import Base
  
  class StudentCourse(Base):
      __tablename__ = 'student_courses'
  
      student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
      course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

      def __repr__(self):
          return f"<StudentCourse(student_id={self.student_id}, course_id={self.course_id})>"
  ```

### 3. API Layer Updates

- [ ] Implement the POST endpoint to assign courses to a student.
  - **File**: `api_layer.py`
  
  ```python
  @app.route('/students/<int:id>/courses', methods=['POST'])
  def assign_courses(id):
      # Logic to assign courses
  ```

- [ ] Implement the GET endpoint to retrieve a student’s enrolled courses.
  - **File**: `api_layer.py`
  
  ```python
  @app.route('/students/<int:id>/courses', methods=['GET'])
  def get_student_courses(id):
      # Logic to retrieve courses
  ```

- [ ] Implement the PATCH endpoint to update a student's course enrollment.
  - **File**: `api_layer.py`
  
  ```python
  @app.route('/students/<int:id>/courses', methods=['PATCH'])
  def update_student_courses(id):
      # Logic to update the courses
  ```

### 4. Service Layer Updates

- [ ] Implement business logic for course assignment, retrieval, and updates.
  - **File**: `services/course_service.py`
  
  ```python
  def assign_courses_to_student(student_id, course_ids):
      # Logic to assign courses
  ```

- [ ] Implement logic for retrieving and updating student's course lists.
  - **File**: `services/course_service.py`
  
  ```python
  def get_student_courses(student_id):
      # Logic to fetch courses
  
  def update_student_courses(student_id, course_ids):
      # Logic to update courses
  ```

### 5. Input Validation Logic

- [ ] Implement validation for student and course IDs in service layer.
  - **File**: `services/course_service.py`
  
  ```python
  def validate_student_and_courses(student_id, course_ids):
      # Validation logic
  ```

### 6. Automated Testing

- [ ] Create unit tests for all APIs related to the Student-Course feature.
  - **File**: `tests/api/test_student_courses.py`
  
  ```python
  def test_assign_courses_to_student():
      # Test case for successful course assignment
  
  def test_get_student_courses():
      # Test case for retrieving courses
  
  def test_update_student_courses():
      # Test case for updating course enrollments
  ```

### 7. Error Handling Implementation

- [ ] Implement structured error handling in the API endpoints.
  - **File**: `api_layer.py`
  
  ```python
  @app.errorhandler(400)
  def bad_request(error):
      return jsonify({'error': {'code': 'E400', 'message': 'Bad Request'}}), 400
  ```

### 8. Logging and Monitoring

- [ ] Set up structured logging for API requests and responses related to the Student-Course relationship.
  - **File**: `app.py`
  
  ```python
  import logging
  
  logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
  ```

### 9. Documentation

- [ ] Update API documentation to include new endpoints and sample responses.
  - **File**: `docs/api_documentation.md`
  
  ```markdown
  ### Student-Course Relationship Endpoints
  
  - **POST** `/students/{id}/courses`: Assign courses
  - **GET** `/students/{id}/courses`: Retrieve enrolled courses
  - **PATCH** `/students/{id}/courses`: Update course enrollment
  ```

---

This task breakdown provides a clear and actionable set of steps to implement the feature of adding a course relationship to the Student entity within the existing system while maintaining adherence to the specified guidelines and existing code structures.