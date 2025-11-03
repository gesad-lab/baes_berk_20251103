# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_teacher.py` (2374 bytes)
- `tests/test_student_course.py` (2720 bytes)

---

### Task List

- [ ] **Create Migration Script for Teacher Relationship**
  - **File**: `src/database/migrations/20231014_add_teacher_to_course.py`
  - **Description**: Create a migration script that adds a `teacher_id` column to the `courses` table as a foreign key referencing `teachers.id`.
  
- [ ] **Update Course Model**
  - **File**: `src/models/course.py`
  - **Description**: Modify the `Course` model to include the new `teacher_id` foreign key and relationship with the `Teacher` model.

- [ ] **Update Course Schema**
  - **File**: `src/schemas/course_schema.py`
  - **Description**: Extend `CourseUpdate` and `CourseResponse` schemas to incorporate `teacher_id`.

- [ ] **Implement PUT Endpoint for Assigning Teacher to Course**
  - **File**: `src/routes/course_routes.py`
  - **Description**: Create a route to handle PUT requests for assigning a teacher to a course using `teacher_id`. Validate the request with the updated schemas.

- [ ] **Implement GET Endpoint for Course Retrieval**
  - **File**: `src/routes/course_routes.py`
  - **Description**: Update the GET route to return Course details including the associated Teacher information.

- [ ] **Create Unit Tests for Teacher Assignment**
  - **File**: `tests/test_course.py`
  - **Description**: Add test cases for both the PUT endpoint for assigning a teacher and the validation for required fields. Ensure scenarios for successful assignments and error handling are covered.

- [ ] **Create Unit Tests for Course Retrieval with Teacher**
  - **File**: `tests/test_course.py`
  - **Description**: Add test cases for the GET endpoint ensuring it returns the appropriate Course details with Teacher information.

- [ ] **Update Documentation for New Endpoints**
  - **File**: `src/main.py`
  - **Description**: Ensure that FastAPI documentation is updated to reflect the new endpoints and expected behaviors, including the correct format of request and response bodies.

- [ ] **Run Migrations and Verify Data Integrity**
  - **File**: N/A
  - **Description**: Execute the migration in the database, ensuring that existing records remain intact and can be retrieved accurately after the update.

- [ ] **Conduct Integration Testing**
  - **File**: N/A
  - **Description**: Manually test or automate integration tests for the entire workflow of assigning a teacher to a course and retrieving course details including teacher assignment.

---
### Dependencies

Ensure that the tasks are completed in the following order:
1. Create Migration Script for Teacher Relationship
2. Update Course Model
3. Update Course Schema
4. Implement PUT Endpoint for Assigning Teacher to Course
5. Implement GET Endpoint for Course Retrieval
6. Create Unit Tests for Teacher Assignment
7. Create Unit Tests for Course Retrieval with Teacher
8. Update Documentation for New Endpoints
9. Run Migrations and Verify Data Integrity
10. Conduct Integration Testing

This task breakdown focuses on maintaining consistency with existing code styles and patterns, ensuring independent testability for each task, and addressing all aspects outlined in the implementation plan.