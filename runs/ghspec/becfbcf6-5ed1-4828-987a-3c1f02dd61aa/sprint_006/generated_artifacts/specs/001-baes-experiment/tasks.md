# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models/course.py` (200 bytes)
- `src/models/teacher.py` (150 bytes)
- `src/api/routes/course.py` (300 bytes)

---

### Task 1: Update Course Model to Include Teacher ID
- **File**: `src/models/course.py`
- **Description**: Modify the `Course` model to add the `teacher_id` field referencing the `Teacher` model.
- **Dependencies**: None
- **Checklist**:
  - [ ] Add `teacher_id` column to `Course` model with ForeignKey relation to `Teacher`.
  - [ ] Update relationship definitions in both `Course` and `Teacher` models.

### Task 2: Create Database Migration for Teacher ID
- **File**: `migrations/versions/<timestamp>_add_teacher_id_to_courses.py`
- **Description**: Generate a migration script that adds the `teacher_id` column to the Course table.
- **Dependencies**: Task 1
- **Checklist**:
  - [ ] Implement `upgrade()` function to add `teacher_id`.
  - [ ] Implement `downgrade()` function to remove `teacher_id`.

### Task 3: Implement PATCH Endpoint for Assigning Teacher
- **File**: `src/api/routes/course.py`
- **Description**: Create an endpoint to assign a teacher to a course using the `PATCH` method.
- **Dependencies**: Task 1
- **Checklist**:
  - [ ] Define `assign_teacher_to_course` function and route.
  - [ ] Validate `teacher_id` existence in the database.
  - [ ] Update course record and return updated course details on success.

### Task 4: Implement GET Endpoint for Retrieving Course with Teacher Information
- **File**: `src/api/routes/course.py`
- **Description**: Create an endpoint to retrieve course details along with the assigned teacher's information.
- **Dependencies**: Task 1
- **Checklist**:
  - [ ] Define `get_course` function and route.
  - [ ] Include teacher information in the response if assigned.

### Task 5: Create Unit Tests for Assigning Teacher to Course
- **File**: `tests/test_course.py`
- **Description**: Add tests for verifying the assignment of a teacher to a course.
- **Dependencies**: Task 3
- **Checklist**:
  - [ ] Write tests for successfully assigning a valid teacher.
  - [ ] Write tests for handling error when a non-existent teacher is assigned.

### Task 6: Create Unit Tests for Retrieving Course with Teacher Info
- **File**: `tests/test_course.py`
- **Description**: Add tests to verify course retrieval includes teacher information if assigned.
- **Dependencies**: Task 4
- **Checklist**:
  - [ ] Write tests for successfully retrieving a course with a teacher assigned.
  - [ ] Write tests for retrieving a course without a teacher assigned.

### Task 7: Update README Documentation
- **File**: `README.md`
- **Description**: Document new API endpoints for assigning a teacher and retrieving course details.
- **Dependencies**: Tasks 3 and 4
- **Checklist**:
  - [ ] Provide details on the new PATCH endpoint `/courses/{course_id}/assign-teacher`.
  - [ ] Provide details on the new GET endpoint `/courses/{course_id}`.

### Task 8: Run and Verify Database Migrations
- **File**: N/A (Requires migration command)
- **Description**: Apply database migrations to ensure schema changes are reflected in the database.
- **Dependencies**: Task 2
- **Checklist**:
  - [ ] Run migration command to apply changes.
  - [ ] Verify that the `teacher_id` column exists in the `courses` table.

---
