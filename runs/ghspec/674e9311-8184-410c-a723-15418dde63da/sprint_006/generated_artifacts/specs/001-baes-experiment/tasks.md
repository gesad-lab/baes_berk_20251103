# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `models/course.py`
- `api.py`
- `services/course_service.py`
- `tests/test_course.py`

Instructions for Task Breakdown:
1. Identify which existing files need modifications
2. Create new files for new functionality
3. Ensure integration tasks are included
4. Maintain consistency with existing code style and patterns

---

## Task List

- [ ] **Task 1: Update Course Entity**  
  **File:** `models/course.py`  
  **Description:** Add the `teacher_id` foreign key relationship to the Course entity.  
  **Details:** Modify the Course class to include `teacher_id` as a foreign key referencing `Teacher.id`.  
  **Testing:** Verify that the Course model can instantiate with a `teacher_id`.  

- [ ] **Task 2: Implement Database Migration**  
  **File:** `migrations/versions/{timestamp}_add_teacher_id_to_courses.py`  
  **Description:** Create a migration to alter the `courses` table to add the `teacher_id` column.  
  **Details:** Use Alembic to implement the migration script that adds the new column without disrupting existing data.  
  **Testing:** Verify that the migration runs without errors.  

- [ ] **Task 3: Develop Assign Teacher API Endpoint**  
  **File:** `api.py`  
  **Description:** Add a PUT endpoint to assign a teacher to a specific course.  
  **Details:** Implement the route `PUT /courses/{courseId}/assign-teacher` to handle teacher assignments.  
  **Testing:** Test that the endpoint correctly assigns a teacher and returns appropriate success/error messages.  

- [ ] **Task 4: Develop View Course API Endpoint**  
  **File:** `api.py`  
  **Description:** Extend the GET endpoint for courses to include teacher information.  
  **Details:** Modify the route `GET /courses/{courseId}` to return teacher details if assigned.  
  **Testing:** Ensure that the response includes the teacher's details when a teacher is assigned to a course.  

- [ ] **Task 5: Implement Business Logic for Teacher Assignment**  
  **File:** `services/course_service.py`  
  **Description:** Create functions to assign a teacher to a course and retrieve course details.  
  **Details:** Write `assign_teacher` and `get_course_with_teacher` functions to handle business logic.  
  **Testing:** Write unit tests for these functions to validate the business logic in isolation.  

- [ ] **Task 6: Create Unit Tests for Course-Teacher Functionality**  
  **File:** `tests/test_course.py`  
  **Description:** Write unit tests for the new functionalities related to assigning teachers and viewing courses.  
  **Details:** Implement tests for successful teacher assignment, non-existent teacher error handling, and retrieving courses with assigned teachers.  
  **Testing:** Run tests to ensure all pass with appropriate coverage.  

- [ ] **Task 7: Update API Documentation**  
  **File:** `docs/api_documentation.md`  
  **Description:** Update the API documentation to include new endpoints and their specifications.  
  **Details:** Document the request/response formats for assigning a teacher and viewing course details.  
  **Testing:** Review the documentation for clarity and accuracy.  

- [ ] **Task 8: Update README.md**  
  **File:** `README.md`  
  **Description:** Adjust usage instructions to reflect the new teacher assignment feature.  
  **Details:** Provide guidance on how to use the new API endpoints effectively.  
  **Testing:** Ensure readme updates are consistent and clear for users.  

- [ ] **Task 9: Run Full Application Test**  
  **File:** N/A  
  **Description:** Conduct an end-to-end test of the application to ensure that the teacher assignment feature works seamlessly with existing functionalities.  
  **Details:** Test the application in an environment that mimics production to confirm all components interact correctly.  
  **Testing:** Prepare a checklist of features to test during the end-to-end verification.  

These tasks ensure a structured and comprehensive approach to implementing the teacher relationship feature within the course entity, while allowing each task to be independently executed and verified.