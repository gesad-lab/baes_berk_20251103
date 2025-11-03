# Implementation Plan: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Student Management Web Application

## 1. Overview
The objective of this implementation plan is to detail the steps necessary to establish a many-to-many relationship between Student and Course entities within the existing Student Management Web Application. This feature will allow for better tracking and management of student enrollments in courses, thus enhancing the system’s educational tracking capabilities.

## 2. Architecture
The existing microservice architecture will be extended to include a junction table for managing the relationship between Student and Course entities.

### 2.1 Module Breakdown
- **Student Service**: Manages operations related to Student entities.
- **Course Service**: Handles operations related to Course entities and now also manages associations through the StudentCourses table.
- **Database Layer**: The database schema will be updated to include the junction table `StudentCourses`.
- **API Layer**: New API endpoints will be introduced for managing course assignments for students.

## 3. Tech Stack
- **Programming Language**: Python
- **Web Framework**: Flask
- **Database**: SQLite
- **ORM**: SQLAlchemy for database interactions
- **Request Handling**: Marshmallow for request validation and serialization
- **Testing Framework**: pytest for unit and integration testing

## 4. Implementation Approach

### 4.1 Database Schema
A new junction table `StudentCourses` will be created to establish the many-to-many relationship, which links students with the courses that they are enrolled in.

#### Updated Database Schema
- **Table**: StudentCourses
  - **Columns**:
    - `student_id`: INTEGER (foreign key referencing Student `id`)
    - `course_id`: INTEGER (foreign key referencing Course `id`)

#### Migration Strategy
- Use Flask-Migrate to handle the schema migration, ensuring the existing Student and Course data remains intact during this process.
- The migration will include creating the `StudentCourses` table as outlined above.

Example migration code using Flask-Migrate:
```python
from flask_migrate import Migrate, MigrateCommand
from manage import app, db
from models import StudentCourses  # Assume StudentCourses model is defined

migrate = Migrate(app, db)
```

### 4.2 API Endpoints
New API endpoints will be defined as follows:

1. **POST /students/{id}/courses**
   - **Purpose**: To assign courses to a student by their ID.
   - **Request Body**:
     ```json
     {
       "course_ids": [1, 2, 3]  // Array of course IDs to be assigned
     }
     ```
   - **Response**:
     - **Success (200 OK)**:
       ```json
       {
         "message": "Courses successfully assigned."
       }
       ```
     - **Error (400 Bad Request)**:
       ```json
       {
         "error": {
           "code": "E001",
           "message": "Invalid student ID."
         }
       }
       ```

2. **GET /students/{id}/courses**
   - **Purpose**: To retrieve all courses associated with a specific student ID.
   - **Response**:
     - **Success (200 OK)**:
       ```json
       {
         "courses": [
           {
             "id": 1,
             "name": "Mathematics 101",
             "level": "Beginner"
           }
         ]
       }
       ```

3. **DELETE /students/{id}/courses/{course_id}**
   - **Purpose**: To remove a specific course from a student’s enrollment.
   - **Response**:
     - **Success (204 No Content)**: No body content necessary.
     - **Error (404 Not Found)**:
       ```json
       {
         "error": {
           "code": "E002",
           "message": "Course not found for the specified student."
         }
       }
       ```

### 4.3 Functionality Implementation
- **Junction Model**: Create a SQLAlchemy model for `StudentCourses`:
  ```python
  class StudentCourses(db.Model):
      __tablename__ = 'student_courses'
      student_id = db.Column(db.Integer, db.ForeignKey('student.id'), primary_key=True)
      course_id = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)
  ```

- **Routes and Controllers**: Implement Flask routes to handle the logic for assigning, retrieving, and removing courses from students.
- **Example Route Implementation**:
  ```python
  @app.route('/students/<int:id>/courses', methods=['POST'])
  def assign_courses(id):
      data = request.get_json()
      course_ids = data.get("course_ids", [])
      for course_id in course_ids:
          association = StudentCourses(student_id=id, course_id=course_id)
          db.session.add(association)
      db.session.commit()
      return jsonify(message="Courses successfully assigned."), 200
  ```

### 4.4 Testing Strategy
- **Unit Tests**: Create unit tests for methods involving `StudentCourses`, including assigning, retrieving, and removing courses.
- **Integration Tests**: Validate that the API and database operate correctly together, ensuring that calls to endpoints perform as expected.
- Test coverage targets:
  - Minimum 70% coverage for business logic linked to course assignments.
  - 90%+ coverage for critical paths, especially those involving the management and retrieval of student course assignments.

## 5. Security Considerations
- Implement input validation to prevent against SQL injection.
- Ensure no sensitive data is logged, particularly student PII during course assignments and removals.

## 6. Error Handling & Validation
- Clear error messages will be returned when invalid operations are attempted:
  - Invalid student IDs.
  - Course enrollments that rely on non-existing course IDs.

Example error handling structure:
```python
if not student_exists(id):
    return jsonify(error={'code': 'E001', 'message': 'Invalid student ID.'}), 400
```

## 7. Deployment Considerations
- Before deployment, ensure local testing passes successfully.
- Flask-Migrate will handle the migration of schema changes without disrupting current functionality.
- Ensure that the application initializes correctly and that health checks are in place.

## 8. Documentation
- Update the API documentation to reflect the addition of `/students/{id}/courses` endpoints and their descriptions.
- Update `README.md` to include setup instructions relative to the new features.

## 9. Technical Trade-offs
- The decision to use SQLite continues due to its simplicity for the current scope, with future consideration for a more robust database storage solution as the application scales.
- Flask remains the web framework of choice due to its lightweight, performant nature and ease of use for rapidly developing RESTful APIs.

## 10. Success Metrics
- Confirm that all API operations related to course management for students operate successfully without errors.
- Verify the migration creates the new junction table without data loss.
- Ensuring that all features work seamlessly with existing student and course functionalities to maintain backward compatibility.

By following this comprehensive implementation plan, we will successfully establish a robust mechanism for associating courses with students, enhancing the overall functionality of the Student Management Web Application while preserving existing features.