# Implementation Plan: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Entity Management Web Application

## Version: 1.0.0  
## Purpose: To establish a relationship between students and courses in an educational management system, facilitating better enrollment tracking and enhanced user experience for administrators, educators, and students.

---

## I. Architecture Overview

### 1.1 Technical Stack
- **Backend**: Flask (Python)
- **Database**: SQLite
- **API Framework**: Flask-RESTful for creating RESTful APIs
- **ORM**: SQLAlchemy for database interactions
- **Testing Framework**: pytest for unit and integration testing

### 1.2 Overall Architecture
The application will extend the existing MVC (Model-View-Controller) architecture:
- **Model**: Introduce a new mapping table `StudentCourses` to facilitate many-to-many relationships between existing Student entities and Course entities.
- **View**: Implement API responses that manage student-course associations.
- **Controller**: Integrate Flask routes for adding and removing students from courses and retrieving a student's courses.

---

## II. Module Design

### 2.1 Module Structure
```
/educational_management_app
|-- /src
|   |-- /models         
|   |   |-- student.py          # Existing Student model 
|   |   |-- course.py           # Existing Course model 
|   |   |-- student_courses.py   # New mapping model for Student-Course relationships
|   |-- /routes           
|   |   |-- student_routes.py    # Existing routes for Student
|   |   |-- course_routes.py     # Existing routes for Course
|   |   |-- enrollment_routes.py  # New routes for Student-Course enrollment
|   |-- /schemas             
|   |   |-- enrollment_schema.py  # New schema for enrollment validation
|   |-- /services             
|   |   |-- enrollment_service.py  # Business logic for handling enrollments
|   |-- /config             
|-- /tests                  
|   |-- test_enrollment.py   # Tests for Student-Course relationship functionalities
|-- /docs                   
|-- requirements.txt        
|-- app.py                  
```

### 2.2 Module Responsibilities

- **Models (`models/student_courses.py`)**:
  - Define the `StudentCourses` mapping table including foreign keys to Student and Course entities.

- **Routes (`routes/enrollment_routes.py`)**:
  - Implement API endpoints for enrolling/un-enrolling students in courses and retrieving courses for a student.

- **Schemas (`schemas/enrollment_schema.py`)**:
  - Perform validation of student and course IDs during enrollment requests.

- **Services (`services/enrollment_service.py`)**:
  - Implement business logic related to adding/removing enrollments and retrieving student courses.

- **Tests (`tests/test_enrollment.py`)**:
  - Create tests to validate functionality for enrollment-related endpoints.

---

## III. Data Models

### 3.1 StudentCourses Model
#### Schema Definition
```python
from sqlalchemy import Column, Integer, ForeignKey
from app import db

class StudentCourses(db.Model):
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    def __repr__(self):
        return f"<StudentCourse(student_id={self.student_id}, course_id={self.course_id})>"
```

---

## IV. API Contracts

### 4.1 Endpoints
1. **Enroll a Student in a Course**
   - **Endpoint**: `POST /api/v1/enrollments`
   - **Request Body**: 
     ```json
     {
       "student_id": 1,
       "course_id": 2
     }
     ```
   - **Responses**:
     - `201 Created` on successful enrollment.
     - `400 Bad Request` for validation errors (e.g., missing parameters).
     - `409 Conflict` if the enrollment already exists.

2. **Get Courses for a Student**
   - **Endpoint**: `GET /api/v1/students/<student_id>/courses`
   - **Responses**:
     - `200 OK` with a list of courses in JSON format.
     - `404 Not Found` if the student or course associations do not exist.

3. **Unenroll a Student from a Course**
   - **Endpoint**: `DELETE /api/v1/enrollments`
   - **Request Body**: 
     ```json
     {
       "student_id": 1,
       "course_id": 2
     }
     ```
   - **Responses**:
     - `200 OK` if the unenrollment was successful.
     - `404 Not Found` if the student-course association does not exist.

---

## V. Implementation Timeline

### 5.1 Milestones
1. **Week 1**: 
   - Define the `StudentCourses` model schema and add migration scripts using Flask-Migrate to create the new table.

2. **Week 2**: 
   - Implement APIs for enrolling and unenrolling students in courses.
   - Implement retrieval of courses for a specific student.
   - Set up input validation for the enrollment schema.

3. **Week 3**: 
   - Write tests covering all new API functionality, ensuring edge cases are included.
   - Validate that error handling is implemented correctly for all scenarios.

4. **Week 4**: 
   - Perform integration testing to confirm API endpoints and database interactions work.
   - Update relevant documentation to clarify the new API features and their usage.

---

## VI. Testing Plan

### 6.1 Testing Strategy
- **Unit Testing**: 
  - Validate individual functions in services handling enrollment logic.
  
- **Integration Testing**: 
  - Validate end-to-end workflow for enrolling, unenrolling, and retrieving courses.

Testing Coverage Target: Minimum of 70% overall coverage and 90% coverage on critical paths (enrollment and unenrollment functionality).

### 6.2 Sample Tests
- `test_enroll_student_in_course_creates_association`
- `test_get_courses_for_student_returns_correct_list`
- `test_unenroll_student_removes_association_successfully`

---

## VII. Database Migration Strategy

### 7.1 Migration
- Utilize Flask-Migrate's functionality to create and apply migration scripts for adding the `student_courses` mapping table to the database and ensuring existing data remains intact.

```bash
flask db migrate -m "Added StudentCourses mapping table"
flask db upgrade
```

---

## VIII. Documentation
- Update the main project `README.md` file to include instructions for the enrollment-related API.
- Document new API endpoints and their functional requirements in `/docs/api.md`.

### 8.1 API Documentation Example
```markdown
## Enrollment API

### Enroll a Student in a Course
- **POST** `/api/v1/enrollments`
- **Body**:
    ```json
    {
      "student_id": 1,
      "course_id": 2
    }
    ```
- **Responses**:
    - **201 Created**: Enrollment successful.
    - **400 Bad Request**: Invalid input data.
    - **409 Conflict**: Student already enrolled in this course.

### Get Courses for a Student
- **GET** `/api/v1/students/<student_id>/courses`
- **Responses**:
    - **200 OK**: Returns course data for student.
    - **404 Not Found**: Student ID does not exist.

### Unenroll a Student from a Course
- **DELETE** `/api/v1/enrollments`
- **Body**:
    ```json
    {
      "student_id": 1,
      "course_id": 2
    }
    ```
- **Responses**:
    - **200 OK**: Unenrollment successful.
    - **404 Not Found**: Association does not exist.
```

---

## IX. Security Measures
- Implement validation checks to ensure both student and course IDs provided in the requests exist to prevent broken relationships.
- Error messages should not expose any internal structures or data.

---

## Trade-Offs and Decisions
- **Backward Compatibility**: By introducing a mapping table, the existing Student and Course models remain unchanged, preserving data integrity.
- **SQLite**: Continued use of SQLite allows for lightweight implementation without the need for a full-scale database server during development.

---

The provided implementation plan outlines the effective integration of a course relationship into the student entities, allowing for enhanced management and tracking capabilities within the educational management system.