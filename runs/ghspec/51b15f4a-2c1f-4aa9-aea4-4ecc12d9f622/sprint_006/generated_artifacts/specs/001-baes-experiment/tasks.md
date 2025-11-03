# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- models/course.py (updated structure)
- controllers/course_controller.py (API logic)
- schemas/course_schema.py (request validation)
- tests/test_course.py (API tests)

Instructions for Task Breakdown:
1. Identify which existing files need modifications
2. Create new files for new functionality
3. Ensure integration tasks are included
4. Maintain consistency with existing code style and patterns

---

## Task 1: Update Course Model
- **File**: `models/course.py`
- **Task**: Add `teacher_id` column to the `Course` model, along with relationship mapping.
- **Dependencies**: None
- **[ ]** Modify `Course` class to include `teacher_id` as a ForeignKey.
- **[ ]** Add relationship to `Teacher` model within the `Course` class.

---

## Task 2: Implement API Endpoint for Assigning Teacher
- **File**: `controllers/course_controller.py`
- **Task**: Create the `POST /api/v1/courses/{course_id}/assign_teacher` endpoint.
- **Dependencies**: Task 1
- **[ ]** Implement logic to assign a teacher to a course in the `assign_teacher` function.
- **[ ]** Validate existence of both course and teacher.
- **[ ]** Return appropriate JSON responses for success and failure.

---

## Task 3: Implement API Endpoint for Retrieving Course Information
- **File**: `controllers/course_controller.py`
- **Task**: Create the `GET /api/v1/courses/{course_id}` endpoint.
- **Dependencies**: Task 1
- **[ ]** Implement the logic to retrieve course details along with associated teacher information.
- **[ ]** Return JSON structure with correct teacher details if assigned.

---

## Task 4: Update Request Validation Schema
- **File**: `schemas/course_schema.py`
- **Task**: Modify request validation schema to enforce valid `course_id` and `teacher_id`.
- **Dependencies**: Task 1
- **[ ]** Add required fields for `course_id` and `teacher_id` in the schema.

---

## Task 5: Create Database Migration Script
- **File**: `database/migrations/`
- **Task**: Create migration script to add `teacher_id` column to the Course table.
- **Dependencies**: Task 1
- **[ ]** Implement `upgrade` and `downgrade` functions to alter the database schema.

---

## Task 6: Create Unit Tests for Teacher Assignment
- **File**: `tests/test_course.py`
- **Task**: Implement unit tests for assigning teachers to courses 
- **Dependencies**: Task 2
- **[ ]** Write tests for successful assignment of a teacher to a course.
- **[ ]** Write tests for failure scenarios, including assigning non-existent teachers.

---

## Task 7: Create Unit Tests for Retrieving Course Information
- **File**: `tests/test_course.py`
- **Task**: Implement unit tests for retrieving course information with teacher details.
- **Dependencies**: Task 3
- **[ ]** Write tests to confirm retrieval of course details including assigned teacher.
- **[ ]** Write tests for cases where a course does not exist.

---

## Task 8: Update README Documentation
- **File**: `README.md`
- **Task**: Update documentation to include new API endpoints and migration instructions.
- **Dependencies**: All previous tasks
- **[ ]** Document new API endpoint usage for assigning teachers and retrieving course info.

---

## Task 9: Final Integration Testing
- **File**: `tests/test_course.py`
- **Task**: Execute full integration tests to ensure all parts work together.
- **Dependencies**: All previous tasks
- **[ ]** Test the overall API behavior for endpoints implemented and ensure integrity of operations.
- **[ ]** Confirm behavior aligns with defined expected results and statuses.

---

Each task is designed to be independent and focused on a specific file or functionality, allowing for individual testing and integration as the project progresses.