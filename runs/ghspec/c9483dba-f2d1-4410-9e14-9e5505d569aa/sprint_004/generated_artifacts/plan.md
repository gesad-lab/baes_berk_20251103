# Implementation Plan: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

## Version
1.1.0

## Overview
This implementation plan outlines the architecture, technology stack, data models, API contracts, and implementation approach required for adding a course relationship to the student entity within the student management application. This enhancement will allow the association of students with one or more courses, improving the system's capacity to manage student enrollments.

## Architecture

### 1.1 Application Architecture
- **Type**: RESTful web application
- **Design Pattern**: MVC (Model-View-Controller) for separation of concerns
- **Framework**: Flask (Python) for the backend
- **Database**: SQLite for local development and testing, with migration support for schema updates.

### 1.2 Module Structure
1. **Models**:
   - Update the existing `Student` model to include a many-to-many relationship with the `Course` model.
   
2. **Controllers**:
   - Enhance handlers for assigning courses to students and retrieving student details with courses.

3. **Routes**:
   - Define the API endpoints that handle requests for course assignments and retrieval.

4. **Database Management**:
   - Logic for updating the `Student` and `Course` tables to establish the relationship and handle migrations.

## Technology Stack
- **Backend Framework**: Flask
- **Database**: SQLite
- **ORM**: SQLAlchemy for database interactions
- **Request Validation**: Marshmallow for input validation and serialization
- **Testing Framework**: pytest for testing the application
- **Environment Management**: Python 3 and virtual environments

## Data Models

### 2.1 Updated Student Model
```python
from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from your_app.database import Base  # Adjust import based on actual structure

# Association Table for students and courses
student_courses = Table('student_courses', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    courses = relationship('Course', secondary=student_courses, back_populates='students')

    def __repr__(self):
        return f'<Student {self.id}: {self.name}, Email: {self.email}>'

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    students = relationship('Student', secondary=student_courses, back_populates='courses')

    def __repr__(self):
        return f'<Course {self.id}: {self.name}, Level: {self.level}>'
```

### 2.2 Database Schema
The SQLite database will now include the updated structure:
- **students**
  - `id`: Integer (Primary Key, Auto-increment)
  - `name`: String (Non-nullable)
  - `email`: String (Non-nullable)
  
- **courses**
  - `id`: Integer (Primary Key, Auto-increment)
  - `name`: String (Non-nullable)
  - `level`: String (Non-nullable)

- **student_courses** (Association Table)
  - `student_id`: Integer (Foreign Key)
  - `course_id`: Integer (Foreign Key)

## API Contracts

### 3.1 Endpoints
1. **Assign Course to Student**
   - **Endpoint**: `POST /students/{student_id}/courses`
   - **Request Body**:
     ```json
     {
       "course_id": "1"
     }
     ```
   - **Responses**:
     - **200 OK**:
       ```json
       {
         "id": 1,
         "courses": [1]
       }
       ```
     - **400 Bad Request** (if `course_id` is missing):
       ```json
       {
         "error": {
           "code": "E001",
           "message": "Course ID is required"
         }
       }
       ```
     - **404 Not Found** (if the student does not exist):
       ```json
       {
         "error": {
           "code": "E002",
           "message": "Student not found"
         }
       }
       ```

2. **Retrieve Student with Courses**
   - **Endpoint**: `GET /students/{id}`
   - **Responses**:
     - **200 OK**:
       ```json
       {
         "id": 1,
         "name": "John Doe",
         "email": "john.doe@example.com",
         "courses": [
           {
             "id": 1,
             "name": "Mathematics",
             "level": "Beginner"
           }
         ]
       }
       ```
     - **404 Not Found** (if the student does not exist):
       ```json
       {
         "error": {
           "code": "E003",
           "message": "Student not found"
         }
       }
       ```

## Implementation Approach

### 4.1 Steps to Implement
1. **Modify Project Structure**:
   ```bash
   student_management/
       ├── src/
       │   ├── app.py
       │   ├── models.py       # Update with new Student and Course models
       │   ├── controllers/
       │   │   ├── student_controller.py # Updated controller for Student entity
       │   └── database.py
       ├── migrations/         # New migration scripts for relationship establishment
       ├── tests/
       │   ├── test_student.py # Create tests for Student course functionality
       └── README.md
   ```

