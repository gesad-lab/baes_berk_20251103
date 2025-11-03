# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models/student.py` (existing model file)
- `src/routes/student_routes.py` (existing routes file)
- `tests/test_student_routes.py` (existing test file for student routes)
- `tests/test_student.py` (existing test file for student model)

---

## Task Breakdown

### Database Schema Update
- [ ] **Task 1**: Update the `Student` model to include `email` field.  
    **File**: `src/models/student.py`  
    **Details**: Modify the existing `Student` class to add `email` as a `Column` of type `String`, set to `nullable=False` and `unique=True`.  
    - Implementation:  
    ```python
    class Student(Base):
        __tablename__ = 'students'
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String, nullable=False)
        email = Column(String, nullable=False, unique=True)  # New field
    ```

### Database Migration
- [ ] **Task 2**: Create migration script to add `email` field to the `Student` table.  
    **File**: `migrations/versions/<unique_migration_id>_add_email_to_student.py`  
    **Details**: Implement `upgrade` and `downgrade` functions for schema migration using Alembic.  
    - Implementation:  
    ```python
    def upgrade():
        op.add_column('students', sa.Column('email', sa.String(), nullable=False))
        op.create_unique_constraint('uq_student_email', 'students', ['email'])

    def downgrade():
        op.drop_constraint('uq_student_email', 'students', type_='unique')
        op.drop_column('students', 'email')
    ```

### API Development
- [ ] **Task 3**: Modify the `/students` POST endpoint to accept `email` in the request body.  
    **File**: `src/routes/student_routes.py`  
    **Details**: Update the endpoint logic to validate the email presence and formatting before creating a student.  
    - Implementation: Add validation and response handling within the `create_student` function.

- [ ] **Task 4**: Update the `/students/{id}` GET endpoint to include the `email` field in the response.  
    **File**: `src/routes/student_routes.py`  
    **Details**: Ensure the endpoint fetches and returns the email along with the student's ID and name.  

### Input Validation
- [ ] **Task 5**: Implement input validation for email format and uniqueness in the `create_student` function.  
    **File**: `src/routes/student_routes.py`  
    **Details**: Implement regex validation for the email format and check for uniqueness before creating a new student entry. 

### Testing
- [ ] **Task 6**: Extend unit tests to cover scenarios involving the new email field.  
    **File**: `tests/test_student.py`  
    **Details**: Write test cases that check creation of a student with valid email, handling of missing email, and handling of invalid email format.  
  
- [ ] **Task 7**: Update integration tests for the `/students` API to check email-related scenarios.  
    **File**: `tests/test_student_routes.py`  
    **Details**: Ensure that tests cover creating students with valid and invalid email formats, including assertions for error handling.

### Documentation
- [ ] **Task 8**: Update API documentation to include new email field requirements and formats.  
    **File**: `docs/api_documentation.md`  
    **Details**: Reflect changes in API routes, including input and output specifications for the `email` field for both creation and retrieval.

- [ ] **Task 9**: Update README.md with new setup instructions and migration instructions.  
    **File**: `README.md`  
    **Details**: Ensure instructions on running migrations and any other relevant changes are clearly stated for local development.

### Error Handling
- [ ] **Task 10**: Implement structured error responses for invalid email inputs in the API.  
    **File**: `src/routes/student_routes.py`  
    **Details**: Modify the error handling logic to provide user-friendly responses for invalid email inputs. 

---

By completing the above tasks, the application’s student management functionality will be incrementally enhanced to include an email field while ensuring all existing features remain operational and correctly integrated.