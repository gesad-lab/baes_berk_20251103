# Implementation Plan: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---

## Overview
This implementation plan outlines the integration of a many-to-many relationship between the Student and Course entities. The main goal is to allow a Student to enroll in multiple Courses, facilitating future functionalities for tracking student progress and managing educational pathways. The implementation will involve adding new API endpoints for enrolling students in courses, retrieving students' course enrollments, and updating the database schema accordingly.

## Architecture
The architecture follows the Model-View-Controller (MVC) pattern, with the following components impacted by this implementation:

- **API Layer**: New endpoints for enrolling students in courses and retrieving student course details.
- **Service Layer**: Logic for handling student enrollments and fetching course information.
- **Data Access Layer (DAL)**: Updates to the data models to accommodate the many-to-many relationship.
- **Database**: The SQLite database schema will be updated to establish a join table for the Student-Course relationship.

### Module Boundaries
- **api.py**: Introduce new endpoints for enrolling students in courses and retrieving student course enrollments.
- **models.py**: Update existing Student and Course models to define relationships and create a new join table model (StudentCourse).
- **services.py**: Define business logic for enrolling students and fetching their courses.
- **database.py**: Implement migration functionality to add the joining table for Student and Course relationships.

## Technology Stack
- **Programming Language**: Python 3.11+
- **Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Serialization/Validation**: Pydantic
- **Testing Framework**: pytest

## Implementation Steps

### 1. Environment Setup
- Utilize the existing environment setup from the previous sprints. Ensure that FastAPI and SQLAlchemy remain installed; no new installations are necessary.

### 2. Define Data Models
- Update the existing `Student` and `Course` models in `models.py` to establish a relationship and create a new `StudentCourse` join table model:

```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    courses = relationship("StudentCourse", back_populates="student")

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    students = relationship("StudentCourse", back_populates="course")

class StudentCourse(Base):
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship(Student, back_populates="courses")
    course = relationship(Course, back_populates="students")
```

- Define a Pydantic schema for enrolling a student in a course in `schemas.py`:

```python
from pydantic import BaseModel

class EnrollStudent(BaseModel):
    course_id: int
```

### 3. Database Management
- Create a migration script using Alembic to create the `student_courses` join table without affecting existing data in the `students` and `courses` tables. Example migration script:

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

### 4. Implement API Endpoints
- Add a new `POST /students/{student_id}/courses` endpoint in `api.py` for enrolling students:

```python
@app.post("/students/{student_id}/courses")
def enroll_student(student_id: int, enrollment: EnrollStudent):
    return enroll_student_service(student_id, enrollment.course_id)
```

- Implement the `GET /students/{student_id}/courses` endpoint in `api.py` to retrieve all courses for a student:

```python
@app.get("/students/{student_id}/courses")
def get_student_courses(student_id: int):
    return get_student_courses_service(student_id)
```

### 5. Implement Business Logic
- Define service functions in `services.py` to handle the enrollment logic and fetching course information:

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

### 6. Error Handling
- Ensure appropriate error handling in `api.py` for cases of missing student or course IDs:

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

### 7. Testing
- Create a new test file `tests/test_student_courses.py` to cover the new functionality, ensuring that tests are included for both enrollment functionality and fetching student courses:

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

### 8. Documentation
- Update the existing `README.md` file to include new API requirements for enrolling students in courses and retrieving enrolled courses, along with usage examples.

## Scalability and Security Considerations
- **Scalability**: The many-to-many relationships are designed to scale without issues, allowing for a high number of enrollments while keeping API stateless.
- **Security**: Validate all inputs to prevent SQL injection attacks, and ensure that error messages provide no sensitive information.

## Deployment Considerations
- Migrate the database schema to include the new relationships during the deployment process. Execute the migration commands as follows:

```bash
alembic upgrade head
```

## Conclusion
This implementation plan details the structured approach for adding a course relationship to the student entity. It allows students to enroll in multiple courses while maintaining backward compatibility and ensuring a robust API structure. The defined steps ensure thorough testing and comprehensive error handling, facilitating smooth integration into the existing application framework.

### Existing Code Files Modifications
- **api.py** will have new endpoints for enrolling students in courses and retrieving course information.
- **models.py** will need modification to add the `StudentCourse` join table.
- **services.py** will be updated with new services for course enrollment and retrieval.
- A new file `schemas.py` will be created to manage validation schemas.
- **tests/test_student_courses.py** will be newly created for comprehensive course-related tests.