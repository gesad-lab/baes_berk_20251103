# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models/course.py` 
- `src/models/teacher.py`
- `src/services/course_service.py`
- `src/controllers/course_controller.py`
- `src/migrations/2023_10_01_0001_initial_setup.py` 
- `tests/test_course.py` 

---

## Task Breakdown

### 1. Update Course Model

- [ ] **Modify Course Model**  
  **File Path**: `src/models/course.py`  
  **Description**: Add a `teacher_id` attribute to the `Course` model and create a relationship with the `Teacher` model.  
  **Testable Outcome**: The application should not break on loading the model and should reflect the new schema.

### 2. Update Teacher Model

- [ ] **Update Teacher Model for Back-references**  
  **File Path**: `src/models/teacher.py`  
  **Description**: Ensure the `Teacher` model includes a back-reference to courses.  
  **Testable Outcome**: The absence of errors while loading the updated model.

### 3. Update API Controller for Course Management

- [ ] **Add Teacher Association Endpoint**  
  **File Path**: `src/controllers/course_controller.py`  
  **Description**: Implement the `POST /courses/{course_id}/teacher/{teacher_id}` endpoint to allow associating a teacher with a course.  
  **Testable Outcome**: Confirm successful assignment through API testing.

- [ ] **Add Teacher Removal Endpoint**  
  **File Path**: `src/controllers/course_controller.py`  
  **Description**: Implement the `DELETE /courses/{course_id}/teacher` endpoint to allow removing a teacher from a course.  
  **Testable Outcome**: Confirm successful dissociation through API testing.

- [ ] **Retrieve Course Details Endpoint**  
  **File Path**: `src/controllers/course_controller.py`  
  **Description**: Ensure the `GET /courses/{id}` endpoint retrieves course details including the associated teacher information.  
  **Testable Outcome**: Course details with teacher information are correctly returned.

### 4. Create Service Layer Logic

- [ ] **Implement Course-Service Logic for Assisting Teacher**  
  **File Path**: `src/services/course_service.py`  
  **Description**: Add methods for associating and dissociating teachers with courses, including validation for existence checks.  
  **Testable Outcome**: The service methods work without error and execute as expected.

### 5. Database Migration

- [ ] **Create Migration for Adding Teacher Relationship**  
  **File Path**: `src/migrations/2023_10_01_0002_add_teacher_relationship.py`  
  **Description**: Write a migration script to add the `teacher_id` column to the `courses` table and define foreign key constraints.  
  **Testable Outcome**: Migration executes successfully without data loss.

### 6. Write Unit Tests

- [ ] **Test Teacher Assignment**  
  **File Path**: `tests/test_course.py`  
  **Description**: Add tests to verify assigning a teacher to a course works correctly.  
  **Testable Outcome**: The test passes confirming the assignment functionality.

- [ ] **Test Teacher Removal**  
  **File Path**: `tests/test_course.py`  
  **Description**: Add tests to verify removing a teacher from a course works correctly.  
  **Testable Outcome**: The test passes confirming the removal functionality.

- [ ] **Test Course Retrieval including Teacher Data**  
  **File Path**: `tests/test_course.py`  
  **Description**: Add tests to confirm course details returned include teacher data.  
  **Testable Outcome**: The test passes confirming proper data retrieval.

- [ ] **Test Non-existent Teacher Assignment**  
  **File Path**: `tests/test_course.py`  
  **Description**: Confirm the application correctly handles attempts to assign a non-existent teacher.  
  **Testable Outcome**: The test returns a 404 error as expected.

### 7. Documentation

- [ ] **Update API Documentation**  
  **File Path**: `src/docs/openapi.yaml`  
  **Description**: Document the new API endpoints created for handling teacher relationships with courses.  
  **Testable Outcome**: The documentation includes correct details for endpoints and is validated through a Swagger UI load.

- [ ] **Update README**  
  **File Path**: `README.md`  
  **Description**: Modify the README to reflect changes in course management regarding teacher assignments.  
  **Testable Outcome**: README accurately describes the setup and new functionalities.

### 8. Integration Tasks

- [ ] **Test Migration in Development**  
  **File Path**: N/A  
  **Description**: After creating the migration, run it in a development environment to ensure integrity and confirm the application behaves as expected.  
  **Testable Outcome**: No errors occur in the application, and the database structure reflects changes.

- [ ] **Verify Logging captures teacher assignment/removal**  
  **File Path**: `src/utils/logging_config.py`  
  **Description**: Ensure that logs correctly capture events when assigning/removing teachers from courses.  
  **Testable Outcome**: Logs generated contain relevant information for the actions taken.

---

This detailed task breakdown ensures a structured approach to successfully integrate the teacher relationship into the Course entity while maintaining the best practices and facilitating independent testing of each task.