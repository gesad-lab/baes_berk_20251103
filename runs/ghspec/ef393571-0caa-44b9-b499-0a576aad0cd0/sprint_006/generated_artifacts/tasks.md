# Tasks: Add Teacher Relationship to Course Entity

---

## Task Breakdown

### Task 1: Update Course Model

- **File**: `api/models/courses.py`
- **Description**: Update the `Course` model to include a `teacher_id` attribute.
- **Action Items**:
  - Add `teacher_id: Optional[int]` to the `Course` Pydantic model.

- [ ] Update the Course Pydantic model to include `teacher_id`.

---

### Task 2: Modify Course Database Schema

- **File**: `migrations/add_teacher_relationship.py`
- **Description**: Create a migration script to add the `teacher_id` column to the `Course` table.
- **Action Items**:
  - Implement a function to execute the SQL command: 
    ```sql
    ALTER TABLE course ADD COLUMN teacher_id INTEGER REFERENCES teacher(id);
    ```
  - Ensure this migration retains existing data integrity.

- [ ] Create migration script to add `teacher_id` to Course table.

---

### Task 3: Create API Endpoint for Updating Courses

- **File**: `api/courses.py`
- **Description**: Create a PATCH endpoint to update a Course entity with a teacher association.
- **Action Items**:
  - Implement the endpoint `/courses/{course_id}` to accept a `CourseUpdateRequest` payload.
  - Write logic to validate teacher associations to prevent overlapping course assignments.
  - Update the course and return a `CourseResponse`.

- [ ] Implement PATCH endpoint to update course with teacher association.

---

### Task 4: Create API Endpoint for Retrieving Course Details

- **File**: `api/courses.py`
- **Description**: Create a GET endpoint to fetch course details, including associated teacher information.
- **Action Items**:
  - Implement the endpoint `/courses/{course_id}` to return course details including `teacher_id`.

- [ ] Implement GET endpoint to retrieve course details with associated teacher.

---

### Task 5: Validation Logic for Teacher Assignment

- **File**: `api/courses.py`
- **Description**: Implement validation to check for overlapping course assignments when assigning a teacher.
- **Action Items**:
  - Write a function to check existing course schedules against the requested teacher's courses.

- [ ] Implement validation to prevent overlapping course assignments.

---

### Task 6: Update Documentation with New Endpoints

- **File**: `README.md`
- **Description**: Update the documentation to include new API endpoints for the Course-Teacher relationship.
- **Action Items**:
  - Add sections to document the new PATCH and GET endpoints including request/response formats.

- [ ] Update README.md for Course-Teacher API documentation.

---

### Task 7: Write Unit Tests for Course Update API

- **File**: `tests/api/test_courses.py`
- **Description**: Create unit tests for the PATCH endpoint and validation logic.
- **Action Items**:
  - Ensure tests cover successful updates, validation failures, and checking for overlapping assignments.

- [ ] Write unit tests for course update functionality.

---

### Task 8: Write Integration Tests for Database Migration

- **File**: `tests/integration/test_migration.py`
- **Description**: Write integration tests to confirm the migration correctly updates the database schema without data loss.
- **Action Items**:
  - Verify that existing Course and Teacher data remains intact after the migration.

- [ ] Create integration tests for database migration.

---

These tasks break down the implementation of the "Add Teacher Relationship to Course Entity" into manageable pieces, ensuring that each can be executed and tested independently while maintaining a consistent approach to coding standards.