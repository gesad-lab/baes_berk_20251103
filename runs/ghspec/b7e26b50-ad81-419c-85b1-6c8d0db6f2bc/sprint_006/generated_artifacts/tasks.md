# Tasks: Add Teacher Relationship to Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `models.py` (define models including Course and Teacher)
- `api.py` (handles API requests)
- `errors.py` (centralized error handling)
- `tests/test_api.py` (contains existing tests)

---

### Task List

#### 1. Update Database Models

- [ ] **Task 1.1**: Add `teacher_id` field to `Course` model in `src/models.py`  
  **File**: `src/models.py`  
  **Description**: Modify the `Course` class to include `teacher_id` as an integer foreign key referencing the `Teacher`.  
  ```python
  teacher_id = Column(Integer, ForeignKey('teachers.id'))  # Relationship with Teacher
  ```

- [ ] **Task 1.2**: Create migration script to add `teacher_id` to `courses` table  
  **File**: `src/migrations/versions/<timestamp>_add_teacher_id_to_courses.py`  
  **Description**: Write a migration script to alter the `courses` table and add the `teacher_id` field, ensuring all existing data remains intact. Use Flask-Migrate to create this.  

#### 2. Implement API Endpoint

- [ ] **Task 2.1**: Add PATCH endpoint for assigning teacher to course in `src/api.py`  
  **File**: `src/api.py`  
  **Description**: Implement the logic for `PATCH /courses/{id}` to update the course with a `teacher_id`, including input validation and response formatting.  

#### 3. Handle Errors

- [ ] **Task 3.1**: Implement centralized error handling for course and teacher assignment in `src/errors.py`  
  **File**: `src/errors.py`  
  **Description**: Create utility functions to handle 404 errors for invalid course and teacher IDs, ensuring consistent response structure.  

#### 4. Write Tests

- [ ] **Task 4.1**: Write unit tests for the teacher assignment functionality in `tests/test_api.py`  
  **File**: `tests/test_api.py`  
  **Description**: Add tests to validate the API behavior for assigning teachers to courses, including successful assignments and handling of invalid IDs. Ensure at least 70% coverage for new functionality.  

#### 5. Update Documentation

- [ ] **Task 5.1**: Update `README.md` to document new API endpoint  
  **File**: `README.md`  
  **Description**: Add documentation for the `PATCH /courses/{id}` endpoint, detailing request body structure, response formats, and error messages.  
   
- [ ] **Task 5.2**: Include docstrings in new functions and classes in `src/api.py` and `src/errors.py`  
  **File**: `src/api.py`, `src/errors.py`  
  **Description**: Ensure all new API functions and error handling methods have appropriate docstrings explaining their purpose, parameters, and return values.  

#### 6. Review & Test Migration

- [ ] **Task 6.1**: Verify database migration  
  **File**: Project database configuration  
  **Description**: Test the migration on a local development database to ensure it executes without errors and all data is preserved.  
   
---

### Task Execution Notes:
- Each task should be executed independently to maintain focus and allow for specific testing.
- Ensure that all changes adhere to the existing code style and patterns within the project.
- Integration tests should be considered after implementing the individual unit tests to confirm feature reliability.