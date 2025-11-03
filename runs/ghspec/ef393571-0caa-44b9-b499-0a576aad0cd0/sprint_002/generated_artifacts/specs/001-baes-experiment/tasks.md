# Tasks: Add Email Field to Student Entity

---

INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- The existing FastAPI application and SQLite database structure for managing Student entities.

Instructions for Task Breakdown:
1. Identify which existing files need modifications:
   - `src/models/student.py`
   - `src/api/student.py`
   - `migrations/` (for database migration)
   - `README.md`
   - `tests/api/test_student.py`
  
2. Create new files for new functionality: 
   - No new files required, modifications suffice.

3. Ensure integration tasks are included:
   - Update API contracts with new endpoints and request/response structures.
   - Implement database migration to preserve existing data and integrate email functionality.

4. Maintain consistency with existing code style and patterns.

---

## Task Breakdown

### Database Migration Tasks
- [ ] **Task 1**: Update the database schema to include the email field for the Student entity.
    - **File**: `migrations/migrate_students.py`
    - **Description**: Implement a migration strategy that alters the Student table to add the email column.
    - **Code**:
      ```python
      import aiosqlite

      async def migrate():
          async with aiosqlite.connect("students.db") as db:
              await db.execute("ALTER TABLE students ADD COLUMN email TEXT NOT NULL UNIQUE")
              await db.commit()
      ```

### Pydantic Model Tasks
- [ ] **Task 2**: Update the Pydantic model for Student creation and response to include the email field.
    - **File**: `src/models/student.py`
    - **Description**: Modify the existing models to validate the new email field using Pydantic.
    - **Code**:
      ```python
      from pydantic import BaseModel, EmailStr, constr

      class StudentCreate(BaseModel):
          name: constr(min_length=1)  # Required field
          email: EmailStr  # New field with validation for email format

      class StudentResponse(BaseModel):
          id: int
          name: str
          email: str  # Return email field in response
      ```

### API Endpoint Tasks
- [ ] **Task 3**: Update the POST API endpoint to handle the new email field.
    - **File**: `src/api/student.py`
    - **Description**: Modify the logic to accept an email in the payload when creating a new student and ensure valid data insertion.
    - **Code**:
      ```python
      from fastapi import FastAPI, HTTPException
      from .models.student import StudentCreate, StudentResponse

      @app.post("/students", response_model=StudentResponse)
      async def create_student(student: StudentCreate):
          # Logic to add the student while ensuring email uniqueness and validation
      ```

- [ ] **Task 4**: Update the GET API endpoint to return email information for all students.
    - **File**: `src/api/student.py`
    - **Description**: Ensure the API retrieves and includes email in the student data response.
    - **Code**:
      ```python
      @app.get("/students", response_model=List[StudentResponse])
      async def get_students():
          # Logic to retrieve all student data, including emails
      ```

### Testing Tasks
- [ ] **Task 5**: Write unit tests for the scenarios of adding a student with valid and invalid email formats.
    - **File**: `tests/api/test_student.py`
    - **Description**: Implement unit tests to ensure new email functionality and validation logic work properly.
    - **Code**:
      ```python
      def test_student_creation_invalid_email(client):
          response = client.post("/students", json={"name": "Test Student", "email": "not-an-email"})
          assert response.status_code == 400
          assert response.json()["error"]["code"] == "E002"  # Assuming E002 for invalid email format
      ```

### Documentation Tasks
- [ ] **Task 6**: Update the README.md file to reflect changes related to the new email field in API functionality.
    - **File**: `README.md`
    - **Description**: Document the new endpoint and the expected request/response structure including email requirements.
   
### Final Integration Tasks
- [ ] **Task 7**: Ensure the application runs successfully with the new changes and migrations are applied seamlessly.
    - **File**: N/A
    - **Description**: Perform final integration testing to validate that all changes are functional and that no existing features were broken.

---

By breaking down the implementation of the email field for the Student entity into these actionable tasks, we can maintain clarity and focus, ensuring each part of the implementation is thoroughly tested and integrated.