# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `models/course.py` (XXX bytes)
- `models/teacher.py` (XXX bytes)
- `api/course.py` (XXX bytes)
- `services/course_service.py` (XXX bytes)
- `db/database.py` (XXX bytes)
- `tests/test_course.py` (XXX bytes)

---

## Task Breakdown

### 1. Modify Course Entity
- [ ] **Task**: Extend `Course` model to include the `teacher_id` field.
- **File**: `src/models/course.py`
- **Description**: Update the `Course` model to include a foreign key relationship to the `Teacher` model.
```python
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)
    teacher = relationship("Teacher", back_populates="courses")
```

### 2. Modify Teacher Entity
- [ ] **Task**: Update the `Teacher` model to reflect the reverse relationship with `Course`.
- **File**: `src/models/teacher.py`
- **Description**: Implement the relationship as a back-reference to `Course`.
```python
    courses = relationship("Course", back_populates="teacher")
```

### 3. Create Migration for Database Schema
- [ ] **Task**: Write a migration script to alter the `courses` table.
- **File**: `migrations/202XXXXXX_add_teacher_relationship.py`
- **Description**: Add the `teacher_id` column and foreign key constraint to the `courses` table.
```sql
ALTER TABLE courses
ADD COLUMN teacher_id INTEGER,
ADD FOREIGN KEY (teacher_id) REFERENCES teachers(id);
```

### 4. Update API Endpoints
- [ ] **Task**: Create endpoint for assigning a teacher to a course.
- **File**: `src/api/course.py`
- **Description**: Add a POST route `/courses/{course_id}/assign-teacher` for assigning a teacher.
```python
@router.post("/courses/{course_id}/assign-teacher")
```

### 5. Implement Course Service Logic
- [ ] **Task**: Add business logic for assigning teachers in `course_service.py`.
- **File**: `src/services/course_service.py`
- **Description**: Implement `assign_teacher` method to handle teacher assignment and validation.
```python
async def assign_teacher(course_id: int, data: dict):
    # Fetch and assign teacher
```

### 6. Validation for Teacher Assignment
- [ ] **Task**: Create a validation function for checking teacher existence.
- **File**: `src/validators/course_validator.py`
- **Description**: Implement a function to validate if the `teacher_id` exists before assignment.
```python
def validate_teacher_id(teacher_id: int):
    # Validation logic
```

### 7. Create Test Cases for Teacher Assignment
- [ ] **Task**: Write unit tests for teacher assignment in `test_course.py`.
- **File**: `tests/test_course.py`
- **Description**: Add tests for successful teacher assignments and error scenarios.
```python
def test_assign_teacher_valid_data():
    # Test logic for valid assignment
def test_assign_teacher_invalid_teacher():
    # Test handling of non-existent teacher
```

### 8. Testing Course Retrieval with Teacher Info
- [ ] **Task**: Add integration tests for course retrieval including teacher data.
- **File**: `tests/test_course.py`
- **Description**: Ensure courses can be retrieved with associated teacher details.
```python
def test_retrieve_course_with_teacher():
    # Test logic for retrieving course info with teacher
```

### 9. Documentation Update
- [ ] **Task**: Update the README.md with new API details.
- **File**: `README.md`
- **Description**: Document the new endpoints and expected behavior for assigning a teacher to a course.

### 10. Implement Error Handling
- [ ] **Task**: Ensure proper error handling for teacher assignment failures.
- **File**: `src/services/course_service.py`
- **Description**: Handle exceptions for invalid teacher IDs and existing assignments.

---

Each task is designed to be executed independently and testable within the scope of that task, ensuring a smooth integration of the teacher relationship into the course entity.