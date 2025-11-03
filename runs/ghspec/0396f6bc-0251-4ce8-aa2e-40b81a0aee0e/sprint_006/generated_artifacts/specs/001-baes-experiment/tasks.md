# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- models.py
- api.py
- services.py
- database.py
- tests/test_courses.py

---

## Task Breakdown

### Task 1: Update Course Model
- **File**: `src/models.py`
- **Description**: Add `teacher_id` foreign key to the `Course` class and define relationship with `Teacher`.
- **Subtasks**:
  - Add a new column `teacher_id` as a foreign key in the `Course` model.
  - Define the relationship with `Teacher`.
- [ ] **Task 1 Completed**

### Task 2: Implement Database Migration
- **File**: `src/database.py`
- **Description**: Create Alembic migration script to add `teacher_id` column to `Course` table.
- **Subtasks**:
  - Generate migration file using Alembic.
  - Ensure migration script adds foreign key constraint correctly.
- [ ] **Task 2 Completed**

### Task 3: Add API Endpoint for Assigning Teacher
- **File**: `src/api.py`
- **Description**: Create endpoint for `PATCH /courses/{courseId}/assign-teacher`.
- **Subtasks**:
  - Implement endpoint handler to accept `teacherId` in the request body.
  - Validate `courseId` and ensure it corresponds to an existing course.
  - Call service function to assign the teacher to the course.
  - Return success message or appropriate error responses.
- [ ] **Task 3 Completed**

### Task 4: Add API Endpoint for Retrieving Course Details
- **File**: `src/api.py`
- **Description**: Create endpoint for `GET /courses/{courseId}` to retrieve course details including assigned teacher.
- **Subtasks**:
  - Implement endpoint handler to fetch course data.
  - Include assigned teacher information in the response.
  - Validate `courseId` and return 404 if course does not exist.
- [ ] **Task 4 Completed**

### Task 5: Implement Service Functions
- **File**: `src/services.py`
- **Description**: Create functions for business logic related to course-teacher assignments.
- **Subtasks**:
  - Implement `assign_teacher_to_course(course_id: int, teacher_id: int)`.
  - Implement `get_course_details(course_id: int)` and ensure it fetches the teacher info.
- [ ] **Task 5 Completed**

### Task 6: Create Unit Tests for New API Functionality
- **File**: `tests/test_courses.py`
- **Description**: Write tests for the new functionality.
- **Subtasks**:
  - Test PATCH request for assigning a teacher to a course with valid and invalid inputs.
  - Test GET request for retrieving course details with and without assigned teacher.
  - Ensure all tests cover expected error cases (404 and 400 statuses).
- [ ] **Task 6 Completed**

### Task 7: Documentation Update
- **File**: `README.md`
- **Description**: Update the documentation to include new API endpoints.
- **Subtasks**:
  - Detail the request and response formats for the new endpoints.
  - Provide usage instructions for assigning teachers and retrieving course details.
- [ ] **Task 7 Completed**

### Task 8: Review and Testing
- **File**: `src` and `tests/`
- **Description**: Review all implemented code and run tests to ensure functionality.
- **Subtasks**:
  - Verify that all tests pass.
  - Ensure that the application starts successfully without errors.
  - Conduct a code review for best practices adherence.
- [ ] **Task 8 Completed**

---

This structured task breakdown ensures that all necessary modifications and integrations are addressed systematically while maintaining compliance with the existing codebase and best practices.