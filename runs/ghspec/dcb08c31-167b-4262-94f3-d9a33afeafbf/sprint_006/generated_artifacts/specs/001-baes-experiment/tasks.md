# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models/course.py` (450 bytes)
- `src/models/teacher.py` (300 bytes)
- `src/routes/course_routes.py` (600 bytes)
- `src/database/migrations/` (Directory for migration scripts)
- `tests/routes/test_course_routes.py` (2500 bytes)
- `tests/integration/test_integration.py` (2553 bytes)

## Task Breakdown

### Task 1: Update Course Model
- **File**: `src/models/course.py`
- **Details**: Add the `teacher_id` field to the `Course` model as a foreign key to the `Teacher` model.
- **Dependencies**: Requires the existing `Teacher` model to be set up.
- **Test**: Ensure the updated model functions correctly.
- [ ] Modify `Course` class to include `teacher_id`.

### Task 2: Create Migration Script
- **File**: `src/database/migrations/008_add_teacher_relationship_to_courses.py`
- **Details**: Write a migration script using Alembic to add the `teacher_id` column to the `courses` table.
- **Dependencies**: Task 1 should be completed.
- **Test**: Run migration to confirm it completes without data loss.
- [ ] Create Alembic migration script for updating the `courses` table.

### Task 3: Implement API Endpoint for Assigning Teacher to Course
- **File**: `src/routes/course_routes.py`
- **Details**: Implement the `PATCH /courses/{courseId}` endpoint to allow teacher assignment.
- **Dependencies**: Task 1 must be complete.
- **Test**: Validate that the endpoint correctly assigns a teacher and returns the updated course object.
- [ ] Add code for PATCH endpoint to assign a teacher to a course.

### Task 4: Update API Endpoint for Retrieving Course Details
- **File**: `src/routes/course_routes.py`
- **Details**: Update the `GET /courses/{courseId}` endpoint to include the assigned teacher's name and email in the response.
- **Dependencies**: Task 1 must be complete.
- **Test**: Ensure the response includes the teacher's details.
- [ ] Modify GET endpoint to return teacher information alongside course data.

### Task 5: Implement Validation Logic
- **File**: `src/routes/course_routes.py`
- **Details**: Validate that the `teacher_id` provided during assignment exists in the `Teacher` table.
- **Dependencies**: Task 3 must be complete.
- **Test**: Verify that attempts to assign invalid teacher IDs return appropriate error messages.
- [ ] Add validation logic for teacher assignment input.

### Task 6: Update Unit Tests for Teacher Assignment
- **File**: `tests/routes/test_course_routes.py`
- **Details**: Write unit tests for the PATCH endpoint to cover successful assignments and error cases.
- **Dependencies**: Tasks 3 and 5 must be complete.
- **Test**: Confirm tests achieve at least 70% coverage for these new functionalities.
- [ ] Add unit tests for teacher assignment to course.

### Task 7: Update Integration Tests
- **File**: `tests/integration/test_integration.py`
- **Details**: Include integration tests to check overall functionality of teacher assignment and retrieval for courses.
- **Dependencies**: Tasks 3, 4, and 5 must be complete.
- **Test**: Ensure integration tests confirm end-to-end process works as expected.
- [ ] Add integration tests for course-teacher relationships.

### Task 8: Documentation Update
- **File**: `README.md`
- **Details**: Update documentation to reflect the new API endpoints, including usage examples for the teacher assignment feature.
- **Dependencies**: All tasks must be completed.
- **Test**: Ensure documentation accurately covers the new feature.
- [ ] Document API changes related to course and teacher assignment.

### Task 9: Ensure Logging is Set Up
- **File**: `src/routes/course_routes.py`
- **Details**: Implement logging for actions related to course-teacher assignments.
- **Dependencies**: Tasks 3 and 5 must be complete.
- **Test**: Verify that logging captures relevant events and errors.
- [ ] Add structured logging for teacher assignment activities.

### Task 10: Conduct Final Review and Testing
- **File**: N/A (Cross-file check)
- **Details**: Review all changes and tests for completeness, run all tests, and confirm system integrity.
- **Dependencies**: All tasks must be completed.
- **Test**: Ensure no regressions and confirm all tests pass successfully.
- [ ] Perform final code review and ensure all tests pass.

--- 

This structured task breakdown ensures a clear progression towards implementing and testing the teacher relationship in the course entity, adhering to guidelines set forth in the implementation plan.