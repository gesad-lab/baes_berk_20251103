# Implementation Plan: Add Course Relationship to Student Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---

## 1. Technical Architecture

### 1.1 Overview
This implementation plan focuses on establishing a relationship between the Student entity and the Course entity in the existing educational management system. The architecture maintains the microservices model, ensuring clear separation of concerns across the API layer, service layer, and data layer.

### 1.2 Components
- **API Layer**: New endpoints to handle course enrollment and retrieval functionalities.
- **Service Layer**: Introducing business logic to manage the enrollments and relationships between Students and Courses.
- **Data Layer**: Update existing data models to include an Enrollment table, serving as a join table between Students and Courses.
- **Database**: Extend the existing database schema to incorporate the Enrollment table while preserving current Student and Course data.

## 2. Technology Stack

### 2.1 Programming Language
- **Python**: Stays consistent as the language of choice.

### 2.2 Framework
- **Flask**: To create new endpoints for handling enrollments between students and courses.

### 2.3 Database
- **SQLite**: The existing choice; it will support the creation of new tables and relationships.

### 2.4 Dependencies
- **Flask-RESTful**: Utilized for building REST APIs.
- **Flask-SQLAlchemy**: Continues to be used for ORM capabilities.
- **Marshmallow**: To handle data serialization and validation, extended to manage Enrollment data.

## 3. Module Boundaries and Responsibilities

### 3.1 API Module
- **New Endpoints**:
  - `POST /enrollments`: To enroll a student in a course.
  - `GET /students/<id>/courses`: To retrieve all courses a specific student is enrolled in.

### 3.2 Service Module
- **New Functions**:
  - `enroll_student_in_course(student_id: int, course_id: int) -> dict`: To manage the enrollment of students in courses.
  - `get_courses_for_student(student_id: int) -> list`: To fetch courses associated with a student.

### 3.3 Data Access Module
- **New Model**:
  - `Enrollment`: A join table model representing Student-Course relationships.

## 4. Data Models

### 4.1 Updated Student and Course Models
```python
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    # Other fields...

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    # Other fields...

class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)

    student = db.relationship('Student', backref=db.backref('enrollments', lazy=True))
    course = db.relationship('Course', backref=db.backref('enrollment_list', lazy=True))
```

## 5. API Contracts

### 5.1 Request/Response Format

#### 5.1.1 Enroll Student in Course
- **Request**:
    - Method: `POST`
    - URL: `/enrollments`
    - Body: `{ "student_id": 1, "course_id": 2 }`
- **Response**:
    - Status: `201 Created`
    - Body: `{ "message": "Student enrolled successfully.", "student_id": 1, "course_id": 2 }`

#### 5.1.2 Retrieve Student Courses
- **Request**:
    - Method: `GET`
    - URL: `/students/<id>/courses`
- **Response**:
    - Status: `200 OK`
    - Body: `[ { "course_id": 2, "course_name": "Math 101" }, ... ]`

#### 5.1.3 Error Handling for Invalid Enrollment
- **Request**:
    - Method: `POST`
    - URL: `/enrollments`
    - Body: `{ "student_id": 99, "course_id": 2 }`  (Assuming student ID 99 does not exist)
- **Response**:
    - Status: `400 Bad Request`
    - Body: `{ "error": {"code": "E123", "message": "Student ID does not exist."} }`

## 6. Implementation Approach

### 6.1 Setup and Configuration
- Extend the Flask application to handle the new enrollments and retrieval endpoints.

### 6.2 Database Initialization
- A migration strategy using Flask-Migrate will be employed to create the Enrollment table in the SQLite database:
  
```bash
flask db migrate -m "Add enrollments table for Student and Course relationship"
flask db upgrade
```

### 6.3 RESTful Endpoints
- Implement the `POST` and `GET` routes, ensuring that valid enrollment is performed and courses are retrievable.

### 6.4 Testing Strategy
- Develop unit tests for the service functions managing enrollments and the new API endpoints.
- Integration tests will validate the main enrollment and retrieval flows.

### 6.5 Error Handling
- Ensure that the enrollment process captures and returns appropriate error responses for invalid inputs.

## 7. Scalability, Security, and Maintainability Considerations

### 7.1 Scalability
- The use of join tables allows future expansions on enrollments without altering existing structures heavily.

### 7.2 Security
- Input validation will be enforced to secure against SQL injection and ensure that only valid Student and Course IDs are processed.

### 7.3 Maintainability
- Code must adhere to clean coding principles, making documentation and future alterations straightforward.

## 8. Documentation

### 8.1 README.md
- Update the `README.md` to provide information about the new enrollment functionality and API interaction.

## 9. Deployment Considerations

### 9.1 Production Readiness
- Confirm that the application launches without issues, and the new `enrollments` table is created correctly, maintaining existing data.

## 10. Success Criteria
- Students can be successfully enrolled in courses.
- Courses are retrievable via the correct endpoints.
- Validation errors return meaningful messages.
- Comprehensive tests validate functionality and error handling.
- Documentation aligns with changes made and instructions for new features.

### Existing Code Files Modifications

**File: src/models.py**
- Add the `Enrollment` class to represent the join table between Students and Courses.

**File: src/services/enrollment_service.py**
- Implement the `enroll_student_in_course` and `get_courses_for_student` methods to manage the enrollment logic.

**File: src/api/routes.py**
- Create routes for enrollment management:
  - `POST /enrollments` for enrolling students.
  - `GET /students/<id>/courses` for retrieving courses for a specific student.

**File: tests/api/test_routes.py**
- Enhance tests to verify that enrollment can be created and that a student's courses can be retrieved correctly.

**File: tests/services/test_enrollment_service.py**
- Develop unit tests to assess the business logic for enrolling a student and returning course lists.

**Migration Strategy**
- Using `Flask-Migrate`, generate the migration scripts for adding necessary changes:
  
```bash
flask db migrate -m "Add enrollments table"
flask db upgrade
```

By adhering to this implementation plan, the team will effectively integrate the Course relationship into the existing Student entity, supporting better academic management, while ensuring integrity and clarity of the application structure.