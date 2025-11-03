# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models.py` (Existing Course and Teacher models)
- `src/schemas.py` (Existing Pydantic schemas)
- `src/routes/course_routes.py` (Existing course API endpoints)
- `tests/test_course_routes.py` (Existing course API tests)
- `src/database.py` (Database connection and setup)

---

## Task Breakdown

### Task 1: Update Course Model to Include Teacher Relationship
- **File**: `src/models.py`
- **Description**: Modify the existing Course SQLAlchemy model to add a new field `teacher_id` which will reference the Teacher entity.
- **Dependencies**: None

```
- [ ] Update Course model to include teacher_id field.
  - File: src/models.py
```

### Task 2: Update Pydantic Schemas for Teacher Association
- **File**: `src/schemas.py`
- **Description**: Modify existing Pydantic schemas to support the new API for associating a teacher with a course, particularly for the request and response format.
- **Dependencies**: Task 1

```
- [ ] Update Pydantic schemas to include teacherId for course assignment.
  - File: src/schemas.py
```

### Task 3: Implement API Endpoint for Associating Teacher with Course
- **File**: `src/routes/course_routes.py`
- **Description**: Create the new API endpoint `POST /courses/{courseId}/assignTeacher` to handle requests for associating a teacher with a course.
- **Dependencies**: Task 2

```
- [ ] Implement POST /courses/{courseId}/assignTeacher API endpoint.
  - File: src/routes/course_routes.py
```

### Task 4: Modify Database Schema for Teacher Relationship
- **File**: `src/database.py`
- **Description**: Update the database initialization process to add the `teacher_id` column in the Courses table.
- **Dependencies**: Task 1

```
- [ ] Update database initialization to include teacher_id foreign key.
  - File: src/database.py
```

### Task 5: Create Database Migration Script
- **File**: `migrations/versions/YYYYMMDDHHMMSS_add_teacher_id_to_courses.py` (to be created)
- **Description**: Create a new Alembic migration script to add the `teacher_id` foreign key column to the Courses table while preserving existing data.
- **Dependencies**: Task 4

```
- [ ] Create Alembic migration to add teacher_id to Courses.
  - File: migrations/versions/YYYYMMDDHHMMSS_add_teacher_id_to_courses.py
```

### Task 6: Write Unit Tests for Teacher Association Functionality
- **File**: `tests/test_course_routes.py`
- **Description**: Develop unit tests for the new functionality to ensure the API correctly associates a teacher with a course and handles non-existent teacher scenarios properly.
- **Dependencies**: Task 3

```
- [ ] Write unit tests for teacher assignment API behavior.
  - File: tests/test_course_routes.py
```

### Task 7: Update Documentation for New API Endpoint
- **File**: `README.md`
- **Description**: Update the README file to include usage instructions and example requests for the newly implemented API endpoint that associates teachers with courses.
- **Dependencies**: Task 3

```
- [ ] Update README.md with new API endpoint details.
  - File: README.md
```

### Task 8: Validate Error Handling for Invalid Teacher ID
- **File**: `src/routes/course_routes.py`
- **Description**: Ensure that the error handling for API responses is correctly implemented and that appropriate error messages are returned when a non-existent teacher ID is provided.
- **Dependencies**: Task 3

```
- [ ] Validate error handling for non-existent teacher associations.
  - File: src/routes/course_routes.py
```

### Task 9: Verify Migration Impact on Existing Data
- **File**: Test database migrations (to be conducted as part of integration testing)
- **Description**: Ensure through integration testing that existing data (Students and Courses) remains intact after the migration is applied.
- **Dependencies**: Task 5

```
- [ ] Conduct integration tests to verify existing data integrity post-migration.
  - File: N/A (Test database migration)
```

---

With this task breakdown, each task is clearly defined and scoped to a single file, providing a structured approach to implementing the feature to add a teacher relationship to the Course entity while adhering to the guidelines stated.