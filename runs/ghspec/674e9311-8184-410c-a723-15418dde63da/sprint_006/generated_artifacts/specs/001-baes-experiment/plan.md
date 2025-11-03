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
# Implementation Plan: Student Management Web Application

## Version
1.1.0

## Overview
This implementation plan outlines the architecture, technology stack, and implementation approach for establishing a relationship between the `Course` and `Teacher` entities within the educational management system. This will enhance course management capabilities, allowing for better course assignments and oversight.

## Architecture
The application will maintain a modular architecture, ensuring seamless integration of the Course-Teacher relationship without disrupting existing functionalities.

- **API Layer**: Handles incoming requests and responses related to course and teacher management.
- **Service Layer**: Contains business logic for assigning teachers to courses and retrieving course information.
- **Data Access Layer (DAL)**: Manages interactions related to the Course and Teacher entities.
- **Database Layer**: Updates the existing `Course` table to include a foreign key reference to the `Teacher` entity.

## Technology Stack
- **Language**: Python 3.11
- **Web Framework**: Flask
- **Database**: SQLite
- **Data Modeling**: SQLAlchemy ORM
- **API Documentation**: OpenAPI (Swagger)
- **Testing Framework**: pytest

## Module Boundaries and Responsibilities
1. **API Module** (`api.py`)
   - Implement new API endpoints for assigning a teacher to a course and viewing course details with assigned teacher information.

2. **Service Module** (`services/course_service.py`)
   - Encapsulate business logic for assigning teachers to courses and retrieving courses with teacher information.

3. **Data Access Module** (`models/course.py`)
   - Modify the `Course` entity to include the `teacher_id` foreign key.

4. **Configuration Module** (`config.py`)
   - No changes needed.

5. **Testing Module** (`tests/test_course.py`)
   - Implement tests for assigning teachers to courses and retrieving course details.

## Data Model and API Contracts

### Data Model
**Course Entity**
- `id`: Integer (auto-generated ID)
- `title`: String (not null)
- `description`: String
- `teacher_id`: Integer (nullable, foreign key referencing `Teacher.id`)

### API Endpoints
**1. Assign a Teacher to a Course**
- **Endpoint**: `PUT /courses/{courseId}/assign-teacher`
- **Request Body**:
   ```json
   {
     "teacher_id": "integer"
   }
   ```
- **Responses**:
   - **200 OK**: Successful assignment
     ```json
     {
       "message": "Teacher assigned successfully."
     }
     ```
   - **404 Not Found**: Teacher not found
     ```json
     {
       "error": {
         "code": "E003",
         "message": "Teacher not found."
       }
     }
     ```

**2. View Course with Assigned Teacher**
- **Endpoint**: `GET /courses/{courseId}`
- **Responses**:
   - **200 OK**: Course details with teacher information (if assigned)
     ```json
     {
       "id": "integer",
       "title": "string",
       "description": "string",
       "teacher": {
         "id": "integer",
         "name": "string"
       }
     }
     ```

## Implementation Approach

### Step-by-Step Implementation

1. **Setup Project Structure**
   - Maintain the existing project structure while adding necessary modifications to integrate the teacher relationship into the course entity.

2. **Modify Database Schema**
   - In `models/course.py`, update the `Course` entity definition to include the `teacher_id` foreign key:
   ```python
   from sqlalchemy import Column, Integer, String, ForeignKey
   from sqlalchemy.orm import relationship

   class Course(Base):
       """Model representing a Course with an optional associated Teacher."""
       
       __tablename__ = 'courses'
       
       id = Column(Integer, primary_key=True, autoincrement=True)
       title = Column(String, nullable=False)
       description = Column(String)
       teacher_id = Column(Integer, ForeignKey('teachers.id'), nullable=True)

       teacher = relationship("Teacher", back_populates="courses")

       def __init__(self, title: str, description: str, teacher_id: int = None):
           self.title = title
           self.description = description
           self.teacher_id = teacher_id
   ```

3. **Database Migration**
   - Implement a migration to alter the `courses` table to include the `teacher_id` column:
   ```python
   from alembic import op
   from sqlalchemy import Column, Integer, ForeignKey

   def upgrade():
       op.add_column('courses', Column('teacher_id', Integer, ForeignKey('teachers.id'), nullable=True))

   def downgrade():
       op.drop_column('courses', 'teacher_id')
   ```

4. **Develop API Module**
   - Update `api.py` to add handlers for the `PUT /courses/{courseId}/assign-teacher` and `GET /courses/{courseId}` endpoints. Example for assigning a teacher to a course:
   ```python
   from flask import Blueprint, request, jsonify
   from services.course_service import assign_teacher, get_course_with_teacher

   course_bp = Blueprint('course', __name__)

   @course_bp.route('/courses/<int:courseId>/assign-teacher', methods=['PUT'])
   def assign_teacher_endpoint(courseId):
       data = request.json
       try:
           assign_teacher(courseId, data['teacher_id'])
           return jsonify({"message": "Teacher assigned successfully."}), 200
       except KeyError:
           return jsonify({"error": {"code": "E001", "message": "teacher_id is required."}}), 400
       except ValueError as ve:
           return jsonify({"error": {"code": "E003", "message": str(ve)}}), 404

   @course_bp.route('/courses/<int:courseId>', methods=['GET'])
   def get_course_endpoint(courseId):
       course = get_course_with_teacher(courseId)
       return jsonify(course), 200
   ```

