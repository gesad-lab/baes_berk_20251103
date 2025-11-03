# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_teacher.py` (2530 bytes)

---

## Task Breakdown

### 1. Database Schema Updates
- [ ] **Update Course Model**: Modify the existing `src/db/models.py` to add the `teacher_id` field to the Course model.
  - **File**: `src/db/models.py`
  
- [ ] **Create Migration Script**: Add a migration script under `migrations/` to add the `teacher_id` column to the Course table using Alembic.
  - **File**: `migrations/xxxx_add_teacher_id_to_courses.py`

### 2. API Development
- [ ] **Implement PATCH Endpoint**: Update `src/api/course.py` to handle the PATCH request for assigning a teacher to a course.
  - **File**: `src/api/course.py`
  
- [ ] **Implement GET Endpoint**: Modify the existing GET API endpoint in `src/api/course.py` to include the teacher's name in the course details response.
  - **File**: `src/api/course.py`

### 3. Input Validation
- [ ] **Update Validation Logic**: Modify `src/validations/course_validators.py` to include validation for `teacher_id` to ensure it corresponds to an existing teacher.
  - **File**: `src/validations/course_validators.py`

### 4. Testing
- [ ] **Update Test Cases**: Add new test cases in `tests/test_course.py` to cover the new functionalities including success and error scenarios for the PATCH and GET endpoints.
  - **File**: `tests/test_course.py`

### 5. Documentation
- [ ] **Update README.md**: Add documentation for the new API endpoints related to assigning a teacher to a course and how to retrieve course details with teacher information.
  - **File**: `README.md`

### 6. Error Handling
- [ ] **Error Response Structure**: Ensure that `src/api/course.py` returns appropriate 400 Bad Request errors with correct JSON structure if the `teacher_id` is invalid or if the course doesn't exist.
  - **File**: `src/api/course.py`

### 7. Integration Tasks
- [ ] **Database Migration**: Run and test the database migration to ensure the `teacher_id` foreign key is added correctly without affecting existing data.
  - **Task**: Use Alembic to perform migration; no specific file, but it should be documented in migration logs.

---

Each task is designed to be independently executed and tested, helping ensure that the feature is added to the system cleanly, with appropriate documentation and error handling. Prioritize tasks related to database schema changes and API development first, as they will form the cornerstone of the new functionality.