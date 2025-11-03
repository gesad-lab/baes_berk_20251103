# Tasks: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models/student.py`
- `src/models/course.py`
- `src/models/__init__.py`
- `tests/test_course.py`

Instructions for Task Breakdown:
1. Identify which existing files need modifications
2. Create new files for new functionality
3. Ensure integration tasks are included
4. Maintain consistency with existing code style and patterns
---

## Task List

### Create New Model for Junction Table

- [ ] **Task 1**: Create `StudentCourse` Model  
  **File**: `src/models/student_course.py`  
  - Define a SQLAlchemy model `StudentCourse` to represent the junction table between `Student` and `Course`.  
  - Ensure relationships are set using `relationship()` to link with `Student` and `Course`.

### Update Existing Models to Integrate New Relationships

- [ ] **Task 2**: Modify `Student` Model to Include Course Relationship  
  **File**: `src/models/student.py`  
  - Add a relationship property `courses` to link to the `StudentCourse` model.

- [ ] **Task 3**: Modify `Course` Model to Include Student Relationship  
  **File**: `src/models/course.py`  
  - Add a relationship property `students` to link to the `StudentCourse` model.

- [ ] **Task 4**: Update Imports in `__init__.py`  
  **File**: `src/models/__init__.py`  
  - Import the new `StudentCourse` model in the `__init__.py` file to make it accessible with other models.

### Implement API Endpoints for Associating and Retrieving Courses

- [ ] **Task 5**: Implement Associate Student with Courses Endpoint  
  **File**: `src/controllers/students.py`  
  - Create a `POST` endpoint `/students/{student_id}/courses` that accepts course IDs and associates them with a specified student.  

- [ ] **Task 6**: Implement Retrieve Courses for Student Endpoint  
  **File**: `src/controllers/students.py`  
  - Create a `GET` endpoint `/students/{student_id}/courses` that returns a list of courses associated with a specified student.

### Implement Migration for Database Schema Update

- [ ] **Task 7**: Create Migration for `StudentCourse` Table  
  **File**: Migration script in `migrations/versions/`  
  - Use Alembic to generate a migration script that creates the `student_courses` table while preserving existing Student and Course data.

### Testing Functionality

- [ ] **Task 8**: Write Unit Tests for Course Associations  
  **File**: `tests/test_student_courses.py`  
  - Create tests that validate the following:
    - Successful association of courses with a student.
    - Proper retrieval of courses for a student.
    - Error handling when attempting to associate with a non-existent course.

### Update Documentation

- [ ] **Task 9**: Update README.md with New API Endpoints  
  **File**: `README.md`  
  - Document the newly created API endpoints including request body and response formats.

### Validate Application Functionality

- [ ] **Task 10**: Run Tests and Validate Application  
  **File**: None (Verification step)  
  - Run all tests to ensure that the new functionality works as expected and that no existing functionality is broken.

### Deployment Preparation

- [ ] **Task 11**: Ensure Migrations and Environment are Ready for Deployment  
  **File**: `.env.example`  
  - Document any new configurations if necessary. Prepare migration documentation for deployment.

---

This structured task list outlines the specific, file-scoped tasks necessary to implement the relationship between `Student` and `Course` entities while ensuring adherence to the project’s guidelines and practices. Each task can be executed independently for focused development and testing.