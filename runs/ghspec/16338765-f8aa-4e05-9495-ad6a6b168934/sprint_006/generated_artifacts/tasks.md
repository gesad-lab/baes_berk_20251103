# Tasks: Add Teacher Relationship to Course Entity

---

INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_teacher_api.py` (2455 bytes)

---

## Task Breakdown

### Database Schema Update

- [ ] **Modify Course Model**  
  **File**: `src/models/course.py`  
  Update the existing Course model to include the `teacher_id` foreign key field.
  
  - Add `teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)` to the Course class.
  
- [ ] **Create Database Migration Script**  
  **File**: `migrations/versions/xxxxxx_add_teacher_relationship.py`  
  Create a migration script using Alembic that adds the `teacher_id` column to the Course table without affecting existing data.
  
  - Ensure the script handles adding a nullable foreign key reference to the teachers table.

### API Endpoints Implementation

- [ ] **Implement Assign Teacher Endpoint**  
  **File**: `src/api/course_api.py`  
  Add the POST endpoint to assign a teacher to a course.
  
  - Create function `assign_teacher(course_id: int, request: AssignTeacherRequest)` handling `POST /courses/{course_id}/assign-teacher`.

- [ ] **Implement Remove Teacher Endpoint**  
  **File**: `src/api/course_api.py`  
  Add the DELETE endpoint to remove a teacher from a course.
  
  - Create function `remove_teacher(course_id: int)` handling `DELETE /courses/{course_id}/remove-teacher`.

- [ ] **Implement View Course Endpoint**  
  **File**: `src/api/course_api.py`  
  Add the GET endpoint to retrieve course details with teacher information.
  
  - Create function `get_course(course_id: int)` handling `GET /courses/{course_id}`.

### Request and Response Models

- [ ] **Define Pydantic Models**  
  **File**: `src/models/schemas.py`  
  Create request and response models for handling the Course-Teacher relationship.
  
  - Define `AssignTeacherRequest` and `CourseDetailsResponse` classes.

### Error Handling

- [ ] **Implement Error Handling for Assign and Remove Teacher**  
  **File**: `src/api/course_api.py`  
  Add error handling to the `assign_teacher` and `remove_teacher` functions for invalid course or teacher IDs.
  
  - Raise HTTP exceptions with clear error messages where applicable.

### Testing Coverage

- [ ] **Create Unit Tests for New Endpoints**  
  **File**: `tests/test_course_api.py`  
  Write unit tests for:
  
  - Assigning a teacher to a course.
  - Removing a teacher from a course.
  - Retrieving course details including teacher information.
  
- [ ] **Create Integration Tests for API Functionality**  
  **File**: `tests/test_integration_api.py` (new file)  
  Implement tests to validate the API endpoints operate correctly:
  
  - Test the POST, DELETE, and GET requests regarding teacher assignments and ensure proper responses.

### Documentation

- [ ] **Update README.md with New API Endpoints**  
  **File**: `README.md`  
  Include detailed information about the new endpoints added for managing Course-Teacher relationships.
  
  - Provide examples of request bodies, response formats, and any relevant error messages.

### Version Control and Deployment

- [ ] **Commit Changes with Clear Messages**  
  Commit all changes in logical chunks with messages detailing each modification related to the Course-Teacher relationship management.

- [ ] **Prepare Migration for Deployment**  
  Test the migration thoroughly in the staging environment. Ensure the application starts successfully and all functionalities are intact.

--- 

This task breakdown provides actionable, file-scoped steps to implement the feature, maintaining clarity and separating concerns for easier management and testing.