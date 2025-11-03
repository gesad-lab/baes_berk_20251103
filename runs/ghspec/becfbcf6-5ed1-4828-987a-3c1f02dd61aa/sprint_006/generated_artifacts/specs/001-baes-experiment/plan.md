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

## 1. Architecture Overview

To integrate the Teacher relationship into the Course entity, the existing microservice architecture of the Student Management Web Application will be leveraged. This integration will enhance course management capabilities while ensuring that the current functionalities related to courses and students remain unaffected.

- **API Layer**: Extend the Course API to add capabilities for associating teachers with courses.
- **Service Layer**: Add the business logic to manage course assignments and validations.
- **Data Layer**: Update the current database schema to add a `teacher_id` field in the Course entity without disrupting existing data.

## 2. Technology Stack

- **Programming Language**: Python 3.x
- **Web Framework**: Flask
- **Database**: SQLite (to maintain consistency with prior implementations)
- **ORM Tool**: SQLAlchemy
- **Serialization**: Marshmallow
- **Migration Tool**: Alembic for database migrations

## 3. Module Boundaries and Responsibilities

### 3.1 API Layer
- **Responsibilities**:
  - Add new endpoints for assigning a teacher to a course and retrieving course information with teacher details.

- **Endpoints**:
  - `PATCH /courses/{course_id}/assign-teacher`: Assign a teacher to a course.
  - `GET /courses/{course_id}`: Retrieve a course with all relevant details, including the assigned teacher.

### 3.2 Service Layer
- **Responsibilities**:
  - Manage course assignments and ensure validations are in place for teacher existence.

### 3.3 Data Layer
- **Responsibilities**:
  - Implement migrations to enhance the Course data model by adding a `teacher_id`.
  - Maintain interaction logic with the existing data while ensuring referential integrity.

## 4. Data Models

### 4.1 Updated Course Model
Enhance the existing Course model to include a `teacher_id` field:
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)  # Foreign key reference to Teacher

    teacher = relationship("Teacher", back_populates="courses")

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)  # Email should be unique
    courses = relationship("Course", back_populates="teacher")
```

### 4.2 Database Model Migration
Create a migration that adds the `teacher_id` field to the Course table:
```python
def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer(), nullable=True))
    op.create_foreign_key('fk_teacher_courses', 'courses', 'teachers', ['teacher_id'], ['id'])

def downgrade():
    op.drop_constraint('fk_teacher_courses', 'courses', type_='foreignkey')
    op.drop_column('courses', 'teacher_id')
```

## 5. API Contracts

### Endpoint: Assign a Teacher to a Course
- **Method**: PATCH
- **URL**: `/courses/{course_id}/assign-teacher`
- **Request Body**:
```json
{
  "teacher_id": 1
}
```
- **Success Response**:
  - **Status**: 200 OK
  - **Body**:
```json
{
  "id": 1,
  "name": "Mathematics",
  "level": "Intermediate",
  "teacher_id": 1
}
```

### Error Response: Teacher Not Found
- **Status**: 400 Bad Request
- **Body**:
```json
{
  "error": {
    "code": "E001",
    "message": "Teacher does not exist."
  }
}
```

### Endpoint: Retrieve a Course with Teacher Information
- **Method**: GET
- **URL**: `/courses/{course_id}`
- **Success Response**:
  - **Status**: 200 OK
  - **Body**:
```json
{
  "id": 1,
  "name": "Mathematics",
  "level": "Intermediate",
  "teacher": {
    "id": 1,
    "name": "John Doe",
    "email": "johndoe@example.com"
  }
}
```

## 6. Implementation Approach

### 6.1 Setting Up the Environment
Ensure the required packages are installed:
```bash
pip install Flask Flask-SQLAlchemy Flask-Marshmallow Alembic
```

### 6.2 Database Migration Strategy
1. Use Alembic to generate a new migration script to add the `teacher_id` field while creating the foreign key constraint.
2. Apply migrations on application startup to keep data integrity:
   ```bash
   alembic upgrade head
   ```

### 6.3 API Development Updates
Introduce the new API routes in the Flask application:
```python
from flask import request, jsonify
from app import app, db, Course, Teacher

@app.route('/courses/<int:course_id>/assign-teacher', methods=['PATCH'])
def assign_teacher_to_course(course_id):
    data = request.get_json()
    teacher_id = data.get('teacher_id')

    # Validate the provided teacher_id
    if not Teacher.query.get(teacher_id):
        return jsonify({"error": {"code": "E001", "message": "Teacher does not exist."}}), 400

    course = Course.query.get(course_id)
    course.teacher_id = teacher_id
    db.session.commit()
    
    return jsonify({
        "id": course.id,
        "name": course.name,
        "level": course.level,
        "teacher_id": course.teacher_id
    }), 200

@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": {"code": "E002", "message": "Course not found."}}), 404

    teacher_info = None
    if course.teacher_id:
        teacher_info = {
            "id": course.teacher.id,
            "name": course.teacher.name,
            "email": course.teacher.email
        }

    return jsonify({
        "id": course.id,
        "name": course.name,
        "level": course.level,
        "teacher": teacher_info
    }), 200
```

## 7. Testing Strategy

### 7.1 Test Coverage
Develop tests for the following scenarios:
- Assigning a teacher to a course.
- Retrieving course details along with teacher information.
- Handling scenarios with invalid teacher_id assignment.

### 7.2 Test Scenarios
1. **Assign a Teacher**: Validate successful assignment and response correctness including the assigned teacher ID.
2. **Invalid Teacher Assignment**: Ensure API returns the appropriate error when assigning a non-existent teacher (E001).
3. **Retrieve a Course**: Confirm retrieval of course information and ensure that assigned teacher details are correctly included.

## 8. Security Considerations

- Sanitize all user inputs to prevent SQL injection attacks.
- Ensure teacher existence validations are performed before assignment actions to retain database integrity.

## 9. Deployment Considerations

### 9.1 Production Deployment
Perform database migration on production to integrate the `teacher_id` into the Course entity without impacting live existences.

### 9.2 Health Check Endpoint
Maintain a health check endpoint to ensure the application’s availability:
```python
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200
```

## 10. Documentation

Update `README.md` to reflect:
- New API endpoint `/courses/{course_id}/assign-teacher` (PATCH) to assign teachers.
- Endpoint `/courses/{course_id}` (GET) to retrieve course details along with the associated teacher information.
- Examples of expected requests and responses.

## Technical Trade-offs

1. **Database Relationships**: Adding foreign key constraints on the `teacher_id` ensures referential integrity but adds complexity in managing error states when assigning teachers.
2. **Error Reporting**: Improved error messages assist users but lead to additional checks during the assignment processes, which must be efficiently handled to avoid performance impacts.

This implementation plan describes a methodical approach to enhancing the Student Management system to support the assignment of teachers to courses, maintaining existing functionalities while providing the necessary architecture for future developments.