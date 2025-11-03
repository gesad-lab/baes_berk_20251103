# Implementation Plan: Add Teacher Relationship to Course Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

### Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---

## Version: 1.0.1
**Purpose**: Introduce a relationship between the `Course` and `Teacher` entities in the educational management system, enabling better tracking and management of course assignments to teachers.

---

## I. Architecture Overview

### 1.1 Application Architecture
- **Type**: RESTful API
- **Framework**: Flask (Python)
- **Database**: SQLite
- **Structure**: MVVM (Model-View-ViewModel) pattern:
  - **Models**: Represent the data structure (Student, Course, Teacher).
  - **Views**: Define API endpoints.
  - **ViewModels**: Manage data flow and business logic.

### 1.2 Module Components
1. **Models**: Update the existing `Course` model to include a foreign key relationship to the `Teacher` model.
2. **Routes**: Define new routes for assigning teachers to courses and retrieving courses associated with teachers.
3. **Controllers**: Implement business logic for handling teacher-course assignments.
4. **Database Management**: Execute migration scripts to add the `teacher_id` field in the `Courses` table.

---

## II. Technology Stack

- **Programming Language**: Python 3.11+
- **Web Framework**: Flask
- **ORM**: SQLAlchemy
- **Database**: SQLite
- **Testing Framework**: pytest
- **Environment Management**: pipenv

### Trade-offs
- SQLite allows for easy development and testing, providing sufficient performance for the current scope while maintaining schema integrity.

---

## III. Data Models

### 3.1 Course Model - Updated
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # New field

    teacher = relationship("Teacher", back_populates="courses")
```

### 3.2 Teacher Model Update for Relationship
```python
class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    courses = relationship("Course", back_populates="teacher")  # Bidirectional relationship
```

### 3.3 Migrations
- Use **Alembic** to create migration scripts to add the `teacher_id` column to the `Courses` table.
- Example migration script to modify the existing `Courses` table:
```bash
# Command to create migration
alembic revision --autogenerate -m "Add teacher_id to Courses table"
# Command to apply migration
alembic upgrade head
```

---

## IV. API Endpoints

### 4.1 API Endpoints Overview

1. **Assign a Teacher to a Course**: `PATCH /courses/{course_id}/assign-teacher`
   - **Request**:
     ```json
     {
       "teacher_id": 1
     }
     ```
   - **Response**: 
     ```json
     {
       "message": "Teacher assigned to course successfully."
     }
     ```

2. **Retrieve Courses for a Teacher**: `GET /teachers/{teacher_id}/courses`
   - **Response**:
     ```json
     {
       "courses": [
         {
           "id": 1,
           "name": "Math 101",
           "level": "Beginner"
         },
         ...
       ]
     }
     ```

### 4.2 Error Responses
- **Error Response Example**:
  - For non-existing teacher ID during assignment:
  ```json
  {
    "error": {
      "code": "E001",
      "message": "Teacher with the specified ID does not exist."
    }
  }
  ```

---

## V. Implementation Approach

### 5.1 Flask Application Setup
- Update the `app.py` file to include new routes for assigning teachers and retrieving courses.
- Implement controllers to handle business logic.

### 5.2 Error Handling & Validation
- Validate `teacher_id` during assignment to ensure it corresponds to an existing teacher in the database, returning appropriate error responses if invalid.

### 5.3 Testing Strategy
- Write unit and integration tests for:
  - Successful teacher-course assignment.
  - Error conditions for invalid `teacher_id`.

```python
def test_assign_teacher_to_course(client):
    # Assuming a course with ID 1 exists and teacher with ID 1 exists
    response = client.patch('/courses/1/assign-teacher', json={'teacher_id': 1})
    assert response.status_code == 200
    assert response.json['message'] == "Teacher assigned to course successfully."

def test_assign_teacher_to_non_existing_course(client):
    response = client.patch('/courses/999/assign-teacher', json={'teacher_id': 1})
    assert response.status_code == 404

def test_assign_non_existing_teacher_to_course(client):
    response = client.patch('/courses/1/assign-teacher', json={'teacher_id': 999})
    assert response.json['error']['code'] == 'E001'
```

---

## VI. Database Management

### 6.1 Schema Update
- The migration should add the `teacher_id` column to the `Courses` table using SQLAlchemy's migration scripts while maintaining existing data.

### 6.2 Migrations
- Create migration scripts with Alembic and ensure successful schema migrations without data loss.

```bash
# Command to initialize migrations if not done previously
alembic init migrations
# Command to generate a migration
alembic revision --autogenerate -m "Add teacher relationship to Courses"
# Command to apply migrations
alembic upgrade head
```

---

## VII. Configuration Management

### 7.1 Environment Variables
- Update configurations if needed and make sure to document changes in the `.env` file, with a `.env.example` included for developer reference.

---

## VIII. Logging & Monitoring

### 8.1 Logging Implementation
- Incorporate structured logging for API requests that affect teachers and courses.

---

## IX. Deployment Considerations

- **Development Environment**: Leverage Flask's development server; continue using pytest for testing.
- **Production Readiness**: Introduce containerization strategies (e.g., Docker) to streamline production deployments. Validate migrations and stability through rigorous testing.

---

## X. Success Criteria Validation

- Each functionality will be validated through unit tests:
  - Successful teacher assignment to a course.
  - Appropriate error messages when invalid `teacher_id` is provided.
  - Successful database schema migration that maintains data integrity.

---

## XI. User Documentation

- Update the `README.md`:
  - Instructions for setup and running the application.
  - Descriptions of newly implemented API endpoints, outlining request and response formats.
  - Notes on testing strategies and highlighting available endpoints.

---

## XII. Future Enhancements

- Subsequent sprints may consider implementing features such as role-based permissions or more granular course management functionalities.

### Conclusion
This implementation plan outlines a comprehensive approach to establishing a relationship between Teachers and Courses in the educational management system while ensuring integration with existing entities, thorough input validation, and comprehensive testing to maintain the overall quality and reliability of the system.

---

### Existing Code Files / Modifications:
**File**: `src/models/__init__.py`
```python
# Existing import statements
from .student import Student
from .course import Course  # Updated Course import with new relationship
from .teacher import Teacher  # Ensure Teacher model is imported if it exists
```

**Modifications to Existing Files**:
- Update the `Course` class in `src/models/course.py` to include the new `teacher_id` field as described above.
- Adjust the corresponding controller for handling course assignments in `src/controllers/course_controller.py`, ensuring to implement and validate the new teacher assignment logic.

This plan aligns with the project's coding standards and principles, promoting maintainability and future scalability while ensuring that existing operations are not hindered by new changes.