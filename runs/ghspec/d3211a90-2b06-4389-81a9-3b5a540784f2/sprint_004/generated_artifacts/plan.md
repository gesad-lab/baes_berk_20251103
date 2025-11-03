# Implementation Plan: Add Course Relationship to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---

## I. Architecture Overview

### 1.1 System Architecture
- **Architecture Pattern**: MVC (Model-View-Controller)
- **Components**:
  - **Model**: Manages data (SQLite database).
  - **View**: Web interface for user interactions (HTML/CSS/JavaScript).
  - **Controller**: Handles API requests (Flask application).

### 1.2 Technology Stack
- **Backend Framework**: Flask (Python 3.11+)
- **Database**: SQLite
- **Frontend**: Basic HTML/CSS with JavaScript for interactivity
- **API Format**: JSON
- **Package Management**: pip (using `requirements.txt`)

## II. Module Boundaries and Responsibilities

### 2.1 Modules
- **Student Model**: Updated model to handle relationships with courses.
- **Course Model**: Already defined; no changes needed.
- **API Controller**: New controller handling operations for student-course associations.
- **Validation Layer**: New validation for student-course associations.
- **Database Migration**: Implement migration to create a junction table for students and courses.

### 2.2 Module Responsibilities
1. **Student Model**:
   - Extend functionality to accommodate a many-to-many relationship with Course entities.

2. **API Controller**:
   - Implement routes for:
     - `POST /students/<student_id>/courses`: Associate courses with a student.
     - `GET /students/<student_id>`: Retrieve student details including associated courses.
     - `DELETE /students/<student_id>/courses/<course_id>`: Remove a course from a student's associations.

3. **Validation Layer**:
   - Implement functions to validate the presence of student and course IDs when associating and removing courses.

4. **Database Migration**:
   - Create migration scripts to add the `student_courses` junction table while preserving existing data.

## III. Data Models and API Contracts

### 3.1 Data Model
```python
from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Define junction table for Student-Course relationship
student_courses = Table('student_courses', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
```

### 3.2 API Contracts
- **Associate Courses with Student**
  - **Endpoint**: `POST /students/<student_id>/courses`
  - **Request Body**: 
    ```json
    {
      "course_ids": [1, 2, 3]
    }
    ```
  - **Responses**:
    - Success (200 OK):
      ```json
      {
        "message": "Courses associated successfully."
      }
      ```
    - Error (404 Not Found for student):
      ```json
      {
        "error": {
          "code": "E002",
          "message": "Student does not exist."
        }
      }
      ```

- **Retrieve Student with Courses**
  - **Endpoint**: `GET /students/<id>`
  - **Responses**:
    - Success (200 OK):
      ```json
      {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com",
        "courses": [1, 2]
      }
      ```
    - Error (404 Not Found for student):
      ```json
      {
        "error": {
          "code": "E002",
          "message": "Student does not exist."
        }
      }
      ```

- **Remove Course from Student**
  - **Endpoint**: `DELETE /students/<student_id>/courses/<course_id>`
  - **Responses**:
    - Success (200 OK):
      ```json
      {
        "message": "Course removed successfully."
      }
      ```
    - Error (404 Not Found for student or course):
      ```json
      {
        "error": {
          "code": "E002",
          "message": "Student does not exist."
        }
      }
      ```

## IV. Implementation Approach

### 4.1 Development Environment Setup
1. Update the virtual environment and install necessary dependencies:
    ```bash
    pip install Flask Flask-SQLAlchemy
    ```

2. Update `requirements.txt`:
    ```
    Flask==2.0.3
    Flask-SQLAlchemy==2.5.1
    ```

### 4.2 Database Initialization and Migration
- Create a migration script to add the `student_courses` junction table:
```python
from sqlalchemy import create_engine, Table, Column, MetaData, Integer, ForeignKey

def create_student_courses_table():
    engine = create_engine('sqlite:///database.db')  # Ensuring this matches existing database path
    metadata = MetaData(bind=engine)
    
    student_courses_table = Table('student_courses', metadata,
        Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
        Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
    )
    metadata.create_all(engine)  # Create table if not exists
```

### 4.3 Input Validation
- Implement validation for student-course association:
```python
def validate_student_course_data(student_id, course_ids):
    if not isinstance(student_id, int):
        raise ValueError("Invalid student ID.")
    if not isinstance(course_ids, list) or not all(isinstance(course_id, int) for course_id in course_ids):
        raise ValueError("Course IDs must be a list of integers.")
```

