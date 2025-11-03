# Tasks: Add Teacher Relationship to Course Entity

---

INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- tests/test_teachers.py (2903 bytes)

---

### Task Breakdown

- **Task 1: Modify Course Model to Include Teacher Relationship**
  - **File**: `src/models.py`
  - **Description**: Update the `Course` model to add a new field `teacher_id`, and establish the relationship with the `Teacher` model.
  - **Code Change**: Add `teacher_id` field and update the relationship configuration.
  - **Dependencies**: None
  - **Test Initially**: Verify that the models compile without errors.
  - [ ] Update `Course` model in `src/models.py`

- **Task 2: Create Database Migration for Course Table Update**
  - **File**: `src/migrations.py`
  - **Description**: Implement the `migrate_add_teacher_id_to_courses` function to add the `teacher_id` column to the `courses` table while ensuring data integrity.
  - **Dependencies**: Task 1 (the model needs to be updated first)
  - **Test Initially**: Execute the migration script in a test database and verify the structure.
  - [ ] Implement migration function in `src/migrations.py`
    
- **Task 3: Implement API Endpoint to Assign Teacher to Course**
  - **File**: `src/courses.py`
  - **Description**: Create a new endpoint `PUT /courses/{course_id}/assign-teacher` that accepts a JSON payload with `teacher_id` and updates the course's teacher assignment.
  - **Dependencies**: Task 1
  - **Test Initially**: Send a request to the new endpoint and verify successful assignment in the database.
  - [ ] Add assignment logic in `src/courses.py`

- **Task 4: Modify Course Detail Retrieval Endpoint to Include Teacher Info**
  - **File**: `src/courses.py`
  - **Description**: Update the existing `GET /courses/{course_id}` endpoint to return the teacher information if assigned.
  - **Dependencies**: Task 1
  - **Test Initially**: Retrieve course details and check if teacher info is included in the response.
  - [ ] Update course detail endpoint in `src/courses.py`

- **Task 5: Create an Endpoint to List Courses with Teachers**
  - **File**: `src/courses.py`
  - **Description**: Implement the `GET /courses` endpoint that returns a list of courses along with their associated teacher information.
  - **Dependencies**: Task 1
  - **Test Initially**: Send a request to the endpoint and verify the correct format of the response.
  - [ ] Implement course listing endpoint in `src/courses.py`

- **Task 6: Add Unit Tests for Course-Teacher Relationship Functionality**
  - **File**: `tests/test_courses.py`
  - **Description**: Develop unit tests to validate the functionality of assigning a teacher to a course and retrieving course details with teacher information.
  - **Dependencies**: Tasks 3, 4, 5
  - **Test Initially**: Ensure that tests run successfully and validate correct scenarios and expected outcomes.
  - [ ] Create tests in `tests/test_courses.py`

- **Task 7: Update Documentation for New API Endpoints**
  - **File**: `README.md`
  - **Description**: Document the new endpoints for assigning teachers and retrieving course details, including request formats and example responses.
  - **Dependencies**: Tasks 3, 4, 5
  - **Test Initially**: Ensure README.md updates are clear and comprehensible.
  - [ ] Update `README.md` for new API details

---

### Success Criteria Verification
- Each task must be verified through unit tests or API tests to confirm the correct implementation.
- Ensure performance metrics are achieved and errors are handled as specified in the implementation plan.

### Summary
These tasks will ensure the implementation of the teacher relationship in the course entity follows a structured and incremental approach, providing clarity and focus on each modification required to meet the project specifications.