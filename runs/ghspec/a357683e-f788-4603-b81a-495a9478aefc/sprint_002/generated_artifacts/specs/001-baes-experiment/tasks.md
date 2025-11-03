# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_api.py` (4424 bytes)
- `tests/test_database.py` (2451 bytes)

---

## Task Breakdown

### 1. Setup Project Environment
- [ ] **Update environment dependencies**
  - **File**: `requirements.txt`
  - **Task**: Add `email-validator` library for email validation.

### 2. Modify Database Schema
- [ ] **Create migration script to add email column**
  - **File**: `migrations/versions/XXXX_add_email_to_student.py`
  - **Task**: Implement a migration script that adds an `email` column to the `students` table with a NOT NULL constraint preserving existing data.

### 3. Update API Module
- [ ] **Modify POST endpoint to include email field**
  - **File**: `src/api/students.py`
  - **Task**: Update the handler for creating a student to accept the `email` field and return it in the response.

- [ ] **Modify GET endpoint to include email in student list**
  - **File**: `src/api/students.py`
  - **Task**: Update the handler for retrieving students to include the `email` field in each returned student record.

- [ ] **Modify PUT endpoint to allow email updates**
  - **File**: `src/api/students.py`
  - **Task**: Update the handler for updating a student to accept an `email` field and return it in the response.

### 4. Implement Email Validation Logic
- [ ] **Create email validation utility function**
  - **File**: `src/utils/validation.py`
  - **Task**: Implement a utility function to validate email formats using the `email-validator` library.

- [ ] **Integrate email validation into route handlers**
  - **File**: `src/api/students.py`
  - **Task**: Use the email validation utility function within the student creation and update routes with appropriate error handling.

### 5. Ensure Error Handling
- [ ] **Adapt global error handler for email validation**
  - **File**: `src/error_handling.py`
  - **Task**: Adjust the global error handler to return specific error messages for invalid email formats.

### 6. Testing
- [ ] **Update existing tests for new functionality**
  - **File**: `tests/test_api.py`
  - **Task**: Modify current tests to cover scenarios involving the new `email` field.

- [ ] **Write new unit tests for email validation**
  - **File**: `tests/test_utils.py`
  - **Task**: Create unit tests for the email validation utility function to ensure proper functionality.

- [ ] **Write integration tests for email handling in API**
  - **File**: `tests/test_api.py`
  - **Task**: Create integration tests that check the entire process for creating, updating, and retrieving students with email.

### 7. Documentation
- [ ] **Update README.md with new API details**
  - **File**: `README.md`
  - **Task**: Add section for the new email field, including instructions for using the endpoints.

- [ ] **Add docstrings for modified API endpoints**
  - **File**: `src/api/students.py`
  - **Task**: Document the API endpoints with descriptions for the new email field.

- [ ] **Update migration documentation**
  - **File**: `README.md`
  - **Task**: Include instructions on how to run database migrations for adding the email field.

---

This task breakdown provides a structured approach to implement the feature, ensuring that each task is focused, consistent with existing code, and independently testable.