# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models.py`
- `src/main.py`
- `tests/test_success_criteria.py`
- `tests/test_api/test_student_api.py`
- `tests/test_services/test_student_service.py`

---

## Task List

### 1. Update the Student Model
- **Task**: Add `email` field to the `Student` model.
  - **File**: `src/models.py`
  - **Description**: Modify the existing `Student` class to include a new column for email.
  - **Dependencies**: None
  - **Testable**: Verify that the model generates the expected schema in the database.
  - [ ] Update Student model to include email field.

### 2. Update API Endpoints
- **Task**: Update the POST endpoint to create a new student with an email field.
  - **File**: `src/main.py`
  - **Description**: Modify the existing FastAPI POST method to accept and process the new email field.
  - **Dependencies**: Task 1
  - **Testable**: Test the endpoint with valid input data to ensure it correctly creates a student with an email.
  - [ ] Modify POST endpoint to include email in /students endpoint.

- **Task**: Update the GET endpoint to return email along with student data.
  - **File**: `src/main.py`
  - **Description**: Modify the FastAPI GET method to ensure it returns both name and email for all students.
  - **Dependencies**: Task 1
  - **Testable**: Run the GET endpoint to verify expected return format with emails included.
  - [ ] Modify GET endpoint to include email in /students endpoint.

### 3. Update Pydantic Model for Validation
- **Task**: Update the input Pydantic model to require email.
  - **File**: `src/main.py`
  - **Description**: Ensure that the `StudentCreate` model enforces that the email field is mandatory for new student creation.
  - **Dependencies**: Task 1
  - **Testable**: Verify that the validation fails when email is missing in API requests.
  - [ ] Update Pydantic model to validate email field.

### 4. Implement Database Migration
- **Task**: Create a migration script to add the email field to the existing database schema.
  - **File**: Migration Scripts or `version_control/migrations/`
  - **Description**: Write a migration file for creating the new `email` column in the `students` table.
  - **Dependencies**: Task 1
  - **Testable**: Run the migration and check that it updates the database schema without data loss.
  - [ ] Write migration script to add email column.

### 5. Update Tests for New Feature
- **Task**: Add test cases for successful creation of student with email.
  - **File**: `tests/test_api/test_student_api.py`
  - **Description**: Write tests that check new students can be created successfully and validate their emails.
  - **Dependencies**: Task 2
  - **Testable**: Run the tests to confirm that new student entities can be created with expected email fields.
  - [ ] Add tests for creating student with email.

- **Task**: Write tests for handling errors when email is missing.
  - **File**: `tests/test_api/test_student_api.py`
  - **Description**: Validate that attempting to create a student without an email returns the correct error response.
  - **Dependencies**: Task 2
  - **Testable**: Check error messages and codes in response when email is not provided.
  - [ ] Add tests for validation of email field during student creation.

### 6. Ensure JSON Response Structure
- **Task**: Confirm all API responses return valid JSON format.
  - **File**: `src/main.py`
  - **Description**: Ensure that all responses from both student creation and listing endpoints conform to the required JSON structure.
  - **Dependencies**: Task 2
  - **Testable**: Perform manual API calls to verify JSON structure matches specifications.
  - [ ] Validate JSON response structure for all endpoints.

### 7. Update Documentation
- **Task**: Update the README.md file to reflect changes in API functionality.
  - **File**: `README.md`
  - **Description**: Document new endpoints and expected request/response structure, including the email field details.
  - **Dependencies**: Tasks 2, 5
  - **Testable**: Review the README to ensure it accurately reflects the functionality and can be understood by new developers/users.
  - [ ] Update README documentation for new email feature.

---

This structured task breakdown outlines the actionable steps needed to successfully implement the email field for the Student entity, ensuring a coherent and maintainable process. Each task is designed to be independent and focuses on specific aspects of the implementation plan.