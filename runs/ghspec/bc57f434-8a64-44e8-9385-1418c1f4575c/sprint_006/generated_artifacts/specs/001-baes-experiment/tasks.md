# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models/course.py` (350 bytes)
- `src/models/teacher.py` (200 bytes)
- `src/api/course.py` (800 bytes)
- `src/database/migrations/` (Alembic migrations)

Instructions for Task Breakdown:
1. Identify which existing files need modifications
2. Create new files for new functionality
3. Ensure integration tasks are included
4. Maintain consistency with existing code style and patterns

---

### Task List

- [ ] **Modify Course Model to Add Teacher ID**  
  **File**: `src/models/course.py`  
  **Description**: Update the `Course` class to include `teacher_id` as a foreign key referencing `Teacher.id`. Add a relationship for `teacher`.  

- [ ] **Create Migration Script for Course Table Update**  
  **File**: `src/database/migrations/versions/`  
  **Description**: Use Alembic to create a migration script that adds the `teacher_id` column to the `Course` table while preserving existing data integrity.  

- [ ] **Implement PUT API Endpoint for Course Update**  
  **File**: `src/api/course.py`  
  **Description**: Add a PUT endpoint `/courses/{id}` to update the course with a `teacher_id`. Include validation logic to ensure the teacher exists.

- [ ] **Implement GET API Endpoint for Course Retrieval**  
  **File**: `src/api/course.py`  
  **Description**: Add a GET endpoint `/courses/{id}` to retrieve course details, including associated teacher information. Ensure the response format is JSON and follows defined error formats.

- [ ] **Update Pydantic Models for API Validation**  
  **File**: `src/models/course.py`  
  **Description**: Modify existing Pydantic models or create new models as necessary to validate input and output for course updates and retrievals.

- [ ] **Develop Unit Tests for Course Teacher Relationship**  
  **File**: `tests/test_api_courses.py`  
  **Description**: Create unit tests for the new functionality, including tests for updating courses with valid and invalid teacher IDs and retrieving course details.

- [ ] **Create Integration Tests for Course-Teacher-Fetch Functionality**  
  **File**: `tests/test_integration_courses.py`  
  **Description**: Add integration tests that ensure the new API endpoints function correctly with the database and return expected results. 

- [ ] **Implement Error Handling for Invalid Teacher Assignment**  
  **File**: `src/api/course.py`  
  **Description**: Ensure consistent error responses for invalid teacher ID assignments in the PUT endpoint; return standardized error JSON as specified.

- [ ] **Document Database Changes and New Endpoints**  
  **File**: `README.md`  
  **Description**: Update the documentation to include descriptions of the new field, endpoints, and usage instructions for the `teacher_id` in course management.

- [ ] **Verify All Tasks Meet Acceptance Criteria**  
  **File**: `tests/test_api_courses.py`  
  **Description**: Ensure all developed functionalities and tests adhere to the specified acceptance criteria and maintain performance standards. 

--- 

By following this structured task list, the implementation of the teacher relationship for courses can be systematically approached, ensuring clarity, traceability, and maintainability throughout the development process.