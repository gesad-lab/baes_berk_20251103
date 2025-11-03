# Tasks: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models/student.py`
- `src/models/course.py`
- `src/api/routes.py`
- `src/services/student_service.py`
- `src/services/course_service.py`
- `tests/api/test_student_api.py`
- `tests/integration/test_student_integration.py`

## Task Breakdown

### Database Schema Update
- [ ] **Task 1**: Create migration script to add `student_course` junction table, preserving existing data  
  **File**: `migrations/versions/add_student_course_relationship.py`
  
```python
"""
Add student_course table.
"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'student_course',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['students.id']),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id']),
        sa.PrimaryKeyConstraint('student_id', 'course_id')
    )

def downgrade():
    op.drop_table('student_course')
```

### Models Update
- [ ] **Task 2**: Modify the `Student` model to add relationship to the `StudentCourse` entity  
  **File**: `src/models/student.py`

```python
from sqlalchemy.orm import relationship

class Student(Base):
    ...
    courses = relationship("StudentCourse", back_populates="student")
```

- [ ] **Task 3**: Modify the `Course` model to add relationship to the `StudentCourse` entity  
  **File**: `src/models/course.py`

```python
from sqlalchemy.orm import relationship

class Course(Base):
    ...
    students = relationship("StudentCourse", back_populates="course")
```

- [ ] **Task 4**: Create the `StudentCourse` model in a new file  
  **File**: `src/models/student_course.py`

```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class StudentCourse(Base):
    __tablename__ = 'student_course'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")
```

### API Endpoints Implementation
- [ ] **Task 5**: Implement API endpoint for enrolling student in course  
  **File**: `src/api/routes.py`

```python
@app.route('/api/v1/students/<int:student_id>/enroll', methods=['POST'])
def enroll_student(student_id):
    # Logic to enroll the student in a course
    ...
```

- [ ] **Task 6**: Implement API endpoint for disassociating student from course  
  **File**: `src/api/routes.py`

```python
@app.route('/api/v1/students/<int:student_id>/courses/<int:course_id>', methods=['DELETE'])
def disassociate_student(student_id, course_id):
    # Logic to disassociate the student from a course
    ...
```

- [ ] **Task 7**: Implement API endpoint for retrieving student's courses  
  **File**: `src/api/routes.py`

```python
@app.route('/api/v1/students/<int:student_id>/courses', methods=['GET'])
def get_student_courses(student_id):
    # Logic to retrieve courses for the student
    ...
```

### Business Logic Services
- [ ] **Task 8**: Create service functions for enrollment and disassociation logic  
  **File**: `src/services/student_service.py`

```python
def enroll_student_in_course(student_id, course_id):
    # Business logic to enroll student
    ...

def disassociate_student_from_course(student_id, course_id):
    # Business logic to disassociate student
    ...
```

### Input Validation
- [ ] **Task 9**: Implement input validation for student and course IDs  
  **File**: `src/validation/input_validation.py`

```python
def validate_student_course_ids(student_id, course_id):
    # Logic to validate IDs
    ...
```

### Testing & Quality Assurance
- [ ] **Task 10**: Write unit tests for the new service functions  
  **File**: `tests/unit/test_student_service.py`

- [ ] **Task 11**: Write integration tests for API endpoints  
  **File**: `tests/integration/test_student_integration.py`

```python
def test_enroll_student_api(client):
    # Test for the API endpoint to enroll a student
    ...

def test_get_student_courses_api(client):
    # Test for the API endpoint to get student's courses
    ...
```

### Documentation
- [ ] **Task 12**: Update the `README.md` with new API endpoint documentation  
  **File**: `README.md`

```markdown
## New Endpoints

- **Enroll Student in Course**: `POST /api/v1/students/<student_id>/enroll`
- **Disassociate Student from Course**: `DELETE /api/v1/students/<student_id>/courses/<course_id>`
- **Get Student Courses**: `GET /api/v1/students/<student_id>/courses`
```

---

This task breakdown provides a clear and structured path for implementing the feature of adding a course relationship to the student entity while ensuring all functionalities are retained and aligned with existing design patterns in the application.