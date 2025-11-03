# Tasks: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `models/course.py` (688 bytes)
- `api/routes/students.py` (2482 bytes)
- `api/routes/courses.py` (2213 bytes)
- `tests/test_courses.py` (2297 bytes)

---

## Task Breakdown

### Task 1: Create Junction Table Migration
- **File**: `migrations/versions/create_student_courses_table.py`
- **Description**: Create a migration script for the new `student_courses` junction table that establishes the many-to-many relationship between students and courses.
- **Action Items**:
  - Write Alembic migration code to create the `student_courses` table with `student_id` and `course_id` as foreign keys.
```python
# migrations/versions/create_student_courses_table.py
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), nullable=False),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), nullable=False),
        sa.PrimaryKeyConstraint('student_id', 'course_id')
    )

def downgrade():
    op.drop_table('student_courses')
```
- [ ] Task 1 Complete

### Task 2: Update Student Model
- **File**: `models/student.py`
- **Description**: Modify the `Student` model to include a relationship with the `Course` model via the `student_courses` junction table.
- **Action Items**:
  - Add `courses` attribute using SQLAlchemy `relationship` definition.
```python
# models/student.py
from sqlalchemy.orm import relationship

class Student(db.Model):
    # Existing fields...
    courses = relationship('Course', secondary='student_courses', back_populates='students')
```
- [ ] Task 2 Complete

### Task 3: Update Course Model
- **File**: `models/course.py`
- **Description**: Modify the `Course` model to include a relationship back to the `Student` model.
- **Action Items**:
  - Add `students` attribute in `Course` model using SQLAlchemy `relationship` definition.
```python
# models/course.py
from sqlalchemy.orm import relationship

class Course(db.Model):
    # Existing fields...
    students = relationship('Student', secondary='student_courses', back_populates='courses')
```
- [ ] Task 3 Complete

### Task 4: Create Course Association Endpoint
- **File**: `api/routes/students.py`
- **Description**: Implement the POST endpoint for associating courses with a student.
- **Action Items**:
  - Implement logic to validate course existence and associate courses if valid.
```python
# api/routes/students.py
@students_bp.route('/students/<int:student_id>/courses', methods=['POST'])
def associate_courses(student_id):
    data = request.json
    course_ids = data.get('courseIds', [])
    existing_student = Student.query.get(student_id)

    if not existing_student:
        return jsonify({"error": {"code": "E002", "message": "Student not found."}}), 404

    for course_id in course_ids:
        existing_course = Course.query.get(course_id)
        if not existing_course:
            return jsonify({"error": {"code": "E001", "message": f"Course with ID {course_id} does not exist."}}), 404
        existing_student.courses.append(existing_course)

    db.session.commit()
    return jsonify({"message": "Courses associated successfully.", "courses": [course.serialize() for course in existing_student.courses]}), 200
```
- [ ] Task 4 Complete

### Task 5: Create Retrieve Courses Endpoint
- **File**: `api/routes/students.py`
- **Description**: Implement the GET endpoint for retrieving courses associated with a student.
- **Action Items**:
  - Implement logic to fetch courses for the given student ID.
```python
# api/routes/students.py
@students_bp.route('/students/<int:student_id>/courses', methods=['GET'])
def get_courses(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student not found."}}), 404
    
    courses = [course.serialize() for course in student.courses]
    return jsonify({"courses": courses}), 200
```
- [ ] Task 5 Complete

### Task 6: Write Unit Tests for Course Association
- **File**: `tests/test_students.py`
- **Description**: Create unit tests for the new course association endpoint.
- **Action Items**:
  - Write tests for successful course associations and errors for non-existent courses.
```python
# tests/test_students.py
def test_associate_courses_success(client):
    # Create a student and a course for testing
    student = Student(name='Test Student')
    db.session.add(student)
    db.session.commit()
    
    course = Course(name='Introduction to Python', level='Beginner')
    db.session.add(course)
    db.session.commit()

    response = client.post(f'/students/{student.id}/courses', json={'courseIds': [course.id]})
    assert response.status_code == 200
    assert 'courses' in response.get_json()

def test_associate_courses_non_existent_course(client):
    response = client.post('/students/1/courses', json={'courseIds': [99]})
    assert response.status_code == 404
    assert response.get_json()['error']['code'] == 'E001'
```
- [ ] Task 6 Complete

### Task 7: Write Tests for Retrieving Courses
- **File**: `tests/test_students.py`
- **Description**: Create unit tests for the endpoint retrieving courses associated with a student.
- **Action Items**:
  - Write tests ensuring the correct retrieval of courses for valid students and error responses for invalid students.
```python
def test_get_courses_success(client):
    # Create a student and associate a course
    student = Student(name='Test Student')
    db.session.add(student)
    db.session.commit()
    
    course = Course(name='Introduction to Python', level='Beginner')
    db.session.add(course)
    db.session.commit()
    
    student.courses.append(course)
    db.session.commit()

    response = client.get(f'/students/{student.id}/courses')
    assert response.status_code == 200
    assert len(response.get_json()['courses']) == 1

def test_get_courses_non_existent_student(client):
    response = client.get('/students/999/courses')
    assert response.status_code == 404
    assert response.get_json()['error']['code'] == 'E002'
```
- [ ] Task 7 Complete

### Task 8: Update API Documentation
- **File**: `README.md` or appropriate API documentation file
- **Description**: Add documentation for new API endpoints relevant to course associations.
- **Action Items**:
  - Document usage details for both the POST and GET requests for course associations.
```markdown
## Courses API

### Associate Courses with Student

**POST /students/{studentId}/courses**

Request:
```json
{
  "courseIds": [1, 2]
}
```

Response:
- 200 OK
- 404 Not Found if the course does not exist

### Retrieve Courses for Student

**GET /students/{studentId}/courses**

Response:
- 200 OK with a list of courses associated with the student
- 404 Not Found if the student does not exist
```
- [ ] Task 8 Complete

### Task 9: Validate and Run Migrations
- **File**: Migration script file
- **Description**: Validate that migrations run successfully and no data integrity is lost.
- **Action Items**:
  - Use Alembic to run the migrations in the development environment, verifying the new junction table is created properly.
```bash
alembic upgrade head
```
- [ ] Task 9 Complete

### Task 10: Tag and Deploy Changes
- **File**: N/A
- **Description**: Tag the changes in version control, prepare for deployment.
- **Action Items**:
  - Ensure all tasks are completed, tested, and committed.
  - Create a release tag for deployment.
```bash
git tag -a v1.0.0 -m "Add Course Relationship to Student Entity"
git push origin v1.0.0
```
- [ ] Task 10 Complete

---

Upon completion of all tasks, the implementation of the course relationship within the Student entity will be thoroughly integrated, unit tested, and documented, ensuring readiness for production deployment.