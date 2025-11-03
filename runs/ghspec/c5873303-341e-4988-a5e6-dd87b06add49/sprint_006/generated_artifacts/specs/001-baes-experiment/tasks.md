# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models.py` (2050 bytes)
- `src/schemas.py` (1830 bytes)
- `src/routes/courses.py` (2900 bytes)
- `tests/test_courses.py` (1450 bytes)

Instructions for Task Breakdown:
1. Identify which existing files need modifications
2. Create new files for new functionality
3. Ensure integration tasks are included
4. Maintain consistency with existing code style and patterns

---

### Task 1: Update Course Model

- **File**: `src/models.py`
- **Description**: Modify the existing `Course` model to add a `teacher_id` foreign key.
- **Task**:
  ```python
  def update_course_model_with_teacher_id():
      # Add teacher_id column to the Course model in models.py
  ```
- [ ] Implement the new field in the Course class and add relationship.

---

### Task 2: Create Pydantic Schema for Assigning Teacher

- **File**: `src/schemas.py`
- **Description**: Create a new Pydantic schema for validating the request body for assigning a teacher to a course.
- **Task**:
  ```python
  def create_assign_teacher_schema():
      # Define AssignTeacher schema in schemas.py
  ```
- [ ] Define Pydantic model for `AssignTeacher` with `teacher_id`.

---

### Task 3: Create Pydantic Schema for Course Response

- **File**: `src/schemas.py`
- **Description**: Extend existing schemas to include a response model that includes a teacher's details.
- **Task**:
  ```python
  def create_course_response_schema():
      # Define CourseResponse schema in schemas.py
  ```
- [ ] Include `teacher` object in CourseResponse schema.

---

### Task 4: Implement Assign Teacher Endpoint

- **File**: `src/routes/teachers.py`
- **Description**: Create a new API route for assigning a teacher to a specific course.
- **Task**:
  ```python
  def create_assign_teacher_endpoint():
      # Add new POST endpoint in teachers.py
  ```
- [ ] Implement endpoint `POST /courses/{course_id}/assign_teacher`.

---

### Task 5: Implement Retrieve Course with Teacher Endpoint

- **File**: `src/routes/teachers.py`
- **Description**: Add a new endpoint for retrieving course details along with teacher information.
- **Task**:
  ```python
  def create_get_course_with_teacher_endpoint():
      # Add new GET endpoint in teachers.py
  ```
- [ ] Implement endpoint `GET /courses/{course_id}`.

---

### Task 6: Create Database Migration Script

- **File**: `src/database.py`
- **Description**: Implement a migration script that modifies the courses table to add the `teacher_id` field.
- **Task**:
  ```python
  def create_migration_script():
      # Write migration script to add teacher_id to courses table
  ```
- [ ] Write SQL script or use Alembic to alter the Course table.

---

### Task 7: Implement Unit Tests for Assign Teacher Functionality

- **File**: `tests/test_teachers.py`
- **Description**: Write unit tests for the functionality of assigning teachers to courses.
- **Task**:
  ```python
  def test_assign_teacher_to_course():
      # Write a test case for the successful assignment of a teacher
  ```
- [ ] Create tests for successful and unsuccessful assignment scenarios.

---

### Task 8: Implement Unit Tests for Retrieve Course with Teacher Functionality

- **File**: `tests/test_teachers.py`
- **Description**: Write tests to verify the response when retrieving course details with associated teacher.
- **Task**:
  ```python
  def test_retrieve_course_with_teacher():
      # Write a test case to ensure course retrieval includes teacher data
  ```
- [ ] Include tests that validate both presence and absence of the teacher.

---

### Task 9: Update README with New Endpoints

- **File**: `README.md`
- **Description**: Update documentation to reflect new API endpoints for assigning teachers and retrieving course information.
- **Task**:
  ```markdown
  def update_api_documentation():
      # Add endpoint information for POST /courses/{course_id}/assign_teacher and GET /courses/{course_id}
  ```
- [ ] Ensure the README reflects any changes in the API usage and functionality.

--- 

### Task 10: Hold Review for Implementation

- **File**: `N/A`
- **Description**: Organize a code review session to discuss changes and ensure coherence with existing functionality.
- **Task**:
  ```markdown
  def organize_code_review():
      # Schedule a meeting for the team to review the changes made
  ```
- [ ] Collect feedback and make necessary adjustments before merging.

--- 

This structured breakdown provides clear tasks focusing on specific files and functionalities while ensuring that essential integration aspects and validation mechanisms are addressed. Each task is independently testable to allow for smooth execution and evaluation.