# Tasks: Add Teacher Relationship to Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models.py` (2000 bytes)
- `src/routes.py` (1800 bytes)
- `src/db.py` (1500 bytes)
- `tests/test_routes.py` (3403 bytes)
- `tests/test_services.py` (2112 bytes)

---

### Task List

- [ ] **Task 1**: Update Course Model to Include `teacher_id`
  - **File Path**: `src/models.py`
  - **Description**: Modify the `Course` class to add an optional foreign key field `teacher_id` that references the `Teacher` entity.

- [ ] **Task 2**: Create Migration Script for Database Update
  - **File Path**: `src/db.py`
  - **Description**: Write a migration script using Alembic to add the `teacher_id` foreign key column in the `courses` table.

- [ ] **Task 3**: Update API Routes to Handle Teacher Assignment when Creating Courses
  - **File Path**: `src/routes.py`
  - **Description**: Modify the course creation endpoint to accept `teacher_id` in the request body and adjust the logic accordingly.

- [ ] **Task 4**: Update API Routes to Handle Teacher Assignment when Updating Courses
  - **File Path**: `src/routes.py`
  - **Description**: Update the course update endpoint to support changing the associated teacher for an existing course.

- [ ] **Task 5**: Implement Course Service Logic
  - **File Path**: `src/services.py`
  - **Description**: Add service methods to handle the business logic for creating and updating courses with teacher associations, ensuring appropriate validation occurs.

- [ ] **Task 6**: Write Tests for Course Creation and Teacher Assignment
  - **File Path**: `tests/test_routes.py`
  - **Description**: Add test cases to verify that an admin can successfully create a course and assign a teacher, including input validation tests for non-existent teachers.

- [ ] **Task 7**: Write Tests for Course Updates and Teacher Changes
  - **File Path**: `tests/test_routes.py`
  - **Description**: Add test cases to ensure that an admin can successfully update a course to change its assigned teacher, including various validation scenarios.

- [ ] **Task 8**: Write Tests for Course Retrieval with Teacher Info
  - **File Path**: `tests/test_services.py`
  - **Description**: Implement tests that confirm the application accurately retrieves course details, including the associated teacher information if applicable.

- [ ] **Task 9**: Document Changes and New API Endpoints
  - **File Path**: `README.md`
  - **Description**: Update the documentation to reflect the newly added `teacher_id` functionality and provide usage examples for the updated endpoints.

- [ ] **Task 10**: Perform Manual Testing to Validate Functionality
  - **File Path**: `src/app.py`
  - **Description**: Manually test the new features in the application to ensure correct functionality and data integrity, documenting any issues found.

--- 

These tasks have been structured to ensure a logical progression in dependencies, maintainability, and independent testability of each function. The tasks follow the existing code patterns to ensure consistency and ease of comprehension.