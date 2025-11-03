# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- **models.py** - to modify the Student model
- **api.py** - to update API endpoints
- **database_migrations.py** - to create migration script

Instructions for Task Breakdown:
1. Identify which existing files need modifications
2. Create new files for new functionality
3. Ensure integration tasks are included
4. Maintain consistency with existing code style and patterns

## Task List

### Task 1: Update Student Model to Include Email Field
- **File**: `src/models.py`
- **Description**: Modify the existing `Student` model to add an `email` field with appropriate constraints.
- **Code Changes**:
  ```python
  email = Column(String, nullable=False, unique=True)  # New email field
  ```
- [ ] Implement Model Change

### Task 2: Update Request Validation for Creating Students
- **File**: `src/models.py`
- **Description**: Update the Pydantic model to include email validation for student creation.
- **Code Changes**:
  ```python
  class StudentCreate(BaseModel):
      name: str
      email: EmailStr  # Validate email format
  ```
- [ ] Implement Validation Changes

### Task 3: Implement Create Student API Endpoint
- **File**: `src/api.py`
- **Description**: Create the POST endpoint `/students` to allow for student creation with name and email.
- **Code Changes**: 
  - Implement logic to handle request body and create Student instance in the database.
  - Return appropriate response status and body.
- [ ] Implement API Endpoint

### Task 4: Implement Retrieve Students API Endpoint
- **File**: `src/api.py`
- **Description**: Create the GET endpoint `/students` to return a list of all students including their email addresses.
- **Code Changes**: 
  - Fetch all students from the database and return in JSON format.
- [ ] Implement API Endpoint

### Task 5: Add Input Validation Logic
- **File**: `src/api.py`
- **Description**: Validate that the `name` and `email` fields are non-empty and correctly formatted before processing.
- **Code Changes**:
  - Return 400 status if validation fails, with error message.
- [ ] Implement Input Validation

### Task 6: Create Migration Script for Database Schema Update
- **File**: `src/database_migrations.py`
- **Description**: Write a migration script to add the `email` column to the `students` table.
- **Code Changes**:
  ```python
  def upgrade():
      op.add_column('students', sa.Column('email', sa.String(), nullable=False))
      op.create_unique_constraint('uq_email', 'students', ['email'])

  def downgrade():
      op.drop_column('students', 'email')
  ```
- [ ] Implement Migration Script

### Task 7: Write Unit Tests for Creating Students
- **File**: `tests/test_api.py`
- **Description**: Create unit tests to verify that students can be created successfully with valid inputs.
- **Test Cases**:
  - Test creation of a student with valid name and email.
- [ ] Implement Unit Tests

### Task 8: Write Unit Tests for Retrieving Students
- **File**: `tests/test_api.py`
- **Description**: Create unit tests to verify that retrieving students returns the correct data format.
- **Test Cases**:
  - Ensure retrieved students include name and email.
- [ ] Implement Unit Tests

### Task 9: Write Unit Tests for Input Validation
- **File**: `tests/test_api.py`
- **Description**: Create tests to validate error handling for invalid student data inputs.
- **Test Cases**:
  - Test creation with an empty name, invalid email format.
- [ ] Implement Unit Tests

### Task 10: Update README.md Documentation
- **File**: `README.md`
- **Description**: Document the newly added email field, updated API endpoints, and usage examples.
- [ ] Update Documentation

### Task 11: Conduct Integration Tests
- **File**: `tests/test_integration.py` (New file)
- **Description**: Create integration tests to check end-to-end functionality of creating and retrieving student records.
- [ ] Implement Integration Tests

### Task 12: Test Migration on Development Database
- **File**: N/A
- **Description**: Execute the migration script against a development SQLite database to ensure no data loss and schema is updated correctly.
- [ ] Test Migration

## Conclusion
Following this task breakdown will enable the implementation of the email field in the Student entity while adhering to best practices for code organization, testing, and documentation.