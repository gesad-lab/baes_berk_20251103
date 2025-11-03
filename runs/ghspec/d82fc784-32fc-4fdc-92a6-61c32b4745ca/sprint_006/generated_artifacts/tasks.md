# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/api/test_teacher_routes.py` (2133 bytes)
- `tests/migration/test_migration_integration.py` (3343 bytes)
- `tests/services/test_teacher_service.py` (2284 bytes)

---

## Task Breakdown

### 1. Modify Course Model
- **Task**: Update the `Course` model to include `teacher_id`.
- **File**: `src/models.py`
- **Description**: Add a `teacher_id` column to the existing `Course` class and establish a relationship with the `Teacher` class.
- **Dependencies**: None
- [ ] Update `Course` class in `src/models.py`.

### 2. Create Migration Script
- **Task**: Implement the migration script to alter the `courses` table.
- **File**: `migrations/versions/add_teacher_relationship.py`
- **Description**: Create a new migration file that adds a `teacher_id` column to the `courses` table and manages its foreign key relationship with the `teachers` table.
- **Dependencies**: Task 1 (Course Model update)
- [ ] Create migration script in `migrations/versions/add_teacher_relationship.py`.

### 3. Develop Update Course API Endpoint
- **Task**: Implement the API endpoint to assign a teacher to a course.
- **File**: `src/api/routes/course_routes.py`
- **Description**: Add a `PATCH` endpoint for updating a course with a specified `teacher_id`.
- **Dependencies**: Task 1 (Course Model update)
- [ ] Add `PATCH /courses/{course_id}` endpoint to `src/api/routes/course_routes.py`.

### 4. Develop Retrieve Course API Endpoint
- **Task**: Implement the API endpoint to retrieve a course with associated teacher details.
- **File**: `src/api/routes/course_routes.py`
- **Description**: Add a `GET` endpoint that returns course details including teacher information, if available.
- **Dependencies**: Task 1 (Course Model update)
- [ ] Add `GET /courses/{course_id}` endpoint to `src/api/routes/course_routes.py`.

### 5. Update Tests for Course Updates
- **Task**: Create unit tests for updating a course with a teacher.
- **File**: `tests/api/test_teacher_routes.py`
- **Description**: Write tests to verify that the `PATCH` endpoint correctly updates the course with the provided `teacher_id`.
- **Dependencies**: Task 3 (Update Course API Endpoint)
- [ ] Add tests in `tests/api/test_teacher_routes.py` for updating course with teacher.

### 6. Update Tests for Retrieve Course
- **Task**: Create unit tests for retrieving a course with a teacher.
- **File**: `tests/api/test_teacher_routes.py`
- **Description**: Write tests to ensure that the `GET` endpoint correctly retrieves the course details along with the teacher's information.
- **Dependencies**: Task 4 (Retrieve Course API Endpoint)
- [ ] Add tests in `tests/api/test_teacher_routes.py` for retrieving course with teacher.

### 7. Validate Migration Integration Tests
- **Task**: Write integration tests to verify existing data integrity after migration.
- **File**: `tests/migration/test_migration_integration.py`
- **Description**: Implement tests to confirm that the existing records in the `Student`, `Course`, and `Teacher` tables are not affected by the schema changes.
- **Dependencies**: Task 2 (Create Migration Script)
- [ ] Add integration tests in `tests/migration/test_migration_integration.py`.

### 8. Document API Contracts
- **Task**: Update API documentation to reflect new endpoints.
- **File**: `docs/api_reference.md`
- **Description**: Ensure that the API documentation includes information on the new endpoints and their expected request/response formats.
- **Dependencies**: Tasks 3 and 4 (API Endpoints)
- [ ] Update API documentation in `docs/api_reference.md` with new endpoint details.

### 9. Test Coverage Implementation
- **Task**: Ensure test coverage for the new functionalities meets required thresholds.
- **File**: `pytest.ini`
- **Description**: Verify that unit and integration tests provide at least 70% coverage for the new functionalities, focusing on critical paths for course-teacher relationships.
- **Dependencies**: Tasks 5, 6, and 7 (Testing)
- [ ] Update test coverage settings in `pytest.ini`.

### 10. Perform Migration Testing
- **Task**: Validate the migration script in a test database.
- **File**: `tests/migration/test_migration_integration.py`
- **Description**: Execute the migration script and confirm the `courses` table is updated correctly.
- **Dependencies**: Task 2 (Create Migration Script)
- [ ] Run migration test in `tests/migration/test_migration_integration.py`.

---
Each task should be independently testable, ensuring that the entire implementation can be developed incrementally while aligning with existing project conventions.