# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `api.py` (1524 bytes)
- `models.py` (634 bytes)
- `services.py` (1024 bytes)
- `database.py` (450 bytes)
- `tests/test_api.py` (1792 bytes)
- `tests/test_services.py` (2110 bytes)

Instructions for Task Breakdown:
1. Identify which existing files need modifications
2. Create new files for new functionality
3. Ensure integration tasks are included
4. Maintain consistency with existing code style and patterns

---

## Task Breakdown

### 1. Update Student Model
- **Task**: Modify `models.py` to add email field to Student model
  - **File**: `src/models.py`
  - **Description**: Update the Student model to include a new required email field.
  - Action: Add the line `email = Column(String, nullable=False)` to the Student class.

  ```markdown
  - [ ] Change `models.py` to add email field to Student model
    - File: `src/models.py`
  ```

---

### 2. Update Pydantic Schema
- **Task**: Update the Pydantic schema for Student creation
  - **File**: `src/models.py`
  - **Description**: Modify the `StudentCreate` model to include email validation.

  ```markdown
  - [ ] Modify `StudentCreate` Pydantic schema to include email
    - File: `src/models.py`
  ```

---

### 3. Update Database Migration Script
- **Task**: Create a migration to add the email field to the Students table
  - **File**: `src/database.py`
  - **Description**: Implement database migration using Alembic to add the new email column.

  ```markdown
  - [ ] Create a migration script to add email field in database
    - File: `src/database.py`
  ```

---

### 4. Update POST API Endpoint
- **Task**: Modify `api.py` to handle email in POST request for creating a Student
  - **File**: `src/api.py`
  - **Description**: Update the endpoint to accept an email field and return it in the response.

  ```markdown
  - [ ] Modify `POST /students` endpoint to include email handling
    - File: `src/api.py`
  ```

---

### 5. Update GET API Endpoint
- **Task**: Modify `api.py` to return email in GET request response for Students
  - **File**: `src/api.py`
  - **Description**: Ensure that the `GET /students` endpoint includes the email field in the response.

  ```markdown
  - [ ] Modify `GET /students` endpoint to return email field
    - File: `src/api.py`
  ```

---

### 6. Implement Business Logic for Student Creation
- **Task**: Update functions in `services.py` to include email when creating a Student
  - **File**: `src/services.py`
  - **Description**: Ensure that the business logic handles the email parameter properly during Student creation.

  ```markdown
  - [ ] Update business logic in `services.py` for email handling
    - File: `src/services.py`
  ```

---

### 7. Implement Error Handling
- **Task**: Update error handling in `api.py` for missing email during Student creation
  - **File**: `src/api.py`
  - **Description**: Create descriptive error messages for requests missing name or email fields.

  ```markdown
  - [ ] Implement error handling for missing email in requests
    - File: `src/api.py`
  ```

---

### 8. Extend Unit Tests for API
- **Task**: Update existing tests in `tests/test_api.py` for creating Students with and without email
  - **File**: `tests/test_api.py`
  - **Description**: Add unit tests to cover scenarios for POST requests with missing email.

  ```markdown
  - [ ] Extend tests to cover creation of Students with email
    - File: `tests/test_api.py`
  ```

---

### 9. Extend Unit Tests for Services
- **Task**: Add tests in `tests/test_services.py` to verify functionality with email
  - **File**: `tests/test_services.py`
  - **Description**: Ensure business logic and service layer tests recognize and validate the email field.

  ```markdown
  - [ ] Extend service tests to verify email handling
    - File: `tests/test_services.py`
  ```

---

### 10. Update Documentation
- **Task**: Update `README.md` to include information about the new API requirements
  - **File**: `README.md`
  - **Description**: Modify the existing documentation to reflect the new email field in Student creation and retrieval.

  ```markdown
  - [ ] Update README.md with new API details for Student
    - File: `README.md`
  ```

---

This breakdown separates the implementation into actionable tasks that can be conducted independently, ensuring clarity and focus on the code changes specific to the addition of the email field to the Student entity.