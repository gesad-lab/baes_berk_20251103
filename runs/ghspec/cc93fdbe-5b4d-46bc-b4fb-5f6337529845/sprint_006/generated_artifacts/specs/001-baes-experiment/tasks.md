# Tasks: Add Teacher Relationship to Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

### Existing Code to Build Upon:
- `src/models.py` (354 bytes)
- `src/services/course_service.py` (450 bytes)
- `src/main.py` (623 bytes)
- `tests/services/test_course_service.py` (299 bytes)
- `tests/integration/test_course_api.py` (395 bytes)

---

### Task 1: Update Course Model
- **File**: `src/models.py`
- **Task**: Add the `teacher_id` attribute as a foreign key in the `Course` model. 
- **Action**: Modify the existing `Course` class to include the `teacher_id` column.
- **Priority**: High
- **Dependency**: None

```python
# Update Course model in src/models.py
def update_course_model():
    """
    Add teacher_id as a foreign key to Course model.
    """ 
    # Modification here
```

- [ ] Implement `teacher_id` in `src/models.py`.

---

### Task 2: Create Teacher Service
- **File**: `src/services/teacher_service.py`
- **Task**: Create a new service to manage Teacher-related operations.
- **Action**: Define the service logic to create, update or manage teachers.
- **Priority**: Medium
- **Dependency**: None

```python
# Create teacher service in src/services/teacher_service.py
def create_teacher_service():
    """
    Service for managing Teacher entity operations.
    """
    # Service logic here
```

- [ ] Implement a new Teacher Service in `src/services/teacher_service.py`.

---

### Task 3: Update Course Service
- **File**: `src/services/course_service.py`
- **Task**: Add a method for assigning a teacher to a course.
- **Action**: Include logic for updating the `teacher_id` in the existing `CourseService`.
- **Priority**: High
- **Dependency**: Task 1

```python
# Add method in src/services/course_service.py
def update_teacher_for_course(course_id: int, teacher_id: int):
    """
    Assign a teacher to a course by updating the teacher_id.
    """
    # Implement logic here
```

- [ ] Implement teacher assignment logic in `src/services/course_service.py`.

---

### Task 4: Create API Endpoint
- **File**: `src/main.py`
- **Task**: Introduce the PATCH endpoint for assigning a teacher to a course.
- **Action**: Configure the new route and connect it to the service.
- **Priority**: High
- **Dependency**: Task 3

```python
# Add PATCH endpoint in src/main.py
@app.patch("/courses/{course_id}", response_model=CourseResponse)
def assign_teacher_to_course(course_id: int, teacher: TeacherUpdate):
    """
    API endpoint to assign a teacher to a course.
    """
    # Endpoint logic here
```

- [ ] Implement the PATCH endpoint in `src/main.py`.

---

### Task 5: Create Migration Script
- **File**: `src/migrations/versions/`
- **Task**: Generate a migration script using Alembic to add the `teacher_id` column.
- **Action**: Create a migration file to add the teacher foreign key.
- **Priority**: High
- **Dependency**: Task 1

```bash
# Create migration file in src/migrations/versions/
alembic revision --autogenerate -m "Add teacher_id to courses table"
```

- [ ] Generate migration script for `teacher_id`.

---

### Task 6: Test Course Service Update
- **File**: `tests/services/test_course_service.py`
- **Task**: Write unit tests for the new teacher assignment logic.
- **Action**: Create tests ensuring proper assignment of teachers to courses.
- **Priority**: High
- **Dependency**: Task 3, Task 1

```python
# Add tests in tests/services/test_course_service.py
def test_assign_teacher_success():
    """
    Test successful assignment of teacher to a course.
    """
    # Test logic here
```

- [ ] Implement unit tests for teacher assignment in `tests/services/test_course_service.py`.

---

### Task 7: Test Course API Endpoint
- **File**: `tests/integration/test_course_api.py`
- **Task**: Write integration tests for the new API endpoint.
- **Action**: Validate functionality of the PATCH request for teacher assignment.
- **Priority**: High
- **Dependency**: Task 4, Task 5

```python
# Add tests in tests/integration/test_course_api.py
def test_update_course_teacher_api():
    """
    Test API endpoint for updating course with new teacher.
    """
    # Test logic here
```

- [ ] Implement integration tests for the API endpoint in `tests/integration/test_course_api.py`.

---

### Task 8: Update Project Documentation
- **File**: `README.md`
- **Task**: Document the new API endpoint and migration process.
- **Action**: Update the project documentation to reflect changes in the API and schema.
- **Priority**: Medium
- **Dependency**: Task 4, Task 5

```markdown
# Update README.md
## API Changes
- PATCH /courses/{course_id}
...
```

- [ ] Update `README.md` with new endpoint and migration documentation.

---

### Task 9: Conduct Performance Testing
- **File**: N/A
- **Task**: Validate the performance impact of adding the new relationship.
- **Action**: Ensure that adding the teacher relationship does not degrade system performance.
- **Priority**: Medium
- **Dependency**: All implementation tasks

```bash
# Performance testing procedures not in codebase
```

- [ ] Conduct performance testing after completing all tasks.

---

By completing these tasks in a structured manner, the integration of the `Teacher` entity with the `Course` will be implemented effectively, maintaining project consistency and ensuring robust validation and testing.