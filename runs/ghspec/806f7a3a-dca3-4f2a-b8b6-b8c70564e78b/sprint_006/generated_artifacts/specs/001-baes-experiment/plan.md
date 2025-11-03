# Implementation Plan: Add Teacher Relationship to Course Entity

## INCREMENTAL DEVELOPMENT CONTEXT

**Previous Sprint Plan:**  
# Implementation Plan: Create Teacher Entity

## INCREMENTAL DEVELOPMENT CONTEXT

**Previous Sprint Plan:**  
# Implementation Plan: Add Course Relationship to Student Entity

## INCREMENTAL DEVELOPMENT CONTEXT

**Previous Sprint Plan:**  
# Implementation Plan: Create Course Entity

## INCREMENTAL DEVELOPMENT CONTEXT

**Previous Sprint Plan:**  
# Implementation Plan: Add Email Field to Student Entity

## INCREMENTAL DEVELOPMENT CONTEXT

**Previous Sprint Plan:**  
# Implementation Plan: Student Entity Management Web Application

## Version: 1.0.0  
## Purpose: To establish a relationship between Course and Teacher entities in the educational management system for improved instructional management.

---

## I. Architecture Overview

### 1.1 Technical Stack
- **Backend**: Flask (Python)
- **Database**: SQLite
- **API Framework**: Flask-RESTful for creating RESTful APIs
- **ORM**: SQLAlchemy for database interactions
- **Testing Framework**: pytest for unit and integration testing

### 1.2 Overall Architecture
The architecture will build upon the existing MVC structure with the following adjustments:
- **Model**: Update the `Course` model to include `teacher_id` which will establish a foreign key relationship with the `Teacher` model.
- **View**: Implement new API responses for course management that include teacher data.
- **Controller**: Modify existing routes to manage the teacher assignments within courses.

---

## II. Module Design

### 2.1 Module Structure
```
/educational_management_app
|-- /src
|   |-- /models         
|   |   |-- student.py          # Existing Student model
|   |   |-- course.py           # Existing Course model (modified to add Teacher_ID)
|   |   |-- teacher.py          # Existing Teacher model 
|   |-- /routes           
|   |   |-- student_routes.py    # Existing routes for Student
|   |   |-- course_routes.py     # Modified routes for Course
|   |   |-- teacher_routes.py     # Existing routes for Teacher
|   |-- /schemas             
|   |   |-- course_schema.py     # New schema for Course validation (modified)
|   |-- /services             
|   |   |-- course_service.py    # New service for handling Course teacher assignments
|   |-- /config             
|-- /tests                  
|   |-- test_course.py          # Tests for Course functionalities 
|-- /docs                   
|-- requirements.txt        
|-- app.py                  
```

### 2.2 Module Responsibilities

- **Models (`models/course.py`)**:
  - Update the `Course` model to include a `teacher_id` column, establishing a foreign key relationship with the `Teacher` model.

- **Routes (`routes/course_routes.py`)**:
  - Modify existing API endpoints to support teacher assignments to courses.

- **Schemas (`schemas/course_schema.py`)**:
  - Update input validation schema for course to include teacher ID.

- **Services (`services/course_service.py`)**:
  - Implement business logic to manage teacher assignments to courses.

- **Tests (`tests/test_course.py`)**:
  - Add tests covering the functionality of assigning and removing teachers from courses.

---

## III. Data Models

### 3.1 Course Model
#### Schema Definition
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app import db

class Course(db.Model):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

    teacher = relationship("Teacher", back_populates="courses")

    def __repr__(self):
        return f"<Course(id={self.id}, title='{self.title}', teacher_id={self.teacher_id})>"
