# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

### Existing Code to Build Upon:
- `models.py`
- `schemas.py`
- `api.py`
- `database.py`
- `requirements.txt`
- `README.md`

### Instructions for Task Breakdown:
1. Identify which existing files need modifications
2. Create new files for new functionality
3. Ensure integration tasks are included
4. Maintain consistency with existing code style and patterns

---

## Task List:

### Database Changes

- [ ] **Task 1**: Update the Student model to include the email field  
   **File**: `src/models.py`  
   **Details**: Add a new column `email = Column(String, nullable=False)` to the `Student` class.

- [ ] **Task 2**: Create a migration script to add the email column to the Student table  
   **File**: `migrations/versions/<migration_filename>.py`  
   **Details**: Generate and implement a migration script that executes `ALTER TABLE students ADD COLUMN email STRING NOT NULL;`.

### API Changes

- [ ] **Task 3**: Update API request handling to include the email field in POST requests  
   **File**: `src/api.py`  
   **Details**: Modify the `POST /students` endpoint to accept and process the `email` field from the request body.

- [ ] **Task 4**: Update API request handling to include the email field in PUT requests  
   **File**: `src/api.py`  
   **Details**: Modify the `PUT /students/{id}` endpoint to accept and process the email field from the request body.

- [ ] **Task 5**: Update API GET response to include email in response objects  
   **File**: `src/api.py`  
   **Details**: Modify the `GET /students` endpoint to return student objects with the email field included.

### Validation Logic

- [ ] **Task 6**: Implement email validation logic in the service layer  
   **File**: `src/services/student_service.py` (create if not existing)  
   **Details**: Write a function to validate the email format and return appropriate error messages for invalid inputs.

- [ ] **Task 7**: Update Pydantic schemas to include email field validation  
   **File**: `src/schemas.py`  
   **Details**: Extend the existing schemas to validate that email is in the proper format.

### Testing

- [ ] **Task 8**: Write unit tests for email validation  
   **File**: `tests/test_email_validation.py` (create if not existing)  
   **Details**: Create tests to check various scenarios of valid and invalid email formats.

- [ ] **Task 9**: Write integration tests for student CRUD operations including email  
   **File**: `tests/test_api.py`  
   **Details**: Extend existing tests to cover scenarios involving creating, updating, and retrieving student records with the email field.

### Documentation

- [ ] **Task 10**: Update API documentation in README.md  
   **File**: `README.md`  
   **Details**: Reflect changes to API contracts including the addition of the email field in all relevant sections.

### Integration Tasks

- [ ] **Task 11**: Ensure all changes are backward compatible with existing data models  
   **File**: `src/models.py`, `migrations/versions/<migration_filename>.py`  
   **Details**: Review modifications to ensure that existing student data remains intact and accessible.

- [ ] **Task 12**: Run all migrations and verify database integrity after changes  
   **File**: Database console or migration runner (e.g., Alembic command line)  
   **Details**: Execute migration to add the email column and check for data integrity.

## Conclusion

This structured task breakdown provides a clear outline for implementing the addition of an email field to the Student entity while ensuring each modification is traceable, testable, and consistent with existing code patterns.