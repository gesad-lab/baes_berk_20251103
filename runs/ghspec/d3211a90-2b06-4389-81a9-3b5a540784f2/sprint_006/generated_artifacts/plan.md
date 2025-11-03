# Implementation Plan: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity
  
---
INCREMENTAL DEVELOPMENT CONTEXT

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
- **Course Model Modification**: Update to include relationship to Teacher.
- **API Controller**: Modify existing controller to manage Course entity operations.
- **Validation Layer**: Enhance existing validation for Course updates.
- **Database Migration**: Implement migration to update the Course table.

### 2.2 Module Responsibilities
1. **Course Model Modification**:
   - Update the Course entity to include the `teacher_id` foreign key, establishing the one-to-many relationship where a Teacher can teach multiple Courses but each Course has only one associated Teacher.

2. **API Controller**:
   - Implement routes for:
     - `PUT /courses/<course_id>`: Assign a Teacher to a Course.
     - `GET /courses/<course_id>`: Retrieve details of a specific Course, including the associated Teacher.

3. **Validation Layer**:
   - Implement functions to validate the existence of the Course and Teacher when making assignments.

4. **Database Migration**:
   - Create migration scripts to add the `teacher_id` foreign key to the Course table without affecting existing Student, Course, and Teacher data.

## III. Data Models and API Contracts

### 3.1 Data Model
Update the existing Course model to include a foreign key for Teacher:

```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))  # New foreign key

    teacher = relationship('Teacher')  # Relationship to Teacher

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

# Database initialization code
def initialize_database():
    engine = create_engine('sqlite:///database.db')  # Database connection
    Base.metadata.create_all(engine)  # Create tables if they do not exist
```

### 3.2 API Contracts
- **Assign Teacher to Course**
  - **Endpoint**: `PUT /courses/<course_id>`
  - **Request Body**: 
    ```json
    {
      "teacher_id": 1
    }
    ```
  - **Responses**:
    - Success (200 OK):
      ```json
      {
        "message": "Teacher assigned successfully to course.",
        "course": {
          "id": 1,
          "name": "Mathematics",
          "teacher_id": 1
        }
      }
      ```
    - Error (404 Not Found for course):
      ```json
      {
        "error": {
          "code": "E001",
          "message": "Course not found."
        }
      }
      ```
    - Error (400 Bad Request if teacher does not exist):
      ```json
      {
        "error": {
          "code": "E002",
          "message": "Teacher does not exist."
        }
      }
      ```

- **Retrieve Course Details**
  - **Endpoint**: `GET /courses/<course_id>`
  - **Responses**:
    - Success (200 OK):
      ```json
      {
        "id": 1,
        "name": "Mathematics",
        "teacher": {
          "id": 1,
          "name": "Jane Doe"
        }
      }
      ```
    - Error (404 Not Found for course):
      ```json
      {
        "error": {
          "code": "E001",
          "message": "Course not found."
        }
      }
      ```

## IV. Implementation Approach

### 4.1 Development Environment Setup
1. Ensure the virtual environment is prepared and contains relevant dependencies:
    ```bash
    pip install Flask Flask-SQLAlchemy
    ```

2. Update `requirements.txt`:
    ```
    Flask==2.0.3
    Flask-SQLAlchemy==2.5.1
    ```

### 4.2 Database Initialization and Migration
- Create a migration script to update the `courses` table:
```python
from sqlalchemy import create_engine, Column, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker
from models import Course

def upgrade():
    engine = create_engine('sqlite:///database.db')  # Ensure the path matches existing db
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Add foreign key column
    with engine.connect() as connection:
        connection.execute('ALTER TABLE courses ADD COLUMN teacher_id INTEGER REFERENCES teachers(id);')
    
    session.commit()
```

