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
## 1. Overview
This implementation plan outlines the architectural enhancements, technology stack, and implementation approach to establish a relationship between the Student and Course entities in the existing application. The feature will enable students to enroll in multiple courses, which will enhance educational management capabilities and academic tracking.

## 2. Architecture
The current layered architecture will be extended to include an `Enrollment` mapping table that links the Student and Course entities. This addition will preserve existing data integrity and provide new functionality through existing app components.

### 2.1 Components
- **API Layer**: New API endpoints will be created for enrollment management.
- **Service Layer**: Modifications will be made to handle the business logic for enrolling students in courses and retrieving a student's courses.
- **Data Access Layer (DAL)**: New methods will be added to interact with the new `Enrollment` mapping table.
- **Database**: A new join table, `Enrollment`, will be introduced while preserving existing `Student` and `Course` data.

### 2.2 Technologies
- **Programming Language**: Python 3.11+
- **Framework**: FastAPI for building the RESTful API
- **Database**: SQLite for persistence
- **ORM**: SQLAlchemy for database interaction
- **Data Validation**: Pydantic for request body validation and serialization
- **Testing**: pytest for unit and integration testing

## 3. Data Models
### 3.1 Enrollment Model Creation
A new `Enrollment` model will be defined to capture the relationship between the Student and Course entities. It will include `student_id` and `course_id` as foreign keys.

```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Enrollment(Base):
    __tablename__ = 'enrollments'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")
```

### 3.2 Updating Student Model
The existing Student model should have a relationship for enrollments.

```python
class Student(Base):
    # Existing fields...
    
    enrollments = relationship("Enrollment", back_populates="student")
```

### 3.3 Updating Course Model
The existing Course model should also have a relationship.

```python
class Course(Base):
    # Existing fields...
    
    enrollments = relationship("Enrollment", back_populates="course")
```

## 4. API Contracts
### 4.1 Endpoints for Enrollment Management
- **Enroll Student in Course**
  - **Method**: POST
  - **URL**: `/enrollments`
  - **Request Body**:
    ```json
    {
      "student_id": integer,
      "course_id": integer
    }
    ```
  - **Response**:
    - **201 Created**:
      ```json
      {
        "student": {
          "id": integer,
          "name": "string",
          "enrollments": [
            {
              "course_id": integer,
              "course_name": "string"
            }
          ]
        }
      }
      ```
    - **404 Not Found** (if student or course does not exist):
      ```json
      {
        "error": {
          "code": "E004",
          "message": "Either the student or course does not exist."
        }
      }
      ```

- **Retrieve Student’s Courses**
  - **Method**: GET
  - **URL**: `/students/{student_id}/courses`
  - **Response**:
    - **200 OK**:
      ```json
      {
        "student_id": integer,
        "courses": [
          {
            "course_id": integer,
            "name": "string"
          }
        ]
      }
      ```
    - **404 Not Found**:
      ```json
      {
        "error": {
          "code": "E005",
          "message": "Student not found."
        }
      }
      ```

## 5. Error Handling
Error handling strategies will include validation for student and course existence during enrollment.

### 5.1 Input Validation
- Validate that both `student_id` and `course_id` are integers and exist in the respective tables.
- Return `404 Not Found` if validation fails.

### 5.2 Exception Handling
- Provide user-friendly error messages when attempts to enroll a student with non-existent IDs occur.

## 6. Database Initialization
### 6.1 Migration Strategy
SQLAlchemy migrations will be used to automatically create the `enrollments` table while preserving existing data in Student and Course tables.

### 6.2 Initialization Code for Migration
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def initialize_database():
    engine = create_engine('sqlite:///app.db')
    Base.metadata.create_all(engine)  # Create all tables including Enrollment

    # Ensure that all existing Student and Course data remain unaffected.
```

## 7. Testing Strategy
### 7.1 Test Coverage
- **Unit Tests**: Include tests for both enrollment creation and retrieval scenarios.
- **Integration Tests**: Verify that AI endpoints for enrolling students and fetching courses work correctly.
- **Contract Tests**: Validate that API responses align with specifications.

### 7.2 Organization
Tests should cover the following scenarios:
- `test_enroll_student_succeeds_when_valid_ids_provided`
- `test_enroll_student_fails_when_student_or_course_invalid`
- `test_retrieve_courses_for_student_returns_correct_data`

## 8. Deployment Considerations
Continue to develop and test the application locally for initial rollout. Future deployment strategies will include ensuring backward compatibility with existing data.

## 9. Scalability Considerations
The current SQLite implementation serves for development but can be transitioned to a more robust solution like PostgreSQL as data volume increases.

## 10. Security Considerations
Ensure best security practices are followed by validating and sanitizing input data to prevent vulnerabilities.

## 11. Documentation
Update the `README.md` to include:
- Instructions for using the new enrollment endpoints.
- Changes to existing API documentation reflecting the new resource interaction.

## 12. Conclusion
This implementation plan provides a structured approach to establish a relationship between Students and Courses within the application. By following the outlined steps and leveraging existing components, compatibility with the current architecture is maintained while enhancing the application's functionality.

## Existing Code Files Modifications Needed
### Modifications
- **File**: `src/models/enrollment.py`
  - Create a new `Enrollment` model as defined above.

- **File**: `src/models/student.py`
  - Update the Student model to include a relationship to the Enrollment model.

- **File**: `src/models/course.py`
  - Update the Course model to include a relationship to the Enrollment model.

- **File**: `src/api/enrollment.py`
  - Implement new API endpoints to handle student enrollment in courses and retrieval of student courses.

- **File**: `tests/api/test_enrollment.py`
  - Create tests to validate new enrollment functionality and error handling.

This implementation plan defines a roadmap to integrate course relationships for students effectively, supporting both immediate needs and future expansion opportunities.