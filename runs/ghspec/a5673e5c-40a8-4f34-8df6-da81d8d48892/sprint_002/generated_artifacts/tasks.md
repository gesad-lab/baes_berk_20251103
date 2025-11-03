# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/api.py` (XXX bytes)
- `src/models.py` (XXX bytes)
- `src/schemas.py` (XXX bytes)
- `tests/test_api.py` (2144 bytes)

## Task Breakdown

### Task 1: Update Student Model to Include Email
- **File**: `src/models.py`
- **Description**: Modify the `Student` class in the `models.py` to add a new `email` field as a non-nullable string.
- **Implementation**:
  ```python
  # Inside models.py
  email = Column(String, nullable=False)  # New email field
  ```
- [ ] Task 1 - Update Student Model to Include Email

### Task 2: Update Pydantic Schemas to Handle Email
- **File**: `src/schemas.py`
- **Description**: Modify the `StudentCreate` and `StudentUpdate` classes to include email validation using Pydantic's `EmailStr`.
- **Implementation**:
  ```python
  # Inside schemas.py
  from pydantic import EmailStr
  
  class StudentCreate(BaseModel):
      name: str
      email: EmailStr  # Email is now a required field with email validation

  class StudentUpdate(BaseModel):
      email: EmailStr  # Only email update
  ```
- [ ] Task 2 - Update Pydantic Schemas to Handle Email

### Task 3: Modify API Endpoints for Email Handling
- **File**: `src/api.py`
- **Description**: Update the API logic in `api.py` to handle email input in the student creation and update endpoints.
- **Implementation**:
  - Ensure that the `POST /students` endpoint processes email data.
  - Ensure that the `PUT /students/{name}` endpoint allows updating only the email.
- [ ] Task 3 - Modify API Endpoints for Email Handling

### Task 4: Create Database Migration for Email Field
- **File**: `migrations/xxxx_add_email_to_student.py`
- **Description**: Create an Alembic migration file to add the `email` column to the existing `students` table.
- **Implementation**:
  ```python
  """Add email to student model
  
  Revision ID: xxxxxxxx
  Revises: xxxxxxxx
  """
  from alembic import op
  import sqlalchemy as sa
  
  def upgrade():
      op.add_column('students', sa.Column('email', sa.String(), nullable=False))
  
  def downgrade():
      op.drop_column('students', 'email')
  ```
- [ ] Task 4 - Create Database Migration for Email Field

### Task 5: Add Email Validation Logic
- **File**: `src/api.py`
- **Description**: Integrate email validation logic using Pydantic to ensure valid email formats are enforced upon creation or update.
- **Implementation**: Validate emails using Pydantic automatically, handle errors.
- [ ] Task 5 - Add Email Validation Logic

### Task 6: Write Unit Tests for Email Functionality
- **File**: `tests/test_api.py`
- **Description**: Create unit tests in `test_api.py` to validate the functionality related to email handling, including:
  - Successful creation and retrieval of student email.
  - Handling of invalid email formats.
  - Successful updating of the email field.
- [ ] Task 6 - Write Unit Tests for Email Functionality

### Task 7: Update README with API Changes
- **File**: `README.md`
- **Description**: Document changes made to the API in the README file, outlining the new email field and how to use it in requests.
- **Implementation**: Provide examples for creating, retrieving, and updating students with email.
- [ ] Task 7 - Update README with API Changes

## Testing Strategy
- Ensure each task is independently testable, focusing on the new email functionality and creating tests that validate the implementation against the outlined specifications. 

---