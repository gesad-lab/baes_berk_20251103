# Implementation Plan: Add Teacher Relationship to Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Course Relationship to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## Version
1.2.0

## Overview
This implementation plan outlines the technical design for enhancing the Student Management Web Application by establishing a relationship between the Course entity and the Teacher entity. This feature will facilitate better management of course assignments and responsibilities of teaching staff.

## Technology Stack
- **Programming Language**: Python
- **Web Framework**: Flask
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **HTTP Client**: Requests (for potential testing/interaction)
- **Testing Framework**: pytest
- **API Documentation**: Swagger (Flasgger)

## Architecture Overview
1. **API Layer**: Handles HTTP requests for assigning, unassigning, and retrieving Course entities along with their associated Teacher entities.
2. **Service Layer**: Contains business logic for managing Course and Teacher relationships, including assignments and retrievals.
3. **Data Access Layer**: Interacts with the SQLite database via SQLAlchemy for both Course and Teacher entities.
4. **Model Layer**: Enhancements to the existing Course model to include a reference to the Teacher model.

## Module Breakdown
### 1. API Layer (`api.py`)
- New endpoint definitions for:
  - `PUT /courses/{course_id}/assign-teacher/{teacher_id}`: Assign a teacher to a specific course.
  - `DELETE /courses/{course_id}/unassign-teacher`: Remove the teacher assignment from a course.
  - `GET /courses/{course_id}`: Retrieve the details of a specific course, including the assigned teacher.
  - `GET /courses`: Retrieve a list of all courses along with their assigned teachers.

### 2. Service Layer (`course_service.py`)
- Implement new functions related to Course management with Teacher assignments:
  - `assign_teacher_to_course(course_id, teacher_id)`: Assigns a specific teacher to the given course.
  - `unassign_teacher_from_course(course_id)`: Unassigns the teacher from the specified course.
  - `get_course_details(course_id)`: Retrieves course details, including the associated teacher.
  - `list_courses_with_teachers()`: Retrieves all courses with their assigned teachers.

### 3. Data Access Layer (`models.py`)
- Update the `Course` class to include a reference to the `Teacher` class:
  ```python
  from sqlalchemy import Column, Integer, String, ForeignKey
  from sqlalchemy.orm import relationship
  from sqlalchemy.ext.declarative import declarative_base
  
  Base = declarative_base()

  class Course(Base):
      __tablename__ = 'courses'
      id = Column(Integer, primary_key=True, autoincrement=True)
      name = Column(String, nullable=False)
      level = Column(String, nullable=False)
      teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New field

      teacher = relationship("Teacher", back_populates="courses")  # Establish relationship

  class Teacher(Base):
      __tablename__ = 'teachers'
      id = Column(Integer, primary_key=True, autoincrement=True)
      name = Column(String, nullable=False)
      email = Column(String, nullable=False, unique=True)
      courses = relationship("Course", back_populates="teacher")  # Establish relationship
  ```

### 4. Migration Scripts (`migrations/`)
- Create a new migration script to safely alter the existing Course table to include the `teacher_id` column:
  ```python
  from sqlalchemy import create_engine, Column, Integer, ForeignKey, Table, MetaData

  def upgrade(migrate_engine):
      meta = MetaData(bind=migrate_engine)
      courses = Table('courses', meta, autoload=True)
      # Adding new column
      teacher_id_col = Column('teacher_id', Integer, ForeignKey('teachers.id'), nullable=True)
      teacher_id_col.create(courses)

  def downgrade(migrate_engine):
      meta = MetaData(bind=migrate_engine)
      courses = Table('courses', meta, autoload=True)
      # Dropping new column
      courses.c.teacher_id.drop()
  ```
  This migration will establish the `teacher_id` foreign key within the existing Course table without losing existing data.

### 5. Testing Suite (`tests/test_api.py`)
- Additional test cases for the new functionalities related to course and teacher assignments. Include tests for assigning/unassigning teachers, and retrieving courses with teacher details.

