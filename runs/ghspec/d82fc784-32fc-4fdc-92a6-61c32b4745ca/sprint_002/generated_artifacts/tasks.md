# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models.py` (880 bytes)
- `src/routes.py` (1250 bytes)
- `tests/test_routes.py` (2440 bytes)

## Task List

### 1. Database Schema Update in Student Model
- [ ] Update `src/models.py` to include the new email field in the `Student` class.
  - **File Path**: `src/models.py`
  - **Description**: Add the line `email = Column(String(254), nullable=False)` to the `Student` class definition.

### 2. Create Migration Script
- [ ] Create a migration script using Alembic to add the email column to the `students` table.
  - **File Path**: `src/migrations/add_email_to_students.py`
  - **Description**: Implement the `upgrade()` function to add the `email` column and the `downgrade()` function to drop it.

### 3. Update Create Student API
- [ ] Update the `POST /students` endpoint in `src/routes.py` to require an email.
  - **File Path**: `src/routes.py`
  - **Description**: Modify the `create_student()` function to handle the new email field.

### 4. Update Retrieve Students API
- [ ] Ensure the `GET /students` endpoint in `src/routes.py` returns the email field.
  - **File Path**: `src/routes.py`
  - **Description**: Modify the function that retrieves students to include the email in the JSON response.

### 5. Update Update Student API
- [ ] Update the `PUT /students/{id}` endpoint in `src/routes.py` to allow updating the email field.
  - **File Path**: `src/routes.py`
  - **Description**: Modify the function to handle updates to the email field alongside the name.

### 6. Implement Integration Tests for Email Functionality
- [ ] Add integration tests in `tests/test_routes.py` for creating, updating, and retrieving students with email.
  - **File Path**: `tests/test_routes.py`
  - **Description**: Write tests like `test_create_student_with_email()`, `test_update_student_email()`, and `test_retrieve_students_with_email()`.

### 7. Validate Email Presence in Create Requests
- [ ] Implement validation to reject creation of students without an email.
  - **File Path**: `src/routes.py`
  - **Description**: Update the `create_student()` function to return an error if the email is missing or invalid.

### 8. Ensure Logging for API Requests
- [ ] Update logging in `src/routes.py` to include logs for email-related events.
  - **File Path**: `src/routes.py`
  - **Description**: Ensure that email events during student creation, update, and retrieval are logged with appropriate details.

### 9. Documentation Update
- [ ] Update README.md with changes regarding the new email field and its requirements.
  - **File Path**: `README.md`
  - **Description**: Describe the new email field, its requirements in API calls, and any relevant migration details.

---

### Final Notes:
- Each task is focused on a single file to maintain clarity and independence.
- Ensure all modifications adhere to the project's existing coding standards and styles.
- Tasks should be kept small and implementable independently for easier testing and integration.