### 4.3 Input Validation
- Implement validation for Course updates ensuring relationships between entities are valid:
```python
def validate_course_update(course_id, teacher_id):
    # Check if Course exists
    course = session.query(Course).filter_by(id=course_id).first()
    if not course:
        raise ValueError("Course not found.")
    
    # Check if Teacher exists
    teacher = session.query(Teacher).filter_by(id=teacher_id).first()
    if not teacher:
        raise ValueError("Teacher does not exist.")
```

### 4.4 Routing and Controllers
- Modify the existing routes in the Flask API for Course to include assignments and retrieval:
```python
from flask import Blueprint, request, jsonify
from models import Course, Teacher  # Import models
from database import session  # Database session management

courses_bp = Blueprint('courses', __name__)

@courses_bp.route('/courses/<int:course_id>', methods=['PUT'])
def assign_teacher_to_course(course_id):
    data = request.json
    teacher_id = data.get('teacher_id')
   
    validate_course_update(course_id, teacher_id)

    # Assign teacher to course
    course = session.query(Course).filter_by(id=course_id).first()
    course.teacher_id = teacher_id
    session.commit()

    return jsonify({
        "message": "Teacher assigned successfully to course.",
        "course": {
            "id": course.id,
            "name": course.name,
            "teacher_id": course.teacher_id
        }
    }), 200

@courses_bp.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = session.query(Course).filter_by(id=course_id).first()

    if not course:
        return jsonify({"error": {"code": "E001", "message": "Course not found."}}), 404

    teacher = session.query(Teacher).filter_by(id=course.teacher_id).first() if course.teacher_id else None
    teacher_info = {"id": teacher.id, "name": teacher.name} if teacher else None

    return jsonify({
        "id": course.id,
        "name": course.name,
        "teacher": teacher_info
    }), 200
```

## V. Testing Strategy

### 5.1 Test Coverage
- Include unit tests for the validation of Course updates and API responses.

### 5.2 Testing Types
- Create unit and integration tests to validate the functionality of the Course assignment to Teachers.
- Ensure that existing tests for Course remain functional with the added relationship.

### 5.3 Test Framework
- Use pytest for the testing framework:
    ```bash
    pip install pytest pytest-flask
    ```

Example test for assigning a Teacher to a Course:
```python
def test_assign_teacher_to_course(client):
    # Assuming we have a teacher with ID 1 and a course with ID 1 exists
    response = client.put('/courses/1', json={'teacher_id': 1})
    assert response.status_code == 200
    assert response.json['message'] == "Teacher assigned successfully to course."
    
    response = client.get('/courses/1')
    assert response.json['teacher']['name'] == 'Jane Doe'  # Assuming teacher's name
```

## VI. Security Considerations

### 6.1 Data Protection
- Validate inputs on relationships to prevent SQL injection and other vulnerabilities.
- Ensure sensitive information is not logged during API interactions.

### 6.2 Dependency Security
- Regularly review and update dependencies to avoid known vulnerabilities.

## VII. Deployment Considerations

### 7.1 Deployment Configuration
- Ensure configuration settings in `.env` file reflect any new environment-related settings concerning the new relationship.

### 7.2 Production Readiness
- Conduct thorough testing, particularly concerning data migration, to prevent any data loss during the addition of the `teacher_id` column.

## VIII. Documentation and Maintenance

### 8.1 Documentation
- Update README and API documentation to include new endpoints and features related to Course and Teacher interactions.

### 8.2 Code Maintenance
- Ensure code adheres to coding standards. Refactor where necessary for clarity and maintainability.

---

## Summary of Trade-offs
- The decision to extend the **Course** model with a foreign key relationship to **Teacher** maintains a normalized database structure while enabling easier data retrieval.
- Validation ensures robust API handling of relationships, preventing data integrity issues through rigorous checks on Course and Teacher existence.
- This implementation plan provides a structured approach to enhancing the Course-Teacher relationship while ensuring backward compatibility with existing functionality.

This plan outlines the step-by-step approach needed to effectively implement the teacher relationship in Courses, maintaining scalability, security, and maintainability within the existing architecture.