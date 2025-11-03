# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models/student.py` (existing Student model)
- `src/api/student.py` (existing API routes for Student entity)
- `tests/test_student.py` (existing tests for Student API)

Instructions for Task Breakdown:
1. Identify which existing files need modifications.
2. Create new files for new functionality.
3. Ensure integration tasks are included.
4. Maintain consistency with existing code style and patterns.

---

## Task Breakdown

- [ ] **Task 1: Update Student Model**  
  **File**: `src/models/student.py`  
  **Description**: Modify the Student model to include the required email field.  
  **Code Change**:
  ```python
  class Student(Base):
      __tablename__ = "students"
  
      id = Column(Integer, primary_key=True, index=True)
      name = Column(String, nullable=False)
      email = Column(String, nullable=False, unique=True)  # Add email field
  ```

- [ ] **Task 2: Create Migration Script for Email Field**  
  **File**: `migrations/add_email_field.py`  
  **Description**: Create a migration script using Alembic to add the email field to the students table with backward compatibility.  
  **Code Change**:
  ```python
  def upgrade():
      op.add_column('students', sa.Column('email', sa.String(), nullable=False))
      op.create_unique_constraint('uq_email', 'students', ['email'])
  
  def downgrade():
      op.drop_column('students', 'email')
  ```

- [ ] **Task 3: Implement Create Student API Endpoint**  
  **File**: `src/api/student.py`  
  **Description**: Implement the POST /students endpoint to create a new student, accepting name and email in the request body.  
  **Code Change**:
  ```python
  @app.post("/students", response_model=StudentResponse)
  async def create_student(student: StudentCreate):
      ...
      # Implement input validation for email logic here
  ```

- [ ] **Task 4: Implement Retrieve Student API Endpoint**  
  **File**: `src/api/student.py`  
  **Description**: Add the GET /students/{id} endpoint to retrieve student details, including the email field.  
  **Code Change**:
  ```python
  @app.get("/students/{id}", response_model=StudentResponse)
  async def read_student(id: int):
      ...
  ```

- [ ] **Task 5: Validate Email Input**  
  **File**: `src/api/student.py`  
  **Description**: Create validation logic to ensure the email is present and properly formatted when creating a student.  
  **Code Change**:
  ```python
  # Implement regex email format validation
  if not re.match(r"[^@]+@[^@]+\.[^@]+", student.email):
      raise HTTPException(status_code=400, detail="Invalid email format")
  ```

- [ ] **Task 6: Update Tests for New Email Field**  
  **File**: `tests/test_student.py`  
  **Description**: Extend existing unit tests to cover scenarios for creating a student with and without an email.  
  **Code Change**:
  ```python
  def test_create_student_with_email():
      ...
      
  def test_create_student_without_email():
      ...
      
  def test_create_student_with_invalid_email():
      ...
  ```

- [ ] **Task 7: Update Test Integration**  
  **File**: `tests/test_integration.py`  
  **Description**: Add integration tests to verify that the API behaves correctly when creating and retrieving student data with the email field.  
  **Code Change**:
  ```python
  def test_integration_create_student():
      ...
      
  def test_integration_get_student():
      ...
  ```

- [ ] **Task 8: Update README for New Functionality**  
  **File**: `README.md`  
  **Description**: Document the new API endpoints, including the request and response formats for creating and retrieving students.  
  **Code Change**:
  ```markdown
  ### New Endpoints
  - **POST /students**: Create a new student with name and email.
  - **GET /students/{id}**: Retrieve a student's details including email.
  ```

- [ ] **Task 9: Initial Database Migration on Startup**  
  **File**: `src/main.py`  
  **Description**: Add migration handling in the FastAPI startup event to ensure migrations are executed on application startup.  
  **Code Change**:
  ```python
  @app.on_event("startup")
  async def startup():
      ...
      command.upgrade(alembic_cfg, "head")
  ```

---

Each task is small, file-scoped, and focused, allowing for independent testing and execution while following the project specifications and guidelines.