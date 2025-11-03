# Tasks: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `models.py`
- `api.py`
- `student_service.py`
- `migrations/`

Instructions for Task Breakdown:
1. Identify which existing files need modifications.
2. Create new files for new functionality.
3. Ensure integration tasks are included.
4. Maintain consistency with existing code style and patterns.

---

## Tasks Breakdown

### Database Schema Modifications

- [ ] **Task 1: Update `models.py` to define the `StudentCourse` class**  
  **File**: `src/models.py`  
  **Description**: Define the new junction table `StudentCourse` to establish a many-to-many relationship between `Student` and `Course`.  
  **Dependencies**: None.  

```python
class StudentCourse(Base):
    __tablename__ = 'student_courses'
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship("Student", backref="courses")
    course = relationship("Course", backref="students")
```

---

### Migration Script

- [ ] **Task 2: Create migration script for `student_courses` table**  
  **File**: `src/migrations/20231017_create_student_courses.py`  
  **Description**: Write a migration script that creates the `student_courses` table without affecting existing data in the Student or Course tables.  
  **Dependencies**: Task 1.  

```python
from sqlalchemy import create_engine, MetaData, Column, Integer, ForeignKey, Table

def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    student_courses = Table('student_courses', meta,
        Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
        Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True),
    )
    meta.create_all()

def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    student_courses = Table('student_courses', meta, autoload=True)
    student_courses.drop()
```

---

### API Layer Modifications

- [ ] **Task 3: Update `api.py` to add new API endpoints**  
  **File**: `src/api.py`  
  **Description**: Implement the following endpoints:  
    - `POST /students/{student_id}/courses`: Enroll a student in a course.  
    - `GET /students/{student_id}/courses`: Retrieve a list of courses a student is enrolled in.  
    - `DELETE /students/{student_id}/courses/{course_id}`: Remove a course from a student's enrollment.  
  **Dependencies**: Task 1.  

```python
@app.route('/students/<int:student_id>/courses', methods=['POST'])
def enroll_student_in_course(student_id):
    # Implement the endpoint logic

@app.route('/students/<int:student_id>/courses', methods=['GET'])
def get_student_courses(student_id):
    # Implement the endpoint logic

@app.route('/students/<int:student_id>/courses/<int:course_id>', methods=['DELETE'])
def remove_course_from_student(student_id, course_id):
    # Implement the endpoint logic
```

---

### Service Layer Implementations

- [ ] **Task 4: Implement enrollment logic in `student_service.py`**  
  **File**: `src/student_service.py`  
  **Description**: Create functions for handling course enrollment, retrieving student courses, and removing a course from a student.  
  **Dependencies**: Task 1.  

```python
def enroll_student_in_course(student_id, course_id):
    # Implement the service logic to enroll a student

def get_student_courses(student_id):
    # Implement the service logic to retrieve courses

def remove_course_from_student(student_id, course_id):
    # Implement the service logic to remove a course
```

---

### Testing

- [ ] **Task 5: Update tests for new functionalities in `test_api.py`**  
  **File**: `tests/test_api.py`  
  **Description**: Add test cases for the new API endpoints ensuring successful enrollments, retrieval, and removal of courses, as well as handling errors related to invalid enrollments.  
  **Dependencies**: Task 3, Task 4.  

```python
def test_enroll_student_in_course():
    # Tests for successful and unsuccessful enrollments

def test_get_student_courses():
    # Tests to verify retrieval of course list

def test_remove_course_from_student():
    # Tests for successful removal of a course
```

---

### Documentation Updates

- [ ] **Task 6: Update Swagger documentation in `api.py` for new endpoints**  
  **File**: `src/api.py`  
  **Description**: Ensure the Swagger documentation includes the new API endpoints and their expected request/response formats.  
  **Dependencies**: Task 3.  

```python
# Update the documentation strings for new endpoints
```

---

## Conclusion

Once all tasks are completed, the feature to establish a relationship between the Student and Course entities will be implemented, allowing for organized tracking of student enrollments and smooth integration into the existing application without disrupting current functionalities. Each task can be tested independently, ensuring the gradual and efficient build-up of this feature.