# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models/student.py`
- `src/api/student.py`
- `src/tests/api/test_student.py`

---

## Task Breakdown

### Add Email Field to Student Model
- [ ] **Task 1**: Modify Student model to include `email` field  
  **File**: `src/models/student.py`  
  **Description**: Update the SQLAlchemy model to add a new `email` column, ensuring it is marked as required and includes a unique constraint. 
  ```python
  # Add these lines in the Student model
  email = Column(String, nullable=False)
  ```

### Update Database Migration
- [ ] **Task 2**: Implement Database Migration for Email Field  
  **File**: `src/database/migrations.py`  
  **Description**: Write migration logic to add the `email` column to the existing `students` table while preserving existing data.
  ```python
  def upgrade():
      with op.batch_alter_table("students") as batch_op:
          batch_op.add_column(Column("email", String, nullable=False))
  ```

### Update API Endpoints
- [ ] **Task 3**: Modify API endpoint to create a Student  
  **File**: `src/api/student.py`  
  **Description**: Update the POST `/students` endpoint to accept the `email` field in the request body and return it in the response.
  
- [ ] **Task 4**: Modify API endpoint to retrieve a Student  
  **File**: `src/api/student.py`  
  **Description**: Ensure the GET `/students/{id}` endpoint includes the `email` field in its response.

- [ ] **Task 5**: Modify API endpoint to update a Student  
  **File**: `src/api/student.py`  
  **Description**: Update the PUT `/students/{id}` endpoint to allow the modification of the `email` field.

### Implement Email Validation
- [ ] **Task 6**: Add email validation logic in the Service Layer  
  **File**: `src/services/student_service.py`  
  **Description**: Implement validation checks to ensure the provided email is in a valid format.

### Testing Changes
- [ ] **Task 7**: Update API tests for creating a Student  
  **File**: `src/tests/api/test_student.py`  
  **Description**: Add tests to verify that creating a student with a valid email works as expected and returns the correct response.

- [ ] **Task 8**: Update API tests for retrieving a Student  
  **File**: `src/tests/api/test_student.py`  
  **Description**: Ensure existing tests verify that the email is included when fetching student details.

- [ ] **Task 9**: Update API tests for updating a Student  
  **File**: `src/tests/api/test_student.py`  
  **Description**: Add tests to check that updating a student's email functions correctly.

- [ ] **Task 10**: Add tests for invalid email scenarios  
  **File**: `src/tests/api/test_student.py`  
  **Description**: Implement tests that verify the API response when a student is created with an invalid email format.

### Documentation
- [ ] **Task 11**: Update API documentation  
  **File**: `src/docs/api_documentation.md`  
  **Description**: Ensure the API documentation reflects the new `email` field in all relevant request and response schemas.

- [ ] **Task 12**: Update README.md  
  **File**: `README.md`  
  **Description**: Document the new email field and any necessary configuration changes needed for deployment.

---

## Completion Criteria
- Each file modification task is implemented and independently testable.
- All newly added functionality is covered by appropriate tests with a focus on correctness.
- Documentation is updated to provide clear guidance on changes made to the API.
- Application passes all tests related to the email field functionality.