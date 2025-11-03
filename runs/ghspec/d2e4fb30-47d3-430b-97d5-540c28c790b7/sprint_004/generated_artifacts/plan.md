# Implementation Plan: Add Course Relationship to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

## Version
1.0.0

## Purpose
To implement the feature that allows a relationship to be established between the existing Student entity and the newly created Course entity. This implementation will facilitate course assignments and tracking for students in the educational application.

## Technology Stack
- **Backend Framework**: FastAPI (Python)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Data Validation**: Pydantic
- **API Documentation**: Swagger (automatically provided by FastAPI)
- **Testing Framework**: pytest
- **Deployment**: Docker for containerization
- **Environment Management**: .env files for configuration 

## Architectural Overview
The application will maintain a clean architecture, ensuring proper separation of concerns between different modules:
- **API Layer**: Manages HTTP requests and responses related to course assignments.
- **Service Layer**: Contains business logic for assigning courses to students and retrieving student course data.
- **Data Access Layer**: Interacts with the database to manage relationships and ensure data integrity.
- **Database Layer**: Configuration of database models and management of the new `student_courses` linking table.

## Module Responsibilities

### 1. API Layer
- Handles incoming HTTP requests for course assignments and retrieval of enrolled courses.
- Maps requests to appropriate service methods.
- Responsible for input validation and returning appropriate responses, including error messages.

### 2. Service Layer
- Implements business logic for assigning courses to students.
- Validates input data and ensures correctness before interacting with the data access layer.

### 3. Data Access Layer
- Manages interactions with the database using SQLAlchemy to perform operations related to student-course relationships.
- Implements functionality to create and query the `student_courses` table.

## Data Models

### Student Model
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    # ... existing fields
```

### Course Model (Create in `src/models/course.py`)
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    level = Column(String(255), nullable=False)
```

### Student-Course Linking Table (To be created)
```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class StudentCourse(Base):
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")
```

## API Contracts

### Assign Courses to Student
- **Endpoint**: `POST /students/{studentId}/courses`
- **Request Body**:
    ```json
    {
        "courseIds": ["course1", "course2"]
    }
    ```
- **Response** (Success - 200 OK):
    ```json
    {
        "message": "Courses assigned successfully.",
        "assignedCourses": ["course1", "course2"]
    }
    ```
- **Response** (Error - 404 Not Found):
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Course ID course1 not found."
        }
    }
    ```

### Retrieve Enrolled Courses
- **Endpoint**: `GET /students/{studentId}/courses`
- **Response** (Success - 200 OK):
    ```json
    [
        {
            "id": 1,
            "name": "Math 101",
            "level": "Beginner"
        },
        {
            "id": 2,
            "name": "Science 201",
            "level": "Intermediate"
        }
    ]
    ```

## Implementation Steps

1. **Project Setup**
   - Maintain the existing FastAPI project structure set up in previous implementations.
   - Ensure Docker is configured for PostgreSQL as per the existing setup.

2. **Model Creation**
   - Create the `Course` model and the linking table `StudentCourse` in the `src/models/course.py` file, as shown in the data models above.
   
3. **Database Schema Management**
   - Create an Alembic migration script to add the `student_courses` linking table while preserving existing Student and Course data.
   ```bash
   alembic revision --autogenerate -m "Add Student-Course Relationship"
   ```
   - The migration script should include:
     ```python
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

4. **API Development**
   - Create a new API router for handling the course assignments in `src/routes/student.py`.
   
   ```python
   from fastapi import APIRouter, HTTPException, Depends
   from sqlalchemy.orm import Session
   from ..models.course import Course
   from ..models.student import Student
   from ..models.student_course import StudentCourse
   from ..database import get_db

   router = APIRouter()

   class CourseAssignment(BaseModel):
       courseIds: List[str]

   @router.post("/students/{student_id}/courses")
   async def assign_courses(student_id: int, course_assignment: CourseAssignment, db: Session = Depends(get_db)):
       student = db.query(Student).filter(Student.id == student_id).first()
       if not student:
           raise HTTPException(status_code=404, detail="Student not found")
       
       assigned_courses = []
       for course_id in course_assignment.courseIds:
           course = db.query(Course).filter(Course.id == course_id).first()
           if not course:
               raise HTTPException(status_code=404, detail=f"Course ID {course_id} not found.")
           assigned_courses.append(course)
           student_course = StudentCourse(student_id=student.id, course_id=course.id)
           db.add(student_course)
       db.commit()
       return {"message": "Courses assigned successfully.", "assignedCourses": course_assignment.courseIds}

   @router.get("/students/{student_id}/courses")
   async def get_courses(student_id: int, db: Session = Depends(get_db)):
       student_courses = db.query(StudentCourse).filter(StudentCourse.student_id == student_id).all()
       if not student_courses:
           raise HTTPException(status_code=404, detail="No courses found for this student.")
       
       courses = []
       for student_course in student_courses:
           course = db.query(Course).filter(Course.id == student_course.course_id).first()
           courses.append({"id": course.id, "name": course.name, "level": course.level})
       return courses
   ```

5. **Update Main Application**
   - Integrate the updated student router into the main FastAPI application in `src/main.py`:
   ```python
   from fastapi import FastAPI
   from .routes.student import router as student_router

   app = FastAPI()

   app.include_router(student_router)
   ```

6. **Testing**
   - Create a test file `tests/test_students.py` to add tests for the new course assignment and retrieval functionalities:
   ```python
   from fastapi.testclient import TestClient
   from your_project.main import app

   client = TestClient(app)

   def test_assign_courses():
       response = client.post("/students/1/courses", json={"courseIds": ["1", "2"]})
       assert response.status_code == 200
       assert response.json() == {"message": "Courses assigned successfully.", "assignedCourses": ["1", "2"]}

   def test_get_courses():
       response = client.get("/students/1/courses")
       assert response.status_code == 200
       assert isinstance(response.json(), list)

   def test_assign_invalid_course():
       response = client.post("/students/1/courses", json={"courseIds": ["invalid-course"]})
       assert response.status_code == 404
       assert response.json() == {"detail": "Course ID invalid-course not found."}
   ```

7. **Documentation**
   - Ensure that the FastAPI automatically generates documentation for the new endpoints in Swagger. Validate that the `/students/{studentId}/courses` endpoints are described accurately.

8. **Deployment**
   - Update Docker configurations if necessary for migrations.
   - Validate the success of the migration in local and production environments.

## Success Criteria
- **Assign Courses**: Successfully assigning courses returns a status code of 200 with confirmation details.
- **Retrieve Courses**: The endpoint returns a list of courses for the specified student with a status code of 200.
- **Validation**: Handling of invalid requests correctly returns a status code of 404 with appropriate messages.
- **Database Migration**: The migration for the `student_courses` linking table executes without affecting existing records, enabling smooth application startup.

## Trade-offs and Considerations
- **Migration Overheads**: Introducing a migration step may add complexity but is crucial for maintaining database integrity.
- **Error Messaging**: Basic error messages are provided; more detailed messages can be added in future iterations.
- **Testing Depth**: Although test coverage is essential for new functionality, comprehensive tests will ensure that existing features remain reliable after integration.

## Conclusion
This implementation plan outlines the structured steps needed to introduce a course relationship to the existing Student entity in the educational application, ensuring adherence to established architecture principles and maintaining code maintainability for future enhancements.