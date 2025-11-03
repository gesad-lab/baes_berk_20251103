# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- src/models.py (1000 bytes)
- src/services/course_service.py (800 bytes)
- src/api/routes.py (500 bytes)
- tests/api/test_routes.py (2815 bytes)
- tests/services/test_course_service.py (2260 bytes)

---

## Task Breakdown

### 1. Update Existing Code Files

- [ ] **Update Course Model to Add Foreign Key**
  - **File**: `src/models.py`
  - **Description**: Modify the `Course` class to include a new field `teacher_id` (foreign key referencing `Teacher`).
  
- [ ] **Implement Assign Teacher Logic**
  - **File**: `src/services/course_service.py`
  - **Description**: Add the function `assign_teacher_to_course(course_id: int, teacher_id: int) -> dict` to handle assigning a teacher to a course.

- [ ] **Implement Get Course Details Logic**
  - **File**: `src/services/course_service.py`
  - **Description**: Add the function `get_course_details(course_id: int) -> dict` to fetch course details including the assigned teacher.

- [ ] **Add Routes for Teacher Assignments**
  - **File**: `src/api/routes.py`
  - **Description**: Create new routes for `POST /courses/<course_id>/assign_teacher` and `GET /courses/<course_id>`.

### 2. Create New Files for New Functionality

- [ ] **Create Teacher Service Test File**
  - **File**: `tests/services/test_teacher_service.py`
  - **Description**: Set up tests for logic related to teacher assignments in the course service.

### 3. Integration Tasks

- [ ] **Database Migration for Foreign Key**
  - **File**: Migration script (generated via CLI)
  - **Description**: Use `Flask-Migrate` to create a migration that adds the `teacher_id` to the `Course` table.
    - Command: `flask db migrate -m "Add foreign key from Course to Teacher"`

- [ ] **Upgrade Database to Apply Migration**
  - **File**: Migration script (generated via CLI)
  - **Description**: Apply the migration to the database.
    - Command: `flask db upgrade`

### 4. Testing Tasks

- [ ] **Develop Integration Tests for New API Endpoints**
  - **File**: `tests/api/test_routes.py`
  - **Description**: Create tests for the new endpoints to validate correct behavior when assigning teachers and retrieving courses.

- [ ] **Develop Unit Tests for Service Logic**
  - **File**: `tests/services/test_course_service.py`
  - **Description**: Implement unit tests to ensure `assign_teacher_to_course` and `get_course_details` function correctly.

### 5. Documentation Task

- [ ] **Update README Documentation**
  - **File**: `README.md`
  - **Description**: Revise the README file to include instructions for the new API endpoints and how to use them.

### 6. Deployment Considerations

- [ ] **Verify Application Initialization**
  - **File**: Application startup process
  - **Description**: Test that the application starts without issues and the database schema updates correctly.

By completing these tasks, the team will successfully implement the desired functionality while adhering to existing code styles and structures.