5. **Develop Service Layer**
   - In `services/course_service.py`, implement the logic for assigning teachers to courses and retrieving course details:
   ```python
   from models.course import Course
   from models.teacher import Teacher
   from sqlalchemy.orm import Session

   def assign_teacher(courseId: int, teacherId: int) -> None:
       course = db_session.query(Course).filter(Course.id == courseId).first()
       teacher = db_session.query(Teacher).filter(Teacher.id == teacherId).first()

       if not teacher:
           raise ValueError("Teacher not found.")
       
       if course:
           course.teacher_id = teacherId
           db_session.commit()
       else:
           raise ValueError("Course not found.")

   def get_course_with_teacher(courseId: int) -> dict:
       course = db_session.query(Course).filter(Course.id == courseId).first()
       if course:
           return {
               "id": course.id,
               "title": course.title,
               "description": course.description,
               "teacher": {
                   "id": course.teacher.id,
                   "name": course.teacher.name
               } if course.teacher else None
           }
       else:
           raise ValueError("Course not found.")
   ```

6. **Testing**
   - Create `tests/test_course.py` for testing the endpoints related to teacher assignment and course details:
   ```python
   import pytest
   from flask import Flask
   from src.api import create_app
   from models.course import Course  # Import Course model
   from models.teacher import Teacher  # Import Teacher model

   @pytest.fixture
   def app():
       app = create_app()
       app.config['TESTING'] = True
       return app

   def test_assign_teacher_to_course(client):
       # Create a course and teacher here for testing
       # Example:
       # teacher = Teacher(name="Jane Doe", email="jane@example.com")
       # course = Course(title="Calculus", description="Intro to Calculus")
       
       response = client.put('/courses/1/assign-teacher', json={"teacher_id": 1})
       assert response.status_code == 200
       assert response.get_json()['message'] == "Teacher assigned successfully."
   
   def test_assign_non_existent_teacher(client):
       response = client.put('/courses/1/assign-teacher', json={"teacher_id": 999})
       assert response.status_code == 404
       assert "Teacher not found." in response.get_json()['error']['message']

   def test_get_course_with_teacher(client):
       response = client.get('/courses/1')
       assert response.status_code == 200
       course_data = response.get_json()
       assert "teacher" in course_data
   ```

7. **Documentation**
   - Update API documentation to include new endpoints for assigning teachers to courses and viewing course details.
   - Adjust the `README.md` file to reflect usage instructions for the new features.

### Scalability, Security, and Maintainability Considerations
- **Scalability**: While the current SQLite setup is adequate for development, consider transitioning to a more robust database like PostgreSQL for production use.
- **Security**: Enhance input validation to prevent injection attacks and ensure data integrity. Ensure that sensitive information is never logged or exposed.
- **Maintainability**: Follow best practices for modularity and separation of concerns to facilitate future enhancements and bug fixes.

## Technical Trade-offs and Decisions
- We opted for SQLite for rapid prototyping and ease of use, but future scalability requirements may necessitate transitioning to a more powerful RDBMS.
- Using SQLAlchemy allows for abstraction over direct SQL queries, improving maintainability and allowing for database-agnostic development.

## Configuration Management
- No additional configuration management changes needed for the course-teacher assignment implementation.

## Logging & Monitoring
- Integrate structured logging to track assignment requests and any errors that occur in the teacher assignment process.

## Deployment Considerations
- Ensure that migration scripts are run during the deployment process to include the new foreign key relationship in the database schema.

## Future Enhancements
- Future enhancements might include the ability to change or remove assigned teachers from courses, or implementing alerts for courses without assigned teachers.

## Conclusion
This implementation plan lays out a clear path for establishing a relationship between `Courses` and `Teachers` within the educational management system, significantly enhancing its course management capabilities while adhering to established coding standards and practices.

### Existing Code Files: Modifications Needed
1. **Update File**: `models/course.py` - Add the `teacher_id` foreign key and relationship.
2. **Update File**: `api.py` - Add routes for teacher assignment to courses and fetching course details.
3. **New File**: `services/course_service.py` - Implement business logic for course-teacher assignments and retrieval.
4. **New File**: `tests/test_course.py` - Create tests for new functionalities related to course and teacher assignments.

### Existing Code Files
- **`models/__init__.py`**: No changes needed.
- **`api.py`**: Add imports and route registrations as outlined in the API Module section.

This plan allows for the smooth integration of teacher assignments into courses while ensuring all existing functionalities remain intact and operational.