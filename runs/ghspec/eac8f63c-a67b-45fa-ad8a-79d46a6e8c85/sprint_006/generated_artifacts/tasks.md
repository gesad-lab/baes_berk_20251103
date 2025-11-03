# Tasks: Add Teacher Relationship to Course Entity

---

INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models/course.py` (Existing Course model)
- `src/controllers/course_controller.py` (Existing Course controller)
- `src/services/course_service.py` (Existing Course service)
- `src/repositories/course_repository.py` (Existing Course repository)
- `tests/controllers/test_course_controller.py` (Existing tests for Course controller)
- `tests/services/test_course_service.py` (Existing tests for Course service)
- `migrations/` (Existing migration scripts)

---

## Task Breakdown

### Task 1: Update Course Model

- **File**: `src/models/course.py`
- **Description**: Extend the existing Course model to include a foreign key reference to the Teacher entity via `teacher_id`.
- **Implementation**:
    ```python
    class Course(Base):
        # Existing fields
        teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New foreign key relationship
        teacher = relationship("Teacher")  # Define relationship with Teacher
    ```
- **Dependencies**: None
- **Testability**: Ensure the model correctly reflects the database schema after the migration.

- [ ] **Update Course Model** - `src/models/course.py`

### Task 2: Modify Course Controller

- **File**: `src/controllers/course_controller.py`
- **Description**: Implement PATCH endpoint for assigning a teacher to a course and GET endpoint to retrieve course details with teacher information.
- **Implementation**: 
    - Add methods to handle requests for course updates and retrieval as specified in the API Contracts.
- **Dependencies**: Task 1
- **Testability**: Verify that endpoints return correct course details including the teacher.

- [ ] **Modify Course Controller** - `src/controllers/course_controller.py`

### Task 3: Extend Course Service

- **File**: `src/services/course_service.py`
- **Description**: Implement business logic for assigning teachers to courses, including validating teacher IDs.
- **Implementation**: 
    - Create methods to manage teacher assignments and ensure proper error handling.
- **Dependencies**: Task 1
- **Testability**: Unit tests should validate that the logic for assigning teachers functions correctly.

- [ ] **Extend Course Service** - `src/services/course_service.py`

### Task 4: Update Course Repository

- **File**: `src/repositories/course_repository.py`
- **Description**: Modify the repository layer to accommodate changes in the Course model for teacher assignments.
- **Implementation**: 
    - Update existing methods for course data management to include teacher associations.
- **Dependencies**: Task 1
- **Testability**: Ensure that the repository interacts correctly with the database for teacher assignments.

- [ ] **Update Course Repository** - `src/repositories/course_repository.py`

### Task 5: Create Migration Script

- **File**: `migrations/`
- **Description**: Write migration script using Alembic to add the `teacher_id` column to the `courses` table.
- **Implementation**: Use the provided example to create the migration function for altering the table.
- **Dependencies**: Task 1
- **Testability**: Run migration script and verify the structure of the database.

- [ ] **Create Migration Script** - `migrations/`

### Task 6: Extend Unit Tests for Course Controller

- **File**: `tests/controllers/test_course_controller.py`
- **Description**: Add tests to validate the new functionality for assigning a teacher and retrieving course information.
- **Implementation**: Implement test cases for successful and unsuccessful operations based on user scenarios.
- **Dependencies**: Task 2
- **Testability**: Ensure test coverage meets at least 70% for new functionalities.

- [ ] **Extend Unit Tests for Course Controller** - `tests/controllers/test_course_controller.py`

### Task 7: Extend Unit Tests for Course Service

- **File**: `tests/services/test_course_service.py`
- **Description**: Add tests to validate the logic for course-teacher assignments and proper error handling.
- **Implementation**: Implement test cases to ensure that teacher assignments and validations are functioning as expected.
- **Dependencies**: Task 3
- **Testability**: Ensure adequate coverage of all scenarios specified in testing requirements.

- [ ] **Extend Unit Tests for Course Service** - `tests/services/test_course_service.py`

---

By following this structured task breakdown, we will effectively add the teacher relationship to the Course entity while ensuring that all modifications are independently testable and maintain the integrity of existing functionality.