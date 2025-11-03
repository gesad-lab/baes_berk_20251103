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
# Implementation Plan: Student Entity Management Web Application

## I. Architecture Overview
The Educational Management System will be enhanced to establish a relationship between the Course and Teacher entities, allowing each course to associate with a specified teacher. This integration will improve course organization and facilitate better tracking and management of educational administration processes. Updates will be necessary across the API layer, service layer, data access layer, and the database schema, assuring existing functionalities and data integrity are preserved.

### 1.1 Architecture Components
- **API Layer**: A new endpoint will be created to facilitate the relationship assignment between Courses and Teachers.
- **Service Layer**: A `CourseService` will manage the business logic for assigning teachers to courses.
- **Data Access Layer (DAL)**: A `CourseRepository` will manage database interactions concerning Course entities, updating to include the teacher relationship.

### 1.2 Technology Stack
- **Programming Language**: Python
- **Web Framework**: Flask
- **Database**: SQLite (for local development; migration to PostgreSQL anticipated)
- **ORM**: SQLAlchemy
- **Testing Framework**: PyTest
- **Environment Management**: Virtualenv
- **API Testing Tool**: Postman

## II. Module Breakdown

### 2.1 API Layer
#### Endpoints
1. **Assign Teacher to Course**
   - Method: `PATCH`
   - Path: `/courses/{course_id}/assign-teacher`
   - Request Body:
     ```json
     {
       "teacher_id": "integer" (required)
     }
     ```
   - Success Response (200 OK):
     ```json
     {
       "message": "Teacher assigned to course successfully.",
       "course": {
         "id": "integer",
         "teacher_id": "integer"
       }
     }
     ```
   - Error Responses:
     - (404 Not Found):
     ```json
     {
       "error": {
         "code": "E002",
         "message": "Teacher not found."
       }
     }
     ```

### 2.2 Service Layer
- **CourseService**:
  - This service will handle the business logic for assigning a teacher to a course, including validation of teacher existence.

### 2.3 Data Access Layer
- **CourseRepository**:
  - Manages all CRUD operations related to Course entities, including the new relationship with Teacher entities.

## III. Data Model and Schema

### 3.1 Database Schema
The existing Course table will be modified to include a new foreign key column referencing the Teacher entity:
- **teacher_id**: Foreign key (integer, optional, references Teachers)

### 3.2 Data Model Definition
The updated Course model will be defined as follows:
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
    
    # Establish relationship
    teacher = relationship("Teacher", back_populates="courses")

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    
    # Establish reverse relationship
    courses = relationship("Course", back_populates="teacher")
