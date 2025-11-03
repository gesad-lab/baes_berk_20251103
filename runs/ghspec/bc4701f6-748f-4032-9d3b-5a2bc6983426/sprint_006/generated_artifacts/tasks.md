# Tasks: Add Teacher Relationship to Course Entity

---

INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models/course.py`
- `src/api/course.py`
- `tests/api/test_course.py`

---

## Task Breakdown

### Modify Existing Models

- [ ] **Task 1**: Update the Course model to include a foreign key to the Teacher model.
  - **File Path**: `src/models/course.py`
  - **Description**: Modify the existing Course class to add `teacher_id` foreign key referencing Teacher.id and adjust relationships accordingly. Ensure alignment with the coding standards for readability and documentation.

- [ ] **Task 2**: Verify Teacher model is correctly defined and referenced.
  - **File Path**: `src/models/course.py`
  - **Description**: Ensure the Teacher model is correctly structured and importable in the Course model file. Document any necessary changes to ensure clarity.

### Implement API Endpoints

- [ ] **Task 3**: Create API endpoint for assigning a teacher to a course.
  - **File Path**: `src/api/course.py`
  - **Description**: Implement a PATCH endpoint to `/courses/{course_id}`, updating course records with an associated teacher based on incoming requests. Add validation and proper error handling for 404 cases.

- [ ] **Task 4**: Create API endpoint for retrieving course details including teacher information.
  - **File Path**: `src/api/course.py`
  - **Description**: Implement a GET endpoint to fetch course details, ensuring that if a teacher is associated, their information is included in the response JSON. Handle error cases appropriately as per specifications.

### Database Schema Migration

- [ ] **Task 5**: Implement database migration to add the teacher_id foreign key to the courses table.
  - **File Path**: `src/database/migrate.py` (if the file doesn't exist, create a new migration file)
  - **Description**: Write migration code that updates the courses table to include a foreign key relationship with the teachers table, ensuring backward compatibility and existing data integrity.

- [ ] **Task 6**: Add initialization code for database migration.
  - **File Path**: `src/database/__init__.py` (or specific migration script file)
  - **Description**: Set up code to initialize the database and apply migrations on application startup, including schema adjustments for new relationships.

### Testing New Functionality

- [ ] **Task 7**: Create unit tests for course model updates.
  - **File Path**: `tests/api/test_course.py`
  - **Description**: Add tests to validate the changes made to the Course model, ensuring that the `teacher_id` field is functioning as expected.

- [ ] **Task 8**: Write integration tests for the teacher assignment endpoint.
  - **File Path**: `tests/api/test_course.py`
  - **Description**: Implement tests for the new PATCH endpoint to ensure assignments can be made correctly and inappropriate requests return the expected error responses. Include tests for both successful assignments and failures due to non-existent entities.

- [ ] **Task 9**: Write integration tests for the endpoint that retrieves course details including teacher information.
  - **File Path**: `tests/api/test_course.py`
  - **Description**: Develop tests to verify that course lookup returns the correct teacher information when assigned and correctly handles 404 cases for missing courses.

### Documentation

- [ ] **Task 10**: Update README.md to include new API endpoint documentation.
  - **File Path**: `README.md`
  - **Description**: Provide clear instructions for utilizing the new course management API endpoints, including expected request and response formats. Ensure it reflects the functionality introduced in the recent changes.

---

This task breakdown creates clear, actionable items that are easily testable and follow the structure laid out in the initial specification. Each task is focused on a single file or operation conforming to your implementation requirements.