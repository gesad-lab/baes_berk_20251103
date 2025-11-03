# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- api/courses.py (initial setup for the courses API)
- db/models.py (administrative models including Course)
- tests/test_courses.py (initial test setup for courses)

---

## Task Breakdown

### Task 1: Update Course Model
- **File Path**: `db/models.py`
- **Description**: Modify the `Course` model to add a `teacher_id` foreign key that references the `Teacher` entity.
- **Checklist**:
  - [ ] Add a `teacher_id` column to the `Course` model with proper foreign key validation.

### Task 2: Create Migration Script
- **File Path**: `db/migrations/2023_add_teacher_relationship.py`
- **Description**: Create and define the migration script to add the `teacher_id` column to the `courses` table without disrupting existing data.
- **Checklist**:
  - [ ] Write `upgrade()` function to add `teacher_id`.
  - [ ] Write `downgrade()` function to remove `teacher_id`.

### Task 3: Implement PATCH API Endpoint
- **File Path**: `api/courses.py`
- **Description**: Define the PATCH endpoint for `/courses/{course_id}` to associate a teacher with a course.
- **Checklist**:
  - [ ] Create endpoint to accept `teacher_id` and return success message.
  - [ ] Implement input validation for `course_id` and `teacher_id`.

### Task 4: Implement GET API Endpoint
- **File Path**: `api/courses.py`
- **Description**: Define the GET endpoint for `/courses/{course_id}` to retrieve course details including associated teacher.
- **Checklist**:
  - [ ] Create endpoint to return course details including `teacher_id`.

### Task 5: Business Logic for Teacher Association
- **File Path**: `services/course_service.py`
- **Description**: Implement the business logic for associating a teacher with a course.
- **Checklist**:
  - [ ] Create a function `associate_teacher(course_id, teacher_id)` to update course with teacher.
  - [ ] Create a function `get_course_details(course_id)` to retrieve course details.

### Task 6: Write Unit Tests for Business Logic
- **File Path**: `tests/test_courses.py`
- **Description**: Write unit tests to validate the business logic methods in `course_service.py`.
- **Checklist**:
  - [ ] Write tests for successful and unsuccessful teacher associations.
  - [ ] Include tests for retrieving course details.

### Task 7: Write Integration Tests for API Endpoints
- **File Path**: `tests/test_courses_api.py`
- **Description**: Write integration tests for the new PATCH and GET API endpoints.
- **Checklist**:
  - [ ] Test successful teacher association with PATCH.
  - [ ] Test retrieval of course details with GET.
  - [ ] Test handling of invalid `teacher_id`.

### Task 8: Update Requirements File
- **File Path**: `requirements.txt`
- **Description**: Ensure that all relevant packages are included in the requirements file.
- **Checklist**:
  - [ ] Check and update the requirements for database migration dependencies if necessary.

### Task 9: Validate Input Data
- **File Path**: `api/courses.py`
- **Description**: Implement input validation for `course_id` and `teacher_id`.
- **Checklist**:
  - [ ] Validate that `teacher_id` exists before attempting an association.
  - [ ] Validate that `course_id` corresponds to an existing course.

### Task 10: Documentation Update
- **File Path**: `README.md`
- **Description**: Update the project documentation to reflect the new API endpoints and usage instructions.
- **Checklist**:
  - [ ] Document new PATCH and GET endpoints with request and response examples.

---

By following this structured task breakdown, the development team can implement the teacher relationship feature systematically, ensuring every part of the requirement is met while maintaining code quality and testing coverage. Each of these tasks can be executed independently and are designed to be made testable on their own, aligning with the project's coding standards.