2. **Database Migration**:
   - Utilize Flask-Migrate (using Alembic) for managing migrations.
   - Create a new migration script to add the relationships:
     ```bash
     flask db migrate -m "Add many-to-many relationship between Students and Courses"
     flask db upgrade
     ```

3. **Route Definitions**:
   - Define new `POST /students/{student_id}/courses` and `GET /students/{id}` routes in `app.py`:
     ```python
     @app.route('/students/<int:student_id>/courses', methods=['POST'])
     @app.route('/students/<int:id>', methods=['GET'])
     ```

4. **Controller Logic**:
   - Implement logic in `student_controller.py` to handle assignment and retrieval of courses for students, ensuring input validations:
     ```python
     from flask import request, jsonify
     from models import Student, Course, db  # Import necessary components

     @app.route('/students/<int:student_id>/courses', methods=['POST'])
     def assign_course(student_id):
         data = request.get_json()
         course_id = data.get('course_id')

         if not course_id:
             return jsonify({"error": {"code": "E001", "message": "Course ID is required"}}), 400
         
         student = Student.query.get(student_id)
         if not student:
             return jsonify({"error": {"code": "E002", "message": "Student not found"}}), 404

         course = Course.query.get(course_id)
         if not course:
             return jsonify({"error": {"code": "E003", "message": "Course not found"}}), 404

         student.courses.append(course)
         db.session.commit()
         return jsonify({"id": student.id, "courses": [c.id for c in student.courses]}), 200

     @app.route('/students/<int:id>', methods=['GET'])
     def get_student(id):
         student = Student.query.get(id)
         if not student:
             return jsonify({"error": {"code": "E003", "message": "Student not found"}}), 404
         
         courses = [{"id": course.id, "name": course.name, "level": course.level} for course in student.courses]
         return jsonify({"id": student.id, "name": student.name, "email": student.email, "courses": courses}), 200
     ```

5. **Validation and Error Handling**:
   - Ensure validation logic for `course_id` and checks for validity of the student ID.
   - Use Marshmallow for additional validation as needed.

6. **Testing**:
   - Create unit tests in `test_student.py` for both the assignment and retrieval functionalities.
   - Ensure a minimum of 70% coverage for this new functionality.

## Security Considerations
- Validate course and student inputs to avoid SQL injection and other vulnerabilities.
- Sanitize inputs to prevent injection risks.

## Scalability Considerations
- While starting with SQLite, the design should allow future transitions to a more robust database system (e.g., PostgreSQL) as the student management application scales.

## Conclusion
This implementation plan provides a comprehensive approach for integrating a course relationship into the student entity. Following this plan will ensure a seamless enhancement while maintaining existing application integrity and user needs.

Existing Code Files:
- Update `src/models.py` to include many-to-many relationship, create a `src/controllers/student_controller.py`, and manage migration files in the `migrations/` directory.
- Create tests in `tests/test_student.py`.

```python
# tests/test_student.py
import pytest
from app import app  # Assuming 'app' is the Flask app instance
from models import Student, Course, db  # Assuming both models are defined in 'models.py'

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_assign_course_success(client):
    """Test assigning a course to a student with valid IDs."""
    # Set up necessary data
    course = Course(name='Mathematics', level='Beginner')
    student = Student(name='John Doe', email='john.doe@example.com')
    db.session.add(course)
    db.session.add(student)
    db.session.commit()

    # Assign course to student
    response = client.post(f'/students/{student.id}/courses', json={'course_id': course.id})
    assert response.status_code == 200
    assert response.json == {'id': student.id, 'courses': [course.id]}

def test_assign_course_invalid_student(client):
    """Test assigning a course to a non-existent student."""
    response = client.post('/students/999/courses', json={'course_id': '1'})
    assert response.status_code == 404
    assert response.json['error']['code'] == 'E002'

def test_get_student_courses(client):
    """Test retrieving a student with their assigned courses."""
    course = Course(name='Mathematics', level='Beginner')
    student = Student(name='John Doe', email='john.doe@example.com', courses=[course])
    db.session.add(course)
    db.session.add(student)
    db.session.commit()

    response = client.get(f'/students/{student.id}')
    assert response.status_code == 200
    assert response.json['courses'] == [{'id': course.id, 'name': 'Mathematics', 'level': 'Beginner'}]
```

This plan outlines how new modules will integrate with existing components, requiring modifications rather than complete replacements. The backward compatibility of data models will be adhered to with clear migration strategies documented effectively.