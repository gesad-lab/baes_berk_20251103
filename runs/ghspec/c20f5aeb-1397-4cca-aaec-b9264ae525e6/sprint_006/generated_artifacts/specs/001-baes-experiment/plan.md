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

## 1. Overview
This implementation plan outlines the necessary functionality to establish a relationship between the Course and Teacher entities within the Student Management Web Application. This feature will allow a single Teacher to be assigned to each Course, thereby enhancing the organization of course management.

## 2. Architecture

### 2.1. High-Level Architecture
- **Client**: HTTP client (e.g., Postman, curl) to interact with the API.
- **Server**: Flask web server providing REST API endpoints for managing Course and Teacher entities.
- **Data Layer**: SQLite database managing Teacher and Course entities.

### 2.2. Component Diagram
```plaintext
+-------------+       +------------+       +------------------+
|   HTTP      | <---> |   Web      | <---> |      SQLite      |
|   Client    |       |   Server   |       |      Database    |
+-------------+       +------------+       +------------------+
```

## 3. Technology Stack
- **Programming Language**: Python
- **Web Framework**: Flask
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing Framework**: pytest
- **API Documentation**: Swagger (optional)

## 4. Modules and Responsibilities

### 4.1. Module Structure
```
student_management/
│
├── src/
│   ├── app.py                     # Application entry point
│   ├── models.py                  # Database models including Course and Teacher
│   ├── schemas.py                 # Validation schemas for Course and Teacher data
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py              # API endpoint definitions
│   │   └── errors.py              # Custom error handling
│   ├── database.py                # Database setup, migration process
│   └── config.py                  # Configuration settings
│
├── tests/
│   ├── test_routes.py             # Tests for API routes including Course and Teacher functionality
│   └── test_models.py             # Tests for Course and Teacher data models
│
├── requirements.txt               # Python package dependencies
└── README.md                      # Project documentation
```

## 5. Data Models

### 5.1. Updated Course Model
#### 5.1.1. Course Model
```python
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)  # Required field
    description = Column(String)  # Optional field
    teacher_id = Column(Integer, ForeignKey('teachers.id'))  # New field for Teacher reference
    teacher = relationship("Teacher")  # Relationship to Teacher model
```

### 5.2. Updated Teacher Model
#### 5.2.1. Teacher Model
```python
class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Required field
    email = Column(String, nullable=False, unique=True)  # Required field, unique constraint
```

### 5.3. API Contracts

#### 5.3.1. Assign Teacher to Course
- **Endpoint**: `POST /courses/{course_id}/assign-teacher`
- **Request Body**: 
  ```json
  {
    "teacher_id": 1
  }
  ```
- **Response**:
  ```json
  {
    "message": "Teacher assigned to course successfully."
  }
  ```

#### 5.3.2. Retrieve Course with Teacher Details
- **Endpoint**: `GET /courses/{course_id}`
- **Response**:
  ```json
  {
    "id": 1,
    "title": "Mathematics",
    "description": "Introduction to Mathematics",
    "teacher": {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
  }
  ```

## 6. Implementation Steps

### 6.1. Application Initialization
1. **Modify `models.py`:**
   - Extend the Course model to include the `teacher_id` field and relationship to the Teacher model.

### 6.2. API Endpoint Implementation
1. **Modify `routes.py`:**
   - **Add `assign_teacher_to_course(course_id)`** for `POST /courses/{course_id}/assign-teacher`:
     - Validate the `teacher_id` to ensure it corresponds to a valid Teacher.
     - On success, update the Course record with the `teacher_id` and return a confirmation message.

   - **Enhance `get_course(course_id)`** for `GET /courses/{course_id}`:
     - Modify the retrieval logic to fetch and return associated Teacher details alongside Course information.

### 6.3. Input Validation
- Utilize schemas (e.g., Marshmallow) to validate that `teacher_id` is present and corresponds to a valid Teacher. Return a 400 status code with relevant error messages for any validation failures.

### 6.4. Database Migration Strategy
1. **Create Migration Script** with Alembic:
   - Add `teacher_id` to the `courses` table without disrupting existing records.

#### Migration Script Example
```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column('courses', sa.Column('teacher_id', sa.Integer, sa.ForeignKey('teachers.id')))

def downgrade():
    op.drop_column('courses', 'teacher_id')
```

### 6.5. Testing Strategy
1. **Update `test_routes.py`:**
   - Add tests for assigning a Teacher to a Course:
     - `test_assign_teacher_to_course_success()`: Ensure success with valid data.
     - `test_assign_teacher_invalid_id()`: Ensure graceful handling with invalid Teacher ID.

   - Modify tests for retrieving Course details to include Teacher information.

2. **Update `test_models.py`:**
   - Include tests to verify Course-Teacher relationships and constraints are maintained appropriately.

### Existing Code Files for Modification
**File: tests/test_routes.py**
```python
def test_assign_teacher_to_course_success(client):
    """Test successful assignment of a Teacher to a Course."""
    # First create a Teacher for the test
    teacher_response = client.post('/teachers', json={"name": "John Doe", "email": "john.doe@example.com"})
    assert teacher_response.status_code == 200
    teacher_id = teacher_response.get_json()['id']

    # Create a Course for assignment
    course_response = client.post('/courses', json={"title": "Mathematics", "description": "Intro Math"})
    assert course_response.status_code == 200
    course_id = course_response.get_json()['id']
    
    # Assign Teacher to Course
    response = client.post(f'/courses/{course_id}/assign-teacher', json={"teacher_id": teacher_id})
    assert response.status_code == 200
    assert response.get_json()['message'] == "Teacher assigned to course successfully."

def test_assign_teacher_invalid_id(client):
    """Test that assigning a Teacher with invalid ID handles error correctly."""
    response = client.post('/courses/1/assign-teacher', json={"teacher_id": 999})
    assert response.status_code == 400
    assert "Invalid teacher id" in response.get_json()['error']['message']
```

**File: tests/test_models.py**
```python
def test_course_teacher_relationship():
    """Test that Course can be associated with a Teacher."""
    teacher = Teacher(name="Jane Doe", email="jane.doe@example.com")
    db.session.add(teacher)
    db.session.commit()
    
    course = Course(title="History", description="World History", teacher_id=teacher.id)
    db.session.add(course)
    db.session.commit()

    assert course.teacher_id == teacher.id
    assert course.teacher.name == "Jane Doe"
```

## 7. Scalability and Security Considerations
- **Scalability**: The updated implementation facilitates future extensions, such as allowing multiple Teachers per Course.
- **Security**: Input validation for teacher IDs prevents injection attacks and ensures data integrity. Log any invalid access attempts for monitoring.

## 8. Configuration Management
- Update `.env.example` to reflect any new configuration options required for the Course-Teacher functionality.

## 9. Deployment Considerations
- Ensure migration scripts are executed as part of the deployment process.
- Perform integration tests post-deployment to validate new API functionalities work as expected.

## 10. Summary of Trade-offs
- **Increased Complexity**: Introduction of a new foreign key and relationship logic requires diligent testing and validation to maintain integrity.
- **Validation Overhead**: Improved data integrity through enhanced validation mechanisms will offset the slight increase in request processing times.

## 11. Success Criteria Validation
- Performance standards require response times for the new endpoints to remain under 2 seconds.
- Any invalid `teacher_id` input must return appropriate error messages.

## 12. Documentation
- Update API documentation in the code and include information about the new endpoints in `README.md` for clear guidance on usage.

This implementation plan aims to effectively extend the capabilities of the Student Management Web Application by enhancing the interplay between Course and Teacher entities, improving educational administration functionalities.
