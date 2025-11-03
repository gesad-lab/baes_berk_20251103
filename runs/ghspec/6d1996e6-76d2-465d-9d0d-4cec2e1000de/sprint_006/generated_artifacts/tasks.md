# Tasks: Add Teacher Relationship to Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models/course.py` (existing course model)
- `src/app.py` (existing route handlers)
- `src/services/course.py` (existing course service)
- `src/db/database.py` (existing database logic)
- `tests/test_course.py` (existing course tests)

### Task Breakdown

1. **Update the Course Model**
   - **Task**: Add `teacher_id` column to the `Course` model
   - **File**: `src/models/course.py`
   - **Description**: Modify the `Course` class to include a `teacher_id` attribute as a nullable foreign key referencing the `Teacher` entity.
   - **Dependencies**: None
   - 
   - [ ] **Update Course Model** in `src/models/course.py`

2. **Implement Database Migration**
   - **Task**: Create migration script for adding `teacher_id` column
   - **File**: `src/db/database.py`
   - **Description**: Implement logic in the migration script to alter the `courses` table by adding the `teacher_id` column and ensure existing data integrity.
   - **Dependencies**: Task 1
   - 
   - [ ] **Create Migration Script** in `src/db/database.py`

3. **Add Endpoint for Assigning Teacher to Course**
   - **Task**: Implement `PUT /courses/{id}/assign-teacher` endpoint
   - **File**: `src/app.py`
   - **Description**: Define a new route to assign a teacher to a course, including input validation and response handling.
   - **Dependencies**: Tasks 1, 2
   - 
   - [ ] **Implement Assign Teacher Endpoint** in `src/app.py`

4. **Update Course Service for Teacher Assignment**
   - **Task**: Extend course service to manage teacher assignments
   - **File**: `src/services/course.py`
   - **Description**: Add methods to handle the logic for assigning and removing teachers from courses.
   - **Dependencies**: Task 3
   - 
   - [ ] **Extend Course Service** in `src/services/course.py`

5. **Add Endpoint for Removing Teacher from Course**
   - **Task**: Implement `DELETE /courses/{id}/remove-teacher` endpoint
   - **File**: `src/app.py`
   - **Description**: Define a new route to remove the teacher from a course, including input validation and response handling.
   - **Dependencies**: Task 4
   - 
   - [ ] **Implement Remove Teacher Endpoint** in `src/app.py`

6. **Implement Unit Tests for Course Service**
   - **Task**: Create unit tests for assigning and removing teachers
   - **File**: `tests/test_course.py`
   - **Description**: Implement tests to validate the functionalities provided by the course service related to teacher assignments.
   - **Dependencies**: Task 4
   - 
   - [ ] **Add Unit Tests for Course Service** in `tests/test_course.py`

7. **Implement Integration Tests for Course-Teacher Functionality**
   - **Task**: Create integration tests for the new endpoints
   - **File**: `tests/test_course_teacher_integration.py`
   - **Description**: Add tests that cover the new API endpoints for assigning and removing teachers, checking that responses are correct and the database reflects changes accurately.
   - **Dependencies**: Tasks 5, 6
   - 
   - [ ] **Add Integration Tests** in `tests/test_course_teacher_integration.py`

8. **Update Documentation**
   - **Task**: Update README.md with new endpoint descriptions
   - **File**: `README.md`
   - **Description**: Modify the documentation to include new API endpoints, request structures, and response formats related to the teacher assignment functionality.
   - **Dependencies**: Tasks 5, 7
   - 
   - [ ] **Update API Documentation** in `README.md`

9. **Ensure Proper Error Handling and Validation**
   - **Task**: Implement error handling for non-existent teachers and courses
   - **File**: `src/services/course.py`
   - **Description**: Ensure validation checks for invalid teacher IDs and non-existent courses are implemented in the service layer.
   - **Dependencies**: Tasks 3, 4
   - 
   - [ ] **Implement Error Handling** in `src/services/course.py`

### Summary of Tasks
These tasks are organized sequentially based on their dependencies, ensuring that each aspect of the feature can be developed, tested, and deployed effectively while maintaining consistent coding standards. Each task is independently testable post-implementation.