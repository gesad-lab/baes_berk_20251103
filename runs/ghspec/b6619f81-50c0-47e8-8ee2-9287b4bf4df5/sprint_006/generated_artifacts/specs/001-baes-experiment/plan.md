# Implementation Plan: Add Teacher Relationship to Course Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Teacher Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
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
# Implementation Plan: Student Entity Management

## I. Architecture Overview

### 1.1 System Architecture
- Architecture Type: RESTful API
- Framework: Flask (Python web framework)
- Database: SQLite (for lightweight storage suited for initial development and testing)

### 1.2 Module Boundaries
- **API Module**: Handles HTTP requests related to the Course and Teacher entities and routes them to appropriate services.
- **Service Module**: Contains business logic for managing course assignments and teacher information.
- **Repository Module**: Manages direct interactions with the database for course and teacher data.
- **Model Module**: Defines the data model for the Course and Teacher entities.

## II. Technology Stack

| Component           | Technology                |
|---------------------|---------------------------|
| Web Framework       | Flask                     |
| ORM/Database        | SQLAlchemy with SQLite    |
| Testing Framework    | Pytest                    |
| API Documentation   | Flask-RESTful             |

## III. Data Models

### 3.1 Course Data Model
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))

    teacher = relationship("Teacher", back_populates="courses")

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)

    courses = relationship("Course", back_populates="teacher")

    def __repr__(self):
        return f"<Teacher(id={self.id}, name={self.name}, email={self.email})>"
```

## IV. API Contracts

### 4.1 API Endpoints

1. **Assign Teacher to Course**
   - **Endpoint**: `POST /courses/{course_id}/assign-teacher`
   - **Request Body**: 
     ```json
     {
       "teacher_id": "integer"
     }
     ```
   - **Response**: 
     ```json
     {
       "course_id": "integer",
       "teacher_id": "integer"
     }
     ```

2. **Retrieve Course Information Including Assigned Teacher**
   - **Endpoint**: `GET /courses/{course_id}`
   - **Response**: 
     ```json
     {
       "course_id": "integer",
       "name": "string",
       "level": "string",
       "teacher": {
         "teacher_id": "integer",
         "name": "string",
         "email": "string"
       }
     }
     ```

3. **Update Teacher Assignment for a Course**
   - **Endpoint**: `PUT /courses/{course_id}/update-teacher`
   - **Request Body**: 
     ```json
     {
       "teacher_id": "integer"
     }
     ```
   - **Response**: 
     ```json
     {
       "course_id": "integer",
       "teacher_id": "integer"
     }
     ```

### 4.2 Error Handling
- For all endpoints, return structured JSON error formats:
```json
{
  "error": {
    "code": "E001",
    "message": "Invalid input: 'teacher_id' must be an integer."
  }
}
```

## V. Implementation Approach

### 5.1 Development Steps
1. **Set Up Project Structure**
   ```plaintext
   /course_management
   ├── src/
   │   ├── app.py        # Main application entry point
   │   ├── models.py     # Data model definitions (including Course and Teacher)
   │   ├── repositories/  # Database interactions related to Course and Teacher
   │   ├── services/      # Business logic for Course and Teacher management
   │   └── api.py         # API endpoints related to Course and Teacher management
   ├── tests/            # Automated tests
   ├── migrations/       # Migration scripts for schema changes
   ├── config.py         # Configuration settings
   └── requirements.txt   # List of dependencies
   ```

2. **Implement Database Migration**
   - Create migration script to add `teacher_id` foreign key to the `courses` table:
     ```python
     from alembic import op
     import sqlalchemy as sa

     def upgrade():
         op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id')))

     def downgrade():
         op.drop_column('courses', 'teacher_id')
     ```
   - Ensure that the migration preserves existing data in the `courses`, `students`, and `teachers` tables.

3. **Develop API Endpoints**
   - Utilize Flask to implement routes:
   ```python
   @app.route('/courses/<int:course_id>/assign-teacher', methods=['POST'])
   def assign_teacher(course_id):
       # Logic to assign teacher to course
       pass

   @app.route('/courses/<int:course_id>', methods=['GET'])
   def get_course(course_id):
       # Logic for retrieving course info including teacher
       pass

   @app.route('/courses/<int:course_id>/update-teacher', methods=['PUT'])
   def update_teacher(course_id):
       # Logic for updating assigned teacher for a course
       pass
   ```

4. **Setup Testing Framework**
   - Use Pytest to create unit and integration tests covering:
     - Assigning a teacher to a course.
     - Retrieving course information and associated teacher details.
     - Updates made to teacher assignments are reflected accurately.

### 5.2 Deployment Readiness
- Ensure the application starts and runs without manual configuration.
- Add a `.env.example` file documenting required environment variables.
- Include comprehensive instructions in `README.md` for setup, running, and using the API.

## VI. Testing and Validation

### 6.1 Test Coverage Requirements
- Achieve a minimum test coverage of 70% for all features, ensuring that critical operations exceed 90%.

### 6.2 Testing Strategies
- **Unit Tests**: Validate service functions for managing course assignments and teacher information.
- **Integration Tests**: Verify complete flows through the API for assigning teachers, retrieving course information, and updating assignments.
- **Contract Tests**: Ensure API responses adhere to the specified contracts.

## VII. Security Considerations

- Leverage Flask’s built-in security features to safeguard against SQL Injection and XSS.
- Implement strict input validation for `teacher_id` and ensure only valid numeric IDs are accepted.
- Avoid logging sensitive data such as teacher emails.

## VIII. Performance Considerations

- As the number of courses and teachers grow significantly, consider implementing indexing on `teacher_id` for faster assignments retrieval.
- Investigate database connection pooling as application usage scales.

## IX. Documentation

### 9.1 API Documentation
- Use tools like Flask-RESTful for automatic API documentation generation, including routes and usage examples.

### 9.2 README.md Required
- Supply a step-by-step setup guide, API usage examples, and any migration instructions within the initial README file.

## X. Conclusion

This implementation plan details a structured approach to adding a teacher relationship to the existing Course entity within the educational system. By adhering to defined architecture, secure practices, and comprehensive testing strategies, we aim to enhance the system's capabilities while ensuring data integrity and backward compatibility with existing models.

### Existing Code Files Modifications

**File: src/models.py**
```python
# Update with the new relationship in the existing Course model

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    level = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))  # New field for teacher relationship

    teacher = relationship("Teacher", back_populates="courses")
```

**File: src/api.py**
```python
@app.route('/courses/<int:course_id>/assign-teacher', methods=['POST'])
def assign_teacher(course_id):
    """
    Assign a teacher to a course.

    Request JSON Body:
    - teacher_id (integer): The ID of the teacher to assign

    Returns the course ID along with the teacher ID in JSON format.
    """
    # Logic to assign teacher to the course
```

**File: src/api.py**
```python
@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    """
    Retrieve course information including the assigned teacher.

    Returns course details in JSON format, including teacher information.
    """
    # Logic for retrieving course info including teacher
```

Existing Code Files:
This implementation plan uses the same tech stack as previous sprints. It introduces new modules for handling the relationship between teachers and courses while maintaining backward compatibility with existing data models. The migration strategy is clearly outlined to ensure data integrity during model updates.