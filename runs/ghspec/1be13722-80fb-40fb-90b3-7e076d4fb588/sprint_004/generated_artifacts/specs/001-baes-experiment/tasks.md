# Tasks: Add Course Relationship to Student Entity

---

## INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- tests/api/test_student.py 
- tests/services/test_student_service.py 

---

### Task Breakdown

#### 1. Update Student Model
- **Task**: Modify the existing Student model to include a relationship field for course associations.
- **File**: `/src/models/student.py`
- **Description**: Add a new field `course_ids` of type ARRAY(Integer) to handle associated course IDs.

  ```python
  from sqlalchemy import Column, Integer, String, ARRAY
  from database import Base

  class Student(Base):
      __tablename__ = 'students'
      
      id = Column(Integer, primary_key=True, autoincrement=True)
      name = Column(String, nullable=False)  # Existing field
      course_ids = Column(ARRAY(Integer), nullable=True)  # New relationship field
  ```
- [ ] Implement Student model changes

#### 2. Create Database Migration
- **Task**: Write a migration script to add `course_ids` field to the `students` table.
- **File**: `/src/database/migrations/xxxx_add_course_ids_to_students.py`
- **Description**: Create migration to add column `course_ids`.

  ```python
  from alembic import op
  import sqlalchemy as sa

  def upgrade():
      op.add_column('students', sa.Column('course_ids', sa.ARRAY(sa.Integer), nullable=True))

  def downgrade():
      op.drop_column('students', 'course_ids')
  ```
- [ ] Create migration script

#### 3. Implement API Endpoint for Course Association
- **Task**: Create PATCH endpoint to associate courses with students.
- **File**: `/src/api/student.py`
- **Description**: Define the route to handle the course association.

  ```python
  @router.patch("/students/{student_id}/courses", status_code=200)
  async def associate_course_endpoint(student_id: int, course: CourseAssociation):
      return await associate_course_with_student(student_id, course.course_id)
  ```
- [ ] Implement API endpoint for course association

#### 4. Implement API Endpoint for Retrieving Student Courses
- **Task**: Create GET endpoint to retrieve courses associated with a student.
- **File**: `/src/api/student.py`
- **Description**: Define the route for retrieving student courses.

  ```python
  @router.get("/students/{student_id}/courses", response_model=List[Course])
  async def retrieve_courses_endpoint(student_id: int):
      return await get_student_courses(student_id)
  ```
- [ ] Implement API endpoint for retrieving student courses

#### 5. Implement Business Logic for Course Association
- **Task**: Create business logic to handle course associations.
- **File**: `/src/services/student_service.py`
- **Description**: Define functions to associate courses and get courses for a student.

  ```python
  async def associate_course_with_student(student_id: int, course_id: int):
      # Logic to verify student, verify course exists, and associate.
      ...
  
  async def get_student_courses(student_id: int):
      # Logic to retrieve courses associated with a student.
      ...
  ```
- [ ] Implement business logic for handling course associations

#### 6. Develop Unit Tests for API Endpoints
- **Task**: Write tests for the new API functionalities in the testing suite.
- **File**: `/tests/api/test_student.py`
- **Description**: Create tests for endpoint success and failure cases.

  ```python
  def test_associate_course_success(client):
      ...
  
  def test_associate_course_invalid_student(client):
      ...
  
  def test_associate_course_invalid_id(client):
      ...
  ```
- [ ] Write API tests for course association and retrieval

#### 7. Develop Unit Tests for Business Logic
- **Task**: Write unit tests for the business logic in services.
- **File**: `/tests/services/test_student_service.py`
- **Description**: Create tests for course association service functions.

  ```python
  def test_associate_course_with_student():
      ...
  
  def test_get_student_courses():
      ...
  ```
- [ ] Write service tests for course association logic

#### 8. Update Documentation for New API Features
- **Task**: Document the new endpoints in OpenAPI/Swagger documentation.
- **File**: `/src/api/student.py`
- **Description**: Ensure that new API routes are properly documented.

  ```python
  # In the FastAPI app definition, ensure OpenAPI is updated to include new routes
  ```
- [ ] Update API documentation

---

This breakdown ensures each task is focused on a single file and can be independently tested. The tasks will ultimately lead to a robust solution for associating students with courses while maintaining existing patterns and styles.