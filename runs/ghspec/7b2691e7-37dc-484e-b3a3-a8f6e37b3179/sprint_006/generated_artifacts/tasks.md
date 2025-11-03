# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- models/course.py (400 bytes)
- models/teacher.py (520 bytes)
- api/routes/courses.py (1200 bytes)
- tests/test_courses.py (1500 bytes)

---

## Task Breakdown

### 1. Update Course Entity to Include Teacher Foreign Key

- [ ] **Modify Course Model**  
   **File**: `models/course.py`  
   - Add `teacher_id` foreign key to the `Course` entity.  
   - Update any existing comments/documentation to reflect this change.
   - **Validation**: Ensure adherence to naming conventions and data types.
   ```python
   teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New foreign key to Teacher
   ```

- [ ] **Add Relationship in Course Model**  
   **File**: `models/course.py`  
   - Establish a relationship to the Teacher entity.
   ```python
   teacher = relationship("Teacher", back_populates="courses")  # Establish a relationship to Teacher
   ```

### 2. Conduct Database Migration

- [ ] **Create Migration Script**  
   **File**: `migrations/versions/{timestamp}_add_teacher_relationship_to_course.py`  
   - Write migration script using Alembic to add `teacher_id` foreign key and constraints from Course to Teacher.
   - Ensure rollback capabilities are included.
   ```python
   from alembic import op
   import sqlalchemy as sa

   def upgrade():
       op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
       op.create_foreign_key('fk_course_teacher', 'courses', 'teachers', 'teacher_id', 'id')

   def downgrade():
       op.drop_constraint('fk_course_teacher', 'courses', type_='foreignkey')
       op.drop_column('courses', 'teacher_id')
   ```

### 3. Implement API Endpoints

- [ ] **Create Assign Teacher Endpoint**  
   **File**: `api/routes/courses.py`  
   - Implement POST `/courses/{courseId}/assign-teacher` endpoint to handle teacher assignment.
   - Include input validation for both Course ID and Teacher ID.
   ```python
   @courses_bp.route('/courses/<int:course_id>/assign-teacher', methods=['POST'])
   ```

- [ ] **Return Success Response in API**  
   **File**: `api/routes/courses.py`  
   - Structure the success response message and updated course details.
   ```python
   return jsonify({"message": "Teacher assigned successfully.", "course": { ... }}), 200
   ```

- [ ] **Handle Validation Errors in API**  
   **File**: `api/routes/courses.py`  
   - Implement error response for invalid Course ID and Teacher ID.
   ```python
   return jsonify({"error": {"code": "E001", "message": "Invalid Course ID or Teacher ID."}}), 400
   ```

- [ ] **Create Get Course Details Endpoint**  
   **File**: `api/routes/courses.py`  
   - Implement GET `/courses/{courseId}` to retrieve course details, including the assigned teacher.
   ```python
   @courses_bp.route('/courses/<int:course_id>', methods=['GET'])
   ```

### 4. Testing and Validation

- [ ] **Add Unit Tests for Teacher Assignment**  
   **File**: `tests/test_courses.py`  
   - Write tests for the new teacher assignment feature, ensuring both success and validation error scenarios are covered.
   ```python
   def test_assign_teacher_to_course_success(client):
       # Test case implementation
   ```

- [ ] **Add Tests for Course Retrieval**  
   **File**: `tests/test_courses.py`  
   - Write tests for retrieving a course and ensuring the assigned teacher is returned correctly.

- [ ] **Validate Error Responses**  
   **File**: `tests/test_courses.py`  
   - Implement tests to ensure appropriate error messages are returned for invalid Course and Teacher IDs.

### 5. Documentation

- [ ] **Update API Documentation**  
   **File**: `docs/api_documentation.md`  
   - Document the new API route for assigning a teacher to a course.
   - Provide examples of request and response formats.

- [ ] **Update README for Setup Instructions**  
   **File**: `README.md`  
   - Ensure that README includes changes related to database setup and any environment variables that need to be documented for the new teacher relationship functionality.

### 6. Integration

- [ ] **Confirm Database and API Integration**  
   **File**: `api/routes/courses.py`  
   - Test the end-to-end functionality of assigning teachers and retrieving course information to ensure integration works seamlessly with existing components.

This task breakdown provides a clear set of actionable tasks for implementing the relationship between the Course and Teacher entities, ensuring a structured and incremental approach that adheres to existing project conventions.