# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models.py` (2250 bytes)
- `src/routes.py` (3100 bytes)
- `src/schemas.py` (1500 bytes)
- `src/db.py` (900 bytes)
- `tests/test_routes.py` (2958 bytes)
- `tests/test_models.py` (1819 bytes)

---

## Task Breakdown

### Task 1: Update Course Model to Include `teacher_id`
- **File**: `src/models.py`
- **Description**: Modify the Course model to include a foreign key `teacher_id` referencing the Teacher entity.
- **Dependencies**: None
- [ ] Update Course class to add `teacher_id` field with a foreign key constraint.

### Task 2: Create Marshmallow Schema for Course Update
- **File**: `src/schemas.py`
- **Description**: Define a Marshmallow schema to validate incoming requests that assign a teacher to a course.
- **Dependencies**: Task 1
- [ ] Create `CourseAssignmentSchema` to validate `teacher_id` input upon course updates.

### Task 3: Create API Route for Assigning Teacher to Course
- **File**: `src/routes.py`
- **Description**: Implement the `PUT /courses/{course_id}/assign-teacher` endpoint for assigning a teacher to a course.
- **Dependencies**: Task 2
- [ ] Define a route and controller method to handle teacher assignments to courses.

### Task 4: Implement Course Retrieval with Teacher Information
- **File**: `src/routes.py`
- **Description**: Implement the `GET /courses/{course_id}` endpoint to retrieve course details, including the assigned teacher.
- **Dependencies**: Task 1
- [ ] Extend the existing course retrieval route to include teacher details in the response.

### Task 5: Update Database Initialization Logic for Migrations
- **File**: `src/db.py`
- **Description**: Add logic to perform database migrations that alter the Course table to include the `teacher_id` field.
- **Dependencies**: Task 1
- [ ] Implement the SQL command to alter the Course table and ensure migration integrity.

### Task 6: Create Unit Tests for Teacher Assignment Logic
- **File**: `tests/test_routes.py`
- **Description**: Implement unit tests for the new API endpoints to ensure they function correctly.
- **Dependencies**: Task 3, Task 4
- [ ] Write tests for assigning a teacher to a course with valid and invalid inputs.

### Task 7: Create Unit Tests for Course Retrieval Logic
- **File**: `tests/test_routes.py`
- **Description**: Implement tests to verify that course retrieval correctly includes teacher information.
- **Dependencies**: Task 4
- [ ] Write tests to confirm correct course details are returned along with teacher information.

### Task 8: Document the New Endpoints in README
- **File**: `README.md`
- **Description**: Update the documentation to include new endpoints for assigning teachers and retrieving course details.
- **Dependencies**: Task 3, Task 4
- [ ] Add detailed descriptions of the new API functionality to the README file.

### Task 9: Validate Error Handling for Invalid Associations
- **File**: `src/routes.py`
- **Description**: Ensure error handling is present for invalid teacher or course IDs during the assignment process.
- **Dependencies**: Task 3, Task 2
- [ ] Implement error messages and response codes for non-existent course or teacher scenarios.

### Task 10: Deploy and Migrate the Database
- **File**: `src/db.py`
- **Description**: Execute the migration script to update the database schema with the `teacher_id` field.
- **Dependencies**: Task 5
- [ ] Verify the migration maintains existing data integrity while successfully modifying the Course table.

---

Each task is designed to be small, focused, and independently testable while adhering to the project's incremental development context.