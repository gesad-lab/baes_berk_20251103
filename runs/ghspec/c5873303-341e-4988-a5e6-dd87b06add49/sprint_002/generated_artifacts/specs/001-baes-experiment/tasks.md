# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models.py`
- `src/schemas.py`
- `src/routes/students.py`
- `tests/test_students.py`
- `src/database.py` (for migration setup if needed)

Instructions for Task Breakdown:
1. Identify which existing files need modifications
2. Create new files for new functionality
3. Ensure integration tasks are included
4. Maintain consistency with existing code style and patterns

---

## Task List

- [ ] **Task 1: Update the Student Model**
   - **File**: `src/models.py`
   - **Description**: Add an `email` field to the `Student` model. Ensure it is set to not nullable and follows the appropriate data type.
   - **Dependencies**: None
   - **Testability**: Verify the model can be instantiated with an email.

- [ ] **Task 2: Update Pydantic Schemas for Student Creation and Response**
   - **File**: `src/schemas.py`
   - **Description**: Modify the `StudentCreate` schema to include an `email` field with validation and update the `StudentResponse` schema accordingly.
   - **Dependencies**: Task 1
   - **Testability**: Test the schemas' validity when creating a Student with an email.

- [ ] **Task 3: Create Database Migration Script**
   - **File**: `src/database.py`
   - **Description**: Implement a migration script to add the `email` column to the existing `students` table in the database.
   - **Dependencies**: None
   - **Testability**: Run the migration and verify the `students` table includes the new email column without loss of data.

- [ ] **Task 4: Update Create Student Endpoint**
   - **File**: `src/routes/students.py`
   - **Description**: Modify the `POST /students` endpoint to include email handling in the request body and ensure the response returns the new email field.
   - **Dependencies**: Task 1, Task 2
   - **Testability**: Test the API to ensure valid students can be created and emails are stored.

- [ ] **Task 5: Update Retrieve All Students Endpoint**
   - **File**: `src/routes/students.py`
   - **Description**: Modify the `GET /students` endpoint to return email details alongside student names in the response.
   - **Dependencies**: Task 1
   - **Testability**: Test the API to ensure it returns a list of students with email addresses included.

- [ ] **Task 6: Update Tests for Student Creation and Retrieval**
   - **File**: `tests/test_students.py`
   - **Description**: Add tests for:
     - Successful creation of a student with an email.
     - Retrieval of students ensuring they include emails.
     - Error handling when the email field is missing.
   - **Dependencies**: Task 4, Task 5
   - **Testability**: Run tests to verify all pass without errors.

- [ ] **Task 7: Document Changes in README**
   - **File**: `README.md`
   - **Description**: Update the documentation to include details about the new email field in API requests and responses.
   - **Dependencies**: Task 2, Task 4, Task 5
   - **Testability**: Review documentation for clarity and accuracy in reflecting the new API specs.

---

## Summary
This breakdown provides a clear and implementable set of tasks for adding an email field to the Student entity, focusing on updating the relevant models, API endpoints, and tests while ensuring all modifications align with existing code structures and practices. Each task is designed to be independently testable, contributing to the overall success of the feature implementation.