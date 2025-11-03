# Implementation Plan: Add Course Relationship to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

## Version: 1.1.0

## Overview
This implementation plan outlines the establishment of a many-to-many relationship between the Student and Course entities within the educational management system. This feature facilitates student enrollment in multiple courses, enriching student experiences and enhancing course management abilities.

## Technology Stack
- **Backend Framework**: Flask (Python)
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **API Format**: JSON
- **Testing Framework**: pytest
- **Request Validation**: marshmallow

## Architecture Overview
The application will be updated to include modifications to the existing data model to establish the many-to-many relationship with the following module structure:

### Module Structure
- **src/**
  - **models/**: Contains the database models (e.g., Student, Course, StudentCourses).
    - Implement a `StudentCourses` join table.
  - **repositories/**: Handles database interactions.
    - Implement a `StudentCoursesRepository` for managing relationships between students and courses.
  - **services/**: Contains business logic including student enrollment.
    - Create a service to handle the logic for enrolling students in courses.
  - **api/**: Manages API routes and requests.
    - Add routes for student enrollment and fetching courses for a given student.
  - **db/**: Manages database initialization and migrations.
    - Implement migrations to establish the many-to-many relationship.
  - **config/**: Holds configuration settings.
  - **app.py**: Main application entry point.

- **tests/**: Contains unit and integration tests organized by feature.
  - Add new tests for enrolling students in courses and retrieving their courses.

## Data Model
### StudentCourses Model
```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class StudentCourses(Base):
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

# Update Student Model to include relationship
class Student(Base):
    # existing attributes
    courses = relationship("StudentCourses", back_populates="student")

# Update Course Model to include relationship
class Course(Base):
    # existing attributes
    students = relationship("StudentCourses", back_populates="course")
```

## API Contract
### Endpoints
1. **Enroll Student in Course**
   - **Method**: POST
   - **Endpoint**: `/api/v1/students/enroll`
   - **Request Payload**:
   ```json
   {
     "student_id": 1,
     "course_id": 2
   }
   ```

   - **Response (201 Created)**:
   ```json
   {
     "student_id": 1,
     "course_id": 2,
     "message": "Student has been successfully enrolled in the course."
   }
   ```

   - **Response (400 Bad Request)**:
   ```json
   {
     "error": {
       "code": "E004",
       "message": "Invalid course ID provided for enrollment."
     }
   }
   ```

2. **Retrieve Student's Courses**
   - **Method**: GET
   - **Endpoint**: `/api/v1/students/<int:student_id>/courses`
   - **Response (200 OK)**:
   ```json
   {
     "student_id": 1,
     "courses": [
       {
         "course_id": 2,
         "name": "Introduction to Programming"
       }
     ]
   }
   ```

   - **Response (404 Not Found)**:
   ```json
   {
     "error": {
       "code": "E005",
       "message": "Student not found."
     }
   }
   ```

## Implementation Approach
1. **Set Up Project Structure**:
   - Utilize the existing directory layout and integrate new files and modifications as described.

2. **Create StudentCourses Model**:
   - Implement the `StudentCourses` model to reflect the defined many-to-many relationship, including foreign keys to Student and Course.

3. **Database Schema Update**:
   - Write a database migration script to create the `student_courses` join table while ensuring existing Student and Course data remains intact.
   - Migration example (using SQLAlchemy Migrate or Alembic):
   ```sql
   CREATE TABLE student_courses (
       student_id INTEGER,
       course_id INTEGER,
       PRIMARY KEY (student_id, course_id),
       FOREIGN KEY (student_id) REFERENCES students(id),
       FOREIGN KEY (course_id) REFERENCES courses(id)
   );
   ```

4. **Implement API Endpoints**:
   - Add Flask routes in `api` to handle student enrollment and retrieval of courses by student ID.
   - Implement error handling to manage invalid student or course data.

5. **Create StudentCourses Repository**:
   - Implement the `StudentCoursesRepository` to manage enrollment of students and associate them with courses.

6. **Create Enrollment Service**:
   - Implement a service that encapsulates the business logic for enrolling students in courses, including validation checks for student and course existence.

7. **Testing**:
   - Write unit tests to validate the enrollment and retrieval functionalities for students and courses.
   - Ensure tests cover both successful enrollments and error scenarios involving invalid input.

8. **Documentation**:
   - Update README.md to reflect changes in the API structure, including endpoints for enrolling students in courses and retrieving their courses.

## Key Considerations
- **Scalability**: Structure the `StudentCourses` model to accommodate future additions of more fields if necessary without requiring substantial refactoring.
- **Security**: Ensure proper validation is implemented to prevent invalid or harmful user inputs from being processed.
- **Maintainability**: Adhere to coding standards outlined in the Default Project Constitution to keep the codebase organized and manageable.

## Success Criteria
- 100% success rate for valid enrollment requests, confirming valid student and course IDs are processed correctly.
- 100% success rate for retrieving courses for students, ensuring all relevant details are returned if the student exists.
- Successful application startup without errors, verifying the new schema and ensuring existing Student and Course data remain unaffected.
- All API responses delivered in valid JSON format, with appropriate HTTP status codes.

## Conclusion
This implementation plan specifies the necessary modifications for adding a course relationship to the student entity within the educational management system, providing a clear and structured approach that integrates seamlessly with existing functionality. The plan accounts for future scalability while ensuring the codebase remains straightforward and maintainable.

Existing Code Modifications:
```python
# New File: src/models/student_courses.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class StudentCourses(Base):
    """Join table for Student and Course many-to-many relationship"""
    
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

# Modify File: src/models/student.py
from sqlalchemy.orm import relationship

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    # (...) existing attributes
    courses = relationship("StudentCourses", back_populates="student")

# Modify File: src/models/course.py
from sqlalchemy.orm import relationship

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    # (...) existing attributes
    students = relationship("StudentCourses", back_populates="course")

# New File: src/repositories/student_courses_repository.py
from models.student_courses import StudentCourses
from models.student import Student
from models.course import Course
from database import session

class StudentCoursesRepository:
    """Handles database interactions for Student-Course relationships."""
    
    def enroll_student_in_course(self, student_id, course_id):
        enrollment = StudentCourses(student_id=student_id, course_id=course_id)
        session.add(enrollment)
        session.commit()
        return enrollment

    def get_courses_for_student(self, student_id):
        return session.query(StudentCourses).filter_by(student_id=student_id).all()

# New File: src/services/enrollment_service.py
from repositories.student_courses_repository import StudentCoursesRepository
from models.student import Student
from models.course import Course

class EnrollmentService:
    """Encapsulates the business logic for enrolling students in courses."""
    
    def __init__(self):
        self.enrollment_repo = StudentCoursesRepository()

    def enroll_student(self, student_id, course_id):
        student = session.query(Student).filter_by(id=student_id).first()
        course = session.query(Course).filter_by(id=course_id).first()
        
        if not student:
            raise ValueError("Student not found.")
        if not course:
            raise ValueError("Course not found.")
        
        return self.enrollment_repo.enroll_student_in_course(student_id, course_id)

    def get_courses_for_student(self, student_id):
        return self.enrollment_repo.get_courses_for_student(student_id)

# New File: src/api/enrollment_api.py
from flask import Blueprint, request, jsonify
from services.enrollment_service import EnrollmentService

enrollment_api = Blueprint('enrollment_api', __name__)
enrollment_service = EnrollmentService()

@enrollment_api.route('/api/v1/students/enroll', methods=['POST'])
def enroll_student():
    data = request.json
    try:
        enrollment = enrollment_service.enroll_student(data['student_id'], data['course_id'])
        return jsonify({
            "student_id": enrollment.student_id,
            "course_id": enrollment.course_id,
            "message": "Student has been successfully enrolled in the course."
        }), 201
    except ValueError as e:
        return jsonify({"error": {"code": "E004", "message": str(e)}}), 400

@enrollment_api.route('/api/v1/students/<int:student_id>/courses', methods=['GET'])
def get_student_courses(student_id):
    try:
        courses = enrollment_service.get_courses_for_student(student_id)
        return jsonify({
            "student_id": student_id,
            "courses": [{"course_id": c.course_id, "name": c.course.name} for c in courses]
        }), 200
    except ValueError as e:
        return jsonify({"error": {"code": "E005", "message": str(e)}}), 404

# New tests in tests/test_enrollment.py
def test_enroll_student(enrollment_service):
    """Test enrolling a student in a course."""
    enrollment_data = {
        'student_id': 1,
        'course_id': 2
    }
    enrollment = enrollment_service.enroll_student(enrollment_data['student_id'], enrollment_data['course_id'])
    assert enrollment.student_id == 1
    assert enrollment.course_id == 2

def test_get_student_courses(enrollment_service):
    """Test retrieving courses for a student."""
    student_courses = enrollment_service.get_courses_for_student(1)
    assert len(student_courses) > 0  # Assuming student has enrolled in at least one course
```

This implementation plan ensures a structured approach to adding a course relationship to the student entity in the educational management system, effectively integrating with existing functionalities while adhering to the best coding practices.