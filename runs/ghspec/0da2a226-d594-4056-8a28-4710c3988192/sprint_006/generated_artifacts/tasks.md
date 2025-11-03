# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- tests/test_teacher.py (2398 bytes)

---

## Task 1: Update Course Schema to Include Teacher Foreign Key
- **File**: `src/models/models.py`
- **Description**: Modify the `Course` class to add a `teacher_id` foreign key referencing the `Teacher` entity.
- **Action**:
    - Add the following line in the `Course` class:
    ```python
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)
    ```
- [ ] Update `models.py` with `teacher_id` foreign key.

## Task 2: Create Migration for Database Schema Change
- **File**: `migrations/script.py` (create new migration script)
- **Description**: Use Alembic to create a migration that adds the `teacher_id` foreign key to the `courses` table.
- **Action**:
    ```bash
    alembic revision --autogenerate -m "Add teacher_id foreign key to courses"
    ```
- [ ] Generate and apply the migration script.

## Task 3: Implement Business Logic for Teacher Assignment
- **File**: `src/services/course_service.py`
- **Description**: Update `course_service.py` to implement the logic for assigning a Teacher to a Course.
- **Action**: Define the method `assign_teacher_to_course(course_id: int, teacher_id: int)` to handle teacher assignments.
- [ ] Implement teacher assignment logic.

## Task 4: Define API Endpoint for Assigning Teacher
- **File**: `src/api/routes.py`
- **Description**: Create a new endpoint to assign a Teacher to a Course.
- **Action**: 
    - Add the following route:
    ```python
    @router.post("/courses/{course_id}/assign_teacher")
    ```
- [ ] Define API endpoint for assigning a teacher.

## Task 5: Define API Endpoint to Retrieve Courses with Teachers
- **File**: `src/api/routes.py`
- **Description**: Create an endpoint to retrieve all Courses with their associated Teacher information.
- **Action**:
    - Add the following route:
    ```python
    @router.get("/courses")
    ```
- [ ] Set up retrieval of courses along with teacher details.

## Task 6: Implement Input Validation for Assign Teacher Request
- **File**: `src/api/dependencies.py`
- **Description**: Validate incoming requests for the teacher assignment endpoint using Pydantic.
- **Action**: Define a Pydantic model for validation.
- [ ] Implement input validation for `assign_teacher`.

## Task 7: Add Error Handling for Teacher Assignment
- **File**: `src/services/course_service.py`
- **Description**: Implement error handling in the `assign_teacher_to_course` method for invalid IDs and missing selections.
- **Action**: Raise appropriate HTTP exceptions with error messages.
- [ ] Add error handling for teacher assignment process.

## Task 8: Create Unit Tests for Course-Teacher Relationship
- **File**: `tests/test_course.py`
- **Description**: Write unit tests validating the scenarios for assigning a Teacher to a Course and retrieving courses including their Teachers.
- **Action**:
    ```python
    def test_assign_teacher_to_course_with_valid_data():
        # Test logic goes here
    ```
- [ ] Implement unit tests for course-teacher relationship functionalities.

## Task 9: Update Documentation for New API Endpoints
- **File**: `README.md`
- **Description**: Update the README file to document new API endpoints for assigning Teachers and retrieving Courses.
- **Action**: Include usage examples and response formats.
- [ ] Document new API functionalities in README.

## Task 10: Review Code for Consistency and Quality
- **File**: All modified files
- **Description**: Conduct a thorough review of all implemented code to ensure it adheres to project coding standards and guidelines.
- **Action**: Make necessary revisions for style and consistency.
- [ ] Perform code review and refine implementations.

--- 

This task breakdown provides clear, actionable items that align with the implementation plan for adding the Teacher relationship to the Course entity, ensuring each task is scoped to a specific file and independent for testing.