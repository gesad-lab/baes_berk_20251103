# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `models.py`
- `routes/courses.py`
- `tests/test_courses.py`
- `requirements.txt`
- `README.md`

Instructions for Task Breakdown:
1. Identify which existing files need modifications
2. Create new files for new functionality
3. Ensure integration tasks are included
4. Maintain consistency with existing code style and patterns

---

- [ ] **Task 1: Update Course Model to Include Foreign Key**  
  **File**: `src/models.py`  
  **Description**: Add `teacher_id` column to the Course class and establish a relationship with the Teacher model.  
  ```python
  # models.py
  teacher_id = Column(Integer, ForeignKey('teachers.id'))  # Foreign key added
  ```

- [ ] **Task 2: Implement Assign Teacher API Endpoint**  
  **File**: `src/routes/courses.py`  
  **Description**: Create a POST endpoint to assign a teacher to a course by accepting `teacher_id` in the request body. Ensure that proper validation logic is included.  
  ```python
  @router.post('/courses/{course_id}/assign-teacher')
  ```

- [ ] **Task 3: Implement Retrieve Course with Teacher Information Endpoint**  
  **File**: `src/routes/courses.py`  
  **Description**: Update the GET endpoint for course retrieval to include the associated teacher's data in the response.  
  ```python
  @router.get('/courses/{course_id}')
  ```

- [ ] **Task 4: Update Course Response Schema**  
  **File**: `src/schemas.py`  
  **Description**: Add Pydantic models to include teacher information in course responses appropriately.  
  ```python
  class CourseResponse(BaseModel):
      teacher: TeacherResponse  # Add teacher response schema as a nested item
  ```

- [ ] **Task 5: Create Database Migration Script**  
  **File**: `migrations/versions/<migration_file>.py`  
  **Description**: Use Alembic to create a migration that adds the `teacher_id` column to the `courses` table. This script should be reversible and maintain data integrity.  
  ```bash
  alembic revision --autogenerate -m "Add teacher_id to Course"
  ```

- [ ] **Task 6: Add Tests for Assign Teacher Functionality**  
  **File**: `tests/test_courses.py`  
  **Description**: Create unit tests to validate assigning a teacher to a course, ensuring both happy path and error scenarios are covered.  
  ```python
  def test_assign_teacher_to_course(client):  # Happy path test
  ```

- [ ] **Task 7: Add Tests for Retrieve Course with Teacher Information**  
  **File**: `tests/test_courses.py`  
  **Description**: Implement tests to check if course retrieval includes associated teacher information, and validate failures on invalid IDs.  
  ```python
  def test_get_course_with_teacher(client):  # Include the teacher in response validation
  ```

- [ ] **Task 8: Update README.md for New API Endpoints**  
  **File**: `README.md`  
  **Description**: Document the new API endpoints for assigning a teacher to a course and retrieving course information with included teacher details.  
  ```markdown
  ### New API Endpoints
  ```

- [ ] **Task 9: Update Requirements if Necessary**  
  **File**: `requirements.txt`  
  **Description**: Check the dependency list to ensure all required packages for new functionalities are included and up-to-date, particularly for database migrations if using Alembic.  
  ```plaintext
  alembic==<version>
  ```

---

This structured breakdown of tasks allows for isolated execution and testing of each part of the implementation to enhance efficiency and maintainability.