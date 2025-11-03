# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `models.py`
- `repository.py`
- `service.py`
- `main.py`
- Migration script (new)

## Task Breakdown

### 1. Update Database Model
- **Task**: Add Email Field to Student Model
   - **File**: `src/models.py`
   - **Description**: Modify the existing `Student` class in `models.py` to include the `email` field as a required string.
   - **Dependencies**: None
   - [ ] Implement email field in the Student model.

### 2. Update Repository Layer
- **Task**: Update Save Method to Include Email
   - **File**: `src/repository.py`
   - **Description**: Modify the `save()` method to handle the new email field for student records.
   - **Dependencies**: Task 1
   - [ ] Update `save()` method to accommodate the email field.

- **Task**: Update Get By ID Method to Return Email
   - **File**: `src/repository.py`
   - **Description**: Update the `get_by_id()` method to return email along with student details.
   - **Dependencies**: Task 1
   - [ ] Update `get_by_id()` method to include email in response.

### 3. Update Service Layer
- **Task**: Modify Add Student Functionality
   - **File**: `src/service.py`
   - **Description**: Update the `add_student()` method to require and validate the email field upon student creation.
   - **Dependencies**: Task 1
   - [ ] Implement requirements for the email field in `add_student()`.

### 4. Update API Routes
- **Task**: Change Create Student API to Handle Email
   - **File**: `src/main.py`
   - **Description**: Update the API endpoint for creating a new student to include email in request and response.
   - **Dependencies**: Task 1, Task 2
   - [ ] Modify POST route to handle and return email.

- **Task**: Change Get Student API to Return Email
   - **File**: `src/main.py`
   - **Description**: Update the API endpoint for retrieving student details to also return the email field.
   - **Dependencies**: Task 1, Task 2
   - [ ] Modify GET route to include email in response.

### 5. Input Validation
- **Task**: Add Pydantic Model for Validation
   - **File**: `src/schema.py` (new)
   - **Description**: Create a Pydantic model for validating the request body for creating a student.
   - **Dependencies**: Task 1
   - [ ] Implement Pydantic model for student creation with email.

### 6. Error Handling
- **Task**: Implement Error Handling for Missing Email
   - **File**: `src/service.py`
   - **Description**: Update error handling logic to provide descriptive errors when the email field is missing.
   - **Dependencies**: Task 1, Task 3
   - [ ] Implement clear error messages for validation failures.

### 7. Create Database Migration
- **Task**: Create Migration Script to Add Email Field
   - **File**: `src/migrations/versions/` (new)
   - **Description**: Create a new Alembic migration script to add the email field to the existing students table while preserving existing data.
   - **Dependencies**: Task 1
   - [ ] Generate migration script to update students table.

### 8. Write Unit Tests
- **Task**: Write Tests for Student Creation
   - **File**: `tests/test_service.py`
   - **Description**: Add unit tests to verify the creation of student records including the email field, and test for validation errors when missing.
   - **Dependencies**: Task 1, Task 3
   - [ ] Implement unit tests for the student creation logic.

- **Task**: Write Tests for Fetching Student Details
   - **File**: `tests/test_service.py`
   - **Description**: Write tests to confirm that retrieving student details includes the email field.
   - **Dependencies**: Task 1, Task 2
   - [ ] Implement unit tests for fetching student details with email.

## Final Review
- **Task**: Review Application Documentation
   - **File**: `README.md`
   - **Description**: Update the project README to reflect changes in API endpoints and functionality regarding email.
   - **Dependencies**: All tasks
   - [ ] Ensure README is up-to-date with the new feature and usage instructions.
  
By following this task breakdown, the Students Entity feature will be effectively implemented with the new email field, ensuring compliance with the specified requirements and proper testing for functionality.