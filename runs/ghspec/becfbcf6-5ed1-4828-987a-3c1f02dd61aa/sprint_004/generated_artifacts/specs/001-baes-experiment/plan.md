# Implementation Plan: Add Course Relationship to Student Entity

---
## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---
## 1. Architecture Overview

The architecture for extending the Student Management Web Application to incorporate a relationship between Students and Courses will continue with the existing microservice architecture pattern. This integration allows us to establish a many-to-many relationship between Students and Courses without compromising our existing functionality or data integrity.

- **API Layer**: Extend the established API to include endpoints that manage Course assignments for Students.
- **Service Layer**: Add business logic for course assignment, retrieval, and validation of course IDs.
- **Data Layer**: Incorporate migrations to establish the necessary database structure for the new relationship using a junction table (join table) for student-course associations.

## 2. Technology Stack

- **Programming Language**: Python 3.x
- **Web Framework**: Flask
- **Database**: SQLite
- **ORM Tool**: SQLAlchemy
- **Serialization**: Marshmallow
- **Migration Tool**: Alembic for database migrations

## 3. Module Boundaries and Responsibilities

### 3.1 API Layer
- **Responsibilities**:
  - Introduce endpoints for assigning courses to students and retrieving associated courses.

- **Endpoints**:
  - `POST /students/{student_id}/courses`: Assign a course to a student.
  - `GET /students/{student_id}/courses`: Retrieve all courses for a given student.

### 3.2 Service Layer
- **Responsibilities**:
  - Handle the logic related to course assignments and retrieval of course data, including validation for course IDs.

### 3.3 Data Layer
- **Responsibilities**:
  - Manage database interactions and the requirement for migration to implement the new relations.

## 4. Data Models

### 4.1 Updated Student Model
Define the Student entity with a many-to-many relationship with Course:
```python
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Junction table for many-to-many relationship
student_courses = Table('student_courses', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    # Existing fields...

    # Relationship to courses
    courses = relationship('Course', secondary=student_courses, back_populates='students')

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    students = relationship('Student', secondary=student_courses, back_populates='courses')
```

## 5. API Contracts

### Endpoint: Assign a Course to a Student
- **Method**: POST
- **URL**: `/students/{student_id}/courses`
- **Request Body**:
```json
{
  "course_id": 1
}
```
- **Success Response**:
  - **Status**: 201 Created
  - **Body**:
```json
{
  "student_id": 1,
  "courses": [
    {
      "id": 1,
      "name": "Introduction to Python",
      "level": "Beginner"
    }
  ]
}
```

### Error Response: Invalid Course ID
- **Status**: 400 Bad Request
- **Body**:
```json
{
  "error": {
    "code": "E002",
    "message": "Invalid course ID."
  }
}
```

### Endpoint: Retrieve Courses for a Student
- **Method**: GET
- **URL**: `/students/{student_id}/courses`
- **Success Response**:
  - **Status**: 200 OK
  - **Body**:
```json
[
  {
    "id": 1,
    "name": "Introduction to Python",
    "level": "Beginner"
  },
  {
    "id": 2,
    "name": "Advanced Java",
    "level": "Advanced"
  }
]
```

## 6. Implementation Approach

### 6.1 Setting Up the Environment
1. Make sure the required packages are installed:
   ```bash
   pip install Flask Flask-SQLAlchemy Flask-Marshmallow Alembic
   ```

### 6.2 Database Migration Strategy
- Incorporate Alembic migrations to create the junction table for the Student-Course relationship:
  1. Create migration script to establish `student_courses` table.
```python
def upgrade():
    op.create_table('student_courses',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['students.id']),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id'])
    )

def downgrade():
    op.drop_table('student_courses')
```
- Ensure that migrations run on application startup and maintain existing data integrity.

### 6.3 API Development Updates
- Introduce the `/students/{student_id}/courses` endpoint route in the Flask app:
```python
@app.route('/students/<int:student_id>/courses', methods=['POST'])
def assign_course_to_student(student_id):
    data = request.get_json()
    course_id = data.get('course_id')
    
    # Validating the course_id
    if not course_id or not Course.query.get(course_id):
        return jsonify({"error": {"code": "E002", "message": "Invalid course ID."}}), 400

    student = Student.query.get(student_id)
    if student:
        student.courses.append(Course.query.get(course_id))
        db.session.commit()
        return jsonify({
            "student_id": student.id,
            "courses": [{"id": course.id, "name": course.name, "level": course.level} for course in student.courses]
        }), 201
    return jsonify({"error": "Student not found"}), 404

@app.route('/students/<int:student_id>/courses', methods=['GET'])
def get_courses_for_student(student_id):
    student = Student.query.get(student_id)
    if not student:
        return jsonify({"error": {"code": "E003", "message": "Student not found."}}), 404
    
    return jsonify([{"id": course.id, "name": course.name, "level": course.level} for course in student.courses]), 200
```

## 7. Testing Strategy

### 7.1 Test Coverage
Develop tests for the new endpoints:
- Test successful assignments of courses to students and accurate retrieval of courses.
- Validate responses for incorrect course IDs and missing students.

### 7.2 Test Scenarios
1. **Assign a Course to a Student**: Ensure API succeeds and updates student data.
2. **Error Handling for Invalid Course ID**: Check API returns 400 error for invalid course.
3. **Retrieve Courses for a Student**: Confirm correct courses are returned associated with that student.

## 8. Security Considerations

- Sanitize all user inputs against SQL injections during assignments.
- Validate existence of `course_id` with pre-defined list of input formats.

## 9. Deployment Considerations

### 9.1 Production Deployment
- Ensure migration scripts are executed on production for seamless integration without downtime.
  
### 9.2 Health Check Endpoint
- Maintain a health check endpoint to monitor application status.

```python
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200
```

## 10. Documentation

Update `README.md`:
- Add the new endpoint documentation for `/students/{student_id}/courses`.
- Clearly provide usage examples and test cases for validating course assignments.

## Technical Trade-offs

1. **Implementing Junction Table**: Facilitates many-to-many relationships, but adds complexity to migration and data retrieval.
2. **Error Response Management**: Provides clarity but necessitates thorough validation to prevent misuse of the API.
3. **Maintaining Backward Compatibility**: Ensures existing Student entity functionality is intact while extending capabilities.

This implementation plan delineates the steps necessary for incorporating the course relationship into the Student Management System, ensuring expanded functionality while safeguarding existing data integrity and compatibility.