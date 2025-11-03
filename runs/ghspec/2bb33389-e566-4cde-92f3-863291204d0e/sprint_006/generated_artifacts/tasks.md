# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models.py` (existing models for Course and Teacher)
- `src/api.py` (existing API routes for courses)
- `tests/test_integration/test_teacher_api.py` (existing integration tests)

## Task Breakdown

### Task 1: Update Course Model
- **File**: `src/models.py`
- Task: Extend the `Course` model to include the `teacher_id` foreign key and corresponding relationship to the `Teacher` model.
- Dependencies: None
- Testability: Check that the `Course` model includes the new `teacher_id` and validates relationships.

```markdown
- [ ] Extend the Course model in `src/models.py` to include `teacher_id` as a foreign key.
```

### Task 2: Create Migration Script
- **File**: `migrations/versions/add_teacher_relationship.py`
- Task: Create an Alembic migration script to add the `teacher_id` column to the `courses` table.
- Dependencies: Task 1 (Course model update)
- Testability: Run the migration and ensure the database schema is updated.

```markdown
- [ ] Create migration script in `migrations/versions/` to add `teacher_id` to `courses`.
```

### Task 3: Implement Assign Teacher API Endpoint
- **File**: `src/api.py`
- Task: Implement the `POST /courses/:course_id/assign-teacher` endpoint to assign a teacher to a course.
- Dependencies: Task 1 (Course model update)
- Testability: Ensure the endpoint works as specified and handles appropriate error responses.

```markdown
- [ ] Implement `POST /courses/:course_id/assign-teacher` in `src/api.py`.
```

### Task 4: Implement Retrieve Course API Endpoint
- **File**: `src/api.py`
- Task: Implement the `GET /courses/:course_id` endpoint to retrieve course details including the assigned teacher.
- Dependencies: Task 1 (Course model update)
- Testability: Ensure the endpoint returns course and teacher details as specified.

```markdown
- [ ] Implement `GET /courses/:course_id` in `src/api.py`.
```

### Task 5: Add Input Validation for API Requests
- **File**: `src/api.py`
- Task: Add input validation for the `POST /courses/:course_id/assign-teacher` endpoint to check the existence of course ID and teacher ID.
- Dependencies: Task 3 (Assign Teacher API Endpoint)
- Testability: Verify that validation errors return the correct responses.

```markdown
- [ ] Add input validation for IDs in `POST /courses/:course_id/assign-teacher` in `src/api.py`.
```

### Task 6: Update Error Handling for API Requests
- **File**: `src/api.py`
- Task: Implement error handling to return specific error responses for non-existent courses and teachers.
- Dependencies: Task 3 (Assign Teacher API Endpoint), Task 4 (Retrieve Course API Endpoint)
- Testability: Confirm that appropriate error messages are returned.

```markdown
- [ ] Implement error handling for course and teacher not found in `src/api.py`.
```

### Task 7: Create Integration Tests for New Endpoints
- **File**: `tests/test_integration/test_teacher_api.py`
- Task: Develop tests to cover the new assignment and retrieval functionality for courses and teachers, including edge cases.
- Dependencies: Task 3 (Assign Teacher API Endpoint), Task 4 (Retrieve Course API Endpoint)
- Testability: Run tests to ensure both endpoints function correctly.

```markdown
- [ ] Create integration tests for new API endpoints in `tests/test_integration/test_teacher_api.py`.
```

### Task 8: Update OpenAPI Documentation
- **File**: `src/api.py`
- Task: Update the OpenAPI documentation to include the new API endpoints for assigning teachers and retrieving course details.
- Dependencies: Task 3 (Assign Teacher API Endpoint), Task 4 (Retrieve Course API Endpoint)
- Testability: Check that the documentation reflects the new functionality.

```markdown
- [ ] Update OpenAPI documentation in `src/api.py` for new endpoints.
```

### Task 9: Verify Database Migration at Startup
- **File**: `src/main.py`
- Task: Ensure the database migration script runs during application startup to maintain schema integrity.
- Dependencies: Task 2 (Create Migration Script)
- Testability: Confirm that the app starts without errors and the migration is applied.

```markdown
- [ ] Verify migration script execution during app startup in `src/main.py`.
```

Each task is designed to focus on a single file and can be executed independently, ensuring modular development and facilitating easy testing as part of a cohesive implementation process.