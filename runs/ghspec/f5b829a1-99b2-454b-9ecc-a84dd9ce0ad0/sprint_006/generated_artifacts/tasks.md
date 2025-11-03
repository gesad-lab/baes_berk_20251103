# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models.py` (existing Course and Teacher models)
- `src/services/course_service.py` (utilities related to Course service)
- `tests/api/test_routes.py` (existing API tests)

---

## Task Breakdown

### 1. Update Database Schema

- [ ] **1.1** Create migration file for adding `teacher_id` to `courses` table  
  **File:** `migrations/versions/<timestamp>_add_teacher_id_to_courses.py`  
  **Details:** Implement migration to add `teacher_id` foreign key in courses.

### 2. Modify Course Model

- [ ] **2.1** Update `Course` model to include `teacher_id`  
  **File:** `src/models.py`  
  **Details:** Add `teacher_id` column to the `Course` class with necessary relationships.

### 3. Create CourseService Logic

- [ ] **3.1** Implement method for assigning a teacher in CourseService  
  **File:** `src/services/course_service.py`  
  **Details:** Create `assign_teacher(course_id: int, teacher_id: int)` method with necessary validations.

- [ ] **3.2** Implement method for unassigning a teacher in CourseService  
  **File:** `src/services/course_service.py`  
  **Details:** Create `unassign_teacher(course_id: int)` method to set `teacher_id` to `None`.

### 4. Add API Endpoints

- [ ] **4.1** Define route for assigning a teacher to a course  
  **File:** `src/main.py`  
  **Details:** Add `PUT /courses/{course_id}/assign-teacher` endpoint and link it to the `assign_teacher` service method.

- [ ] **4.2** Define route for unassigning a teacher from a course  
  **File:** `src/main.py`  
  **Details:** Add `DELETE /courses/{course_id}/unassign-teacher` endpoint and link it to the `unassign_teacher` service method.

### 5. Create Tests

- [ ] **5.1** Create tests for assigning a teacher to a course  
  **File:** `tests/api/test_routes.py`  
  **Details:** Write tests for successful assignment and error handling for `assign-teacher` endpoint.

- [ ] **5.2** Create tests for unassigning a teacher from a course  
  **File:** `tests/api/test_routes.py`  
  **Details:** Write tests for successful unassignment for `unassign-teacher` endpoint.

- [ ] **5.3** Create business logic tests for CourseService  
  **File:** `tests/services/test_course_service.py`  
  **Details:** Write tests to cover assignment and unassignment logic in `CourseService`.

### 6. Documentation and Error Handling

- [ ] **6.1** Update API documentation for new endpoints  
  **File:** `docs/api.md`  
  **Details:** Document request and response structures for `assign-teacher` and `unassign-teacher` endpoints.

- [ ] **6.2** Ensure structured error responses are implemented  
  **File:** `src/main.py`  
  **Details:** Confirm that endpoints return appropriate error codes and messages.

### 7. Run Migrations

- [ ] **7.1** Run database migrations to update the schema  
  **File:** Command line operation  
  **Details:** Execute the migration file to apply changes in the database schema.

--- 

This task breakdown ensures clarity and focus on implementing the feature in a modular and testable manner while adhering to the existing code styles and projects' architectural patterns.