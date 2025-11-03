# Tasks: Add Email Field to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- The existing structure of the `student_app` with files for controllers, models, services, and tests needs modification and expansion.

---

### Task List

1. **Update Student Model to Include Email Column**
   - **File Path**: `src/models/student.py`
   - **Task**: Modify the `Student` class to add a new `email` column with the appropriate data type and constraints.
   - **Checkbox**: [ ] Ensure that the model correctly reflects the new email property.

2. **Create Database Migration Script**
   - **File Path**: `migrations/versions/**/*.py` (replace with appropriate directory structure for migrations)
   - **Task**: Create a migration script using Alembic to add the `email` column to the `students` table.
   - **Checkbox**: [ ] The migration script must be reversible and handle existing records.

3. **Implement Email Validation Logic in the Service Layer**
   - **File Path**: `src/services/student_service.py`
   - **Task**: Add logic to validate the email format using an appropriate library (e.g., `email_validator`) in the `create_student` function.
   - **Checkbox**: [ ] Ensure that the validation raises an informative error when the email is invalid.

4. **Implement Create Student API Endpoint**
   - **File Path**: `src/controllers/student_controller.py`
   - **Task**: Update the `POST /students` endpoint to accept an email field in the request body and return the student record upon successful creation.
   - **Checkbox**: [ ] Verify that the correct status codes and response structures are implemented.

5. **Implement Retrieve Students API Endpoint**
   - **File Path**: `src/controllers/student_controller.py`
   - **Task**: Ensure the `GET /students` endpoint returns a list of all students, including their emails.
   - **Checkbox**: [ ] Validate that the response contains the newly added email field.

6. **Write Unit Tests for Create Student Endpoint**
   - **File Path**: `tests/test_student.py`
   - **Task**: Create unit tests for the `POST /students` API, covering successful creation and various invalid input scenarios (valid name and email, invalid email).
   - **Checkbox**: [ ] Confirm that all tests pass and cover the required cases.

7. **Write Unit Tests for Retrieve Students Endpoint**
   - **File Path**: `tests/test_student.py`
   - **Task**: Create unit tests for the `GET /students` API to validate the response structure, ensuring the email field is included.
   - **Checkbox**: [ ] Ensure that the tests accurately reflect the expected output.

8. **Run Migration to Update Database Schema**
   - **File Path**: (Database migration command)
   - **Task**: Execute the migration script to update the database schema to include the email field.
   - **Checkbox**: [ ] Verify that the migration ran successfully without causing data loss.

9. **Document Environment Variables in .env.example**
   - **File Path**: `.env.example`
   - **Task**: Update the `.env.example` file to include any new environments or configurations required for the email functionality.
   - **Checkbox**: [ ] Ensure that all new configurations are documented clearly.

10. **Review and Refactor Code for Consistency**
    - **File Path**: All modified files
    - **Task**: Review all modified code files for adherence to coding standards and ensure consistency in styling and structure.
    - **Checkbox**: [ ] Confirm that all changes conform to the existing project coding conventions.

---

This structured breakdown provides discrete, actionable tasks for implementing the new email functionality in the Student entity, allowing for focused development and testing of each individual component.