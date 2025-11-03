# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models.py` (1280 bytes)
- `src/services/student_service.py` (864 bytes)
- `src/api/routes.py` (1024 bytes)
- `tests/api/test_routes.py` (2343 bytes)
- `tests/services/test_student_service.py` (1800 bytes)

Instructions for Task Breakdown:
1. Identify which existing files need modifications
2. Create new files for new functionality
3. Ensure integration tasks are included
4. Maintain consistency with existing code style and patterns

---

### Task 1: Update Student Model to Include Email Field
- **File**: `src/models.py`
- **Description**: Add a new `email` field to the `Student` class in the data model.
- **Dependencies**: None
- **Testability**: Ensure the model can be instantiated with the new field.

  - [ ] Update `Student` model by adding `email` column.
  ```python
  class Student(db.Model):
      ...
      email = db.Column(db.String, nullable=False)  # New field for email
  ```
  
### Task 2: Modify Student Service to Handle Email Field
- **File**: `src/services/student_service.py`
- **Description**: Update the functions `create_student` and `get_student_by_id` to handle the new `email` parameter.
- **Dependencies**: Task 1
- **Testability**: Confirm that service endpoints correctly process, create, and return students with email.

  - [ ] Modify `create_student` function to accept and handle email.
  - [ ] Update `get_student_by_id` function to include email in the return object.

### Task 3: Update API Routes to Include Email Field
- **File**: `src/api/routes.py`
- **Description**: Modify the route for creating a new student and retrieving a student to include email in requests and responses.
- **Dependencies**: Task 2
- **Testability**: Verify that API responds with the student’s email when a student is created or retrieved.

  - [ ] Enhance `POST /students` route to accept email.
  - [ ] Adjust `GET /students/<id>` response to include email.

### Task 4: Create Migration Script for Database Update
- **File**: N/A (command line)
- **Description**: Use Flask-Migrate to create and apply a migration to add the email column in the students table.
- **Dependencies**: Task 1
- **Testability**: Ensure that the database schema is updated without data loss.

  - [ ] Generate migration script.
  ```bash
  flask db migrate -m "Add email field to students"
  ```
  - [ ] Apply migration.
  ```bash
  flask db upgrade
  ```

### Task 5: Update Tests for API Routes
- **File**: `tests/api/test_routes.py`
- **Description**: Add unit tests for creating and retrieving students that include the email field.
- **Dependencies**: Task 3
- **Testability**: Validate POST and GET requests for students cover email presence and handle errors.

  - [ ] Write test case for successfully creating student with email.
  - [ ] Write test case for successfully retrieving student with email.

### Task 6: Extend Unit Tests for Student Service
- **File**: `tests/services/test_student_service.py`
- **Description**: Add tests to ensure service methods handle the email parameter correctly.
- **Dependencies**: Task 2
- **Testability**: Ensure that service logic functions correctly with email data.

  - [ ] Add unit tests for creating and retrieving student with email.

### Task 7: Implement Error Handling in API
- **File**: `src/api/routes.py`
- **Description**: Add error responses for missing email when creating a student.
- **Dependencies**: Task 3
- **Testability**: Confirm that the API returns the correct error message when no email is provided.

  - [ ] Update `POST /students` to return a 400 error when email is missing.

### Task 8: Update Documentation
- **File**: `README.md`
- **Description**: Update the README to include details about the new email field and usage instructions for updated API endpoints.
- **Dependencies**: Completion of API and Model changes
- **Testability**: Validate that documentation accurately describes new changes.

  - [ ] Describe new email field in API documentation.
  - [ ] Update example requests/responses to include email.

---

These tasks are structured to ensure that they are small, focused, and testable independently while maintaining the integrity and functionality of the existing system throughout the process.