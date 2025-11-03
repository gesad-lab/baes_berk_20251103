# Tasks: Add Teacher Relationship to Course Entity

---

INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_courses_api.py` (2103 bytes)

## Task Breakdown

### Task 1: Update Course Model to Include Teacher ID
- **File Path**: `src/models/course.py`
- **Description**: Modify the existing Course model to add the `teacher_id` foreign key.
- **Instructions**: Implement the new `teacher_id` field as described in the implementation plan.
- [ ] Implement foreign key relationship in the Course model.

### Task 2: Create Migration Script for Teacher ID Field
- **File Path**: `src/db/migrations/versions/add_teacher_id_to_courses.py`
- **Description**: Create a migration script using Alembic to add the `teacher_id` column to the courses table.
- **Instructions**: Define upgrades and downgrades as described in the implementation plan.
- [ ] Write the Alembic migration script for adding the `teacher_id` field.

### Task 3: Implement API Endpoint for Assigning Teacher to Course
- **File Path**: `src/api/courses.py`
- **Description**: Develop the `POST /courses/{course_id}/assign_teacher` endpoint to assign a teacher to a course.
- **Instructions**: Implement the endpoint handler and validate input IDs.
- [ ] Create the API endpoint for assigning a teacher to a course.

### Task 4: Implement API Endpoint for Retrieving Course Details
- **File Path**: `src/api/courses.py`
- **Description**: Develop the `GET /courses/{course_id}` endpoint to return course details including an assigned teacher's name if available.
- **Instructions**: Ensure the response matches the specified format in the implementation plan.
- [ ] Create the API endpoint for retrieving course details.

### Task 5: Validate Input for Assigning Teacher to Course
- **File Path**: `src/validation/course_validation.py`
- **Description**: Implement input validation for course and teacher IDs during the assignment process.
- **Instructions**: Create methods to validate the presence of existing IDs and return proper error responses.
- [ ] Write input validation functions for course and teacher assignment.

### Task 6: Write Unit Tests for Assigning Teacher to Course
- **File Path**: `tests/test_courses_api.py`
- **Description**: Add unit tests to verify functionality for assigning a teacher to a course.
- **Instructions**: Implement tests that cover both successful assignments and error handling (e.g., invalid IDs).
- [ ] Create test cases for assigning a teacher to a course.

### Task 7: Write Unit Tests for Retrieving Course Details
- **File Path**: `tests/test_courses_api.py`
- **Description**: Add unit tests to verify functionality for retrieving course details, ensuring correct behavior when a teacher is assigned or not.
- **Instructions**: Implement tests that check responses for both cases.
- [ ] Create test cases for retrieving course details.

### Task 8: Document API Endpoints in README
- **File Path**: `README.md`
- **Description**: Update the README file to include documentation for the new API endpoints.
- **Instructions**: Ensure all endpoint descriptions, request formats, and responses are added.
- [ ] Document new API endpoints in the README.

### Task 9: Set Up Logging for API Requests
- **File Path**: `src/main.py`
- **Description**: Integrate structured logging practices for capturing API requests and error events.
- **Instructions**: Configure logging as per the structure outlined in the implementation plan.
- [ ] Implement structured logging for API requests and responses.

### Task 10: Run Migrations and Test the Application
- **File Path**: N/A
- **Description**: Execute migrations and run the application to ensure all changes are reflected properly.
- **Instructions**: Use Alembic to apply the migration and start the application for testing purposes.
- [ ] Run migrations and validate the application behavior.

--- 

This breakdown provides a structured approach to implementing the feature, ensuring that all aspects of development, testing, and documentation are covered consistently with the existing codebase.