```

## IV. Implementation Steps

1. **Setup Environment**
   - Ensure existing environment is operational and all dependencies are up to date:
     ```bash
     pip install Flask SQLAlchemy Flask-Migrate
     ```

2. **Database Migration**
   - Create a migration script to add the `teacher_id` foreign key column to the `courses` table:
     ```python
     """Add teacher_id column to courses table"""
     from alembic import op
     import sqlalchemy as sa

     revision = 'xxxxxx'  # Update as necessary
     down_revision = 'previous_revision'

     def upgrade():
         op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
         op.create_foreign_key('fk_teacher', 'courses', 'teachers', ['teacher_id'], ['id'])

     def downgrade():
         op.drop_constraint('fk_teacher', 'courses', type_='foreignkey')
         op.drop_column('courses', 'teacher_id')
     ```

3. **Create Application Structure**
   ```
   educational_management/
   ├── src/
   │   ├── app.py
   │   ├── models.py    # Include updated Course and Teacher models
   │   ├── services.py   # Implement CourseService
   │   ├── repositories.py # Include CourseRepository
   │   └── database.py
   ├── tests/
   │   ├── test_course_teacher.py # New test file for course-teacher functionalities
   ├── requirements.txt
   ├── .env.example
   └── README.md
   ```

4. **Develop API Endpoints**
   - Extend `app.py` to configure Flask and establish the `/courses/{course_id}/assign-teacher` endpoint.
   - Implement methods in `CourseService` to handle teacher assignment and validation logic.
   - Update `CourseRepository` methods to accommodate the teacher assignment functionality.

5. **Error Handling**
   - Integrate error-handling logic to manage scenarios where a teacher does not exist when assigning them to a course.
   - Return appropriate 404 Not Found responses for invalid teacher references.

6. **Testing**
   - Create `tests/test_course_teacher.py` to encompass:
     - Successful assignment of a teacher to a course.
     - Handling validation errors for non-existent teachers.
     - Verifying correct retrieval of course information inclusive of the teacher assignment.

7. **API Testing**
   - Utilize tools like Postman to verify the functionality of created API endpoints, ensuring compliance with defined specifications.

## V. Testing Strategy

### 5.1 Test Coverage
- Aim for a minimum of 70% coverage for newly implemented features, with critical paths reaching above 90%.
- Testing scenarios will include:
  - Valid assignment of a teacher.
  - Error response when attempting to assign a non-existent teacher.
  - Validation of course details post-assignment.

### 5.2 Test Types
- **Unit tests** for the service and repository layers.
- **Integration tests** in `tests/test_course_teacher.py`.

## VI. Scalability & Maintainability Considerations

### 6.1 Scalability
- SQLite will be used for local and testing environments, with design considerations for easy migration to PostgreSQL for production scenarios.

### 6.2 Maintainability
- Adhere to established coding standards to ensure code readability and maintainability.
- Include sufficient comments and docstrings to elucidate the purpose of all modules and methods.

## VII. Deployment Considerations

### 7.1 Local Development
- Ensure that the application is functional post-implementation, with comprehensive validations across all configuration setups.
- Update `README.md` to reflect changes in environment configurations and setup processes.

### 7.2 Backward Compatibility & Version Control
- Ensure the addition of the `teacher_id` column does not disrupt existing data models or relationships within the system.
- Document the migration steps clearly for transparency in future development contexts.
- Use version control best practices by thoroughly commenting on all changes, particularly those affecting the database scheme.

## Conclusion
This implementation plan provides a detailed strategic approach for integrating the Teacher relationship into the Course entity of the Educational Management System. It maintains existing functionalities, guarantees data integrity, and allows for future scalability and enhancements to the system.

### Existing Code Files Modifications
1. **File Modifications**:
   - **models.py**: Update to include the `teacher_id` foreign key in the Course model and relationship with Teacher.
   - **app.py**: Add new route for assigning a teacher to a course.
   - **repositories.py**: Extend CourseRepository to include functionality for assigning teachers.
   - **test_course_teacher.py**: New test file for validating the course-teacher assignment logic.

New Tests for `test_course_teacher.py`:
```python
import pytest
from flask import json
from app import app, db
from models import Course, Teacher

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # Create all tables
            # Sample data for tests
            teacher = Teacher(name='John Doe', email='john@example.com')
            course = Course(name='Math 101')
            db.session.add(teacher)
            db.session.add(course)
            db.session.commit()
        yield client
        with app.app_context():
            db.drop_all()  # Cleanup after tests

def test_assign_teacher_success(client):
    """Test a successful assignment of teacher to course."""
    course = Course.query.first()
    teacher = Teacher.query.first()
    
    response = client.patch(f'/courses/{course.id}/assign-teacher', json={'teacher_id': teacher.id})
    assert response.status_code == 200
    assert response.json['message'] == "Teacher assigned to course successfully."
    assert response.json['course']['teacher_id'] == teacher.id

def test_assign_teacher_not_found(client):
    """Test assignment of a non-existent teacher returns an error."""
    course = Course.query.first()
    
    response = client.patch(f'/courses/{course.id}/assign-teacher', json={'teacher_id': 999})
    assert response.status_code == 404
    assert response.json['error']['code'] == "E002"
    assert response.json['error']['message'] == "Teacher not found."
```

This comprehensive plan outlines the necessary steps to implement the desired feature while ensuring structural integrity and alignment with existing practices in the Educational Management System.