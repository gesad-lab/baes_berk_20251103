# Tasks: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- tests/test_courses.py (1375 bytes)

## Task Breakdown

### Module Boundary: Models

- [ ] **Update `src/models.py` to define the `StudentCourse` join table**
    - **File Path**: `src/models.py`
    - **Details**: Add the `StudentCourse` model to establish many-to-many relationships between `Student` and `Course`.
    
```python
class StudentCourse(Base):
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship(Student, back_populates="courses")
    course = relationship(Course, back_populates="students")
```

### Module Boundary: Database Management

- [ ] **Create Migration Script for `student_courses` Table**
    - **File Path**: `migrations/versions/create_student_courses_table.py`
    - **Details**: Use Alembic to create a migration script that creates the `student_courses` join table.

```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True),
    )

def downgrade():
    op.drop_table('student_courses')
```

### Module Boundary: API Layer

- [ ] **Implement `POST /students/{student_id}/courses` Endpoint in `src/api.py`**
    - **File Path**: `src/api.py`
    - **Details**: Create an endpoint that allows enrollment of a student in a course based on `student_id` and `course_id`.

```python
@app.post("/students/{student_id}/courses")
def enroll_student(student_id: int, enrollment: EnrollStudent):
    return enroll_student_service(student_id, enrollment.course_id)
```

- [ ] **Implement `GET /students/{student_id}/courses` Endpoint in `src/api.py`**
    - **File Path**: `src/api.py`
    - **Details**: Create an endpoint to retrieve all courses of a specific student.

```python
@app.get("/students/{student_id}/courses")
def get_student_courses(student_id: int):
    return get_student_courses_service(student_id)
```

### Module Boundary: Service Layer

- [ ] **Define Service Functions in `src/services.py` for Enrollment and Course Retrieval**
    - **File Path**: `src/services.py`
    - **Details**: Implement logic to handle the enrollment process and fetch student courses.

```python
def enroll_student_service(student_id: int, course_id: int):
    enrollment = StudentCourse(student_id=student_id, course_id=course_id)
    session.add(enrollment)
    session.commit()
    return {"message": "Enrollment successful", "student_id": student_id, "course_id": course_id}

def get_student_courses_service(student_id: int):
    student_courses = session.query(StudentCourse).filter(StudentCourse.student_id == student_id).all()
    return [{"id": sc.course.id, "name": sc.course.name, "level": sc.course.level} for sc in student_courses]
```

### Module Boundary: Schema Layer

- [ ] **Create Pydantic Schema for Enrollment in `src/schemas.py`**
    - **File Path**: `src/schemas.py`
    - **Details**: Add a schema to validate the enrollment request payload.

```python
class EnrollStudent(BaseModel):
    course_id: int
```

### Module Boundary: Error Handling

- [ ] **Implement Error Handling Logic in `src/api.py` for Enrollment Endpoint**
    - **File Path**: `src/api.py`
    - **Details**: Add error handling for cases where course ID is missing or student does not exist.

```python
@app.post("/students/{student_id}/courses")
def enroll_student(student_id: int, enrollment: EnrollStudent):
    if not enrollment.course_id:
        raise HTTPException(status_code=400, detail="Course ID is required.")
    return enroll_student_service(student_id, enrollment.course_id)

@app.get("/students/{student_id}/courses")
def get_student_courses(student_id: int):
    if not student_exists(student_id):
        raise HTTPException(status_code=404, detail="Student not found.")
    return get_student_courses_service(student_id)
```

### Module Boundary: Testing

- [ ] **Create Unit Tests for Enrollment and Retrieval in `tests/test_student_courses.py`**
    - **File Path**: `tests/test_student_courses.py`
    - **Details**: Write tests for the new API endpoints and validate the proper handling of requests.

```python
def test_enroll_student(client):
    response = client.post("/students/1/courses", json={"course_id": 2})
    assert response.status_code == 201
    assert response.json()["message"] == "Enrollment successful"

def test_get_student_courses(client):
    response = client.get("/students/1/courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_enroll_student_missing_course(client):
    response = client.post("/students/1/courses", json={})
    assert response.status_code == 400
    assert response.json()["detail"] == "Course ID is required."
```

### Module Boundary: Documentation

- [ ] **Update `README.md` with New API Endpoints and Usage Examples**
    - **File Path**: `README.md`
    - **Details**: Document the new API features, including endpoint descriptions, request/response formats, and usage instructions.

---

This structured task breakdown will help in the incremental implementation of the "Add Course Relationship to Student Entity" feature, ensuring that each part of the specification is addressed methodically.