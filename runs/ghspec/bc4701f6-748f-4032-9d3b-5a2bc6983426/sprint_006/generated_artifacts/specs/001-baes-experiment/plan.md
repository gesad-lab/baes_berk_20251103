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

## 1. Overview
This implementation plan outlines the architectural changes, technology stack, and implementation approach to establish a relationship between the Course and Teacher entities in the existing application. This feature will enhance the educational management capabilities by allowing the assignment of a teacher to a course.

## 2. Architecture
The existing layered architecture will be expanded to incorporate the teacher relationship in the Course entity while maintaining integrity with the existing Student and Course entities.

### 2.1 Components
- **API Layer**: New API endpoints will be created for assigning and retrieving teacher information associated with courses.
- **Service Layer**: Business logic will be implemented to handle the assignment of teachers to courses.
- **Data Access Layer (DAL)**: Adjusted methods for updating Course records to include teacher assignments.
- **Database**: The existing `courses` table will be updated to include a foreign key referencing the `teachers` table.

### 2.2 Technologies
- **Programming Language**: Python 3.11+
- **Framework**: FastAPI for building the RESTful API
- **Database**: SQLite for persistence
- **ORM**: SQLAlchemy for database interaction
- **Data Validation**: Pydantic for request body validation and serialization
- **Testing**: pytest for automated testing

## 3. Data Models
### 3.1 Course Model Modification
Update the `Course` model to include a foreign key that references the `Teacher` entity:

```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)
    teacher = relationship("Teacher", back_populates="courses")

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    courses = relationship("Course", back_populates="teacher")
```

## 4. API Contracts
### 4.1 Endpoints for Course Management
#### Assign Teacher to Course
- **Method**: PATCH
- **URL**: `/courses/{course_id}`
- **Request Body**:
  ```json
  {
    "teacher_id": "integer"
  }
  ```
- **Response**:
  - **200 OK**:
    ```json
    {
      "id": integer,
      "name": "string",
      "teacher_id": "integer"
    }
    ```
  - **404 Not Found**:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Course or Teacher not found."
      }
    }
    ```

#### Retrieve Course Details Including Teacher Information
- **Method**: GET
- **URL**: `/courses/{course_id}`
- **Response**:
  - **200 OK**:
    ```json
    {
      "id": integer,
      "name": "string",
      "teacher": {
        "name": "string",
        "email": "string"
      }
    }
    ```
  - **404 Not Found**:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Course not found."
      }
    }
    ```

## 5. Error Handling
Error handling strategies will validate the presence of required fields in PATCH requests and validate relationships.

### 5.1 Input Validation
- Ensure the `teacher_id` field is present in the request payload.
- Return `400 Bad Request` if the field is missing.

### 5.2 Exception Handling
- Handle cases where fetching a course by ID or updating with a non-existent teacher results in a `404 Not Found`.

## 6. Database Initialization
### 6.1 Migration Strategy
Utilize SQLAlchemy migrations to add the `teacher_id` column to the `courses` table and set up the foreign key relationship with the `teachers` table without affecting existing data.

### 6.2 Initialization Code for Migration
```python
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker

def initialize_database():
    engine = create_engine('sqlite:///app.db')
    metadata = MetaData()

    # Add new column to existing table for teacher relationships
    courses_table = Table('courses', metadata,
                          Column('id', Integer, primary_key=True),
                          Column('teacher_id', Integer, ForeignKey('teachers.id'), nullable=True)
                          )
    metadata.create_all(engine)  # Create or update tables including new column
```

## 7. Testing Strategy
### 7.1 Test Coverage
- **Unit Tests**: Verify the course update and retrieval processes with the teacher relationship.
- **Integration Tests**: Ensure the API endpoints function correctly for assigning a teacher and fetching course details.
- **Contract Tests**: Validate API responses match specified contracts.

### 7.2 Organization
Tests should cover the following scenarios:
- `test_assign_teacher_to_course_succeeds_with_valid_data`
- `test_assign_teacher_to_course_fails_with_nonexistent_teacher`
- `test_get_course_details_includes_teacher_info`
- `test_get_course_fails_with_nonexistent_course`

## 8. Deployment Considerations
Continue local development and testing to facilitate seamless integration. Ensure all migrations occur without downtime or data loss.

## 9. Scalability Considerations
SQLite is sufficient for current needs; future scalability to a more robust database (e.g., PostgreSQL) should be planned as user demand grows.

## 10. Security Considerations
Implement input validation to prevent SQL injection and ensure data integrity when assigning teachers to courses.

## 11. Documentation
Update `README.md` to include:
- Instructions for using the new API endpoints for course management and teacher assignments.
- Documentation reflecting all changes in API specifications and expected behavior.

## 12. Conclusion
This implementation plan outlines a structured approach to integrate the teacher relationship within the course entity effectively, preserving existing functionality while enhancing the educational management capabilities of the application.

## Existing Code Files Modifications Needed
### Modifications
- **File**: `src/models/course.py`
  - Update the existing Course model to include a `teacher_id` foreign key and modify relationships accordingly.

- **File**: `src/api/course.py`
  - Implement new API endpoints for assigning a teacher to a course and retrieving course details including the teacher's information.

- **File**: `tests/api/test_course.py`
  - Create tests to validate the new functionality for course-teacher relationships, including error handling.

This implementation plan provides concrete steps to add teacher management capabilities to the existing application while ensuring data integrity and consistent functionality for existing features.