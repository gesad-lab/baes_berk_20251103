# Tasks: Add Teacher Relationship to Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `models.py`
- `routes.py`
- `validators.py`
- `database.py`
- `tests/api/test_courses.py`
- `tests/database/test_migrations.py`

---

## Task List

### 1. Update `models.py`
- [ ] **Task**: Modify the `Course` model to include a foreign key reference to the `Teacher` model.
  - **File Path**: `src/models.py`
  - **Details**: Add a new column `teacher_id` that references `teachers.id` and establish a relationship.
  
### 2. Create Migration Script
- [ ] **Task**: Implement a migration script to update the `courses` table schema.
  - **File Path**: `src/database/migrations/2023_add_teacher_relationship_to_course.py`
  - **Details**: Use Alembic to create the migration script that adds the `teacher_id` column and sets up the foreign key constraint.

### 3. Update `routes.py`
- [ ] **Task**: Add a route for assigning a teacher to a course.
  - **File Path**: `src/routes.py`
  - **Details**: Implement the PUT `/courses/{course_id}/assign-teacher` endpoint for teacher assignments.
  
- [ ] **Task**: Add a route for retrieving course details including associated teacher info.
  - **File Path**: `src/routes.py`
  - **Details**: Implement the GET `/courses/{course_id}` endpoint to return course and teacher data.

### 4. Update `validators.py`
- [ ] **Task**: Enhance input validation to ensure the `teacher_id` is provided and valid.
  - **File Path**: `src/validators.py`
  - **Details**: Implement checks for the presence and validity of the `teacher_id` field when assigning a teacher to a course.

### 5. Implement Error Handling
- [ ] **Task**: Create structured error responses for invalid teacher assignments.
  - **File Path**: `src/routes.py`
  - **Details**: Ensure error messages are returned in the specified format if an invalid or missing `teacher_id` is detected.

### 6. Update Tests for Course API
- [ ] **Task**: Add test cases to verify the teacher assignment functionality.
  - **File Path**: `tests/api/test_courses.py`
  - **Details**: Write tests for the PUT `/courses/{course_id}/assign-teacher` endpoint checking both successful and unsuccessful assignments.

- [ ] **Task**: Add test cases for retrieving course details including the assigned teacher.
  - **File Path**: `tests/api/test_courses.py`
  - **Details**: Write tests for the GET `/courses/{course_id}` endpoint to verify the response includes teacher details when assigned.

### 7. Migrate Test Database
- [ ] **Task**: Implement database migration tests to validate schema changes.
  - **File Path**: `tests/database/test_migrations.py`
  - **Details**: Create tests to ensure existing data remains intact after schema alterations.

### 8. Update Documentation
- [ ] **Task**: Update API documentation to reflect new endpoints and functionality.
  - **File Path**: `docs/api_reference.md`
  - **Details**: Include descriptions for the new endpoints and expected request/response formats.

---

### Summary of Expected Modifications
- **File**: `src/models.py` - Update Course model for new teacher relationship.
- **File**: `src/database/migrations/2023_add_teacher_relationship_to_course.py` - Create migration for new foreign key.
- **File**: `src/routes.py` - Add new endpoints for assigning and retrieving courses with teachers.
- **File**: `src/validators.py` - Implement validation for teacher assignments.
- **File**: `tests/api/test_courses.py` - New test cases for course-teacher functionalities.
- **File**: `tests/database/test_migrations.py` - Migration validation tests.

This structured task breakdown ensures a focused incremental development approach while adhering to existing code structures and patterns.