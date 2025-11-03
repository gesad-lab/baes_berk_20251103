# Tasks: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models.py` (2340 bytes)
- `src/schemas.py` (1560 bytes)
- `src/routes.py` (1520 bytes)
- `src/db.py` (640 bytes)
- `tests/test_routes.py` (2630 bytes)
- `tests/test_validation.py` (1625 bytes)

## Task List

### Models and Database Schema

- [ ] **Update Course Model**
  - **File**: `src/models.py`
  - **Task**: Add `teacher_id` foreign key to the `Course` model and establish a relationship with the `Teacher` model.
  
- [ ] **Create Migration for Course Table**
  - **File**: `src/db.py`
  - **Task**: Implement database migration logic to add the `teacher_id` column to the `courses` table.

### Marshmallow Schemas

- [ ] **Update Course Schema**
  - **File**: `src/schemas.py`
  - **Task**: Modify the `CourseSchema` to include a nested serialization for the associated Teacher's details.

### API Endpoints

- [ ] **Add Assign Teacher Endpoint**
  - **File**: `src/routes.py`
  - **Task**: Implement the `POST /courses/{course_id}/assign-teacher` endpoint to handle assigning a Teacher to a Course.

- [ ] **Add Retrieve Course with Teacher Endpoint**
  - **File**: `src/routes.py`
  - **Task**: Implement the `GET /courses/{course_id}` endpoint to retrieve Course details, including the associated Teacher's information.

### Input Validation and Error Handling

- [ ] **Implement Input Validation for Teacher Assignment**
  - **File**: `src/routes.py`
  - **Task**: Ensure that assignment requests validate Teacher and Course IDs, returning appropriate error messages for invalid requests.

### Testing

- [ ] **Extend Unit Tests for Input Validation**
  - **File**: `tests/test_validation.py`
  - **Task**: Add test cases to validate ID checks and error responses for assigning Teachers to Courses.

- [ ] **Create Integration Tests for API Endpoints**
  - **File**: `tests/test_routes.py`
  - **Task**: Add tests to verify successful assignments of Teachers and correct retrieval of Courses with Teacher details.

### Documentation and Deployment

- [ ] **Update README Documentation**
  - **File**: `README.md`
  - **Task**: Revise the documentation to reflect new API endpoints and provide examples for assigning Teachers to Courses and retrieving Course details.

## Order of Execution

1. **Update Course Model**
2. **Create Migration for Course Table**
3. **Update Course Schema**
4. **Add Assign Teacher Endpoint**
5. **Add Retrieve Course with Teacher Endpoint**
6. **Implement Input Validation for Teacher Assignment**
7. **Extend Unit Tests for Input Validation**
8. **Create Integration Tests for API Endpoints**
9. **Update README Documentation**

---

This structure provides a clear and detailed plan for implementing the feature, ensuring that all aspects of the task are covered while adhering to the project specifications and coding standards. Each task is focused on a single file to facilitate easy execution and testing.