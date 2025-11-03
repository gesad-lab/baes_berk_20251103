# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `app/models.py` (1250 bytes)
- `app/routes.py` (960 bytes)
- `tests/test_api/test_course.py` (780 bytes)

---

### 🗂️ Database Schema Updates

- [ ] **Task 1**: Update Course model to add `teacher_id`
  - **File Path**: `app/models.py`
  - **Description**: Modify the Course model to include a new nullable foreign key column `teacher_id` that links to the Teacher entity.

- [ ] **Task 2**: Create migration script for adding `teacher_id` to Course table
  - **File Path**: `migrations/versions/<timestamp>_add_teacher_relationship_to_course.py`
  - **Description**: Implement a new migration using Flask-Migrate with the provided code to add the `teacher_id` column to the `courses` table and create the foreign key constraint.

### 🗂️ API Endpoint Modifications

- [ ] **Task 3**: Implement API endpoint for assigning a Teacher to a Course
  - **File Path**: `app/routes.py`
  - **Description**: Add a new POST route `/courses/<int:course_id>/assign-teacher/<int:teacher_id>` that facilitates the assignment of a Teacher to a Course.

- [ ] **Task 4**: Implement API endpoint for retrieving Course details with Teacher information
  - **File Path**: `app/routes.py`
  - **Description**: Add a new GET route `/courses/<int:course_id>` that returns details of a Course, including the associated Teacher's information if present.

### 🗂️ Testing Strategy Implementation

- [ ] **Task 5**: Create unit tests for assigning a Teacher to a Course
  - **File Path**: `tests/test_api/test_course.py`
  - **Description**: Implement unit tests that cover the scenarios for successfully assigning a Teacher, including edge cases for invalid inputs.

- [ ] **Task 6**: Create unit tests for retrieving a Course with Teacher details
  - **File Path**: `tests/test_api/test_course.py`
  - **Description**: Implement tests to ensure the Course retrieval endpoint works as expected and provides the correct Teacher information.

- [ ] **Task 7**: Create tests for handling invalid Teacher assignments
  - **File Path**: `tests/test_api/test_course.py`
  - **Description**: Implement tests that verify error handling when assigning a Teacher to a non-existent Course or providing invalid IDs.

### 🗂️ Documentation Updates

- [ ] **Task 8**: Update API documentation for new endpoints
  - **File Path**: `docs/api_documentation.md`
  - **Description**: Document the new API endpoints including request/response formats for `/assign-teacher` and `/courses/<course_id>`, along with error handling details.

- [ ] **Task 9**: Update `README.md` to reflect database migration and new feature setup
  - **File Path**: `README.md`
  - **Description**: Include setup instructions concerning the database migration and new features for assigning Teachers to Courses.

---

### ⚙️ Notes

- Ensure that all new code adheres to the coding standards outlined in the Default Project Constitution, focusing on readability, naming conventions, and documentation.
- Carry out the implementation in isolated tasks to maintain efficiency, allowing for independent testing of each functionality.
- Consider using fixtures in tests to set up any necessary test database entries for courses and teachers when running the test cases.