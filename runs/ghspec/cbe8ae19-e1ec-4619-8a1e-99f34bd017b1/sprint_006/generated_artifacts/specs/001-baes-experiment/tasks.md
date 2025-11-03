# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `models/course.py` (345 bytes)
- `api.py` (953 bytes)
- `services/course_service.py` (512 bytes)
- `tests/test_course_service.py` (1200 bytes)
- `tests/test_api.py` (2343 bytes)

---

## Task Breakdown

### 1. Update Course Data Model

- [ ] **Task**: Modify Course model to include teacher_id
  - **File Path**: `models/course.py`
  - **Details**: Update the `Course` class to add a new column `teacher_id` as a foreign key referencing the `Teacher` entity.

### 2. Implement Database Migration

- [ ] **Task**: Create migration script to add teacher_id to courses
  - **File Path**: `migrations/20231025_add_teacher_id_to_courses.py`
  - **Details**: Write migration script that adds the `teacher_id` column to the `courses` table and sets up the foreign key relationship.

### 3. Implement Service Layer Logic

- [ ] **Task**: Define function to assign a teacher to a course
  - **File Path**: `services/course_service.py`
  - **Details**: Implement a function `assign_teacher_to_course(course_id, teacher_id)` which includes validation checks.

- [ ] **Task**: Define function to retrieve course details with teacher info
  - **File Path**: `services/course_service.py`
  - **Details**: Implement a function `get_course_details(course_id)` to fetch the course and associated teacher information.

### 4. Build API Layer Endpoints

- [ ] **Task**: Create endpoint to assign teacher to course
  - **File Path**: `api.py`
  - **Details**: Add a new POST endpoint `/api/v1/courses/{course_id}/assign_teacher/{teacher_id}` for handling teacher assignments.

- [ ] **Task**: Create endpoint to retrieve course details
  - **File Path**: `api.py`
  - **Details**: Add a new GET endpoint `/api/v1/courses/{course_id}` to retrieve course details, including the assigned teacher.

### 5. Write Unit Tests for Service Layer

- [ ] **Task**: Create unit tests for the course-service functions
  - **File Path**: `tests/test_course_service.py`
  - **Details**: Write tests for functions handling teacher assignments and course details retrieval.

### 6. Write Integration Tests for API Layer

- [ ] **Task**: Create integration tests for new API endpoints
  - **File Path**: `tests/test_api.py`
  - **Details**: Add tests for the new endpoints related to teacher assignment and course retrieval.

### 7. Document API Usage

- [ ] **Task**: Update README with new API endpoints
  - **File Path**: `README.md`
  - **Details**: Provide documentation on the new functionalities, detailing the requests and responses for the updated API endpoints.

### 8. Implement Input Validation

- [ ] **Task**: Add input validation for course and teacher IDs in API
  - **File Path**: `api.py`
  - **Details**: Ensure that the API checks for valid course or teacher IDs before processing requests.

---

### Completion Criteria

- All mentioned tasks must be completed, ensuring existing functionality is unaffected and new features are properly integrated and tested.
- The new teacher-course relationship functionality must be verifiable through unit tests and integration tests.
- Documentation must be updated to reflect changes in the API.

--- 

This task breakdown provides a clear set of actionable items that align with the implementation plan for adding a teacher relationship to the course entity. Each task focuses on a single file, ensuring ease of testing and implementation.