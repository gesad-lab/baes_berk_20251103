# Implementation Plan: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Previous Sprint Plan:
# Implementation Plan: Create Course Entity

---

## Version: 1.1.0  
**Purpose**: To extend the capabilities of the existing application by establishing a relationship between students and courses through an Enrollment entity, allowing for better tracking of student academic records.

---

## I. Architecture Overview

The application continues to adhere to the MVC (Model-View-Controller) architecture with the following changes:

- **Model**: Introduce a new `Enrollment` model to create a many-to-many relationship between `Student` and `Course`.
- **Controller**: Add new API endpoints to handle enrollment functions.
- **View**: Remains unchanged as the application is API-focused.

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
│   ├── main.py               # Entry point for FastAPI application, with new imports for Enrollment routes
│   ├── models/                # Database models
│   │   ├── student.py         # Existing Student model definition
│   │   ├── course.py          # Existing Course model definition
│   │   └── enrollment.py      # New Enrollment model definition
│   ├── schemas/               # Pydantic schemas for validation
│   │   ├── student.py         # Existing Schema for Student input/output
│   │   ├── course.py          # Existing Schema for Course input/output
│   │   └── enrollment.py      # New Schema for Enrollment input/output
│   ├── services/              # Business logic layer
│   │   ├── student_service.py  # Existing logic for managing students
│   │   ├── course_service.py   # Existing logic for managing courses
│   │   └── enrollment_service.py# New logic for managing enrollments
│   ├── db/                   # Database setup
│   │   └── database.py        # Update to include Enrollment model and migrations, also updated with foreign key constraints
│   └── api/                  # API routes
│       ├── student_routes.py   # Existing routes for student-related endpoints
│       ├── course_routes.py     # Existing routes for course management
│       └── enrollment_routes.py  # New routes for enrollment management
├── tests/                     # Test suite
│   ├── test_student.py        # Existing unit tests for student-related functionalities
│   ├── test_course.py         # Existing unit tests for course-related functionalities
│   └── test_enrollment.py     # New tests for enrollment-related functionalities
├── requirements.txt           # Project dependencies, ensure to reflect any new dependencies
├── .env.example               # Example environment configuration
└── README.md                  # Project documentation, updated with instructions for new feature
```

---

## III. Data Model

### Enrollment Entity
```python
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.db.database import Base

class Enrollment(Base):
    __tablename__ = 'enrollment'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)

    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

    def __repr__(self):
        return f"<Enrollment(student_id={self.student_id}, course_id={self.course_id})>"
```

### Database Migration Strategy
1. Use Alembic to generate a migration script that defines the new `enrollment` table and its fields (`student_id` and `course_id`).
2. Migrate the database by running the migration scripts to add the `enrollment` table while keeping the existing Student and Course tables intact.

---

## IV. API Contracts

### New Endpoints
1. **Enroll a Student in a Course**
   - **Endpoint**: `POST /students/{id}/enroll`
   - **Request Body**:
     ```json
     {
       "course_id": 1
     }
     ```
   - **Response** (200 OK):
     ```json
     {
       "message": "Student enrolled successfully."
     }
     ```

2. **Retrieve a Student's Courses**
   - **Endpoint**: `GET /students/{id}/courses`
   - **Response** (200 OK):
     ```json
     [
       {
         "id": 1,
         "name": "Introduction to Programming",
         "level": "Beginner"
       },
       ...
     ]
     ```

3. **De-enroll a Student from a Course**
   - **Endpoint**: `DELETE /students/{studentId}/courses/{courseId}`
   - **Response** (204 No Content): No content in response body.

### Error Responses
- For invalid requests or errors:
  ```json
  {
    "error": {
      "code": "E001",
      "message": "Student not found.",
      "details": {}
    }
  }
  ```

---

## V. Implementation Approach

### 1. Database Initialization
- Update `database.py` to include the new Enrollment model for creating a many-to-many relationship between students and courses.

### 2. API Development
- Create `enrollment_routes.py` to handle incoming requests related to course enrollments.
- Develop logic in `enrollment_service.py` to encapsulate the business logic for enrolling and de-enrolling students from courses.

### 3. Schemas Modification
Add validation schemas in a new `enrollment.py` file under `schemas`:
```python
from pydantic import BaseModel

class EnrollmentCreate(BaseModel):
    course_id: int

class EnrollmentResponse(BaseModel):
    message: str
```

### 4. Update existing files
- Import the new enrollment routes in `main.py` and include them in the FastAPI application:
```python
from src.api.enrollment_routes import router as enrollment_router
app.include_router(enrollment_router)
```

### 5. Testing
- Implement unit tests in `test_enrollment.py` for:
  - Successful enrollment of a student in a course.
  - Successful retrieval of a student's courses.
  - Successful de-enrollment from a course.
  - Error handling for non-existent students and courses.
- Ensure that unit tests maintain at least 70% coverage of any new logic introduced for enrollments.

---

## VI. Security Considerations
- Validate all inputs for enrollment to prevent SQL injection and other attack patterns.
- Ensure appropriate API authentication and authorization to protect enrollment actions.

---

## VII. Performance Considerations
- Index the foreign keys in the `enrollment` table to optimize query performance as dataset size increases.

---

## VIII. Documentation
- Update OpenAPI documentation to include the new enrollment-related endpoints and their requirements.
- Revise `README.md` to include instructions for the new API endpoints.

---

## IX. Development and Deployment
- Update `requirements.txt` to reflect any new dependencies utilized for this feature (if any).
- Ensure all migration scripts are included in version control.

---

## X. Success Criteria
- The database schema will successfully include the new `enrollment` table without errors.
- All specified API endpoints should function correctly with expected responses.
- Maintain unit test coverage standards to validate enrollment feature functionality.

---

## XI. Trade-offs and Decisions
- **Schema Design**: Creating a separate `enrollment` table allows for flexibility in managing the many-to-many relationship while preserving existing data models.
- **Migration Complexity**: Using SQLite allows simple migrations; reliance on ORM capabilities diminishes the risk of direct manual SQL errors.

---

This structured implementation plan aims to effectively integrate the course relationship into the student entity within the existing application, ensuring that all specified requirements are met while maintaining system integrity and data consistency.