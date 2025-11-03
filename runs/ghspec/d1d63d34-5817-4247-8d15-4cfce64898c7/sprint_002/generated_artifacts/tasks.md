# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models/student.py` (250 bytes)
- `src/services/student_service.py` (1500 bytes)
- `src/database/migrations/` (new migrations folder)
- `src/api/student_api.py` (800 bytes)
- `tests/services/test_student_service.py` (2528 bytes)

---

## Task Breakdown

### Database Migration
- [ ] **Task 1**: Create migration script to add `email` field to Student schema  
   **File Path**: `src/database/migrations/2023_10_30_add_email_to_student_table.py`  
   **Description**: Write an Alembic migration script to add the `email` column to the `student` table while preserving existing data. Include downgrade logic to remove the column.

### Update Models
- [ ] **Task 2**: Update the Student model to include the email field  
   **File Path**: `src/models/student.py`  
   **Description**: Modify the `Student` class to add an `email` attribute with appropriate type validation using Pydantic's `EmailStr`. Ensure all existing functionality and attributes remain intact.

### Implement CRUD Operations
- [ ] **Task 3**: Update `create_student` function to handle email  
   **File Path**: `src/services/student_service.py`  
   **Description**: Modify the `create_student` method to accept and process the email field when creating a new Student record. Ensure validation checks for email format.

- [ ] **Task 4**: Update `get_student` function to include email in response  
   **File Path**: `src/services/student_service.py`  
   **Description**: Adjust the `get_student` method to return the email of the student along with existing details when queried by ID.

- [ ] **Task 5**: Update `update_student` function to allow editing email  
   **File Path**: `src/services/student_service.py`  
   **Description**: Revise the `update_student` method to accept and modify the student's email address, along with other existing attributes.

- [ ] **Task 6**: Update `list_students` function to include email in response  
   **File Path**: `src/services/student_service.py`  
   **Description**: Modify the `list_students` method to return the list of all students, now including the email field.

### API Endpoints
- [ ] **Task 7**: Update API to support new email field in requests  
   **File Path**: `src/api/student_api.py`  
   **Description**: Modify the POST, GET, and PUT API endpoints to accept the email field in requests and return it in responses, including proper status codes for success and error cases.

### Testing
- [ ] **Task 8**: Write unit tests for creating a student with email  
   **File Path**: `tests/services/test_student_service.py`  
   **Description**: Implement tests to ensure that creating a Student with a valid name and email functions correctly and returns the expected response.

- [ ] **Task 9**: Write unit tests for retrieving a student by ID, including email  
   **File Path**: `tests/services/test_student_service.py`  
   **Description**: Create tests to validate that retrieving a student by ID returns correct details including the email address.

- [ ] **Task 10**: Write unit tests for updating a student's email  
   **File Path**: `tests/services/test_student_service.py`  
   **Description**: Implement tests to verify that updating a student's email functions as expected and is reflected in the response.

- [ ] **Task 11**: Write unit tests for listing all students with emails  
   **File Path**: `tests/services/test_student_service.py`  
   **Description**: Create tests that confirm the listing of all students includes their names and email addresses.

### Documentation
- [ ] **Task 12**: Update `README.md` to reflect new API changes  
   **File Path**: `README.md`  
   **Description**: Document the addition of the email field in the Student entity, including examples for all updated API endpoints.

- [ ] **Task 13**: Update `.env.example` if any new environment variables are necessary  
   **File Path**: `.env.example`  
   **Description**: Check if any new configurations are needed (e.g., for database connection if altered for the migration) and adjust accordingly.

---

This structured breakdown consists of focused and independently testable tasks that abide by the provided specifications and guidelines. Each task should be completed iteratively, with proper testing following each significant implementation to ensure correctness and maintainability.