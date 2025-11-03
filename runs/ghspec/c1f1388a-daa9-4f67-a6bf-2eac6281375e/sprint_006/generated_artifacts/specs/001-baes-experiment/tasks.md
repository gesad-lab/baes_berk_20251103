# Tasks: Add Teacher Relationship to Course Entity

---

## Task 1: Modify Course Model to Include `teacher_id`

- **File Path**: `src/models/course.py`
- **Description**: Add a new attribute `teacher_id` to the Course model, which serves as a foreign key reference to the Teacher model.
- **Type**: Model update
- **Dependencies**: None
- [ ] Implement the `teacher_id` column as a foreign key in the Course model.

---

## Task 2: Create Teacher Model

- **File Path**: `src/models/teacher.py`
- **Description**: Define the Teacher model to establish the schema for storing teacher information.
- **Type**: New model creation
- **Dependencies**: None
- [ ] Implement the Teacher class with appropriate attributes and relationships.

---

## Task 3: Update Course Schema to Include `teacher_id`

- **File Path**: `src/schemas/course.py`
- **Description**: Modify the Course Pydantic schema to include the `teacher_id` field for validation purposes.
- **Type**: Schema update
- **Dependencies**: Task 1
- [ ] Add `teacher_id` to the Course schema.

---

## Task 4: Create Teacher Schema

- **File Path**: `src/schemas/teacher.py`
- **Description**: Define the Pydantic schema for the Teacher entity to validate incoming and outgoing data.
- **Type**: New schema creation
- **Dependencies**: None
- [ ] Implement the Teacher schema.

---

## Task 5: Update Database Initialization for Foreign Key Relationships

- **File Path**: `src/db/database.py`
- **Description**: Ensure the database setup facilitates the foreign key relationship between the Course and Teacher tables.
- **Type**: Database setup update
- **Dependencies**: Task 1
- [ ] Update the necessary database init configurations to handle foreign key relationships.

---

## Task 6: Create API Endpoint for Assigning Teacher to Course

- **File Path**: `src/api/course_routes.py`
- **Description**: Implement the POST endpoint `/courses/{course_id}/assign_teacher` to assign a teacher to a course.
- **Type**: API route creation
- **Dependencies**: Task 3, Task 4
- [ ] Implement the route and the related logic for assigning a teacher to a course.

---

## Task 7: Create API Endpoint for Retrieving Courses by Teacher

- **File Path**: `src/api/course_routes.py`
- **Description**: Implement the GET endpoint `/teachers/{teacher_id}/courses` to retrieve all courses taught by a specific teacher.
- **Type**: API route creation
- **Dependencies**: Task 4
- [ ] Implement the route and the logic to return courses for a specific teacher.

---

## Task 8: Create Database Migration for Adding `teacher_id`

- **File Path**: `src/db/migrations/`
- **Description**: Utilize Alembic to create a migration script that adds the `teacher_id` column to the courses table.
- **Type**: Migration
- **Dependencies**: Task 1
- [ ] Generate and write the migration script to add the `teacher_id` column.

---

## Task 9: Write Unit Tests for Teacher Assignment Endpoint

- **File Path**: `tests/test_course.py`
- **Description**: Develop unit tests for the new API endpoint that assigns a teacher to a course.
- **Type**: Test creation
- **Dependencies**: Task 6
- [ ] Implement tests to ensure proper assignment of teachers to courses.

---

## Task 10: Write Unit Tests for Retrieving Courses by Teacher

- **File Path**: `tests/test_course.py`
- **Description**: Develop unit tests for the new API endpoint that retrieves all courses for a specific teacher.
- **Type**: Test creation
- **Dependencies**: Task 7
- [ ] Implement tests to verify the retrieval of courses assigned to a teacher.

---

## Task 11: Implement Error Handling for Invalid Teacher IDs

- **File Path**: `src/api/course_routes.py`
- **Description**: Ensure that the API correctly handles cases where an invalid teacher ID is provided during assignment requests.
- **Type**: Error handling
- **Dependencies**: Task 6
- [ ] Implement error responses for invalid inputs during the teacher assignment.

---

## Task 12: Update Documentation and OpenAPI Specifications

- **File Path**: `README.md` and OpenAPI documentation
- **Description**: Revise project documentation to include details about the new functionality regarding teacher-course relationships.
- **Type**: Documentation update
- **Dependencies**: Task 6, Task 7
- [ ] Update the README and OpenAPI docs for the new endpoints.

---

## Task 13: Ensure Migration Scripts are Tracked in Version Control

- **File Path**: `src/db/migrations/`
- **Description**: Confirm that the generated migration scripts are properly committed to version control for future reference and deployment.
- **Type**: Version control check
- **Dependencies**: Task 8
- [ ] Add migration scripts to the Git repository.

---

This breakdown provides a clear and actionable set of tasks to implement the teacher relationship within the course entity in an organized manner, prioritizing dependencies and keeping in line with the project specifications.