# Tasks: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- models/student.py (existing file)
- tests/test_student_enrollment.py (existing file for new testing)

## Task List

- [ ] **Task 1:** Update the `models/student.py` file to include the relationship with the `Enrollment` model.
  - **File Path**: `models/student.py`
  - **Description**: Add a `courses` relationship in the `Student` class to establish the many-to-many relationship with the `Enrollment` model.

- [ ] **Task 2:** Create a new file for the `Enrollment` model.
  - **File Path**: `models/enrollment.py`
  - **Description**: Define the `Enrollment` class with the necessary attributes (`student_id`, `course_id`) and relationships.

- [ ] **Task 3:** Modify the database migration files to add the `enrollments` table.
  - **File Path**: `database/migrations/`
  - **Description**: Add migration script to create the `enrollments` table linking `student_id` and `course_id`, ensuring rollback functionality is included.

- [ ] **Task 4:** Create a new schema for validating enrollment requests.
  - **File Path**: `schemas/enrollment_schema.py`
  - **Description**: Define a schema that ensures both `student_id` and `course_ids` are valid and present in the request.

- [ ] **Task 5:** Update the existing `controllers/student_controller.py` to handle enrollment-related API endpoints.
  - **File Path**: `controllers/student_controller.py`
  - **Description**: Implement logic for processing the API requests for enrolling students and retrieving their courses.

- [ ] **Task 6:** Implement error handling for invalid course ID enrollment within the `controllers/student_controller.py`.
  - **File Path**: `controllers/student_controller.py`
  - **Description**: Define error response structure for handling invalid course IDs, returning 400 Bad Request with appropriate messages.

- [ ] **Task 7:** Create unit and integration tests for the new functionality in the `tests/test_student_enrollment.py`.
  - **File Path**: `tests/test_student_enrollment.py`
  - **Description**: Write tests for successful student enrollment and retrieval of courses, ensuring both positive and negative scenarios are covered.

- [ ] **Task 8:** Update the README file to document the new API endpoints for enrolling students and retrieving enrolled courses.
  - **File Path**: `README.md`
  - **Description**: Provide clear instructions for new API usage, including request/response structures for the added functionality.

- [ ] **Task 9:** Ensure all changes are committed following the project's Git hygiene standards, documenting any modifications made.
  - **File Path**: N/A (commit changes)
  - **Description**: Make clear, concise commit messages indicating the purpose of changes, adhering to project standards.

Each task represents a focused and manageable piece of the implementation that can be executed, tested, and validated independently, ensuring a smooth development process.