```

### 3.2 Teacher Model Update
- Update the Teacher model to establish the reverse relationship with Courses:
```python
class Teacher(db.Model):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    courses = relationship("Course", back_populates="teacher")
```

---

## IV. API Contracts

### 4.1 Endpoints
1. **Assign a Teacher to a Course**
   - **Endpoint**: `PATCH /api/v1/courses/<course_id>/assign_teacher`
   - **Request Body**: 
     ```json
     {
       "teacher_id": 1
     }
     ```
   - **Responses**:
     - `200 OK` on successful assignment.
     - `400 Bad Request` for invalid teacher ID.
     - `404 Not Found` if the Course ID does not exist.

2. **Get Course Details**
   - **Endpoint**: `GET /api/v1/courses/<course_id>`
   - **Responses**:
     - `200 OK` with course details and associated teacher.
     - `404 Not Found` if the Course ID does not exist.

3. **Remove Teacher from Course**
   - **Endpoint**: `DELETE /api/v1/courses/<course_id>/remove_teacher`
   - **Responses**:
     - `200 OK` confirming teacher disassociation.
     - `404 Not Found` if the Course ID does not exist.

---

## V. Implementation Timeline

### 5.1 Milestones
1. **Week 1**: 
   - Update `Course` model and implement migration scripts using Flask-Migrate to add the `teacher_id` column.

2. **Week 2**: 
   - Modify API endpoints in course management to handle teacher assignment logic.
   - Implement validation and business logic around teacher assignments.

3. **Week 3**: 
   - Write unit and integration tests for course management, with special attention to the new teacher associations.

4. **Week 4**: 
   - Validate all endpoints and ensure integration with the teacher's entity.
   - Update project documentation to reflect new API functionalities.

---

## VI. Testing Plan

### 6.1 Testing Strategy
- **Unit Testing**: 
  - Validate individual functions handling the logic of assigning/removing teachers.
  
- **Integration Testing**: 
  - Validate end-to-end workflows for assigning/removing teachers to/from courses and retrieving course details.

Testing Coverage Target: Minimum of 70% overall coverage with 90% on critical paths (teacher assignment and course details retrieval).

### 6.2 Sample Tests
- `test_assign_teacher_to_course_succeeds_with_valid_data`
- `test_get_course_with_teacher_details_succeeds`
- `test_remove_teacher_from_course_succeeds`

---

## VII. Database Migration Strategy

### 7.1 Migration
- Use Flask-Migrate to create and apply migration for adding `teacher_id` to the courses table.
```bash
flask db migrate -m "Added teacher_id column to Course table"
flask db upgrade
```

---

## VIII. Documentation
- Update the main project `README.md` file to include instructions for the new functionality concerning course-teacher relationships.
- Document new API endpoints and functional requirements clearly in `/docs/api.md`.

### 8.1 API Documentation Example
```markdown
## Course API

### Assign a Teacher to a Course
- **PATCH** `/api/v1/courses/<course_id>/assign_teacher`
- **Body**:
    ```json
    {
      "teacher_id": 1
    }
    ```
- **Responses**:
    - **200 OK**: Teacher assigned successfully.
    - **404 Not Found**: Course ID does not exist.

### Get Course Details
- **GET** `/api/v1/courses/<course_id>`
- **Responses**:
    - **200 OK**: Returns course data with teacher.
    - **404 Not Found**: Course ID does not exist.

### Remove Teacher from Course
- **DELETE** `/api/v1/courses/<course_id>/remove_teacher`
- **Responses**:
    - **200 OK**: Teacher removed successfully.
    - **404 Not Found**: Course ID does not exist.
```

---

## IX. Security Measures
- Implement input validation checks to ensure that the teacher ID provided exists within the Teacher entity.
- Properly handle error responses while avoiding exposure of sensitive internal application data.

---

## Trade-Offs and Decisions
- **Backward Compatibility**: The updated `Course` model and the introduction of the teacher relationship will not alter existing functionality or data integrity.
- **Technology Choices**: The same tech stack as previous sprints was maintained to ensure consistent development practices and integration ease.

--- 

This implementation plan provides a comprehensive approach to integrating a teacher relationship within the course entity, fulfilling the specified user scenarios and functional requirements.