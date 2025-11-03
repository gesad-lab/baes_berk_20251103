# Implementation Plan: Add Course Relationship to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---
## Version
**Version**: 1.1.0

## Technology Stack
- **Backend Framework**: Flask (Python)
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **API Documentation**: Swagger/OpenAPI
- **Testing Framework**: pytest
- **Environment Management**: venv (Python virtual environments)
- **Serialization**: Marshmallow

## Architecture Overview
This implementation establishes a many-to-many relationship between `Student` and `Course` entities through a new `StudentCourses` table. Existing functionalities for both entities will remain intact, ensuring backward compatibility while allowing new features around student enrollments to be developed.

### Module Boundaries
1. **API Module**:
   - Introduce new routes for associating students with courses and retrieving courses for a student.
  
2. **Service Module**:
   - Add handling logic for associating students with courses and retrieving their courses.
  
3. **Data Module**:
   - Define the new `StudentCourses` relationship model.
  
4. **Validation Module**:
   - Implement input validation to ensure the course association adheres to required fields.

5. **Deployment/Configuration Module**:
   - Implement migration logic to introduce the new relationship table.

## Data Models
Define the `StudentCourses` many-to-many relationship model in `src/models/student_courses.py`.

```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StudentCourses(Base):
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")
```

### Updated Student and Course Models
Ensure `Student` and `Course` models are updated to establish relationships.

```python
# src/models/student.py
from sqlalchemy.orm import relationship

class Student(Base):
    __tablename__ = 'students'
    ...
    courses = relationship("StudentCourses", back_populates="student")

# src/models/course.py
from sqlalchemy.orm import relationship

class Course(Base):
    __tablename__ = 'courses'
    ...
    students = relationship("StudentCourses", back_populates="course")
```

### Database Schema
The new `student_courses` table will have the following schema:
- **student_id**: Integer (Foreign Key referencing `students.id`, Primary Key)
- **course_id**: Integer (Foreign Key referencing `courses.id`, Primary Key)

## API Contracts

### 1. Associate a Student with a Course
- **Endpoint**: `POST /students/:student_id/courses`
- **Request Body**:
    ```json
    {
      "course_id": "string"  // required
    }
    ```
- **Responses**:
  - **200 OK**:
    ```json
    {
      "message": "Successfully associated student with course."
    }
    ```
  - **404 Not Found**:
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Course does not exist."
      }
    }
    ```

### 2. Retrieve All Courses for a Student
- **Endpoint**: `GET /students/:student_id/courses`
- **Responses**:
  - **200 OK**:
    ```json
    [
      {
        "course_id": 1,
        "name": "Mathematics",
        "level": "Beginner"
      },
      {
        "course_id": 2,
        "name": "Physics",
        "level": "Intermediate"
      }
    ]
    ```

## Implementation Approach

### Step 1: Setup Project Structure
No changes are needed for the existing project structure.

### Step 2: Install Dependencies
All dependencies remain the same and require no new installations.

### Step 3: Update the Data Module
- Create a new file `src/models/student_courses.py` and implement the `StudentCourses` model as detailed above.
- Update `src/models/student.py` and `src/models/course.py` to include relationships with `StudentCourses`.

### Step 4: Database Migration
- Create a migration script using Flask-Migrate to add the `student_courses` table:
```bash
flask db migrate -m "Add StudentCourses relationship table"
flask db upgrade
```
- Ensure that the migration script does not affect existing `Student` or `Course` data.

### Step 5: Extend the Service Module
- In `src/services/student_course_service.py`, implement functions for associating a student with a course and retrieving a student's courses.

```python
def associate_student_with_course(student_id, course_id):
    # Logic to create a new entry in StudentCourses
    ...

def get_student_courses(student_id):
    # Logic to retrieve courses for a student
    ...
```

### Step 6: Implement the API Module
- Create a new file `src/api/student_course_api.py` and define endpoints for associating a student with a course and retrieving courses for a student.

### Step 7: Input Validation
- In `src/validation/student_course_validation.py`, implement input validation checks.

```python
def validate_association(data: dict) -> bool:
    # Validate the course_id exists in the Course table.
    ...
```

### Step 8: Write Unit Tests
- Create `tests/api/test_student_course_api.py` to test student-course association and retrieval scenarios, ensuring coverage for both success and failure cases.

### Step 9: Documentation
- Update API documentation to reflect the newly implemented endpoints for associating students with courses and retrieving their courses.

### Step 10: Continuous Integration
- Validate existing CI/CD integration with the inclusion of new tests for student-course functionality.

## Summary of Technical Decisions
- Flask and SQLAlchemy continue to provide a cohesive environment for this new feature.
- SQLite remains the chosen database, with a clear migration strategy to safely introduce the `student_courses` table.
- The implementation respects existing models and adds new capabilities without disrupting current processes.

## Next Steps
1. Review this plan with stakeholders for approval.
2. Proceed with the implementation based on the outlined approach.
3. Conduct iterative testing based on outcomes.

## Modifications Needed to Existing Files
1. **src/models/student_courses.py**:
   - Create the new `StudentCourses` model as detailed above.

2. **src/models/student.py**:
   - Add relationship back-reference for `courses`.

3. **src/models/course.py**:
   - Add relationship back-reference for `students`.

4. **src/services/student_course_service.py**:
   - Implement functions for associating students with courses and retrieving their courses.

5. **src/api/student_course_api.py**:
   - Define endpoints for associating students with courses and retrieving courses.

6. **src/validation/student_course_validation.py**:
   - Implement validation for required fields when associating a course with a student.

7. **tests/api/test_student_course_api.py**:
   - Write tests for the student-course association and retrieval functionalities, ensuring both success and error responses are appropriately handled.

## Documentation
- Update API documentation to reflect the changes in endpoint definitions for student-course relationships, ensuring clarity for future reference and usage.

--- 

This implementation plan outlines a comprehensive approach to establish a course relationship to the student entity within existing architecture while maintaining operational integrity.