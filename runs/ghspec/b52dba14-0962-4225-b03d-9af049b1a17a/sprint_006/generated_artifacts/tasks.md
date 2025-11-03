# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- tests/test_teachers.py (2029 bytes)

Instructions for Task Breakdown:
1. Identify which existing files need modifications
2. Create new files for new functionality
3. Ensure integration tasks are included
4. Maintain consistency with existing code style and patterns
---

### Tasks

- [ ] **Update Course Model**
  - **File**: `src/models/course_model.py`  
  - **Description**: Modify the existing `Course` model to include a new `teacher_id` attribute and define the relationship with the `Teacher` model.
  
- [ ] **Create Migration Script**
  - **File**: `src/database/migrations/2023_10_16_add_teacher_id_to_courses.py`  
  - **Description**: Write a migration script that alters the `courses` table to add the `teacher_id` column, ensuring all existing data preservation.

- [ ] **Update Course Service**
  - **File**: `src/services/course_service.py`  
  - **Description**: Enhance the course service to include a method for assigning a teacher to a course by validating `teacher_id` and updating the course.

- [ ] **Implement Course Routes**
  - **File**: `src/api/course_routes.py`  
  - **Description**: Add a new endpoint `PUT /courses/{course_id}/assign_teacher` to handle API requests for assigning a teacher to a course.

- [ ] **Implement Retrieval Endpoint**
  - **File**: `src/api/course_routes.py`  
  - **Description**: Implement the endpoint `GET /courses/{course_id}` to retrieve course details including teacher information if assigned.

- [ ] **Write Unit Tests for Course Service**
  - **File**: `tests/test_courses.py`  
  - **Description**: Add unit tests for the teacher assignment functionality, ensuring that valid and invalid IDs are handled correctly.

- [ ] **Write Integration Tests for API Endpoints**
  - **File**: `tests/test_courses.py`  
  - **Description**: Implement integration tests for the new API endpoints for assigning teachers and retrieving course details.

- [ ] **Update API Documentation** 
  - **File**: `README.md`  
  - **Description**: Modify the project documentation to include the new API contracts for the teacher-course assignment functionalities.

- [ ] **Validate Migration Execution**
  - **File**: `src/database/migrations/2023_10_16_add_teacher_id_to_courses.py`  
  - **Description**: Ensure that the migration script can be executed smoothly without data loss and that it validates existing relationships.

- [ ] **Create Error Response Handling**
  - **File**: `src/api/course_routes.py`  
  - **Description**: Implement error handling for invalid `teacher_id` scenarios, returning appropriate HTTP error messages.

- [ ] **Implement Logging for Teacher Assignments**
  - **File**: `src/services/course_service.py`  
  - **Description**: Add structured logging for operations related to assigning teachers to courses, aiding in debugging and monitoring.

- [ ] **Test Database Migration**
  - **File**: Test the functionality manually / in `tests/test_courses.py`  
  - **Description**: Create tests to validate that the schema updates correctly reflect in both newly created and existing courses.

---

### Next Steps
- Begin implementation based on the outlined tasks, ensuring that each task is executed and thoroughly tested before proceeding to the next. Prioritize creating the model and migration files, as they form the foundation of this feature.