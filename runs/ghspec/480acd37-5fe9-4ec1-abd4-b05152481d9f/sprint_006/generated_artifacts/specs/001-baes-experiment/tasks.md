# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- tests/test_api.py (2179 bytes)

Instructions for Task Breakdown:
1. Identify which existing files need modifications
2. Create new files for new functionality
3. Ensure integration tasks are included
4. Maintain consistency with existing code style and patterns

---

## Task List

- [ ] **Task 1**: Update Course model to include teacher_id.
  - **File Path**: `src/models.py`
  - **Description**: Modify the `Course` class to add a new column `teacher_id` referencing the `Teacher` entity as a ForeignKey.

- [ ] **Task 2**: Create Pydantic schema for course assignment validation.
  - **File Path**: `src/schemas.py`
  - **Description**: Define a new Pydantic model that specifies the structure for the assignment request body, including validation for `teacher_id`.

- [ ] **Task 3**: Implement API endpoint for assigning a teacher to a course.
  - **File Path**: `src/api.py`
  - **Description**: Create the `PATCH /courses/{course_id}/assign-teacher` API endpoint to handle teacher assignment. Include necessary validation and success response.

- [ ] **Task 4**: Implement API endpoint to fetch course details with teacher information.
  - **File Path**: `src/api.py`
  - **Description**: Create the `GET /courses/{course_id}` endpoint to retrieve course details and include assigned teacher's information if it exists.

- [ ] **Task 5**: Create database migration to add teacher_id column to Course table.
  - **File Path**: `migrations/versions/xxxx_add_teacher_relationship.py`
  - **Description**: Use Alembic to generate a migration script that adds the `teacher_id` column to the `courses` table without affecting existing data.

- [ ] **Task 6**: Validate teacher_id during assignment.
  - **File Path**: `src/api.py`
  - **Description**: Implement validation logic to ensure the provided `teacher_id` corresponds to a valid teacher in the database in the patch assignment endpoint.

- [ ] **Task 7**: Modify existing tests to add coverage for new functionality.
  - **File Path**: `tests/test_api.py`
  - **Description**: Write new test cases to validate the new functionality, including checking responses for successful assignments and error handling for invalid `teacher_id`.

- [ ] **Task 8**: Implement integration tests for new API endpoints.
  - **File Path**: `tests/test_integration.py`
  - **Description**: Create integration tests to verify that the entire process of assigning a teacher to a course and fetching the course details functions correctly.

- [ ] **Task 9**: Update README.md with new API documentation.
  - **File Path**: `README.md`
  - **Description**: Add documentation for the new API endpoints, including examples for the request body and the expected response.

---

Each task can be executed independently and should be easily testable upon completion. Please ensure all changes follow the existing code style and maintain compatibility with the current application infrastructure.