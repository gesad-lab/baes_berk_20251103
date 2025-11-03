# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_courses.py` (New Test File)

Instructions for Task Breakdown:
1. Identify which existing files need modifications
2. Create new files for new functionality
3. Ensure integration tasks are included
4. Maintain consistency with existing code style and patterns
---

## Task List

### Database Migration Tasks

- [ ] **Create migration script to add `teacher_id` to `Course` table**  
  **File**: `migrations/versions/add_teacher_id_to_courses.py`  
  - Create an Alembic migration script that adds the `teacher_id` column to the `Course` table.

- [ ] **Implement migration logic in the created script**  
  **File**: `migrations/versions/add_teacher_id_to_courses.py`  
  - Implement the `upgrade` and `downgrade` functions to handle the addition and rollback of the `teacher_id` column.

### Model Update Tasks

- [ ] **Update Course model to include teacher relationship**  
  **File**: `src/models/course.py`  
  - Modify the existing `Course` model to include the `teacher_id` foreign key and relationship to the `Teacher` model.

- [ ] **Update Teacher model to include back-reference for courses**  
  **File**: `src/models/teacher.py`  
  - Modify the existing `Teacher` model to establish a relationship back to the `Course` model.

### API Endpoint Implementation Tasks

- [ ] **Implement endpoint to assign a teacher to a course**  
  **File**: `src/routes/course.py`  
  - Create the `/courses/{course_id}/assign-teacher` PATCH endpoint for assigning a teacher to a course.

- [ ] **Implement endpoint to retrieve course details**  
  **File**: `src/routes/course.py`  
  - Create the `/courses/{course_id}` GET endpoint to retrieve details of the course, including the associated teacher.

- [ ] **Implement endpoint to remove a teacher from a course**  
  **File**: `src/routes/course.py`  
  - Create the `/courses/{course_id}/remove-teacher` PATCH endpoint to remove a teacher from a course.

### Validation and Error Handling Tasks

- [ ] **Implement input validation for teacher assignment**  
  **File**: `src/routes/course.py`  
  - Validate that `teacher_id` and `course_id` are valid before processing requests for assignment or removal.

### Testing Tasks

- [ ] **Add tests for assigning a teacher to a course**  
  **File**: `tests/test_courses.py`  
  - Implement a test for the `/courses/{course_id}/assign-teacher` endpoint to confirm successful assignment.

- [ ] **Add tests for assigning a teacher to a non-existent course**  
  **File**: `tests/test_courses.py`  
  - Implement a test for the `/courses/{course_id}/assign-teacher` endpoint to confirm proper error handling for a non-existent course.

- [ ] **Add tests for retrieving course details with teacher information**  
  **File**: `tests/test_courses.py`  
  - Implement a test for the `/courses/{course_id}` endpoint to confirm returned data includes teacher information.

- [ ] **Add tests for removing a teacher from a course**  
  **File**: `tests/test_courses.py`  
  - Implement a test for the `/courses/{course_id}/remove-teacher` endpoint to confirm the removal functionality.

### Documentation Tasks

- [ ] **Update API documentation to reflect new endpoints**  
  **File**: `README.md`  
  - Modify the README and any auto-generated API documentation to include the new functionality for managing teacher assignments.

- [ ] **Update API usage examples**  
  **File**: `README.md`  
  - Include examples of how to use the new endpoints for assigning and removing teachers from courses.

### Migration Execution Tasks

- [ ] **Ensure migrations run on application startup**  
  **File**: `src/main.py`  
  - Implement startup logic to ensure migrations are executed when the application starts.

---

Each of these tasks is designed to be independently executable and testable, adhering to the principles and standards outlined in the project constitution.