# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models.py`
- `src/main.py`
- `tests/test_api/test_course_api.py`
- `tests/test_services/test_course_service.py`

## Task Breakdown

### 1. Modify Course Model
- **Task**: Update Course class in `src/models.py` to include `teacher_id` foreign key.
- **File**: `src/models.py`
- **Description**: Add the `teacher_id` field to the Course entity, establishing a foreign key relationship with the Teacher entity.
- [ ] Update the Course class to include `teacher_id` field.
- [ ] Ensure the teacher relationship using SQLAlchemy's relationship function.

### 2. Update API Endpoints for Course
- **Task**: Implement the `PATCH` endpoint for updating a course in `src/main.py`.
- **File**: `src/main.py`
- **Description**: Create a new endpoint to allow the association of a teacher with a course.
- [ ] Add `PATCH /courses/{course_id}` endpoint to handle course updates.
- [ ] Validate the incoming JSON payload for `teacher_id`.

- **Task**: Implement the `GET` endpoint for retrieving course details with associated teacher info in `src/main.py`.
- **File**: `src/main.py`
- **Description**: Enhance the current GET endpoint to return course information along with the associated teacher details.
- [ ] Update `GET /courses/{course_id}` endpoint to include teacher's name and email in the response.

### 3. Database Migration
- **Task**: Create a migration script to add `teacher_id` to the courses table.
- **File**: New migration script (e.g., `src/migrations/002_add_teacher_id_to_courses.py`)
- **Description**: Write a migration script for the database schema change to add the `teacher_id` column to the `courses` table and establish a foreign key constraint.
- [ ] Write SQL commands for adding `teacher_id` column and foreign key in the migration script.

### 4. Input Validation Model
- **Task**: Create a Pydantic model for course update requests.
- **File**: `src/schemas.py`
- **Description**: Define a Pydantic model called `CourseUpdate` to validate incoming requests for course updates.
- [ ] Add a new class in `schemas.py` for validating `teacher_id`.

### 5. Write Unit Tests for Course API
- **Task**: Add tests for the course update functionality in `tests/test_api/test_course_api.py`.
- **File**: `tests/test_api/test_course_api.py`
- **Description**: Implement unit tests to ensure that associating a teacher with a course works correctly and handles invalid cases.
- [ ] Write tests for the `PATCH /courses/{course_id}` endpoint to validate successful teacher association.
- [ ] Write tests that check the response for attempts to associate a non-existent teacher.

### 6. Write Input Validation Test Cases
- **Task**: Add tests for input validation in `tests/test_services/test_course_service.py`.
- **File**: `tests/test_services/test_course_service.py`
- **Description**: Implement tests for the service layer to handle invalid `teacher_id` during course updates.
- [ ] Write tests to ensure appropriate error handling for non-existent teachers.

### 7. Update Documentation
- **Task**: Revise `README.md` to include new API endpoints.
- **File**: `README.md`
- **Description**: Document the new endpoints for updating and retrieving courses with teacher associations, including request and response formats.
- [ ] Update usage examples in the README to reflect the new course API functionality.

### 8. Error Handling
- **Task**: Ensure error handling for API responses is implemented correctly.
- **File**: `src/main.py`
- **Description**: Validate inputs and return structured error responses for the new course update and retrieval endpoints.
- [ ] Implement error checks for invalid `teacher_id` during requests.

### 9. Performance Testing
- **Task**: Write performance tests in `tests/test_api/test_performance.py`.
- **File**: `tests/test_api/test_performance.py`
- **Description**: Validate that the new endpoints meet response time requirements (under 2 seconds).
- [ ] Implement performance benchmarks for both the `PATCH` and `GET` endpoints.

### 10. Review and Merge
- **Task**: Prepare code for review and ensure all tasks are complete.
- **File**: N/A
- **Description**: Conduct a final review of all changes for consistency and adherence to project guidelines before merging.
- [ ] Verify all tests pass.
- [ ] Confirm that API documentation is up-to-date.

--- 

These tasks have been structured to ensure that each step is focused on a single file or action, allowing for easier execution and testing of changes as we enhance the system with the teacher relationship to courses.