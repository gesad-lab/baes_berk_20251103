# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models.py`
- `src/schemas.py`
- `src/routes/students.py`
- `tests/test_routes.py`
- `requirements.txt`
- `README.md`
  
Instructions for Task Breakdown:
1. Identify which existing files need modifications
2. Create new files for new functionality
3. Ensure integration tasks are included
4. Maintain consistency with existing code style and patterns

---

## Task Breakdown

### 1. Update Student Model

- [ ] **Task**: Add `email` attribute to the `Student` model  
  **File**: `src/models.py`  
  **Details**: Integrate a new `email` column in the `Student` class while ensuring the integrity of other attributes.  
  **Testability**: Validate by running existing model tests to ensure no breakage.

### 2. Update Pydantic Schema

- [ ] **Task**: Modify request validation schema to include `email`  
  **File**: `src/schemas.py`  
  **Details**: Extend the existing Pydantic schema to validate the `email` attribute, with necessary constraints for presence and format.  
  **Testability**: Write unit tests to confirm the schema correctly validates incoming requests with both valid and invalid email formats.

### 3. Update API Endpoints

- [ ] **Task**: Implement email handling in the student creation endpoint  
  **File**: `src/routes/students.py`  
  **Details**: Modify the logic of the existing `/students` POST endpoint to handle the new `email` field, including verification and storage.  
  **Testability**: Use API tests to verify that valid email submissions succeed and that appropriate error responses are given for missing or invalid emails.

- [ ] **Task**: Ensure email is included in the student retrieval endpoint  
  **File**: `src/routes/students.py`  
  **Details**: Update the `/students` GET endpoint to include emails in the returned student records.  
  **Testability**: Confirm via API tests that the response includes emails for all students.

### 4. Database Migration

- [ ] **Task**: Create Alembic migration to add email field  
  **File**: `migration_script.py` (to be created in a new migrations folder)  
  **Details**: Write a migration to update the `students` table to add the `email` column without data loss.  
  **Testability**: Execute migration script and verify that existing records maintain integrity.

### 5. Testing

- [ ] **Task**: Write unit tests for student creation and retrieval  
  **File**: `tests/test_routes.py`  
  **Details**: Add tests to cover creation of students with an email and for handling errors when email is missing or invalid.  
  **Testability**: Ensure tests pass successfully using pytest.

### 6. Update Documentation

- [ ] **Task**: Update README.md with new API usage details  
  **File**: `README.md`  
  **Details**: Document the changes to the API, including how to create a new student with email and sample request/response structures.  
  **Testability**: Review document clarity and completeness from a user perspective.

---

### Additional Considerations
- Ensure to keep dependencies updated in `requirements.txt` where applicable.
- Follow established coding standards and ensure that all modifications are consistent with existing code structure and practices.