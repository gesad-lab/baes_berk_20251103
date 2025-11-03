# Tasks: Add Email Field to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models.py` (for model updates)
- `src/routes.py` (for API routes)
- `src/controllers.py` (for request handling)
- `src/validation.py` (for input validation)
- `tests/test_student.py` (for testing)
- `README.md` (for documentation updates)

---

## Task Breakdown

### Task 1: Modify Student Model
- **File**: `src/models.py`
- **Description**: Update the `Student` class definition to include an `email` field.
- **Code Change**:
  ```python
  email = Column(String, nullable=False)
  ```
- [ ] Update `src/models.py` to include `email` field for `Student` entity.

### Task 2: Create Migration Script
- **File**: `migrations/add_email_to_students.py`
- **Description**: Create a migration script using Alembic for adding the `email` column to the `students` table.
- **Code Change**:
  ```python
  def upgrade():
      op.add_column('students', sa.Column('email', sa.String(), nullable=False))

  def downgrade():
      op.drop_column('students', 'email')
  ```
- [ ] Create `migrations/add_email_to_students.py` for database schema changes.

### Task 3: Update Routes for Students
- **File**: `src/routes.py`
- **Description**: Add routes for handling requests to create and retrieve students with email.
- [ ] Modify `src/routes.py` to add API endpoints for adding and retrieving students including email.

### Task 4: Implement Controller Logic
- **File**: `src/controllers.py`
- **Description**: Implement functions for processing the requests related to student creation and retrieval that include email handling.
- [ ] Update `src/controllers.py` to process email in request handling functions.

### Task 5: Enhance Validation Logic
- **File**: `src/validation.py`
- **Description**: Add validation logic for the `email` field ensuring it is present and correctly formatted.
- [ ] Update `src/validation.py` to validate the email field input.

### Task 6: Write Unit Tests for Email Feature
- **File**: `tests/test_student.py`
- **Description**: Create unit tests for the new email functionality including validation, adding a student, and retrieving students.
- [ ] Update or create test cases in `tests/test_student.py` to cover the email validation and functionality.

### Task 7: Document the Email Feature
- **File**: `README.md`
- **Description**: Update the README file to include information about the new `email` field, its required format, and validation rules.
- [ ] Update `README.md` for new email field documentation.

---

## Notes
- Ensure all code modifications follow the coding standards outlined in the project constitution.
- Each task should be independently testable and verified to ensure functionality works as intended.