## Data Models
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Reference to Teachers
    teacher = relationship("Teacher", back_populates="courses")

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    courses = relationship("Course", back_populates="teacher")  # Relationship back to Course
```

## API Contracts
### Endpoint: `PUT /courses/{course_id}/assign-teacher/{teacher_id}`
- **Request**: Assigns a teacher to a course.
- **Response** (200 OK):
  ```json
  {
    "message": "Teacher assigned successfully."
  }
  ```

### Endpoint: `DELETE /courses/{course_id}/unassign-teacher`
- **Request**: Removes the teacher from the specified course.
- **Response** (200 OK):
  ```json
  {
    "message": "Teacher unassigned successfully."
  }
  ```

### Endpoint: `GET /courses/{course_id}`
- **Response** (200 OK):
  ```json
  {
    "course": {
      "id": 1,
      "name": "Mathematics 101",
      "level": "Beginner",
      "teacher": {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
    }
  }
  ```

### Endpoint: `GET /courses`
- **Response** (200 OK):
  ```json
  {
    "courses": [
      {
        "id": 1,
        "name": "Mathematics 101",
        "level": "Beginner",
        "teacher": {
          "id": 1,
          "name": "John Doe",
          "email": "john.doe@example.com"
        }
      },
      {
        "id": 2,
        "name": "Biology 202",
        "level": "Intermediate",
        "teacher": null
      }
    ]
  }
  ```

### Error Responses
- **Error when course not found**:
  ```json
  {
    "error": {
      "code": "E404",
      "message": "Course not found."
    }
  }
  ```

## Implementation Approach
1. **Setup Application Structure**:
   - Modify the `Course` model in `models.py` to include the `teacher_id` reference.
   - Create necessary service methods in `course_service.py` for managing teacher assignments to courses.

2. **Define API Endpoints**:
   - Update `api.py` to add the new routes for assigning and unassigning teachers.

3. **Implement Service Logic**:
   - In `course_service.py`, ensure all course-to-teacher relationship operations are implemented correctly.

4. **Database Migration**:
   - Create the migration file to add `teacher_id` to the existing Course table and manage data integrity.

5. **Testing**:
   - Extend `tests/test_api.py` with additional test coverage for course and teacher-related operations.

6. **Documentation**:
   - Update Swagger documentation to reflect new API endpoints and their request-response formats.

## Scalability, Security, and Maintainability Considerations
- The structure is designed to support potential scaling as the application might integrate more complex academic structures, such as departments or subjects.
- Implement proper authentication to restrict assignment and unassignment actions based on user permissions.
- Ensure proper input validations are in place to avoid orphaned entries and maintain database integrity.

## Logging & Monitoring
- Convert all key actions regarding course and teacher assignments into structured logs for better observability.

## Deployment Considerations
- Update the `Dockerfile` to ensure all necessary dependencies for the new feature are included.
- Document the new API endpoints in the README, detailing usage relating to course and teacher management.

## Conclusion
This implementation plan provides a comprehensive structure for integrating a relationship between the Course and Teacher entities within the Student Management Web Application, ensuring alignment with existing functionalities while promoting maintainability, scalability, and robust academic data management.

### Existing Code Files Modifications
#### Modifications Required in `models.py`
- Update the `Course` model to include `teacher_id` and define the relationship with the `Teacher` model, as shown above.

#### New Migration File to Alter `courses` Table
```python
# Migration script content as defined previously.
```
This migration adds the `teacher_id` column while maintaining existing data integrity.

#### New Service File: `course_service.py`
```python
def assign_teacher_to_course(course_id, teacher_id):
    # Logic to assign a teacher to a course
    pass

def unassign_teacher_from_course(course_id):
    # Logic to unassign a teacher from a course
    pass

def get_course_details(course_id):
    # Logic to fetch course details including assigned teacher
    pass

def list_courses_with_teachers():
    # Logic to get all courses with assigned teachers
    pass
```

#### Update `api.py`
```python
@app.route('/courses/<int:course_id>/assign-teacher/<int:teacher_id>', methods=['PUT'])
def assign_teacher():
    # Logic for assigning a teacher to a course based on the request parameters
    pass

@app.route('/courses/<int:course_id>/unassign-teacher', methods=['DELETE'])
def unassign_teacher():
    # Logic for unassigning a teacher from a course
    pass

@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course():
    # Logic for retrieving course details
    pass

@app.route('/courses', methods=['GET'])
def list_courses():
    # Logic for listing all courses with assigned teachers
    pass
```
This structure ensures complete integration of teacher management within the existing course management framework, maintaining elegance and functionality throughout the application.