# Tasks: Add Teacher Relationship to Course Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/routes.py` (API Endpoint logic)
- `tests/test_routes.py` (Existing test cases)

---

### Task 1: Update Course Model

- **File**: `src/models.py`
- **Description**: Add `teacher_id` field to the `Course` model to establish a relationship with the `Teacher` entity.
- **Task**:
  - Modify the `Course` class to include the `teacher_id` field.

```python
# Task
- [ ] Add `teacher_id` field to the Course model with foreign key reference to Teacher entity
```

---

### Task 2: Update Database Initialization Logic

- **File**: `src/database.py`
- **Description**: Incorporate the `teacher_id` foreign key reference in the database setup and ensure backward compatibility with existing data.
- **Task**:
  - Update initialization logic to create the new column for `teacher_id` in the Courses table.

```python
# Task
- [ ] Update `init_db()` function to include migration for adding `teacher_id` column
```

---

### Task 3: Create Migration Script

- **File**: `migrations/003_add_teacher_to_courses.py`
- **Description**: Create a migration script to add `teacher_id` column to the Courses table.
- **Task**:
  - Write the migration logic to safely add the column.

```python
# Task
- [ ] Create migration script to add `teacher_id` to Courses table and ensure it is nullable
```

---

### Task 4: Implement API Endpoint for Updating Courses

- **File**: `src/routes.py`
- **Description**: Implement the PATCH `/courses/{id}` endpoint to assign a teacher to a course.
- **Task**:
  - Add logic to handle requests to update course assignments, including validation and error handling.

```python
# Task
- [ ] Implement PATCH `/courses/{id}` endpoint to update course with teacher assignment
```

---

### Task 5: Implement API Endpoint for Fetching Course Details

- **File**: `src/routes.py`
- **Description**: Implement the GET `/courses/{id}` endpoint to fetch course details along with the assigned teacher.
- **Task**:
  - Add logic to return course details, including teacher information.

```python
# Task
- [ ] Implement GET `/courses/{id}` endpoint to retrieve course details with teacher info
```

---

### Task 6: Update API Response Format

- **File**: `src/routes.py`
- **Description**: Standardize API responses to ensure JSON format for error messages.
- **Task**:
  - Ensure all error responses follow the specified JSON structure.

```python
# Task
- [ ] Update error responses to return consistent JSON format for API endpoints
```

---

### Task 7: Write Unit Tests for Course Assignment Feature

- **File**: `tests/test_routes.py`
- **Description**: Develop tests to validate the functionality of the course assignment feature.
- **Task**:
  - Write tests for successful assignments, invalid course IDs, and non-existent teachers.

```python
# Task
- [ ] Add test cases for successful teacher assignment to course
- [ ] Add test case for assigning teacher to non-existent course (404)
- [ ] Add test case for assigning non-existent teacher to course (400)
```

---

### Task 8: Update Documentation

- **File**: `README.md`
- **Description**: Document the new API endpoints and schema changes in the project documentation.
- **Task**:
  - Add sections to the README that detail the new features regarding course and teacher assignments, including how to use the new endpoints.

```markdown
# Task
- [ ] Update README.md to reflect new API endpoints and database schema changes related to teacher assignments
```

---

### Task 9: Run/Verify Database Migrations

- **File**: `src/database.py`
- **Description**: Ensure the application initializes correctly and runs migrations to update the database schema.
- **Task**:
  - Run migrations and verify that `teacher_id` has been added to the Courses table.

```python
# Task
- [ ] Verify migrations run successfully and `teacher_id` exists in Courses table
```

---

This structured breakdown provides clear, independent tasks that can be executed sequentially while ensuring the integrity of the existing application architecture. Each task is designed to follow the existing coding conventions while focusing on the new teacher-course relationship feature.