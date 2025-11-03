# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models/student.py`
- `src/controllers/student_controller.py`
- `src/validation/student_validation.py`
- `migrations/versions/...` (Migration scripts)
- `README.md`

---

## Task List

### 1. Update Student Model
- **Task**: Modify the `Student` model to include the email field.
  - **File**: `src/models/student.py`
  - **Description**: Add the `email` attribute to the `Student` class; ensure it is marked as required (non-nullable).
  - **Dependencies**: None.
  - [ ] Update the `Student` schema in `student.py`.

### 2. Create Database Migration
- **Task**: Generate a migration script to add the email column to the existing Student table in the database.
  - **File**: `migrations/versions/add_email_to_students.py`
  - **Description**: Implement the migration to add the new email field to the `students` table.
  - **Dependencies**: Task 1 must be completed first.
  - [ ] Create migration script to add email field without data loss.

### 3. Update API Controller for Student Creation
- **Task**: Modify the `student_controller` to handle email during student creation.
  - **File**: `src/controllers/student_controller.py`
  - **Description**: Update the `POST /students` endpoint to accept email and return it in the response.
  - **Dependencies**: Task 1 must be completed first.
  - [ ] Update `POST /students` route to include email in creation.

### 4. Update API Controller for Student Retrieval
- **Task**: Change the student retrieval API to return the email field.
  - **File**: `src/controllers/student_controller.py`
  - **Description**: Modify the `GET /students/<id>` endpoint to include email in the returned JSON response.
  - **Dependencies**: Task 1 must be completed first.
  - [ ] Update `GET /students/<id>` to return email in the response.

### 5. Implement Email Validation Logic
- **Task**: Enhance the validation logic to include required and format validation for the email field.
  - **File**: `src/validation/student_validation.py`
  - **Description**: Update `validate_student_data` to ensure the email is present and valid.
  - **Dependencies**: None.
  - [ ] Add email validation to `validate_student_data`.

### 6. Update Unit Tests for Model
- **Task**: Create/Update unit tests for the `Student` model to validate email handling.
  - **File**: `tests/models/test_student.py`
  - **Description**: Implement tests to verify email field behaves as expected (creation, retrieval).
  - **Dependencies**: Task 1 must be completed first.
  - [ ] Add unit tests for email field in `test_student.py`.

### 7. Update Unit Tests for Validation
- **Task**: Create/Update unit tests for the email validation to ensure it handles various scenarios.
  - **File**: `tests/validation/test_student_validation.py`
  - **Description**: Implement tests covering valid and invalid email cases, including missing email.
  - **Dependencies**: Task 5 must be completed first.
  - [ ] Add validation tests for email in `test_student_validation.py`.

### 8. Update Integration Tests for API
- **Task**: Create/Update integration tests to validate the API's handling of email during student operations.
  - **File**: `tests/controllers/test_student_controller.py`
  - **Description**: Add tests that cover scenarios for creating and retrieving students with email.
  - **Dependencies**: Tasks 3 and 4 must be completed first.
  - [ ] Add integration tests for email handling in `test_student_controller.py`.

### 9. Update README Documentation
- **Task**: Update the README file to document the new email functionality.
  - **File**: `README.md`
  - **Description**: Add information about the email field requirements and the behavioral changes in the API endpoints.
  - **Dependencies**: None.
  - [ ] Update README with new API specifications for email.

---

## Notes
- Ensure that all new changes adhere to the established coding standards and naming conventions.
- Maintain the structure and clarity of existing tests while adding new test cases.
- All tasks should be executable and independently testable before they are marked as complete.