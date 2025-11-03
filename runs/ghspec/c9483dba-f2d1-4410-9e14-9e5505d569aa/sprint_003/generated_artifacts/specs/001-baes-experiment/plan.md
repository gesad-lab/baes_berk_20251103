# Implementation Plan: Create Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Add Email Field to Student Entity

## Version
1.1.0

## Overview
This implementation plan outlines the architecture, technology stack, data models, API contracts, and implementation approach required for adding a new `Course` entity to the student management application. This addition will enhance the system's capabilities to manage educational programs effectively, providing a better structure for course-related data.

## Architecture

### 1.1 Application Architecture
- **Type**: RESTful web application
- **Design Pattern**: MVC (Model-View-Controller) for separation of concerns
- **Framework**: Flask (Python) for the backend
- **Database**: SQLite for local development, with integration via migration for schema changes.

### 1.2 Module Structure
1. **Models**:
   - New Course entity model defined to store course information.
   
2. **Controllers**:
   - Handlers for creating and retrieving courses.
   
3. **Routes**:
   - API endpoints that route requests to the appropriate controllers.

4. **Database Management**:
   - Logic for creating and migrating the database schema to include the new Course entity.

## Technology Stack
- **Backend Framework**: Flask
- **Database**: SQLite
- **ORM**: SQLAlchemy for database interactions
- **Request Validation**: Marshmallow for input validation and serialization
- **Testing Framework**: pytest for testing the application
- **Environment Management**: Python 3 and virtual environments

## Data Models

### 2.1 New Course Model
```python
from sqlalchemy import Column, Integer, String
from your_app.database import Base  # Adjust import based on actual structure

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)

    def __repr__(self):
        return f'<Course {self.id}: {self.name}, Level: {self.level}>'
```

### 2.2 Database Schema
The SQLite database will now include the following new table structure:
- **courses**
  - `id`: Integer (Primary Key, Auto-increment)
  - `name`: String (Non-nullable)
  - `level`: String (Non-nullable)

## API Contracts

### 3.1 Endpoints
1. **Create Course**
   - **Endpoint**: `POST /courses`
   - **Request Body**:
     ```json
     {
       "name": "Mathematics",
       "level": "Beginner"
     }
     ```
   - **Responses**:
     - **201 Created**:
       ```json
       {
         "id": 1,
         "name": "Mathematics",
         "level": "Beginner"
       }
       ```
     - **400 Bad Request** (if `name` or `level` is missing):
       ```json
       {
         "error": {
           "code": "E001",
           "message": "Name and Level are required"
         }
       }
       ```

2. **Retrieve Course**
   - **Endpoint**: `GET /courses/{id}`
   - **Responses**:
     - **200 OK**:
       ```json
       {
         "id": 1,
         "name": "Mathematics",
         "level": "Beginner"
       }
       ```
     - **404 Not Found** (if Course with given ID does not exist):
       ```json
       {
         "error": {
           "code": "E002",
           "message": "Course not found"
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
       │   ├── models.py       # New Course model to be added
       │   ├── controllers/
       │   │   ├── course_controller.py # New controller for Course entity
       │   └── database.py
       ├── migrations/         # New directory for migration scripts
       ├── tests/
       │   ├── test_app.py     # Create new tests for Course functionality
       └── README.md
   ```

2. **Database Migration**:
   - Utilize Flask-Migrate (which uses Alembic) for handling migrations.
   - Create a new migration script that adds the `courses` table:
     ```bash
     flask db migrate -m "Add Course entity to the database"
     flask db upgrade
     ```

3. **Route Definitions**:
   - Define new `POST /courses` and `GET /courses/{id}` routes in `app.py`:
     ```python
     @app.route('/courses', methods=['POST'])
     @app.route('/courses/<int:id>', methods=['GET'])
     ```

4. **Controller Logic**:
   - Implement logic in `course_controller.py` to handle creation and retrieval of courses, ensuring input validations for both `name` and `level`:
     ```python
     from flask import request, jsonify
     from models import Course, db  # Import appropriate components

     @app.route('/courses', methods=['POST'])
     def create_course():
         data = request.get_json()
         name = data.get('name')
         level = data.get('level')
         
         if not name or not level:
             return jsonify({"error": {"code": "E001", "message": "Name and Level are required"}}), 400
         
         course = Course(name=name, level=level)
         db.session.add(course)
         db.session.commit()
         return jsonify({"id": course.id, "name": course.name, "level": course.level}), 201

     @app.route('/courses/<int:id>', methods=['GET'])
     def get_course(id):
         course = Course.query.get(id)
         if not course:
             return jsonify({"error": {"code": "E002", "message": "Course not found"}}), 404
         return jsonify({"id": course.id, "name": course.name, "level": course.level}), 200
     ```

5. **Validation and Error Handling**:
   - Use Marshmallow for validation to ensure `name` and `level` are provided in the correct format before proceeding to create a Course.

6. **Testing**:
   - Create unit tests in `test_app.py` for both the creation and retrieval of courses.
   - Ensure a minimum of 70% coverage for this new functionality.

## Security Considerations
- Ensure input validation to avoid SQL injection and other potential attacks.
- Sanitize course inputs to mitigate risks related to injection attacks.

## Scalability Considerations
- The application starts with SQLite which suits development purposes but should be designed to migrate to a more robust database system (e.g., PostgreSQL) as the application scales.

## Conclusion
This implementation plan provides a clear roadmap for adding a `Course` entity to the student management application. Following this plan will ensure that existing functionality is preserved while delivering new capabilities, leading to a more robust and versatile application.

Existing Code Files:
- Update `src/models.py`, create `src/controllers/course_controller.py`, and add database migration files in the `migrations/` directory. 
- Create tests in `tests/test_app.py`.

Instructions for Technical Plan:
1. Utilize the same tech stack as previous sprints.
2. Document modifications to existing files (not replacements).
3. Ensure backward compatibility with existing data models.
4. Specify database migration strategy clearly to ensure data integrity during changes to the schema.