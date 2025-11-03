# Implementation Plan: Add Teacher Relationship to Course Entity

---

## Version: 1.1.0  
**Purpose**: To enhance the existing application by establishing a relationship between the Course and Teacher entities, allowing better management of course assignments and educator responsibilities.

---

## I. Architecture Overview

The application continues to follow the MVC (Model-View-Controller) architecture with the following changes:

- **Model**: Add the `teacher_id` foreign key in the existing `Course` model to reference the new `Teacher` model.
- **Controller**: Create new API endpoints to manage assignments of teachers to courses.
- **View**: Remains unchanged, as this feature focuses on backend functionality.

### Technology Stack
- **Backend Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy
- **Testing Framework**: pytest
- **Documentation**: OpenAPI

---

## II. Application Structure

```plaintext
project-root/
├── src/
│   ├── main.py               # Entry point for FastAPI application, updated with new course-teacher routes
│   ├── models/                # Database models
│   │   ├── student.py         # Existing Student model definition
│   │   ├── course.py          # Modified Course model definition
│   │   └── teacher.py         # New Teacher model definition (from previous implementation)
│   ├── schemas/               # Pydantic schemas for validation
│   │   ├── student.py         # Existing Schema for Student input/output
│   │   ├── course.py          # Modified Schema for Course input/output (to include teacher_id)
│   │   └── teacher.py         # New Schema for Teacher input/output
│   ├── services/              # Business logic layer
│   │   ├── student_service.py  # Existing logic for managing students
│   │   ├── course_service.py   # Updated logic for managing courses
│   │   └── teacher_service.py   # New logic for managing teachers
│   ├── db/                   # Database setup
│   │   ├── database.py        # Updated to include migrations and foreign key relationships
│   │   └── migrations/        # Folder for Alembic migration scripts
│   └── api/                  # API routes
│       ├── student_routes.py   # Existing routes for student-related endpoints
│       ├── course_routes.py     # Updated routes for course management
│       └── teacher_routes.py     # New routes for teacher management
├── tests/                     # Test suite
│   ├── test_student.py        # Existing unit tests for student-related functionalities
│   ├── test_course.py         # Updated tests for course management
│   └── test_teacher.py        # New tests for teacher-related functionalities
├── requirements.txt           # Project dependencies - ensure it reflects any updated package versions
├── .env.example               # Example environment configuration
└── README.md                  # Project documentation, updated with information for new teacher-course assignments
```

---

## III. Data Model

### Course Entity Modification
```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.db.database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))  # Foreign key reference to Teacher
    
    # Relationship with Teacher
    teacher = relationship("Teacher", back_populates="courses")

    def __repr__(self):
        return f"<Course(id={self.id}, name={self.name}, teacher_id={self.teacher_id})>"
```

### Teacher Entity (for reference)
The `Teacher` entity remains the same as previously defined:
```python
from sqlalchemy import Column, Integer, String
from src.db.database import Base

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    courses = relationship("Course", back_populates="teacher")

    def __repr__(self):
        return f"<Teacher(id={self.id}, name={self.name}, email={self.email})>"
```

### Database Migration Strategy
1. Utilize Alembic to create a migration script that modifies the `courses` table to include the `teacher_id` foreign key.
2. Make sure that this migration does not disrupt existing data by correctly incorporating the new column and properly configuring constraints.

```bash
alembic revision --autogenerate -m "Add teacher_id to course table"
alembic upgrade head
```

---

## IV. API Contracts

### New Endpoints
1. **Assign a Teacher to a Course**
   - **Endpoint**: `POST /courses/{course_id}/assign_teacher`
   - **Request Body**:
     ```json
     {
       "teacher_id": 1
     }
     ```
   - **Response** (200 OK):
     ```json
     {
       "message": "Teacher assigned successfully."
     }
     ```

2. **Retrieve Courses for a Specific Teacher**
   - **Endpoint**: `GET /teachers/{teacher_id}/courses`
   - **Response** (200 OK):
     ```json
     {
       "courses": [
         {
           "id": 1,
           "name": "Mathematics",
           "teacher_id": 1
         },
         ...
       ]
     }
     ```

### Error Responses
- Invalid Teacher ID Assignment:
```json
{
  "error": {
    "code": "E002",
    "message": "Teacher not found.",
    "details": {}
  }
}
```

---

## V. Implementation Approach

### 1. Database Initialization
- Update `database.py` to include the necessary operations that facilitate foreign key linkage between the `courses` and `teachers` tables.

### 2. API Development
- In `course_routes.py`, create the new endpoint for assigning a teacher to a course by updating the `@router` object to handle the `POST /courses/{course_id}/assign_teacher`.
- In the same file, implement the retrieval of courses by a teacher using the `GET /teachers/{teacher_id}/courses` endpoint.

### 3. Update Business Logic
Add relevant functions in `course_service.py` to manage the logic of assigning a teacher and retrieving courses.

### 4. Testing
- Create a test suite for the new features in `test_course.py`:
  - Ensure assignments can successfully link courses with teachers.
  - Confirm courses can be retrieved correctly for any given teacher.
  - Validate proper error handling for invalid inputs.

```python
def test_assign_teacher(client):
    response = client.post("/courses/1/assign_teacher", json={"teacher_id": 1})
    assert response.status_code == 200
    assert response.json() == {"message": "Teacher assigned successfully."}

def test_get_courses_for_teacher(client):
    response = client.get("/teachers/1/courses")
    assert response.status_code == 200
    assert isinstance(response.json()["courses"], list)
```

---

## VI. Security Considerations
- Ensure all endpoints are protected and only accessible by admin users using middleware for authorization checks.

---

## VII. Performance Considerations
- Optimize the retrieval of courses to be efficient, especially when querying related entities by using eager loading when appropriate.

---

## VIII. Documentation
- Update OpenAPI specifications to reflect the new routes and schemas concerning course-teacher relationships.
- Revise `README.md` accordingly to document how to utilize the new API features for proper onboarding of developers.

---

## IX. Development and Deployment
- Update `requirements.txt` to include Alembic for database migrations if it is not already present.
- Confirm that all migration scripts related to the `teacher` and `course` models are tracked and documented in Git.

---

## X. Success Criteria
- All defined API operations should respond as expected under both valid and invalid scenarios.
- The database schema should reflect the new foreign key relationship without data loss.
- Unit tests for both functionalities should cover the minimum requirements outlined.

---

## XI. Trade-offs and Decisions
- **Database Modification**: Adding a foreign key constraint strengthens data integrity but requires migration planning to avoid downtime.
- **API Updates**: By extending existing routes instead of creating new ones, we maintain a cleaner API structure while enhancing functionality related to course management.

---

This implementation plan effectively translates the business requirements into a viable technical strategy, ensuring that all aspects of integrating the teacher relationship into the course entity are covered thoroughly.