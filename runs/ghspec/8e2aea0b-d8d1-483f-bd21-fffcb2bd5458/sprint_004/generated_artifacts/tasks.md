# Tasks: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_routes.py` (2537 bytes)
- `tests/test_models.py` (1984 bytes)

---

## Task Breakdown

### Model Updates
- [ ] **Task 1**: Update the Student model to include an array of course IDs  
  **File**: `src/models.py`  
  **Details**: Modify the `Student` class to add a field for `courses` (array of integers) and update the constructor.

- [ ] **Task 2**: Create the Course model  
  **File**: `src/models.py`  
  **Details**: Define the `Course` class with fields for `id`, `name`, and `level`. Ensure it adheres to requirements.

### Database Migrations
- [ ] **Task 3**: Create migration script for database schema changes  
  **File**: `src/db.py`  
  **Details**: Write a script to alter the `students` table to add a `courses` column and create a new `courses` table. Implement the SQL commands from the specification.

### Input Validation
- [ ] **Task 4**: Create Marshmallow schema for Course  
  **File**: `src/schemas.py`  
  **Details**: Define a new schema for validating course-related data conforming to required fields.

- [ ] **Task 5**: Update Student schema to include course validation  
  **File**: `src/schemas.py`  
  **Details**: Modify the existing Student schema to validate the courses field appropriately.

### API Route Definitions
- [ ] **Task 6**: Define route for enrolling a student in a course  
  **File**: `src/routes.py`  
  **Details**: Implement the `POST /students/{student_id}/enroll` endpoint, including validation and success/error response handling.

- [ ] **Task 7**: Define route for retrieving courses associated with a student  
  **File**: `src/routes.py`  
  **Details**: Implement the `GET /students/{student_id}/courses` endpoint to return a list of courses for a student.

### Error Handling
- [ ] **Task 8**: Enhance error handling for non-existent course enrollment  
  **File**: `src/routes.py`  
  **Details**: Implement error responses according to specifications for invalid course IDs when enrolling students.

### Testing
- [ ] **Task 9**: Update unit tests for Student model  
  **File**: `tests/test_models.py`  
  **Details**: Add tests to validate that the Student model can handle course ID assignments correctly.

- [ ] **Task 10**: Create tests for enroll student in course functionality  
  **File**: `tests/test_routes.py`  
  **Details**: Implement tests to validate both successful enrollment and error handling for enrolling students in courses.

- [ ] **Task 11**: Create tests for retrieving courses for a student  
  **File**: `tests/test_routes.py`  
  **Details**: Confirm that the endpoint for retrieving a student’s courses returns the correct format and data.

### Documentation
- [ ] **Task 12**: Update README.md with new API endpoints  
  **File**: `README.md`  
  **Details**: Document the new functionalities, including details for the updated models, API endpoints, and usage.

---

This structured task breakdown is designed to facilitate incremental development while ensuring each task is scoped to a single file and can be executed and tested independently.