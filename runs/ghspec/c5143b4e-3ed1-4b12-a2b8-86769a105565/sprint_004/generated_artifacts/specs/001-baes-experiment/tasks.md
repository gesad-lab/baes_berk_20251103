# Tasks: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- tests/test_courses.py (2149 bytes)

## Task Breakdown

### Task 1: Environment Setup
- **File**: `requirements.txt`
  - [ ] Add FastAPI, SQLAlchemy, and Alembic dependencies if not already listed in `requirements.txt`.
  
### Task 2: Update Models
- **File**: `src/models.py`
  - [ ] Create a junction table for the Student-Course relationship, adding the `student_courses` table definition as specified.
  
### Task 3: Implement CRUD Operations
- **File**: `src/crud.py`
  - [ ] Add method `link_courses_to_student(student_id: str, course_ids: List[str]) -> Student` to link courses to a student.
  - [ ] Add method `get_student_with_courses(student_id: str) -> Student` to retrieve student details along with enrolled courses.

### Task 4: Define Schemas
- **File**: `src/schemas.py`
  - [ ] Create a Pydantic model for the PATCH request to link courses: 
    ```python
    class StudentCoursesUpdate(BaseModel):
        courses: List[str]
    ```

### Task 5: Update Main Application
- **File**: `src/main.py`
  - [ ] Implement PATCH endpoint `/students/{student_id}` to link courses.
  - [ ] Implement GET endpoint `/students/{student_id}` to retrieve student information including linked courses.

### Task 6: Implement Validation Logic
- **File**: `src/main.py`
  - [ ] Add validation logic in the PATCH endpoint to ensure that all course IDs provided exist in the Courses table and return appropriate error messages.

### Task 7: Migration Setup
- **File**: `src/migrations/versions/`
  - [ ] Create a migration script using Alembic to add the `student_courses` table:
    ```bash
    alembic revision --autogenerate -m "Create student_courses table"
    ```

### Task 8: Write Unit Tests
- **File**: `tests/test_students.py`
  - [ ] Add tests for linking courses using the PATCH endpoint, ensuring that correct course data updates the student’s records.
  - [ ] Add tests for retrieving student details with courses using the GET endpoint.
  - [ ] Add tests for validation, ensuring appropriate error responses for invalid course IDs.

### Task 9: Update Documentation
- **File**: `README.md`
  - [ ] Revise the README to include new API capabilities related to course management, including details on the new endpoints, request, and response formats.

### Task 10: Execute Migration
- **File**: N/A (Command Line Task)
  - [ ] Run the migration command to apply the new `student_courses` table to the database:
    ```bash
    alembic upgrade head
    ```

## Ensure All Tasks Follow
- [ ] Confirm changes maintain existing code style and patterns.
- [ ] Ensure all tasks are independently testable and complete based on the functional requirements outlined.