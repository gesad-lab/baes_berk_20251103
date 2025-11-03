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
This implementation plan establishes a new relationship between the Student entity and the Course entity in the existing Student Management Web Application. The new feature will allow students to enroll in multiple courses, enhancing educational management and tracking capabilities.

## 2. Architecture

### 2.1. High-Level Architecture
- **Client**: HTTP client (e.g., Postman, curl) for API interaction.
- **Server**: Flask web server serving REST API endpoints for managing Student and Course relationships.
- **Data Layer**: SQLite database managing current Student and Course entities along with a new join table.

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
│   ├── app.py                     # Entry point for the application
│   ├── models.py                  # Database models including Student, Course, and StudentCourses
│   ├── schemas.py                 # Validation schemas for input data (including enrollment)
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py              # API endpoint definitions
│   │   └── errors.py              # Error handling and custom exceptions
│   ├── database.py                # Database setup, migration process
│   └── config.py                  # Configuration settings
│
├── tests/
│   ├── test_routes.py             # Tests for API routes including enrollment functionality
│   └── test_models.py             # Tests for data models including validations
│
├── requirements.txt               # Python package dependencies
└── README.md                      # Project documentation
```

## 5. Data Models

### 5.1. Updated Models

#### 5.1.1. Student Model
```python
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Required field
    courses = relationship('StudentCourses', back_populates='student')
```

#### 5.1.2. Course Model
```python
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Required field
    level = Column(String, nullable=False)  # Required field
```

#### 5.1.3. StudentCourses (Join Table)
```python
class StudentCourses(Base):
    __tablename__ = 'student_courses'

    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    student = relationship('Student', back_populates='courses')
    course = relationship('Course')
```

### 5.2. API Contracts

#### 5.2.1. Enroll Student in Course
- **Endpoint**: `POST /students/{student_id}/enroll`
- **Request Body**: 
  ```json
  {
    "course_ids": [1, 2, 3]
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "courses": [
      {"id": 1, "name": "Course 1", "level": "Beginner"},
      {"id": 2, "name": "Course 2", "level": "Intermediate"}
    ]
  }
  ```

#### 5.2.2. Retrieve Student Details
- **Endpoint**: `GET /students/{student_id}`
- **Response**:
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "courses": [
      {"id": 1, "name": "Course 1", "level": "Beginner"},
      {"id": 2, "name": "Course 2", "level": "Intermediate"}
    ]
  }
  ```

## 6. Implementation Steps

### 6.1. Application Initialization
1. **Extend the `models.py`** file with the new `StudentCourses` model as described above.
2. **Modify the database setup** to include this join table in the migration process.

### 6.2. API Endpoint Implementation
1. **Modify the `routes.py`** file to add the following functions:
   - `enroll_in_courses(student_id)` for `POST /students/{student_id}/enroll`:
     - Validate that `student_id` exists.
     - Validate each `course_id` exists.
     - On success, update the corresponding StudentCourses records and return updated student details.

   - `get_student_details(student_id)` for `GET /students/{student_id}`:
     - Fetch the specified Student and their enrolled courses.

### 6.3. Input Validation
- Use schemas to ensure that the `student_id` and `course_ids` are valid before processing requests. Return a 400 status code with an error message for validation failures.

### 6.4. Database Migration Strategy
1. Create a migration script using Alembic to add the new `student_courses` join table.
2. Ensure that existing Student and Course records are preserved and can reference each other through the join table.

#### Migration Script Example
```python
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table('student_courses',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
        sa.ForeignKeyConstraint(['course_id'], ['courses.id'], ),
        sa.PrimaryKeyConstraint('student_id', 'course_id')
    )
    
def downgrade():
    op.drop_table('student_courses')
```

### 6.5. Testing Strategy
1. Add new tests in `test_routes.py` for the enrollment endpoint to check:
   - Successful enrollment with valid course IDs.
   - Invalid student or course ID handling.

2. Add tests in `test_models.py` to verify the integrity of the new data model relationships.

### Existing Code Files for Modification
**File: tests/test_routes.py**
```python
def test_enroll_student_in_course(client):
    """Test that a student can be enrolled in valid courses."""
    response = client.post('/students/1/enroll', json={
        "course_ids": [1, 2, 3]
    })
    assert response.status_code == 200
    assert 'courses' in response.get_json()

def test_enroll_student_invalid_course(client):
    """Test enrolling a student in an invalid course returns error."""
    response = client.post('/students/1/enroll', json={
        "course_ids": [999]  # Non-existent course ID
    })
    assert response.status_code == 400
    assert response.get_json()['error']['message'] == "Invalid course IDs"
```

**File: tests/test_models.py**
```python
def test_student_courses_relation():
    """Test that Student and Course relationship is managed properly."""
    student = Student(name="John Doe")
    course1 = Course(name="Course 1", level="Beginner")
    course2 = Course(name="Course 2", level="Intermediate")

    student.courses.append(StudentCourses(course=course1))
    student.courses.append(StudentCourses(course=course2))
    
    assert len(student.courses) == 2
```

## 7. Scalability and Security Considerations
- **Scalability**: Design end-points to handle increasing numbers of students and courses efficiently.
- **Security**: Ensure proper validation of user input to avoid SQL injection; logs must be compliant with sensitivity principles.

## 8. Configuration Management
- The configuration will make use of environment variables for settings related to the database and app configurations.
- Update `.env.example` to ensure all new configuration options are documented.

## 9. Deployment Considerations
- Include migration scripts in the deployment package.
- Verify functionality through integration tests post-deployment.
- Document new API feature in `README.md`.

## 10. Summary of Trade-offs
- **Complexity of Integration**: Adding a join table does come with the potential for increased complexity in data handling; however, it is necessary for representing a many-to-many relationship.
- **Validation Overhead**: Adding validation logic can increase processing time but enhances reliability and user experience.

## 11. Success Criteria Validation
- Overall functionality must conform to performance standards (response within 2 seconds for both endpoints).
- Ensure appropriate error messages are delivered for invalid requests.

## 12. Documentation
- Update function docstrings and API documentation to outline new functionalities.
- Maintain clarity in `README.md` about endpoint usage, especially the new enrollment feature.

By following this implementation plan, the Student Management Web Application will successfully manage student enrollments in multiple courses, leading to improved educational management capabilities.