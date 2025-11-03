# Tasks: Add Teacher Relationship to Course Entity

---

INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `models/course.py` (existing entity model)
- `models/teacher.py` (539 bytes)
- `tests/test_integration.py` (2252 bytes)
- `tests/test_teacher.py` (1797 bytes)

---

## Task Breakdown

### Task 1: Create Migration File
- **File Path**: `migrations/xxxx_add_teacher_id_to_courses.py`
- **Description**: Create a migration file to add `teacher_id` foreign key column to the `courses` table.
- **Action Items**:
  - Write migration script to add the new column.
  
```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id')))

def downgrade():
    op.drop_column('courses', 'teacher_id')
```
- [ ] Create migration file for adding teacher_id.

---

### Task 2: Update Course Model
- **File Path**: `models/course.py`
- **Description**: Update the existing Course model to include a `teacher_id` attribute.
- **Action Items**:
  - Modify the `Course` class to add the new column definition.
  
```python
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))  # Establishing the relationship
```
- [ ] Add teacher_id column to the Course model.

---

### Task 3: Implement API Endpoint
- **File Path**: `routes.py`
- **Description**: Create a new route to handle teacher assignments to courses.
- **Action Items**:
  - Implement the `POST /courses/{course_id}/assign-teacher` endpoint.
  - Include logic for handling the assignment and validation of teacher existence.
  
```python
@courses_bp.route('/courses/<int:course_id>/assign-teacher', methods=['POST'])
def assign_teacher_to_course(course_id):
    data = request.get_json()
    teacher_id = data.get('teacher_id')
    
    teacher = Teacher.query.get(teacher_id)
    course = Course.query.get(course_id)
    
    if not teacher:
        return jsonify({"error": {"code": "E002", "message": "Teacher ID does not exist."}}), 400
    
    if not course:
        return jsonify({"error": {"code": "E003", "message": "Course ID does not exist."}}), 404

    course.teacher_id = teacher_id
    db.session.commit()

    return jsonify({"id": course.id, "name": course.name, "level": course.level, "teacher_id": course.teacher_id}), 200
```
- [ ] Implement the course-teacher assignment endpoint.

---

### Task 4: Implement Validation Logic
- **File Path**: `routes.py`
- **Description**: Ensure that incoming requests are validated for correct teacher IDs.
- **Action Items**:
  - Integrate validation checks in the assignment logic to confirm teacher validity.

- [ ] Ensure validation for teacher_id in route.

---

### Task 5: Implement Error Handling
- **File Path**: `routes.py`
- **Description**: Set up error handling to return structured JSON responses for invalid requests.
- **Action Items**:
  - Provide a structured error response for invalid `teacher_id`.

- [ ] Implement structured error responses for invalid teacher assignments.

---

### Task 6: Create Unit Tests for API
- **File Path**: `tests/test_teacher.py`
- **Description**: Write tests to verify the new teacher assignment functionality.
- **Action Items**:
  - Add test cases for successful assignments and error handling for invalid teacher IDs.

```python
def test_assign_teacher_to_course(client):
    response = client.post('/courses/1/assign-teacher', json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json['teacher_id'] == 1

def test_assign_teacher_with_invalid_teacher_id(client):
    response = client.post('/courses/1/assign-teacher', json={"teacher_id": 999})
    assert response.status_code == 400
    assert response.json['error']['code'] == "E002"
```
- [ ] Create unit tests for successful and error scenarios in teacher assignment.

---

### Task 7: Update API Documentation
- **File Path**: `README.md` or API documentation source
- **Description**: Update the documentation to include details about the new teacher assignment endpoint.
- **Action Items**:
  - Specify the new endpoint, expected request body, and responses.

- [ ] Update API documentation to reflect new teacher assignment endpoint.

---

### Task 8: Validate Existing Data Integrity
- **File Path**: `tests/test_integration.py` (or a new test file)
- **Description**: Ensure that existing data for students and teachers maintains integrity post-migration.
- **Action Items**:
  - Write integration tests to confirm existing records are retrievable.

- [ ] Create tests for data integrity check after migration.

---

### Task 9: Run Migration and Test Application
- **File Path**: Command line
- **Description**: Execute the migration and run application tests to ensure completion.
- **Action Items**:
  - Apply migration and run all tests to validate incorporation.

- [ ] Run migration and all tests to validate functionality.