# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:  
- `src/models.py`  
- `src/routes.py`  
- `src/database.py`  
- `src/migrations.py`  
- `src/app.py`  
- `tests/test_routes.py`  
- `tests/test_models.py`  

---

## Task Breakdown

- [ ] **Task 1: Update Student Model to Include Email Field**  
  **File Path**: `src/models.py`  
  - Modify the `Student` class to add the `email` attribute as a string that is required and unique.
  
- [ ] **Task 2: Create Migration Script for Email Field**  
  **File Path**: `src/migrations.py`  
  - Write the migration script to add the `email` field to the existing `Student` table while ensuring that data integrity is maintained.

- [ ] **Task 3: Implement Validation Logic for Email Field**  
  **File Path**: `src/routes.py`  
  - Update the `POST /students` endpoint to include validation that checks if the `email` field is present, has a valid format, and is unique.

- [ ] **Task 4: Update API Response for Student Creation**  
  **File Path**: `src/routes.py`  
  - Modify the JSON response returned upon successful creation of a student to include the new `email` field.

- [ ] **Task 5: Update API Response for Retrieving All Students**  
  **File Path**: `src/routes.py`  
  - Ensure that the `GET /students` endpoint response includes the `email` field for all students in the list.

- [ ] **Task 6: Write Unit Tests for New Functionality**  
  **File Path**: `tests/test_routes.py`  
  - Implement unit tests to cover the user scenarios, including adding students with valid email, without email, and with duplicate emails. Include assertions for the expected error messages.

- [ ] **Task 7: Write Tests for Student Model**  
  **File Path**: `tests/test_models.py`  
  - Test the integrity and uniqueness constraints of the new `email` field in the `Student` model.

- [ ] **Task 8: Update README.md Documentation**  
  **File Path**: `README.md`  
  - Document the new `email` functionality, including the requirements for creating a student and updating the API usage examples to reflect these changes.

- [ ] **Task 9: Run Database Migrations**  
  **File Path**: `src/app.py`  
  - Ensure the migration commands for the database are included in the application setup. Test the migration process to guarantee it executes without data loss.

- [ ] **Task 10: Test and Validate Changes Locally**  
  **File Path**: Local Test Environment  
  - Ensure all changes are functioning as expected in your local development environment by running the application and executing all tests. Confirm all scenarios from the specification are passing.

---

Each task is independently actionable, allowing for isolated testing as modifications are made to the codebase.