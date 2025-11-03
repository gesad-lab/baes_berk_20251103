# Implementation Plan: Add Course Relationship to Student Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan: 
# Implementation Plan: Add Course Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan: 
# Implementation Plan: Add Email Field to Student Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan: 
# Implementation Plan: Student Entity Management

## I. Project Overview
The goal of this implementation plan is to establish a relationship between the existing Student entity and the Course entity within the student management system. This new feature enables students to enroll in multiple courses, providing improved curriculum management and academic tracking, setting the stage for future functionalities like course enrollment management.

## II. Technical Architecture

### 1. Architecture Overview
- **Type**: RESTful API
- **Framework**: Flask for Python
- **Database**: SQLite for lightweight and scalable local storage

### 2. Modular Design
- **Module 1: API Layer**
  - Responsible for handling incoming HTTP requests related to student course enrollments and routing them to appropriate service methods.

- **Module 2: Service Layer**
  - Handles business logic for enrolling students in courses, retrieving enrolled courses, and managing validation and error responses.

- **Module 3: Data Access Layer**
  - Interacts with the SQLite database to perform CRUD operations regarding student-course enrollments and includes a migration for the schema update.

## III. Technology Stack
- **Programming Language**: Python
- **Web Framework**: Flask
- **ORM**: SQLAlchemy for database abstraction
- **Database**: SQLite
- **Testing Framework**: pytest
- **Documentation**: Swagger for API documentation

## IV. API Contracts

### 1. Enroll Student in Course
- **Endpoint**: `POST /students/{studentId}/courses`
- **Request Body**: 
```json
{
    "courseId": "integer"
}
```
- **Response**:
  - Success: `201 Created`
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com",
        "course_ids": [1]
    }
    ```
  - Error (missing courseId): `400 Bad Request`
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Course ID is required."
        }
    }
    ```
  
### 2. Get Enrolled Courses
- **Endpoint**: `GET /students/{studentId}/courses`
- **Response**:
  - Success: `200 OK`
    ```json
    [
        {
            "id": 1,
            "name": "Mathematics",
            "level": "Intermediate"
        },
        {
            "id": 2,
            "name": "Science",
            "level": "Advanced"
        }
    ]
    ```

## V. Data Models

### 1. Student Model
- Extend the existing Student model to include a relationship with the Course model.
```python
class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    course_ids = relationship("Course", secondary="student_course", back_populates="students")
```

### 2. Course Model (from previous plan)
```python
class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    students = relationship("Student", secondary="student_course", back_populates="courses")
```

### 3. Association Table
- Use a secondary table for many-to-many relationship.
```python
class StudentCourse(Base):
    __tablename__ = 'student_course'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
```

## VI. Implementation Steps

### Step 1: Environment Setup
- Ensure the Python virtual environment is activated.
- Install necessary packages: Flask, SQLAlchemy, and pytest.

### Step 2: Database Migration
- Create a migration script to update the `students` table by adding a relationship to the `courses` table and create the `student_course` association table.
```python
def upgrade():
    op.create_table('student_course',
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
        sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True)
    )
```

### Step 3: Implement API Endpoints
- Create endpoints for enrolling students in courses and retrieving their enrolled courses.
- Implement the `POST /students/{studentId}/courses` and `GET /students/{studentId}/courses` routes in the API layer.

### Step 4: Validation Logic
- Ensure that the request body for enrolling students validates the presence and validity of a course ID.

### Step 5: Error Handling
- Implement structured error responses for requests missing the course ID or attempting to enroll in a non-existent course.

### Step 6: Write Tests
- Create unit tests for:
  - Successful enrollment of students in existing courses.
  - Handling attempts to enroll in invalid courses and ensuring correct error messages.
  - Retrieval of enrolled courses for specific students.

### Step 7: Documentation
- Update API documentation to reflect the new endpoints `POST /students/{studentId}/courses` and `GET /students/{studentId}/courses`.

## VII. Testing Strategy

### 1. Unit Tests
- Tests should cover:
  - Successful enrollment in a course with a valid course ID.
  - Error handling for invalid or missing course IDs.

### 2. Integration Tests
- Validate interactions between the API, service layer, and database to ensure data persistence and correct functionality.

## VIII. Deployment Considerations

### 1. Production Readiness
- Ensure that the application starts successfully and performs the necessary migrations on startup.
- Implement a health check endpoint for monitoring during production.

### 2. Configuration Management
- Use environment variables for database connection settings and other sensitive configurations to maintain flexibility.

## IX. Security Considerations
- Validate all incoming requests to guard against potential SQL injection and ensure robust error handling practices.

## X. Monitoring & Logging
- Implement logging of API requests and responses without exposing sensitive data for error tracking.

## XI. Documentation
- Update the `README.md` file with instructions on how to set up, run, and use the API for enrolling students into courses.

## XII. Reflection on Trade-offs
- The choice of SQLite allows for a lightweight, efficient solution suitable for small-scale applications while maintaining backward compatibility with existing student records as we enhance course management capabilities.

---

## Modifications to Existing Files

1. **New Models**:
   - Create a new file `models/student_course.py` for the StudentCourse association model:
   ```python
   from app import db
   from sqlalchemy import Column, Integer, ForeignKey

   class StudentCourse(db.Model):
       __tablename__ = 'student_course'
       
       student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
       course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
   ```

2. **API Layer**:  
   - Update the routes in `routes.py` or equivalent to include course enrollment endpoints:
   ```python
   @students_bp.route('/students/<int:student_id>/courses', methods=['POST'])
   def enroll_student_course(student_id):
       data = request.get_json()
       course_id = data.get('courseId')
       if not course_id:
           return jsonify({"error": {"code": "E001", "message": "Course ID is required."}}), 400
       
       # Here we would check if the course exists
       course = Course.query.get(course_id)
       if not course:
           return jsonify({"error": {"code": "E002", "message": "Course does not exist."}}), 404
       
       student = Student.query.get(student_id)
       if student:
           student.courses.append(course)
           db.session.commit()
           return jsonify({"id": student.id, "name": student.name, "email": student.email, "course_ids": [c.id for c in student.courses]}), 201
       
       return jsonify({"error": {"code": "E003", "message": "Student not found."}}), 404

   @students_bp.route('/students/<int:student_id>/courses', methods=['GET'])
   def get_enrolled_courses(student_id):
       student = Student.query.get(student_id)
       if not student:
           return jsonify({"error": {"code": "E003", "message": "Student not found."}}), 404
       
       return jsonify([{"id": course.id, "name": course.name, "level": course.level} for course in student.courses]), 200
   ```

3. **Tests**:
   - In a new test file `tests/test_student_courses.py`, add tests for course enrollment and retrieval:
   ```python
   def test_enroll_student_in_course(client):
       # Assume we have setup for creating a student and a course beforehand
       response = client.post('/students/1/courses', json={"courseId": 1})
       assert response.status_code == 201
       assert 1 in response.json['course_ids']

   def test_enroll_student_in_invalid_course(client):
       response = client.post('/students/1/courses', json={"courseId": 999})
       assert response.status_code == 404
       assert response.json['error']['code'] == "E002"

   def test_get_enrolled_courses(client):
       client.post('/students/1/courses', json={"courseId": 1})
       response = client.get('/students/1/courses')
       assert response.status_code == 200
       assert len(response.json) > 0
   ```

This comprehensive plan outlines the steps necessary to implement the course relationship feature while ensuring compatibility and high-quality standards throughout the ongoing development process.