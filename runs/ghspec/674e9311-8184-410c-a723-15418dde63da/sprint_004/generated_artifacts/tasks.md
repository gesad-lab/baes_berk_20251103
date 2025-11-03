# Tasks: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `models/student.py`
- `models/course.py`
- `api.py`
- `tests/test_student.py`
- `tests/test_course.py`

---

## Task List

### Task 1: Create StudentCourses Model
- **File**: `models/student_course.py`
- **Action**: Implement the `StudentCourses` join table to establish a many-to-many relationship between `Student` and `Course`.
- **Details**: 
    ```python
    from sqlalchemy import Column, Integer, ForeignKey
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()

    class StudentCourses(Base):
        """Model representing the relationship between students and courses."""

        __tablename__ = 'student_courses'

        id = Column(Integer, primary_key=True, autoincrement=True)
        student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
        course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)

        def __init__(self, student_id: int, course_id: int):
            self.student_id = student_id
            self.course_id = course_id
    ```
- [ ] Implement StudentCourses model

### Task 2: Database Migration for StudentCourses
- **File**: `migrations/versions/create_student_courses_table.py`
- **Action**: Write a migration script to create the `student_courses` table.
- **Details**:
    ```python
    from alembic import op
    from sqlalchemy import Column, Integer, ForeignKey

    def upgrade():
        op.create_table(
            'student_courses',
            Column('id', Integer, primary_key=True, autoincrement=True),
            Column('student_id', Integer, ForeignKey('students.id'), nullable=False),
            Column('course_id', Integer, ForeignKey('courses.id'), nullable=False)
        )

    def downgrade():
        op.drop_table('student_courses')
    ```
- [ ] Write migration script for `student_courses` table creation

### Task 3: Implement Enroll Student Endpoint
- **File**: `api.py`
- **Action**: Create the `POST /students/{student_id}/enroll` API endpoint.
- **Details**:
    ```python
    from flask import Blueprint, request, jsonify
    from services.student_course_service import enroll_student_in_course

    student_course_bp = Blueprint('student_course', __name__)

    @student_course_bp.route('/students/<int:student_id>/enroll', methods=['POST'])
    def enroll_student_endpoint(student_id):
        data = request.json
        try:
            enroll_student_in_course(student_id, data['course_id'])
            return jsonify({"message": "Student enrolled successfully."}), 200
        except ValueError as ve:
            return jsonify({"error": {"code": "E001", "message": str(ve)}}), 400
        except Exception as e:
            return jsonify({"error": {"code": "E002", "message": str(e)}}), 400
    ```
- [ ] Implement the enroll student API endpoint

### Task 4: Implement Get Student Courses Endpoint
- **File**: `api.py`
- **Action**: Create the `GET /students/{student_id}/courses` API endpoint.
- **Details**:
    ```python
    @student_course_bp.route('/students/<int:student_id>/courses', methods=['GET'])
    def get_courses_endpoint(student_id):
        courses = get_student_courses(student_id)
        return jsonify(courses), 200
    ```
- [ ] Implement the get student courses API endpoint

### Task 5: Develop Enrollment Service Logic
- **File**: `services/student_course_service.py`
- **Action**: Add functions to handle enrollments and course retrieval logic.
- **Details**:
    ```python
    from models.student_course import StudentCourses
    from sqlalchemy.orm import Session

    def enroll_student_in_course(student_id: int, course_id: int) -> None:
        if not course_exists(course_id):
            raise ValueError("The course does not exist.")
        
        if student_already_enrolled(student_id, course_id):
            raise Exception("The student is already enrolled in this course.")

        enrollment = StudentCourses(student_id=student_id, course_id=course_id)
        db_session.add(enrollment)
        db_session.commit()

    def get_student_courses(student_id: int) -> list:
        enrollments = db_session.query(StudentCourses).filter(StudentCourses.student_id == student_id).all()
        return [{"course_id": enrollment.course_id} for enrollment in enrollments]
        
    def course_exists(course_id: int) -> bool:
        # Logic to check course existence
        pass

    def student_already_enrolled(student_id: int, course_id: int) -> bool:
        # Logic to check if student is already enrolled
        pass
    ```
- [ ] Implement service logic for enrollment and course retrieval

### Task 6: Testing for Enrollment Endpoint
- **File**: `tests/test_student_course.py`
- **Action**: Write unit tests for the enroll student and get courses functionality.
- **Details**:
    ```python
    import pytest

    def test_enroll_student_in_course(client):
        response = client.post('/students/1/enroll', json={"course_id": 1})
        assert response.status_code == 200
        assert response.get_json()['message'] == "Student enrolled successfully."

    def test_enroll_student_non_existent_course(client):
        response = client.post('/students/1/enroll', json={"course_id": 999})
        assert response.status_code == 400
        assert response.get_json()['error']['code'] == 'E001'

    def test_get_student_courses(client):
        response = client.get('/students/1/courses')
        assert response.status_code == 200
    ```
- [ ] Write tests for enrollment and course retrieval functionality

---

By following these tasks, the implementation plan of adding the course relationship to the student entity can proceed in a structured manner, ensuring that each component is developed, tested, and integrated effectively.