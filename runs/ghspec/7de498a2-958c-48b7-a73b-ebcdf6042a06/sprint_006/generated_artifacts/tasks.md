# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models.py` (length before modification TBD)
- `src/api.py` (length before modification TBD)
- `src/services.py` (length before modification TBD)
- `src/database.py` (length before modification TBD)
- `tests/test_api.py` (1399 bytes)
- `tests/test_services.py` (1671 bytes)

---

## Task List

### 1. Modify Course Model
- **Task**: Update the `Course` model to include a `teacher_id` foreign key.
  - **File**: `src/models.py`
  - **Dependencies**: None
  - [ ] Update `src/models.py` to include `teacher_id` as a foreign key referencing the `Teacher` entity.

### 2. Create Database Migration
- **Task**: Create a migration to add the `teacher_id` field to the Course table.
  - **File**: `src/database.py`
  - **Dependencies**: Task 1
  - [ ] Implement Alembic migration steps in `src/database.py` to add the `teacher_id` column.

### 3. Implement API Endpoint for Assigning Teacher
- **Task**: Create the API endpoint to assign a teacher to a course.
  - **File**: `src/api.py`
  - **Dependencies**: Task 1, Task 2
  - [ ] Add `PUT /courses/{course_id}/assign_teacher` endpoint in `src/api.py`.

### 4. Implement API Endpoint for Retrieving Course Information
- **Task**: Modify the API endpoint to return teacher information along with course details.
  - **File**: `src/api.py`
  - **Dependencies**: Task 1
  - [ ] Update `GET /courses/{course_id}` response to include Teacher's details in `src/api.py`.

### 5. Implement API Endpoint for Removing Teacher
- **Task**: Create the API endpoint to remove a teacher from a course.
  - **File**: `src/api.py`
  - **Dependencies**: Task 1
  - [ ] Add `PUT /courses/{course_id}/remove_teacher` endpoint in `src/api.py`.

### 6. Add Business Logic for Assigning Teacher
- **Task**: Implement the logic for assigning a teacher to a course.
  - **File**: `src/services.py`
  - **Dependencies**: Task 1
  - [ ] Write a function in `src/services.py` to handle teacher assignment.

### 7. Add Business Logic for Removing Teacher
- **Task**: Implement the logic for removing a teacher from a course.
  - **File**: `src/services.py`
  - **Dependencies**: Task 1
  - [ ] Write a function in `src/services.py` to handle teacher removal.

### 8. Create Input Validation Models
- **Task**: Define Pydantic models for API request validation.
  - **File**: `src/api.py` (or separate `src/models/input_models.py`)
  - **Dependencies**: Task 1
  - [ ] Create request body validation models for assigning and removing teachers.

### 9. Implement Unit Tests for API
- **Task**: Write unit tests for the new API endpoints.
  - **File**: `tests/test_api.py`
  - **Dependencies**: Tasks 3, 4, 5
  - [ ] Add tests to validate assigning, retrieving, and removing teachers in `tests/test_api.py`.

### 10. Implement Unit Tests for Business Logic
- **Task**: Write unit tests for the business logic related to teacher assignments.
  - **File**: `tests/test_services.py`
  - **Dependencies**: Tasks 6, 7
  - [ ] Add tests to validate the business logic for assigning/removing teachers in `tests/test_services.py`.

### 11. Update Documentation
- **Task**: Update API documentation with new endpoints and functionality.
  - **File**: `README.md` or equivalent documentation
  - **Dependencies**: Tasks 3, 4, 5, 8
  - [ ] Ensure that all new endpoints and their purpose are documented.

### 12. Run Migrations and Test
- **Task**: Execute the database migrations and verify the application functionality.
  - **File**: Command line (not a code file)
  - **Dependencies**: Task 2
  - [ ] Run the migration command and test the application post-migration for integrity.

## Summary
This breakdown provides clear, actionable tasks that adhere to the structured approach needed for implementing the Teacher relationship with the Course entity. Each task is scoped to one file, ensuring focused implementation and easy testing.