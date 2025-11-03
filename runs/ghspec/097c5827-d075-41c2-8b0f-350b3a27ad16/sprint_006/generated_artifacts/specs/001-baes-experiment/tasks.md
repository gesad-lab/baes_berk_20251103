# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- src/models.py (512 bytes)
- src/controllers/course_controller.py (1024 bytes)
- src/services/course_service.py (768 bytes)
- src/database.py (420 bytes)
- tests/test_course.py (800 bytes)
- tests/test_course_integration.py (1500 bytes)

---

## Task List

### Task 1: Update Course Model
- **File**: `src/models.py`
- **Description**: Add a foreign key relationship to the `Course` entity by including `teacherId`.
- **Action**: Modify the `Course` class definition to include `teacherId` as a foreign key.
- **Estimated Time**: 1 hour
- [ ] Update Course model to include teacherId

### Task 2: Add Assign Teacher Endpoint
- **File**: `src/controllers/course_controller.py`
- **Description**: Extend the course controller to handle PATCH requests for assigning a teacher to a course.
- **Action**: Implement a new endpoint `/courses/{courseId}/assign-teacher` to process teacher assignment.
- **Estimated Time**: 1.5 hours
- [ ] Add PATCH endpoint for assigning a teacher to a course

### Task 3: Update Get Course Details Endpoint
- **File**: `src/controllers/course_controller.py`
- **Description**: Modify the existing GET course details endpoint to include teacher information in the response.
- **Action**: Ensure the endpoint returns the teacher details along with course information.
- **Estimated Time**: 1 hour
- [ ] Update GET course details endpoint to include teacher information

### Task 4: Extend Course Service Logic
- **File**: `src/services/course_service.py`
- **Description**: Implement business logic for assigning a teacher to a course, including validation for existing teachers.
- **Action**: Create a new function in the course service to encapsulate the business rules for teacher assignment.
- **Estimated Time**: 1.5 hours
- [ ] Extend course service to handle teacher assignment logic

### Task 5: Create Migration for Database Schema Update
- **File**: `src/database.py`
- **Description**: Implement a migration to modify the `courses` table to include a foreign key for `teacherId`.
- **Action**: Use Alembic commands to create the migration script for adding the `teacherId` column.
- **Estimated Time**: 1 hour
- [ ] Create migration to add teacherId to courses table

### Task 6: Write Unit Tests for New Functionality
- **File**: `tests/test_course.py`
- **Description**: Add unit tests that cover the new logic for assigning teachers and retrieving course details with teacher information.
- **Action**: Write individual test cases for the new functions and endpoints introduced.
- **Estimated Time**: 2 hours
- [ ] Write unit tests for teacher assignment and course details retrieval

### Task 7: Write Integration Tests for New Endpoints
- **File**: `tests/test_course_integration.py`
- **Description**: Develop integration tests to validate the endpoint's functionality for teacher assignments.
- **Action**: Ensure that both successful assignments and error messages are covered in the tests.
- **Estimated Time**: 2 hours
- [ ] Write integration tests for assigning a teacher to a course

### Task 8: Validate Data Integrity in Migration
- **File**: `src/database.py`
- **Description**: Ensure that the migration process preserves existing data integrity during the schema update.
- **Action**: Validate that existing course data remains intact and functions as expected post-migration.
- **Estimated Time**: 1 hour
- [ ] Validate data integrity in migration process

### Task 9: Documentation Updates
- **File**: `README.md`
- **Description**: Update the project documentation to include instructions on how to use the new features related to teacher assignments.
- **Action**: Add details about the new endpoints and expected request/response formats.
- **Estimated Time**: 1 hour
- [ ] Update documentation to reflect new teacher assignment features

---

### Summary Notes
- Ensure all code modifications adhere to existing style guidelines and architecture.
- Prioritize rigorous testing to validate new functionalities, focusing on both unit and integration aspects.
- Maintain clear and concise documentation, highlighting changes made for future reference and usage.

---