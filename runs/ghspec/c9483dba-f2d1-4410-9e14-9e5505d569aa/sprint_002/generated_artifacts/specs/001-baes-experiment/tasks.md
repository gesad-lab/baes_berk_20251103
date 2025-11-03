# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models.py`
- `src/controllers/student_controller.py`
- `src/app.py`
- `tests/test_app.py`

Instructions for Task Breakdown:
1. Identify which existing files need modifications.
2. Create new files for new functionality.
3. Ensure integration tasks are included.
4. Maintain consistency with existing code style and patterns.

---

## Task List

### Task 1: Update Student Model to Include Email Field
- **File Path**: `src/models.py`
- **Description**: Modify the existing `Student` class to add the `email` attribute as a non-nullable and unique field.
- [ ] Modify the `Student` class definition to include `email` field in the database model.

### Task 2: Create Database Migration for Email Field
- **File Path**: (Migration file auto-generated)
- **Description**: Generate and apply a migration script that adds the `email` field to the existing Student table while preserving data.
- [ ] Run `flask db migrate -m "Add email field to Student model"` to generate the migration script.
- [ ] Run `flask db upgrade` to apply the migration to the database.

### Task 3: Define Create Student Endpoint
- **File Path**: `src/app.py`
- **Description**: Add a new route for creating a Student via `POST /students` and ensure it calls the appropriate controller function.
- [ ] Define the endpoint and link it to the create student controller function.

### Task 4: Implement Create Student Logic
- **File Path**: `src/controllers/student_controller.py`
- **Description**: Implement the logic for creating a new Student, including validation checks for `name` and `email`.
- [ ] Create a function `create_student()` to handle incoming requests, validate input, and save the new Student record.

### Task 5: Define Retrieve Student Endpoint
- **File Path**: `src/app.py`
- **Description**: Add a new route for retrieving a Student via `GET /students/{id}` and ensure it routes to the correct controller function.
- [ ] Define the endpoint and link it to the retrieve student controller function.

### Task 6: Implement Retrieve Student Logic
- **File Path**: `src/controllers/student_controller.py`
- **Description**: Implement the logic for retrieving a Student by ID including handling cases where the student does not exist.
- [ ] Create a function `retrieve_student(id)` to fetch student details and return them in the expected JSON format.

### Task 7: Implement Input Validation for Create Student
- **File Path**: `src/controllers/student_controller.py`
- **Description**: Incorporate Marshmallow for input validation to ensure `name` and `email` are provided and formatted correctly.
- [ ] Set up Marshmallow schemas for input validation to enforce required fields.

### Task 8: Implement Error Handling
- **File Path**: `src/controllers/student_controller.py`
- **Description**: Add error handling to return appropriate error messages and codes for missing fields or non-existent students.
- [ ] Implement try-except blocks and format responses according to the specified error response structure.

### Task 9: Update Unit Tests for Create Student Feature
- **File Path**: `tests/test_app.py`
- **Description**: Add unit tests for creating Students to verify both success and failure cases (e.g., missing fields).
- [ ] Write tests to cover scenarios: success, missing name, missing email, and duplicate email.

### Task 10: Update Unit Tests for Retrieve Student Feature
- **File Path**: `tests/test_app.py`
- **Description**: Add unit tests for retrieving Students by ID, ensuring proper response for existing and non-existing students.
- [ ] Write tests to cover scenarios: successful retrieval, non-existent student ID.

### Task 11: Documentation Update for API Changes
- **File Path**: `README.md`
- **Description**: Update the API documentation to reflect the new endpoints for creating and retrieving Students with email fields.
- [ ] Document the request and response formats for both `POST /students` and `GET /students/{id}`.

---

This breakdown ensures that each task is focused on a specific file and responsibility, and all tasks can be executed and tested independently.