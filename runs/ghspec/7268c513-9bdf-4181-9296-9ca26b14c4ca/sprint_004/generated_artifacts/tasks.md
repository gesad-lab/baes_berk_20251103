# Tasks: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- src/models/student.py (Student model)
- src/models/course.py (Course model)
- src/routes.py (Current API routes)
- src/tests/test_student.py (Existing student tests)

---

## Task Breakdown

### 1. **Update Existing Files**

- [ ] **Modify Student Model to Include Course Relationship**  
  **File**: `src/models/student.py`  
  **Task**: Update the `Student` class to include a relationship with the `Course` model.
  
```python
class Student(Base):
    ...
    course_ids = relationship("Course", secondary="student_course", back_populates="students")
```

- [ ] **Modify Course Model to Include Student Relationship**  
  **File**: `src/models/course.py`  
  **Task**: Update the `Course` class to include a relationship with the `Student` model.
  
```python
class Course(Base):
    ...
    students = relationship("Student", secondary="student_course", back_populates="courses")
```

- [ ] **Create StudentCourse Association Model**  
  **File**: `src/models/student_course.py`  
  **Task**: Create the `StudentCourse` model to handle the many-to-many relationship between students and courses.
  
```python
from app import db
from sqlalchemy import Column, Integer, ForeignKey

class StudentCourse(db.Model):
    __tablename__ = 'student_course'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
```

---

### 2. **Implement New Functionality**

- [ ] **Create Database Migration Script**  
  **File**: `src/migrations/versions/xxxx_add_student_course_association.py`  
  **Task**: Write a migration script to create the `student_course` table and establish relationships.
  
```python
def upgrade():
    op.create_table('student_course',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True)
    )
```

- [ ] **Implement Enroll Student in Course API Endpoint**  
  **File**: `src/routes.py`  
  **Task**: Add a route to handle POST requests for enrolling students in courses.

```python
@students_bp.route('/students/<int:student_id>/courses', methods=['POST'])
def enroll_student_course(student_id):
    ...
```

- [ ] **Implement Get Enrolled Courses API Endpoint**  
  **File**: `src/routes.py`  
  **Task**: Add a route to handle GET requests to retrieve courses a student is enrolled in.

```python
@students_bp.route('/students/<int:student_id>/courses', methods=['GET'])
def get_enrolled_courses(student_id):
    ...
```

---

### 3. **Add Validation Logic**

- [ ] **Add Validation for Course ID in Enrollment**  
  **File**: `src/routes.py`  
  **Task**: Ensure that the `courseId` is validated upon enrollment requests.
  
```python
if not course_id:
    return jsonify({"error": {"code": "E001", "message": "Course ID is required."}}), 400
```

---

### 4. **Implement Error Handling**

- [ ] **Add Structured Error Response for Incorrect Course ID**  
  **File**: `src/routes.py`  
  **Task**: Implement error handling for cases where a student attempts to enroll in a non-existent course.
  
```python
if not course:
    return jsonify({"error": {"code": "E002", "message": "Course does not exist."}}), 404
```

---

### 5. **Create & Update Tests**

- [ ] **Create Unit Tests for New Functionality**  
  **File**: `src/tests/test_student_courses.py`  
  **Task**: Write unit tests for new endpoints related to student course enrollments.
  
```python
def test_enroll_student_in_course(client):
    ...
def test_enroll_student_in_invalid_course(client):
    ...
def test_get_enrolled_courses(client):
    ...
```

- [ ] **Update Existing Tests for Impacted Functionality**  
  **File**: `src/tests/test_student.py`  
  **Task**: Review and update existing test cases to ensure compatibility with the new course relationship features.

---

### 6. **Documentation Updates**

- [ ] **Update API Documentation**  
  **File**: `src/docs/api_documentation.md`  
  **Task**: Document new API endpoints for enrolling and retrieving courses.
  
- [ ] **Update README.md with Setup Instructions**  
  **File**: `README.md`  
  **Task**: Ensure the README includes setup and usage details for the new course-related functionality.

---

This structured breakdown provides clear, file-scoped tasks that can be executed independently, ensuring alignment with the project scope and coding standards. Each task is designed to maintain the integrity of the existing application while implementing the new feature effectively.