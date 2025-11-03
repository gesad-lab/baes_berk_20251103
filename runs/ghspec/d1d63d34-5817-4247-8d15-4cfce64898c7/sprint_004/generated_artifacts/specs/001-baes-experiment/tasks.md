# Tasks: Add Course Relationship to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- tests/services/test_student_service.py (2591 bytes)

## Task Breakdown

### 1. Database Migration

- [ ] **Task 1: Create Migration Script**
   - **Description**: Generate a migration script to add the 'courses' column to the 'student' table.
   - **File**: `migrations/versions/add_courses_to_student.py`
   - **Code**:
   ```python
   """Add_courses_to_student

   Revision ID: xxx_revisions
   Revises: previous_revision_id
   Create Date: YYYY-MM-DD
   """
   from alembic import op
   import sqlalchemy as sa

   def upgrade():
       op.add_column('student', sa.Column('courses', sa.Text(), nullable=True))

   def downgrade():
       op.drop_column('student', 'courses')
   ```

### 2. Update Student Entity

- [ ] **Task 2: Update Student Class**
   - **Description**: Modify the Student class to include the courses attribute.
   - **File**: `src/models/student.py`
   - **Code**:
   ```python
   class Student(BaseModel):
       id: int
       name: str
       courses: List[int]  # New attribute to store related Course IDs
   ```

### 3. API Endpoints Implementation

- [ ] **Task 3: Implement Assign Courses to Student Endpoint**
   - **Description**: Create the POST endpoint to assign courses to a student.
   - **File**: `src/routes/student_routes.py`
   - **Code**:
   ```python
   @app.post("/students/{id}/courses")
   async def assign_courses_to_student(student_id: int, course_ids: List[int]):
       # Function implementation goes here
   ```

- [ ] **Task 4: Implement Get Courses of Student Endpoint**
   - **Description**: Create the GET endpoint to retrieve courses for a student.
   - **File**: `src/routes/student_routes.py`
   - **Code**:
   ```python
   @app.get("/students/{id}/courses")
   async def get_student_courses(student_id: int):
       # Function implementation goes here
   ```

- [ ] **Task 5: Implement Remove Course from Student Endpoint**
   - **Description**: Create the DELETE endpoint to remove a course from a student.
   - **File**: `src/routes/student_routes.py`
   - **Code**:
   ```python
   @app.delete("/students/{student_id}/courses/{course_id}")
   async def remove_course_from_student(student_id: int, course_id: int):
       # Function implementation goes here
   ```

### 4. CRUD Operations Implementation

- [ ] **Task 6: Implement assign_courses_to_student Function**
   - **Description**: Define the logic for assigning courses in the service layer.
   - **File**: `src/services/student_service.py`
   - **Code**:
   ```python
   def assign_courses_to_student(student_id: int, course_ids: List[int]) -> List[str]:
       # Function implementation goes here
   ```

- [ ] **Task 7: Implement get_student_courses Function**
   - **Description**: Define the logic for retrieving courses in the service layer.
   - **File**: `src/services/student_service.py`
   - **Code**:
   ```python
   def get_student_courses(student_id: int) -> List[Course]:
       # Function implementation goes here
   ```

- [ ] **Task 8: Implement remove_course_from_student Function**
   - **Description**: Define the logic for removing a course in the service layer.
   - **File**: `src/services/student_service.py`
   - **Code**:
   ```python
   def remove_course_from_student(student_id: int, course_id: int) -> None:
       # Function implementation goes here
   ```

### 5. Testing

- [ ] **Task 9: Write Tests for Assign Courses Endpoint**
   - **Description**: Create unit tests for the assign courses API endpoint.
   - **File**: `tests/services/test_student_service.py`
   - **Code**:
   ```python
   def test_assign_courses_to_student():
       response = client.post("/students/1/courses", json={"course_ids": ["course_id_1", "course_id_2"]})
       assert response.status_code == 201
       assert response.json()["message"] == "Courses assigned successfully."
   ```

- [ ] **Task 10: Write Tests for Get Courses Endpoint**
   - **Description**: Create unit tests for the get courses API endpoint.
   - **File**: `tests/services/test_student_service.py`
   - **Code**:
   ```python
   def test_get_student_courses():
       response = client.get("/students/1/courses")
       assert response.status_code == 200
       assert isinstance(response.json(), list)
   ```

- [ ] **Task 11: Write Tests for Remove Course Endpoint**
   - **Description**: Create unit tests for the remove course API endpoint.
   - **File**: `tests/services/test_student_service.py`
   - **Code**:
   ```python
   def test_remove_course_from_student():
       response = client.delete("/students/1/courses/course_id_1")
       assert response.status_code == 204  # No Content
   ```

### 6. Documentation

- [ ] **Task 12: Update API Documentation**
   - **Description**: Incorporate new endpoints and functionality in the README.md.
   - **File**: `README.md`
   - **Notes**: Ensure that newly added API endpoints are documented with expected requests and responses.

---

This plan breaks down the implementation of the Course relationship to the Student entity into small, manageable tasks that adhere to coding standards. Each task focuses on one specific area, ensuring independent testability and clear dependencies.