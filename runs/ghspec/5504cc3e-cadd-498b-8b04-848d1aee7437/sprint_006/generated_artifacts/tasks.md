# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models/course.py` (326 bytes)
- `src/models/teacher.py` (480 bytes)
- `src/api/courses.py` (2100 bytes)
- `README.md` (1200 bytes)

---

### Task 1: Database Migration Script
- **File Path**: `migrations/versions/20230101_add_teacher_id_to_courses.py`
- **Description**: Create a migration script using Alembic to add a `teacher_id` foreign key to the `courses` table while preserving existing course data.
- [ ] Create migration script and define the `upgrade` and `downgrade` functions.

### Task 2: Update Course Model
- **File Path**: `src/models/course.py`
- **Description**: Modify the `Course` model to include the `teacher_id` field and establish relationship with the `Teacher` model.
- [ ] Add `teacher_id` field definition to `Course`.
- [ ] Establish a relationship to `Teacher` in the Course model.

### Task 3: Update Teacher Model
- **File Path**: `src/models/teacher.py`
- **Description**: Update the `Teacher` model to establish a back-reference to the `Course` model.
- [ ] Add the relationship in the `Teacher` model defining `courses`.

### Task 4: Create Course API for Assigning Teacher
- **File Path**: `src/api/courses.py`
- **Description**: Implement the POST endpoint `/api/v1/courses/<course_id>/assign_teacher` to assign a teacher to a specific course.
- [ ] Define the endpoint and ensure it handles the request payload correctly.
- [ ] Implement response structure as mentioned in the specification.

### Task 5: Create Course API for Retrieving Course Details
- **File Path**: `src/api/courses.py`
- **Description**: Implement the GET endpoint `/api/v1/courses/<course_id>` to retrieve course details along with the assigned teacher's name.
- [ ] Define the endpoint to retrieve the course details.
- [ ] Ensure the response structure includes the teacher's information.

### Task 6: Implement Course Service Logic
- **File Path**: `src/services/course_service.py`
- **Description**: Develop the logic to handle operations for assigning teachers to courses and retrieving course details.
- [ ] Write `assign_teacher_to_course(course_id, teacher_id)` method.
- [ ] Write `get_course_with_teacher(course_id)` method.

### Task 7: Add Input Validation for API
- **File Path**: `src/validation/course_validation.py`
- **Description**: Create validation functions to check the integrity of IDs from API requests.
- [ ] Implement validation logic for Course ID and Teacher ID.

### Task 8: Unit Tests for Service Logic
- **File Path**: `tests/unit/test_course_service.py`
- **Description**: Write unit tests to verify service functions for assigning teachers and retrieving courses.
- [ ] Create tests for `assign_teacher_to_course` function.
- [ ] Create tests for `get_course_with_teacher` function.

### Task 9: Integration Tests for API Endpoints
- **File Path**: `tests/integration/test_course_api.py`
- **Description**: Write integration tests for the new API endpoints to ensure proper functionality.
- [ ] Create tests for the course assignment API endpoint.
- [ ] Create tests for the course details retrieval API endpoint.

### Task 10: Update Documentation
- **File Path**: `README.md`
- **Description**: Update the README file to include new API details, including usage examples for assigning teachers and retrieving course details.
- [ ] Document the new API endpoints with request/response examples.

---

This structured task breakdown will guide the implementation of the teacher-course relationship efficiently while maintaining existing code integrity and ensuring thorough testing for quality assurance.