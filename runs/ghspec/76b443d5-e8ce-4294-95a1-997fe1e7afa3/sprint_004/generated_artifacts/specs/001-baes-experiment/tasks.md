# Tasks: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `tests/test_courses.py` (2222 bytes)

Instructions for Task Breakdown:
1. Identify which existing files need modifications
2. Create new files for new functionality
3. Ensure integration tasks are included
4. Maintain consistency with existing code style and patterns

---

## Task List

### Database Set-Up

- [ ] **Create Enrollment Model**  
  **File**: `src/models/enrollment.py`  
  Create a new file to define the `Enrollment` model to establish the many-to-many relationship.  
  ```python
  from sqlalchemy import Column, ForeignKey
  from sqlalchemy.orm import relationship
  from src.database import Base

  class Enrollment(Base):
      __tablename__ = "enrollments"

      student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
      course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

      student = relationship("Student", back_populates="courses")
      course = relationship("Course", back_populates="students")
  ```

- [ ] **Create Migration Script**  
  **File**: `migrations/versions/<timestamp>_add_enrollment_table.py`  
  Create a migration script to add the `enrollments` table to the database without losing existing data.  
  ```python
  def upgrade():
      op.create_table(
          'enrollments',
          sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), primary_key=True),
          sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'), primary_key=True)
      )

  def downgrade():
      op.drop_table('enrollments')
  ```

### API Development

- [ ] **Implement Enroll Student Endpoint**  
  **File**: `src/routes/student_routes.py`  
  Add a POST endpoint `/students/{studentId}/enroll` for enrolling a student in a course.  
  Ensure the enrollment logic handles course validation and returns the appropriate responses.

- [ ] **Implement Retrieve Student Courses Endpoint**  
  **File**: `src/routes/student_routes.py`  
  Add a GET endpoint `/students/{studentId}/courses` to retrieve all courses a student is enrolled in.  
  Ensure it responds correctly when a student is not found.

### Input Validation

- [ ] **Create Pydantic Model for Enrollment Request**  
  **File**: `src/schemas/enrollment.py`  
  Define Pydantic models for validating the request body of the enrollment endpoint.  
  ```python
  from pydantic import BaseModel

  class EnrollRequest(BaseModel):
      courseId: str
  ```

### Testing  

- [ ] **Create Tests for Enrollment Logic**  
  **File**: `tests/test_enrollments.py`  
  Implement tests for the new endpoints ensuring coverage for successful enrollments, erroneous enrollments (non-existing course), and missing course IDs.  
  Examples are provided in the existing code base.

- [ ] **Create Tests for Retrieving Courses**  
  **File**: `tests/test_enrollments.py`  
  Add tests to check the retrieval of courses for students, including cases where students do not exist.

### Documentation

- [ ] **Update API Documentation**  
  **File**: `README.md`  
  Update the project’s README file to include details about the new functionality, usage of the new endpoints, and examples of request and response formats.

- [ ] **Validate API Documentation with OpenAPI**  
  Ensure the automatically generated OpenAPI documentation via FastAPI reflects the enhancements made.

### Integration Tasks

- [ ] **Apply Database Migrations on Startup**  
  **File**: `src/main.py`  
  Update the FastAPI startup procedure to include the database migration command to ensure the latest changes are applied when the application starts.  
  ```python
  @app.on_event("startup")
  async def startup():
      alembic_cfg = Config("alembic.ini")
      command.upgrade(alembic_cfg, "head")  # Ensure latest migrations run on startup
  ```

## Conclusion

These tasks break down the implementation of adding a course relationship to the Student entity into manageable parts. Each task is designed to be independently executable and testable, ensuring a smooth development process adhering to the provided specifications and existing code standards.