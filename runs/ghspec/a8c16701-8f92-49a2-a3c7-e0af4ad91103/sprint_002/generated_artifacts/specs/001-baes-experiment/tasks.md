# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models.py` (320 bytes)
- `src/api.py` (450 bytes)
- `src/errors.py` (210 bytes)
- `src/app.py` (300 bytes)
- `README.md` (600 bytes)

---

## Task List

- [ ] **Task 1: Modify Student Model**
  - **File**: `src/models.py`
  - **Description**: Update the Student model to include an `email` field as a required string.
  
- [ ] **Task 2: Create Migration for Email Field**
  - **File**: `migrations/versions/add_email_to_student.py`
  - **Description**: Create a migration script using Alembic to add the `email` column to the `students` table, ensuring existing data is preserved. 
    - Include the upgrade and downgrade functions with the appropriate SQLAlchemy commands.

- [ ] **Task 3: Update POST Endpoint for Student Creation**
  - **File**: `src/api.py`
  - **Description**: Modify the `/students` POST route to handle creation of a Student with an `email` field. 
    - Add input validation to ensure the `email` field is provided before creating the student.

- [ ] **Task 4: Update GET Endpoint to Include Email**
  - **File**: `src/api.py`
  - **Description**: Ensure the GET student endpoint (`/students/{id}`) returns the `email` field in the response JSON.

- [ ] **Task 5: Enhance Error Handling for Missing Email**
  - **File**: `src/errors.py`
  - **Description**: Update error handling within the API to provide a specific error message when the `email` field is missing during student creation.

- [ ] **Task 6: Ensure Database Migration on Startup**
  - **File**: `src/app.py`
  - **Description**: Verify and implement the logic to run database migrations on application startup to apply changes to the Student table.

- [ ] **Task 7: Write Unit Tests for Email Field**
  - **File**: `tests/test_api.py`
  - **Description**: Add unit tests validating the new functionality:
    - Test creating a student with a valid name and email.
    - Test error handling when creating a student without an email.
    - Test that existing students are not affected by the migration of the `email` field.

- [ ] **Task 8: Write Unit Tests for Model Changes**
  - **File**: `tests/test_models.py`
  - **Description**: Ensure the tests cover the updated Student model to verify field requirements, including the new email field.

- [ ] **Task 9: Update Documentation for API Changes**
  - **File**: `README.md`
  - **Description**: Update the README to include details about the new email field for the Student entity, including usage examples for the updated API endpoints.

- [ ] **Task 10: Verify Automated Documentation Generation**
  - **File**: `src/app.py` (or where the FastAPI instance is located)
  - **Description**: Confirm that the FastAPI's auto-generated OpenAPI documentation reflects the new `email` field for the student entity.

---

Each task can be completed independently and tested, ensuring clear progress tracking through the implementation plan.