# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models/student.py` (location for model update)
- `tests/test_student.py` (location for unit tests)

---

## Task Breakdown

### Update Model
- [ ] **Task 1**: Update the Student model to include the new `email` field.  
    - **File**: `src/models/student.py`  
    - **Description**: Modify the `Student` class to add the `email` attribute as a required field.
    
### Migrations
- [ ] **Task 2**: Create Alembic migration script to add the email field.  
    - **File**: `migrations/versions/`  
    - **Description**: Use the command `alembic revision --autogenerate -m "Add email to Student entity"` to generate migration code that includes the new `email` column while preserving existing data.

- [ ] **Task 3**: Apply the migration to update the database schema.  
    - **File**: N/A (command line task)  
    - **Description**: Run `alembic upgrade head` to apply the migration and modify the existing `students` table.

### Update API Routes
- [ ] **Task 4**: Create API route for creating students.  
    - **File**: `src/routes/students.py`  
    - **Description**: Implement the POST `/students` endpoint that accepts `{"name": "string", "email": "string"}`.

- [ ] **Task 5**: Create API route for retrieving students.  
    - **File**: `src/routes/students.py`  
    - **Description**: Implement the GET `/students` endpoint that returns a JSON array of students including their emails.

- [ ] **Task 6**: Create API route for updating a student's email.  
    - **File**: `src/routes/students.py`  
    - **Description**: Implement the PUT `/students/{id}` endpoint that updates the email field for a specific student.

### Implement Validation
- [ ] **Task 7**: Add validation for email field on student creation.  
    - **File**: `src/controllers/student_controller.py`  
    - **Description**: Implement validation logic to ensure the email field is present and in a valid format when creating a new student record.

- [ ] **Task 8**: Add validation for email on student update.  
    - **File**: `src/controllers/student_controller.py`  
    - **Description**: Implement logic to validate the email format when the student’s email is being updated.

### Testing
- [ ] **Task 9**: Write unit tests for creating a student with valid data.  
    - **File**: `tests/test_student.py`  
    - **Description**: Create a test case to ensure that a student can be successfully created when a valid name and email are provided.

- [ ] **Task 10**: Write unit tests for creating a student without an email.  
    - **File**: `tests/test_student.py`  
    - **Description**: Create a test case to validate that an error is returned when attempting to create a student without an email.

- [ ] **Task 11**: Write unit tests for retrieving students.  
    - **File**: `tests/test_student.py`  
    - **Description**: Create a test case to ensure that retrieving students returns the correct list with names and emails.

- [ ] **Task 12**: Write unit tests for updating student email successfully.  
    - **File**: `tests/test_student.py`  
    - **Description**: Create a test case for the functionality that updates a student's email, ensuring the email is updated correctly in the database.

- [ ] **Task 13**: Write unit tests for updating student email with invalid format.  
    - **File**: `tests/test_student.py`  
    - **Description**: Create a test case that checks if an error is returned when an invalid email format is submitted during an update.

### Documentation
- [ ] **Task 14**: Update README.md with API usage documentation.  
    - **File**: `README.md`  
    - **Description**: Document how to use the new API endpoints, including request formats and expected responses.

---

This breakdown ensures that the project follows a logical path from model updates, through migration, route definition, and validation, culminating in thorough testing and documentation, all while adhering to the established coding standards and practices.