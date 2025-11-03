# Tasks: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models.py` (for adding new model)
- `src/schemas.py` (for adding new schema)
- `src/routes.py` (for adding new API endpoints)
- `src/db.py` (for updating database schema)
- `tests/test_routes.py` (for new API tests)
- `tests/test_validation.py` (for new validation tests)

---

## Task Breakdown

### Task 1: Update Database Models
- **File**: `src/models.py`
  - **Description**: Add the `StudentCourse` model to represent the many-to-many relationship between Students and Courses.
  - **Action**:
    ```python
    class StudentCourse(db.Model):
        __tablename__ = 'student_courses'
        student_id = db.Column(db.Integer, db.ForeignKey('students.id'), primary_key=True)
        course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)
    ```
  - [ ] Task 1 Complete

### Task 2: Setup Marshmallow Schemas
- **File**: `src/schemas.py`
  - **Description**: Create a new Marshmallow schema for `StudentCourse` to manage serialization and validation.
  - **Action**:
    ```python
    class StudentCourseSchema(Schema):
        student_id = fields.Int(required=True)
        course_id = fields.Int(required=True)
    ```
  - [ ] Task 2 Complete

### Task 3: Implement API Endpoints
- **File**: `src/routes.py`
  - **Description**: Implement the new API endpoints for adding, retrieving, and removing courses related to a Student.
  - **Action**: 
    - `POST /students/{student_id}/courses`
    - `GET /students/{student_id}/courses`
    - `DELETE /students/{student_id}/courses/{course_id}`
  - [ ] Task 3 Complete

### Task 4: Update Database Schema
- **File**: `src/db.py`
  - **Description**: Create a migration script to add the `student_courses` join table to the SQLite database schema.
  - **Action**:
    ```sql
    CREATE TABLE student_courses (
        student_id INTEGER,
        course_id INTEGER,
        PRIMARY KEY(student_id, course_id),
        FOREIGN KEY(student_id) REFERENCES students(id),
        FOREIGN KEY(course_id) REFERENCES courses(id)
    );
    ```
  - [ ] Task 4 Complete

### Task 5: Implement Input Validation
- **File**: `src/routes.py`
  - **Description**: Add logic to handle invalid course associations during the `POST` request.
  - **Action**: Implement error message responses for invalid course IDs.
  - [ ] Task 5 Complete

### Task 6: Extend Unit Tests for Validation Logic
- **File**: `tests/test_validation.py`
  - **Description**: Add tests to validate input when associating courses with a Student.
  - **Action**:
    ```python
    def test_invalid_course_association(client):
        response = client.post('/students/1/courses', data=json.dumps({'course_id': '9999'}), content_type='application/json')
        assert response.status_code == 400
    ```
  - [ ] Task 6 Complete

### Task 7: Extend Integration Tests for API Endpoints
- **File**: `tests/test_routes.py`
  - **Description**: Add tests for the API endpoints for course associations with students.
  - **Action**:
    ```python
    def test_associate_course_to_student(client):
        response = client.post('/students/1/courses', data=json.dumps({'course_id': '1'}), content_type='application/json')
        assert response.status_code == 200
        
    def test_remove_course_from_student(client):
        response = client.delete('/students/1/courses/1')
        assert response.status_code == 200
    ```
  - [ ] Task 7 Complete

### Task 8: Update Documentation
- **File**: `README.md`
  - **Description**: Update the documentation to include new API functionality and example request/response formats.
  - [ ] Task 8 Complete

---

## Final Steps
- [ ] Verify all tasks are complete and pass local testing.
- [ ] Prepare for migration testing in staging environment before production deployment.