### 4.4 Routing and Controllers
- Add new routes for student-course associations in the Flask API:
```python
from flask import Blueprint, request, jsonify
from models.student import Student  # Assuming the Student model is in models/student.py
from models.course import Course  # Assuming the Course model is in models/course.py
from database import session  # Assuming the database session is managed in database.py

students_bp = Blueprint('students', __name__)

@students_bp.route('/students/<int:student_id>/courses', methods=['POST'])
def associate_courses_with_student(student_id):
    data = request.json
    validate_student_course_data(student_id, data['course_ids'])

    student = session.query(Student).filter_by(id=student_id).first()
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student does not exist."}}), 404

    for course_id in data['course_ids']:
        # Assuming you handle duplicate associations at this point
        association = student_courses.insert().values(student_id=student_id, course_id=course_id)
        session.execute(association)

    session.commit()

    return jsonify({"message": "Courses associated successfully."}), 200

@students_bp.route('/students/<int:student_id>', methods=['GET'])
def get_student_with_courses(student_id):
    student = session.query(Student).filter_by(id=student_id).first()
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student does not exist."}}), 404

    course_ids = session.query(student_courses.c.course_id).filter_by(student_id=student_id).all()
    course_ids = [course_id for (course_id,) in course_ids]  # Flatten the list

    return jsonify({
        "id": student.id,
        "name": student.name,
        "email": student.email,
        "courses": course_ids  # List of associated course IDs
    }), 200
    
@students_bp.route('/students/<int:student_id>/courses/<int:course_id>', methods=['DELETE'])
def remove_course_from_student(student_id, course_id):
    student = session.query(Student).filter_by(id=student_id).first()
    if not student:
        return jsonify({"error": {"code": "E002", "message": "Student does not exist."}}), 404

    delete_association = student_courses.delete().where(student_courses.c.student_id == student_id).\
                         where(student_courses.c.course_id == course_id)
    
    result = session.execute(delete_association)
    session.commit()
    
    return jsonify({"message": "Course removed successfully."}), 200
```

## V. Testing Strategy

### 5.1 Test Coverage
- Include unit tests for the validation of student-course associations and API responses.

### 5.2 Testing Types
- Create unit tests to validate the functionality of operations:
  - **Unit Tests**: Check proper association and removal of courses to/from students.
  - **Integration Tests**: Verify the API behaves as expected during student-course interactions.

### 5.3 Test Framework
- Use pytest for the testing framework:
    ```bash
    pip install pytest pytest-flask
    ```

Example test for associating courses:
```python
def test_associate_courses_with_student(client):
    response = client.post('/students/1/courses', json={'course_ids': [1, 2]})
    assert response.status_code == 200
    assert response.json['message'] == "Courses associated successfully."
    
    response = client.get('/students/1')
    assert response.json['courses'] == [1, 2]
```

## VI. Security Considerations

### 6.1 Data Protection
- Validate inputs rigorously to prevent SQL injection and other vulnerabilities.
- Ensure no sensitive data is logged or exposed during API interactions.

### 6.2 Dependency Security
- Regularly review and update dependencies to avoid known vulnerabilities.

## VII. Deployment Considerations

### 7.1 Deployment Configuration
- Ensure configuration settings in `.env` file reflect any new environment-specific settings regarding migration.

### 7.2 Production Readiness
- Conduct thorough testing, particularly concerning data migration, to prevent any data loss during upgrades.

## VIII. Documentation and Maintenance

### 8.1 Documentation
- Update README and API documentation to include new student-course association endpoints and features.

### 8.2 Code Maintenance
- Ensure code adheres to coding standards and best practices. Refactor where necessary for better clarity and maintainability.

---

## Summary of Trade-offs
- The decision to extend the **Flask** framework and **SQLite** database model allows for seamless integration of new course-student relationships while maintaining system stability.
- Rigorous input validation ensures a robust API that prevents unwanted data manipulation and enhances the overall security of the application while respecting existing models.
- This approach allows for careful tracking of academic pathways, ultimately aiding educational insights without compromising the data integrity of existing models.

This implementation plan details the necessary steps to effectively manage course associations with students, ensuring compatibility, maintainability, and scalability within the existing architecture.