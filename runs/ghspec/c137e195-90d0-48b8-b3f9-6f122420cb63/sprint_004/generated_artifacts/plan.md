# Implementation Plan: Add Course Relationship to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:  
# Implementation Plan: Create Course Entity

---
## Version
1.0.0

## Purpose
To establish a many-to-many relationship between the Student and Course entities within the existing system, enabling enhanced course management and student course associations for functionalities such as course registration and student progress tracking.

## Technology Stack
- **Backend Framework**: FastAPI (for building the REST API)
- **Database**: SQLite (for data persistence)
- **ORM**: SQLAlchemy (for database interactions)
- **Data Format**: JSON (for API requests and responses)
- **Testing Framework**: pytest (for unit and integration testing)

## Architecture Overview
This implementation will introduce a new junction table to support the relationship between the `Student` and `Course` entities. The main modules involved will include:
1. **Models**: Defines the StudentCourseAssociation model for managing relationships.
2. **API**: Implements RESTful endpoints for course assignment and retrieval.
3. **Database**: Handles database migrations and schema updates to ensure data integrity.
4. **Error Handling**: Centralizes error responses for API requests.
5. **Testing**: Ensures that new functionalities are adequately covered with tests.

## Module Layout
```
src/
    ├── api/
    │   └── student_courses.py      # New endpoint for student-course associations
    ├── models/
    │   ├── student_course_association.py  # Junction model definition
    │   └── course.py                 # Course model definition (if needed)
    ├── database/
    │   └── db.py                     # Database connection and schema initialization (modified to include new association)
    ├── error_handlers/
    │   └── error_responses.py        # Centralized error handling
    └── main.py                       # Application entry point (modified)
tests/
    ├── test_student_courses.py        # Tests for student-course API endpoints (new)
```

## Implementation Approach

### 1. Database Model
- **StudentCourseAssociation Model**:
    ```python
    from sqlalchemy import Column, ForeignKey
    from sqlalchemy.orm import relationship
    from database.db import Base

    class StudentCourseAssociation(Base):
        __tablename__ = 'student_course_association'
        
        student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
        course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

        student = relationship("Student", back_populates="courses")
        course = relationship("Course", back_populates="students")
    ```

### 2. Modifications to Existing Student and Course Models
- Update the `Student` and `Course` models to include relationships.
    ```python
    # In models/student.py
    class Student(Base):
        __tablename__ = 'students'
        
        id = Column(Integer, primary_key=True, autoincrement=True)
        # ... existing fields
        courses = relationship("StudentCourseAssociation", back_populates="student")

    # In models/course.py
    class Course(Base):
        __tablename__ = 'courses'
        
        id = Column(Integer, primary_key=True, autoincrement=True)
        # ... existing fields
        students = relationship("StudentCourseAssociation", back_populates="course")
    ```

### 3. Database Migration Strategy
- **Automated Schema Update**:
    The application will check for the existence of the new junction table at startup and create it if it does not exist, while ensuring existing data in `students` and `courses` is preserved:
    ```python
    from sqlalchemy import inspect

    def init_db():
        Base.metadata.create_all(bind=engine)  # Ensures all necessary tables are created
        
        inspector = inspect(engine)
        if "student_course_association" not in inspector.get_table_names():  # Check if the junction table exists
            with engine.begin() as connection:
                connection.execute('CREATE TABLE student_course_association (student_id INTEGER, course_id INTEGER, PRIMARY KEY(student_id, course_id))')
                # Optionally add foreign keys for integrity
    ```

