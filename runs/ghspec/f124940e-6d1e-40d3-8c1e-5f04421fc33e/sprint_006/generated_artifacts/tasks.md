# Tasks: Add Teacher Relationship to Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `models.py` (for Course model updates)
- `routers/courses_router.py` (to implement new API routes)
- `tests/test_courses.py` (to add tests for new functionalities)

---

## Tasks Breakdown

### Task 1: Update Course Model
- **File**: `src/models.py`
  - [ ] Modify the `Course` model to include the new `teacher_id` field as a Foreign Key referencing the `Teacher` entity.

### Task 2: Create Migration Script
- **File**: `migrations/versions/add_teacher_id_to_courses.py` (new file)
  - [ ] Create a migration script using Alembic to add the `teacher_id` field to the `courses` table. Ensure the migration is reversible.

### Task 3: Implement Assign Teacher API Endpoint
- **File**: `src/routers/courses_router.py`
  - [ ] Implement the `POST /courses/{course_id}/assign_teacher` endpoint to assign a teacher to a course. Ensure validation for existing teacher_id and return appropriate responses.

### Task 4: Implement Retrieve Course API Endpoint
- **File**: `src/routers/courses_router.py`
  - [ ] Implement the `GET /courses/{course_id}` endpoint to retrieve course details including the assigned teacher information.

### Task 5: Implement Unassign Teacher API Endpoint
- **File**: `src/routers/courses_router.py`
  - [ ] Implement the `DELETE /courses/{course_id}/unassign_teacher` endpoint to unassign a teacher from a course and return the updated course details.

### Task 6: Input Validation for Teacher Assignment
- **File**: `src/routers/courses_router.py`
  - [ ] Add validation to ensure `teacher_id` exists before assignment. Handle invalid assignments returning the appropriate error message.

### Task 7: Write Unit Tests for Assign Teacher Functionality
- **File**: `tests/test_courses.py`
  - [ ] Write tests for the `assign_teacher` API endpoint covering valid and invalid scenarios.

### Task 8: Write Unit Tests for Retrieve Course Functionality
- **File**: `tests/test_courses.py`
  - [ ] Write tests for the `get_course` API endpoint ensuring that the retrieved course includes the assigned teacher details.

### Task 9: Write Unit Tests for Unassign Teacher Functionality
- **File**: `tests/test_courses.py`
  - [ ] Write tests for the `unassign_teacher` API endpoint ensuring that the teacher is successfully removed from the course.

### Task 10: Write Unit Tests for Handling Invalid Teacher Assignments
- **File**: `tests/test_courses.py`
  - [ ] Write tests to validate that requests with nonexistent `teacher_id` return an appropriate 400 Bad Request response.

### Task 11: Documentation Update for New API Endpoints
- **File**: `docs/api_specification.md` (or relevant documentation file)
  - [ ] Update the API documentation to include the new endpoints, request formats, and response formats.

### Task 12: Ensure OpenAPI Documentation is Generated
- **File**: `src/main.py`
  - [ ] Verify that new endpoints are included in the automatically generated OpenAPI documentation by FastAPI.

### Task 13: Deployment Configuration Check
- **File**: `Dockerfile` or relevant deployment files
  - [ ] Review docker configurations to ensure compatibility with new features and APIs.

### Task 14: Assure Test Coverage Requirements are Met
- **File**: `tests/test_courses.py`
  - [ ] Run tests to confirm that test coverage meets the minimum requirement of 70% for the new feature's business logic.

--- 

This task breakdown delineates actions needed to implement the teacher relationship within the course entity, ensuring that required modifications to existing files and new implementations adhere to the project constitution and are adequately tested.