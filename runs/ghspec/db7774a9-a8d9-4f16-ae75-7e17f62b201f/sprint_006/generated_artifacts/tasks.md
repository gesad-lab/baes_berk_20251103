# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_teacher.py` (2483 bytes)

Instructions for Task Breakdown:
1. Identify which existing files need modifications
2. Create new files for new functionality
3. Ensure integration tasks are included
4. Maintain consistency with existing code style and patterns

---

## Task List

### Database Schema Update
- [ ] **Task**: Modify `Course` model to add `teacher_id` field and relationship.
  - **File**: `src/models/course.py`
  - **Description**: Update the `Course` class to include the `teacher_id` foreign key and the relationship with the `Teacher` entity.

### Pydantic Schema Update
- [ ] **Task**: Update Pydantic models for course validation and response.
  - **File**: `src/schemas/course.py`
  - **Description**: Modify the existing `CourseResponse` model to include `teacher_id` and `teacher_name` for structured responses.

### API Endpoints Implementation
- [ ] **Task**: Implement the PATCH endpoint for assigning a teacher to a course.
  - **File**: `src/routes/course_routes.py`
  - **Description**: Add a new route to handle `PATCH /courses/{id}` requests, updating the course with a teacher assignment.

- [ ] **Task**: Implement the GET endpoint for retrieving course information.
  - **File**: `src/routes/course_routes.py`
  - **Description**: Ensure the existing route for `GET /courses/{id}` returns teacher information alongside course details.

- [ ] **Task**: Implement the GET endpoint for listing all courses with their teachers.
  - **File**: `src/routes/course_routes.py`
  - **Description**: Modify the existing route for `GET /courses` to include teacher names in the response.

### Error Handling Implementation
- [ ] **Task**: Implement validation for `teacher_id` to ensure it references an existing teacher.
  - **File**: `src/services/course_service.py`
  - **Description**: Update service logic to validate the `teacher_id` during course updates and return appropriate error messages for invalid IDs.

### Testing Updates
- [ ] **Task**: Update tests to validate course-teacher assignment functionality.
  - **File**: `tests/test_course.py`
  - **Description**: Create/modify tests to cover assigning teachers to courses, retrieving course information including teachers, and error handling for invalid teacher assignments.

### Documentation Updates
- [ ] **Task**: Update the README.md to include new API endpoints and usage examples.
  - **File**: `README.md`
  - **Description**: Document the new feature, API contracts, and include examples for the endpoints that were added/modified.

- [ ] **Task**: Update inline comments and code documentation for modified files.
  - **Files**: 
    - `src/models/course.py`
    - `src/schemas/course.py`
    - `src/routes/course_routes.py`
  - **Description**: Ensure all changes are properly documented with comments explaining the new functionality and code structure.

---

By completing these tasks, the new `Teacher` relationship within the `Course` entity will be successfully implemented, enhancing the authority and management capabilities of the educational database. Each task is designed to be independently testable, ensuring that no existing functionality is broken during the integration.