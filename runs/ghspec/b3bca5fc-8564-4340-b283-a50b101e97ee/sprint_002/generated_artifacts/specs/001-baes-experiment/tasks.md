# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- **models.py**: Update Student model to include the email field.
- **main.py**: Update routes to validate and handle email in the POST request.
- **tests/test_students.py**: Add test cases for student creation with email and retrieval.

Instructions for Task Breakdown:
1. Identify which existing files need modifications
2. Create new files for new functionality
3. Ensure integration tasks are included
4. Maintain consistency with existing code style and patterns

---

### Task List

- [ ] **Task 1: Update Student Model to Include Email Field**  
  - **File**: `src/models.py`  
  - **Description**: Modify the `Student` class in `models.py` to include a new non-nullable `email` field. Ensure that the field is defined correctly in the SQLAlchemy model.  
  - **Dependencies**: None

- [ ] **Task 2: Create Database Migration Script**  
  - **File**: `src/migrations/add_email_field.py`  
  - **Description**: Write a migration script to add the `email` column to the `students` table in the SQLite database. Ensure the existing data is preserved during this migration.  
  - **Dependencies**: Task 1

- [ ] **Task 3: Modify Main API Logic to Handle Email Validation**  
  - **File**: `src/main.py`  
  - **Description**: Update the POST `/students` endpoint logic to validate that the `email` field is present and correctly formatted. Adjust the response messages for success and error cases.  
  - **Dependencies**: Task 1

- [ ] **Task 4: Update the Successful Response Structure for Student Creation**  
  - **File**: `src/main.py`  
  - **Description**: Modify the response output for successful student creation to include the new `email` field in the response JSON.  
  - **Dependencies**: Task 3

- [ ] **Task 5: Implement Input Validation for Email Field**  
  - **File**: `src/validation.py`  
  - **Description**: Create a validation function to check the format of the email field input when a student is created. Ensure it adheres to standard email format validation.  
  - **Dependencies**: Task 1

- [ ] **Task 6: Write Unit Tests for Student Management**  
  - **File**: `tests/test_students.py`  
  - **Description**: Add unit tests for the new functionality that includes cases for creating students with valid/invalid email addresses and retrieving all students.  
  - **Dependencies**: Task 1, Task 3

- [ ] **Task 7: Update API Documentation in README.md**  
  - **File**: `README.md`  
  - **Description**: Revise the API documentation to include the new email field requirements for the POST /students endpoint and provide examples of valid JSON requests and responses.  
  - **Dependencies**: Task 1, Task 3

- [ ] **Task 8: Run Migrated Database and Test New Endpoints**  
  - **File**: No specific file (Command line operation)  
  - **Description**: Execute the database migration script to update the schema and run newly implemented tests to ensure they pass successfully.  
  - **Dependencies**: Task 2, Task 6

### Next Steps
1. Complete each task in the order specified to ensure proper dependencies are respected.
2. Perform thorough testing after implementation.
3. Prepare for deployment once all tasks are complete and validated.