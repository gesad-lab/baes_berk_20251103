# Tasks: Add Teacher Relationship to Course Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models/course.py`
- `src/models/teacher.py`
- `src/controllers/course_controller.py`
- `src/routes/app_routes.py`
- `tests/test_teacher.py`

---

### Task 1: Update Course Model to Include Teacher Relationship
- **File**: `src/models/course.py`
- **Description**: Modify the `Course` class to include `teacher_id` as a foreign key.
- **Dependencies**: None
- **Testability**: Validate that the `Course` object can be instantiated with a `teacher_id`.
- [ ] Implement the `teacher_id` field in the `Course` model.

### Task 2: Update Teacher Model for Bidirectional Relationship
- **File**: `src/models/teacher.py`
- **Description**: Ensure the `Teacher` model has a relationship back to the `Course`.
- **Dependencies**: Task 1
- **Testability**: Confirm that a `Teacher` object can access its `courses`.
- [ ] Implement a relationship in the `Teacher` model pointing to the `Course`.

### Task 3: Create Migration Script for Database Update
- **File**: `migrations/versions/` (directory to contain migration scripts)
- **Description**: Use Alembic to create a migration script that adds the `teacher_id` column to the `Courses` table.
- **Dependencies**: Task 1
- **Testability**: Run the migration and verify that `teacher_id` field exists without loss of data.
- [ ] Generate and test migration script.

### Task 4: Update Routes for Assigning Teacher to Course
- **File**: `src/routes/app_routes.py`
- **Description**: Create a new route `PATCH /courses/{course_id}/assign-teacher` to assign a teacher to a course.
- **Dependencies**: Task 1, Task 3
- **Testability**: Ensure route accepts requests and correctly processes updates.
- [ ] Define the routing logic for assigning a teacher.

### Task 5: Implement Controller Logic for Teacher Assignment
- **File**: `src/controllers/course_controller.py`
- **Description**: Implement the business logic for handling the assignment of a teacher to a course.
- **Dependencies**: Task 4
- **Testability**: Validate that the correct responses (success/error messages) are returned based on the request.
- [ ] Handle teacher assignments in controller.

### Task 6: Update Controller Error Handling & Validation
- **File**: `src/controllers/course_controller.py` (cont.)
- **Description**: Introduce input validation for `teacher_id` and error handling for non-existing teachers.
- **Dependencies**: Task 5
- **Testability**: Ensure correct error messages are returned for invalid requests.
- [ ] Implement validation logic in the controller.

### Task 7: Create Endpoint for Retrieving Courses by Teacher
- **File**: `src/routes/app_routes.py`
- **Description**: Define a new `GET /teachers/{teacher_id}/courses` endpoint.
- **Dependencies**: Task 1
- **Testability**: Ensure that given a valid teacher ID, the endpoint retrieves the associated courses.
- [ ] Add route for retrieving courses for a specific teacher.

### Task 8: Implement Logic for Retrieving Courses in Controller
- **File**: `src/controllers/course_controller.py`
- **Description**: Develop logic to fetch all courses associated with a given teacher in the controller.
- **Dependencies**: Task 7
- **Testability**: Validate that retrieving courses correctly corresponds to teacher IDs.
- [ ] Handle fetching of courses in the controller.

### Task 9: Write Unit Tests for Teacher Assignment
- **File**: `tests/test_teacher.py`
- **Description**: Write unit tests for the endpoint that assigns a teacher to a course.
- **Dependencies**: Task 5
- **Testability**: Confirm that tests validate both the success response and error cases.
- [ ] Implement tests for teacher assignment.

### Task 10: Write Unit Tests for Course Retrieval by Teacher
- **File**: `tests/test_teacher.py` (cont.)
- **Description**: Write unit tests for the endpoint that retrieves courses by teacher ID.
- **Dependencies**: Task 8
- **Testability**: Ensure that these tests validate the response structure and content.
- [ ] Implement tests for course retrieval.

### Task 11: Document Changes in README.md
- **File**: `README.md`
- **Description**: Update the documentation to include new API endpoints, usage details, and environment setup.
- **Dependencies**: All other tasks
- **Testability**: Review documentation for clarity and accuracy.
- [ ] Update README with new features and endpoint descriptions.

### Task 12: Execute Database Migrations
- **File**: N/A (Command Line Task)
- **Description**: Run the Alembic migration to apply schema changes.
- **Dependencies**: Task 3
- **Testability**: Verify that migrations run without errors and the schema reflects changes.
- [ ] Execute migration command.

### Task 13: Validate and Clean Up Codebase
- **File**: All modified files
- **Description**: Perform code review and clean-up to adhere to coding standards.
- **Dependencies**: All tasks
- **Testability**: Ensure that the code meets the readability and documentation standards defined in the project constitution.
- [ ] Review and refactor code as necessary.

---

The tasks outlined above are divided into clear responsibilities, ensuring each implementation aspect of adding the teacher relationship to the course entity is manageable, testable, and adheres to the coding standards established by the project constitution.