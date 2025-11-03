# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/api/test_student_api.py` (3194 bytes)

## Task Breakdown

### Task 1: Update Student Model
- **File**: `src/models/student.py`
- **Description**: Modify the `Student` class to include the new `email` field.
- **Code Update**:
  ```python
  # Add email field to the Student model
  email = Column(String, nullable=False, unique=True)  # Added email field
  ```
- [ ] Task 1: Implement email field in student model

### Task 2: Create Database Migration
- **File**: `migrations/versions/2023XXXXXX_add_email_field.py`
- **Description**: Write a migration script to add the `email` field to the `students` table.
- **Migration Code**:
  ```python
  def upgrade():
      with op.batch_alter_table('students') as batch_op:
          batch_op.add_column(sa.Column('email', sa.String(), nullable=False))
          batch_op.create_unique_constraint('uq_email', ['email'])
  ```

- [ ] Task 2: Create and run migration to add email field

### Task 3: Update Create Student API Endpoint
- **File**: `src/api/student_api.py`
- **Description**: Modify the endpoint to handle the new `email` field in the request body.
- **Code Update**:
  ```python
  @app.route('/students', methods=['POST'])
  def create_student():
      # Extract name and email from request
      # Validate and return ID, name, and email
  ```

- [ ] Task 3: Implement email handling in create student endpoint

### Task 4: Update Get Student API Endpoint
- **File**: `src/api/student_api.py`
- **Description**: Modify the endpoint response to include the `email` field when retrieving student data.
- **Code Update**:
  ```python
  @app.route('/students/<int:id>', methods=['GET'])
  def get_student(id):
      # Fetch student by ID and include email in response
  ```

- [ ] Task 4: Modify get student endpoint to return email field

### Task 5: Update List Students API Endpoint
- **File**: `src/api/student_api.py`
- **Description**: Alter the listing endpoint to display the `email` for each student.
- **Code Update**:
  ```python
  @app.route('/students', methods=['GET'])
  def list_students():
      # List all students with name and email
  ```

- [ ] Task 5: Implement email field in list students endpoint

### Task 6: Write Unit Tests for Email Field
- **File**: `tests/api/test_student_api.py`
- **Description**: Add unit tests to check for the functionality and validation of the email field in student APIs.
- **Test Implementation**:
  ```python
  def test_create_student_with_email():
      # Test creation with valid email
  def test_create_student_without_email():
      # Test error response when email is missing
  ```

- [ ] Task 6: Create tests for email field functionality

### Task 7: Update Existing Tests
- **File**: `tests/api/test_student_api.py`
- **Description**: Ensure existing tests are updated to account for the new email field in student records, maintaining backward compatibility.
  
- [ ] Task 7: Review and update existing tests for email changes

### Task 8: Documentation Update
- **File**: `docs/api_documentation.md`
- **Description**: Update API documentation to reflect the new `email` field in the request and response details.
  
- [ ] Task 8: Modify API documentation to include email field

### Task 9: Run Migrations and Validate
- **File**: N/A
- **Description**: Ensure the migration runs successfully and that the database reflects the new schema without losing existing data.
  
- [ ] Task 9: Execute database migrations and validate schema changes

### Task 10: Review and Merge Changes
- **File**: N/A
- **Description**: Conduct a final review of code changes, tests, and documentation before merging into the main branch.
  
- [ ] Task 10: Perform review and merge update to main branch

--- 

This task breakdown provides a clear set of implementable actions structured around the addition of an email field to the student entity, ensuring adherence to the project constitution and best practices.