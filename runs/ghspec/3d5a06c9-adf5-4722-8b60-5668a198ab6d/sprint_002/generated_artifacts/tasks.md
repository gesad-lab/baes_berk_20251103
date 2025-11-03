# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `/src/models.py`
- `/src/schemas.py`
- `/src/routes/student_routes.py`
- `/src/database.py`
- `/tests/test_student_routes.py`
- `/tests/test_database.py`
- `/requirements.txt`
- `/README.md`

## Task Breakdown

### Tasks for Database Schema Update
- [ ] **Update Student Model to Include Email Field**  
  **File**: `/src/models.py`  
  Update the SQLAlchemy Student model to add an `email` column, ensuring it is a required field and defined unique.

- [ ] **Create Database Migration for Email Field**  
  **File**: Command Line  
  Run command: `alembic revision --autogenerate -m "Add email field to Student entity"`  
  Ensure the migration properly adds the `email` column to the existing `students` table without losing data.

### Tasks for Schema Validation
- [ ] **Update Pydantic Schemas for Student Creation**  
  **File**: `/src/schemas.py`  
  Modify the existing Pydantic schema for creating a student to require an `email` field alongside the `name` field.

- [ ] **Update Pydantic Schemas for Student Response**  
  **File**: `/src/schemas.py`  
  Ensure the response schema includes the `email` attribute alongside `id` and `name`.

### Tasks for API Routes
- [ ] **Implement Create Student Endpoint with Email Validation**  
  **File**: `/src/routes/student_routes.py`  
  Add and test the `POST /students` endpoint to accept both name and email, ensuring correct response formatting.

- [ ] **Implement Update Student Email Endpoint**  
  **File**: `/src/routes/student_routes.py`  
  Add and test the `PUT /students/{id}` endpoint allowing the update of the student email. 

- [ ] **Update List Students Endpoint Response**  
  **File**: `/src/routes/student_routes.py`  
  Ensure the `GET /students` endpoint responses include the new email field for each student.

### Tasks for Error Handling
- [ ] **Add Validation for Required Email on Creation**  
  **File**: `/src/routes/student_routes.py`  
  Implement validation logic in the `POST /students` endpoint to return an error if the email field is missing, in the specified error format.

### Tasks for Testing
- [ ] **Update Unit Tests for Student Creation**  
  **File**: `/tests/test_student_routes.py`  
  Write tests for creating a student with a valid email and ensuring proper error handling when the email is missing.

- [ ] **Update Unit Tests for Updating Student Email**  
  **File**: `/tests/test_student_routes.py`  
  Write tests to ensure that updating a student's email functions correctly and validate the response format.

- [ ] **Add Integration Test for List Students Endpoint**  
  **File**: `/tests/test_student_routes.py`  
  Ensure integration tests confirm that all students, including their email addresses, are correctly returned when listing students.

### Tasks for Documentation Updates
- [ ] **Update README.md for New Feature**  
  **File**: `/README.md`  
  Document the new email field functionality, including usage examples and updated API endpoints for reference.

### Tasks for Dependency Management
- [ ] **Check and Update Requirements File**  
  **File**: `/requirements.txt`  
  Ensure that the Alembic tool and any necessary libraries for schema migrations are included in the requirements.

--- 

By following this structured task breakdown, the implementation of adding an email field to the Student entity can be executed methodically, ensuring multiple components are covered while maintaining code quality and documentation standards.