### 4. API Endpoints
- **Assign Courses to a Student**:
    ```python
    from fastapi import APIRouter, HTTPException
    from models.student_course_association import StudentCourseAssociation
    from models.student import Student
    from models.course import Course
    from database.db import SessionLocal
    from pydantic import BaseModel
    from typing import List

    router = APIRouter()

    class CourseAssignment(BaseModel):
        course_ids: List[int]

    @router.post("/students/{student_id}/courses", status_code=200)
    def assign_courses(student_id: int, assignment: CourseAssignment):
        db = SessionLocal()
        student = db.query(Student).filter(Student.id == student_id).first()
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        
        courses = db.query(Course).filter(Course.id.in_(assignment.course_ids)).all()
        if len(courses) != len(assignment.course_ids):
            raise HTTPException(status_code=404, detail="One or more courses not found")

        for course in courses:
            association = StudentCourseAssociation(student_id=student_id, course_id=course.id)
            db.add(association)
        db.commit()
        
        return {"student_id": student_id, "assigned_courses": [course.id for course in courses]}
    ```

- **Retrieve Student Information with Courses**:
    ```python
    @router.get("/students/{student_id}", status_code=200)
    def get_student_info(student_id: int):
        db = SessionLocal()
        student = db.query(Student).filter(Student.id == student_id).first()
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        
        courses = db.query(Course).join(StudentCourseAssociation).filter(StudentCourseAssociation.student_id == student_id).all()
        return {
            "student_id": student.id,
            "courses": [{"id": course.id, "name": course.name, "level": course.level} for course in courses]
        }
    ```

### 5. Application Entry Point
- **Main Application** (Updated):
    The entry point will integrate the newly created student-course routes:
    ```python
    from fastapi import FastAPI
    from database.db import init_db
    from api.student_courses import router as student_courses_router

    app = FastAPI()

    @app.on_event("startup")
    def startup():
        init_db()

    app.include_router(student_courses_router)
    ```

## Testing Strategy
- **Unit and Integration Tests** implemented with pytest will validate the new student-course relationship functionalities including assignment and retrieval, ensuring appropriate error handling.
- Testing scenarios will include:
    - Assigning valid/invalid course IDs to students.
    - Retrieving student data to verify the courses are properly included in the response.
    - Testing error handling for missing students or courses.

### Testing Structure
- **Unit tests** located in `tests/test_student_courses.py`:
    ```python
    def test_assign_courses_to_student(client):
        response = client.post("/students/1/courses", json={"course_ids": [1, 2]})
        assert response.status_code == 200
        assert response.json()["assigned_courses"] == [1, 2]

    def test_assign_courses_non_existent_student(client):
        response = client.post("/students/999/courses", json={"course_ids": [1]})
        assert response.status_code == 404
        assert "Student not found" in response.json()['detail']

    def test_get_student_info_with_courses(client):
        response = client.get("/students/1")
        assert response.status_code == 200
        # Check if response includes expected student details and courses
    ```

## API Contracts
- **POST /students/{student_id}/courses**:
    - Request:
        ```json
        {
            "course_ids": [1, 2]
        }
        ```
    - Response:
        ```json
        {
            "student_id": 1,
            "assigned_courses": [1, 2]
        }
        ```

- **GET /students/{student_id}**:
    - Response:
        ```json
        {
            "student_id": 1,
            "courses": [
                {
                    "id": 1,
                    "name": "Mathematics",
                    "level": "Advanced"
                },
                {
                    "id": 2,
                    "name": "History",
                    "level": "Intermediate"
                }
            ]
        }
        ```

## Deployment Considerations
- The application will run locally using Uvicorn as the ASGI server.
- Update the `README.md` file to include setup instructions for the new student-course relationship functionality, including endpoints and expected data formats.

## Success Criteria
1. Successful assignment of courses to a student returns a status code of 200 OK and includes the assigned courses.
2. Retrieving student data successfully includes the associated courses in the JSON response.
3. The application handles errors properly, providing meaningful HTTP status codes and error messages without breaking existing functionality.
4. The database schema is updated automatically without requiring user intervention, maintaining the integrity of the existing Student and Course data.

This implementation plan outlines a comprehensive strategy for adding a course relationship to the student entity, ensuring a robust and scalable backend architecture while adhering to the outlined technical standards and ensuring backward compatibility.