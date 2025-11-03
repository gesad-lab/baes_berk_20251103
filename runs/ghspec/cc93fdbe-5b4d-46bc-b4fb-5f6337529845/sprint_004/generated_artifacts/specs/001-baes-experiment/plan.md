# Implementation Plan: Add Course Relationship to Student Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

### Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

### Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

### Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## Version
**Version**: 1.1.0

## 1. Architecture Overview
This implementation enhances the existing application architecture by establishing a many-to-many relationship between `Student` and `Course` entities. We will extend the current use of FastAPI for creating the necessary API endpoints, SQLite as our database, and SQLAlchemy as the ORM for database interactions.

### Architecture Components
- **FastAPI**: Continue for RESTful API development.
- **SQLite**: Remain as the database for lightweight management.
- **SQLAlchemy**: Leverage for managing the new relationship through an additional `student_courses` relationship table.

## 2. Technology Stack
- **Programming Language**: Python 3.11+
- **Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing Framework**: pytest
- **API Testing Tool**: Postman (for manual testing)

## 3. Module Boundaries & Responsibilities
### 3.1 Services
- **StudentService**: Extend existing service to include logic for associating courses with students, specifically add and retrieve courses.
  
### 3.2 Data Models
- **StudentCourses**: New data model representing the relationship between students and courses.
  
### 3.3 API Endpoints
- **POST** `/students/{student_id}/courses`: New endpoint to assign a course to a student.
- **GET** `/students/{student_id}/courses`: New endpoint to retrieve a student's courses.

## 4. Data Models
```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StudentCourses(Base):
    __tablename__ = 'student_courses'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
```

## 5. API Contracts
### 5.1 Endpoints Specification
#### 5.1.1 Assign a Course to a Student
- **Endpoint**: `POST /students/{student_id}/courses`
- **Request Body**:
    ```json
    {
        "course_id": 1
    }
    ```
- **Response** (201 Created):
    ```json
    {
        "message": "Course assigned to student successfully.",
        "student_id": 1,
        "course_id": 1
    }
    ```
- **Error Response** (404 Not Found):
    ```json
    {
        "error": {
            "code": "E003",
            "message": "Invalid course ID."
        }
    }
    ```

#### 5.1.2 Retrieve Courses for a Student
- **Endpoint**: `GET /students/{student_id}/courses`
- **Response (200 OK)**:
    ```json
    [
        {
            "id": 1,
            "name": "Mathematics",
            "level": "Beginner"
        },
        {
            "id": 2,
            "name": "Science",
            "level": "Intermediate"
        }
    ]
    ```
- **Error Response** (404 Not Found):
    ```json
    {
        "error": {
            "code": "E004",
            "message": "Student not found."
        }
    }
    ```

## 6. Database Migration Strategy
### 6.1 Migration Strategy
- The existing `students` and `courses` tables will remain untouched. A new relationship table `student_courses` will be created to implement the many-to-many mapping. Alembic will be used to manage this migration.

```bash
# Create migration file using Alembic 
alembic revision --autogenerate -m "Create student_courses table"
```

### 6.2 Migration Script Example
```python
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'xxxxxxx'
down_revision = 'yyyyyyy'  # Adjust this to match the last migration
branch_labels = None
depends_on = None

def upgrade():
    # Create student_courses table for many-to-many relationship
    op.create_table(
        'student_courses',
        sa.Column('student_id', sa.Integer(), sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer(), sa.ForeignKey('courses.id'), primary_key=True)
    )

def downgrade():
    # Drop student_courses table
    op.drop_table('student_courses')
```

## 7. Testing Approach
### 7.1 Test Cases
1. **Assign Course to Student**: Validate that assigning a valid course ID to a student successfully updates the `student_courses` table.
2. **Retrieve Student Courses**: Validate that the courses returned correspond to the ones associated with the student.
3. **Handling Invalid Course ID**: Ensure that an appropriate error response is returned for invalid course IDs.
4. **Database Schema Verification**: Ensure that `student_courses` is created successfully at application startup.

### 7.2 Testing Framework
- Use `pytest` for unit testing and integration testing of new endpoints.
- Organize tests alongside the existing application structure to maintain clarity.

## 8. Security Considerations
- Input validation must be performed on `course_id` to prevent SQL injection and other vulnerabilities.
- Implement structured responses to prevent leaking sensitive information on error responses.

## 9. Error Handling
- Employ consistent structured error responses throughout the API for course-related requests.
- Ensure validation checks for the existence and integrity of both `student_id` and `course_id` are in place while assigning courses to students.

## 10. Documentation
- Update the API documentation to include new routes and expected responses.
- Document the database schema updates in the `README.md` for clarity on how the new relationships work.

## 11. Deployment Considerations
- Extensively test the new functionality in a staging environment, ensuring no existing functionality is compromised.
- Confirm that all API responses conform to the expected JSON format and standards.

## 12. Version Control Practices
- Maintain clear commit messages relating to the changes made for the new relationship additions.
- Enforce the use of a well-structured `.gitignore` to avoid unnecessary files being added to the version control.

## 13. Implementation Timeline
- **Week 1**: Define and implement the `StudentCourses` model and create the necessary API endpoints.
- **Week 2**: Develop, test, and finalize migration scripts for creating the relationship table.
- **Week 3**: Conduct thorough testing, documentation finalization, and preparation for deployment.

---

**Trade-offs and Decisions**:
- Continued use of SQLite for simplicity and ease of deployment is beneficial for this project phase.
- FastAPI's robust capabilities will enable the rapid development and documentation of APIs, giving full RESTful access to student-course relationships.
- Designing the new table ensures backward compatibility with existing student and course models to safeguard data integrity throughout development and deployment.

This implementation plan establishes a clear path to integrating course relationships into the current application framework, with careful attention to maintaining existing functionality and securing data integrity.