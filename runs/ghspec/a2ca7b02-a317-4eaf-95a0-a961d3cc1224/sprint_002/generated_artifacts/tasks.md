# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- models/student.py (732 bytes)
- api/student.py (649 bytes)
- tests/test_student.py (1297 bytes)

---

## Task Breakdown

### Task 1: Update Student Model
- **File**: `src/models/student.py`
- **Description**: Add the "email" field to the existing Student model to accommodate the new functionality.
- **Implementation**:
  ```python
  class Student(Base):
      ...
      email = Column(String, nullable=False)  # New email field
  ```
- [ ] Implement email field in the Student model

### Task 2: Create Database Migration for Email Field
- **File**: `src/db/migrations/add_email_to_students.py`
- **Description**: Create a new migration script to add the email column to the students table without data loss.
- **Implementation**:
  ```sql
  ALTER TABLE students ADD COLUMN email STRING;
  ```
- [ ] Create a migration script for adding the email column

### Task 3: Update Database Initialization Logic
- **File**: `src/db/database.py`
- **Description**: Ensure the database initialization checks the schema version and applies migrations as needed.
- **Implementation**:
  ```python
  Base.metadata.create_all(bind=engine)  # This will include the email field if it is added
  ```
- [ ] Update database initialization logic to accommodate migrations

### Task 4: Implement Student Creation Logic
- **File**: `src/services/student_service.py`
- **Description**: Modify the student creation logic to handle the new "email" input.
- **Implementation**: Ensure email is validated and saved correctly.
- [ ] Update student creation logic to include email handling

### Task 5: Create API Endpoint for Student Creation
- **File**: `src/api/student.py`
- **Description**: Update the FastAPI routing to include an endpoint for creating students with email.
- **Implementation**:
  ```python
  @app.post("/students")
  async def create_student(student: Student):
      return ...  # Logic to create student including email
  ```
- [ ] Create API endpoint for POST /students to handle email input

### Task 6: Implement Input Validation for Student Creation
- **File**: `src/validators/student_validator.py`
- **Description**: Add validation logic to ensure both email and name are provided and that the email format is valid.
- **Implementation**: Include regex pattern for email validation.
- [ ] Implement input validation logic for email format and requirements

### Task 7: Update Error Handling for Invalid Inputs
- **File**: `src/api/student.py`
- **Description**: Extend error handling to provide meaningful messages for missing or invalid email inputs.
- **Implementation**: Adjust response for 400 Bad Request when email is invalid or missing.
- [ ] Add error handling for missing or invalid email in student creation

### Task 8: Add Tests for Student Creation with Email
- **File**: `tests/test_student.py`
- **Description**: Write unit tests to cover scenarios involving email creation, including valid, missing, and invalid email formats.
- **Implementation**:
  ```python
  def test_create_student_with_valid_email():
      ...
  def test_create_student_with_missing_email():
      ...
  def test_create_student_with_invalid_email():
      ...
  ```
- [ ] Add unit tests for new email functionality for student creation

### Task 9: Add Tests for Retrieving Students
- **File**: `tests/test_student.py`
- **Description**: Ensure tests cover the retrieval of all students and that their email addresses are included in the response.
- **Implementation**:
  ```python
  def test_retrieve_students_includes_email():
      ...
  ```
- [ ] Add tests for verifying email inclusion in student retrieval

### Task 10: Update Documentation
- **File**: `README.md`
- **Description**: Update the documentation to include the new API endpoints, expected input formats, and example responses for the student creation and retrieval.
- [ ] Update README.md to reflect changes in API endpoints and usage

---

Prioritize the above tasks to ensure successful implementation through incremental development while maintaining continuous integration and testing throughout the process.