# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- models.py
- main.py (API routes)

Instructions for Task Breakdown:
1. Identify which existing files need modifications
2. Create new files for new functionality
3. Ensure integration tasks are included
4. Maintain consistency with existing code style and patterns

---

### Task 1: Update Student Model to Include Email Field
- **File Path**: `src/models.py`
- **Description**: Modify the existing `Student` model to add an `email` field as a required, unique string.
- **Dependencies**: None
- **Testability**: Verify if adding the field keeps the current model structure intact and runs without errors.

```python
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)  # Added for email
```
- [ ] Update Student Model with Email Field

---

### Task 2: Implement Database Migration for Email Field
- **File Path**: `src/migrations/add_email_to_student.py`
- **Description**: Create a migration script to add the `email` column to the `students` table in the database while preserving existing data.
- **Dependencies**: Task 1
- **Testability**: Run migration and check if the email field is correctly added without data loss.

```python
# Example migration logic, adjust as necessary for your migration tool
def upgrade():
    op.add_column('students', sa.Column('email', sa.String(), nullable=False, unique=True))

def downgrade():
    op.drop_column('students', 'email')
```
- [ ] Implement Database Migration for Email Field

---

### Task 3: Update API Layer for Create Student Endpoint
- **File Path**: `src/main.py`
- **Description**: Modify the `/students` POST endpoint to handle the `email` field in the request body, ensuring validation is in place for required fields.
- **Dependencies**: Task 1
- **Testability**: Test the endpoint with valid and invalid requests for both name and email.

```python
@app.post("/students")
async def create_student(student: StudentCreate):
    # Validation and student creation logic with email
    pass
```
- [ ] Update API Layer for Create Student Endpoint

---

### Task 4: Update API Layer for Retrieve Student Endpoint
- **File Path**: `src/main.py`
- **Description**: Ensure the `/students/{id}` GET endpoint returns the email field along with other student data.
- **Dependencies**: Task 1
- **Testability**: Test the endpoint for various student IDs and validate the returned data includes the email.

```python
@app.get("/students/{id}")
async def get_student_by_id(id: int):
    # Logic to return student data including email
    pass
```
- [ ] Update API Layer for Retrieve Student Endpoint

---

### Task 5: Implement Validation for Email Field
- **File Path**: `src/validation.py`
- **Description**: Add input validation logic to ensure that the `email` field is required, a valid string format and enforce email uniqueness.
- **Dependencies**: Task 1
- **Testability**: Test the endpoint with various email formats to ensure proper validation.

```python
def validate_student_data(student_data):
    # Ensure email is present and valid
    pass
```
- [ ] Implement Validation for Email Field

---

### Task 6: Add Unit Tests for Student Creation
- **File Path**: `tests/test_main.py`
- **Description**: Write unit tests to cover scenarios for creating students, including valid and invalid email submissions.
- **Dependencies**: Tasks 3 and 5
- **Testability**: Ensure tests check correct API responses for various input conditions.

```python
def test_create_student_with_valid_email(client):
    # Test successful student creation
    pass

def test_create_student_missing_email(client):
    # Test error response for missing email
    pass
```
- [ ] Add Unit Tests for Student Creation

---

### Task 7: Add Unit Tests for Retrieving Students
- **File Path**: `tests/test_main.py`
- **Description**: Write unit tests to validate the functionality of retrieving student information, including email.
- **Dependencies**: Task 4
- **Testability**: Check that tests retrieve correct data for existing and non-existing student IDs.

```python
def test_get_student_by_id(client):
    # Test retrieving a student by id
    pass
```
- [ ] Add Unit Tests for Retrieving Students

---

### Task 8: Update Documentation in README.md
- **File Path**: `README.md`
- **Description**: Update the documentation to include information on the new email field, usage of the POST and GET endpoints, and example requests/responses.
- **Dependencies**: Tasks 3, 4 & 5
- **Testability**: Ensure that the README reflects all changes made in the API and examples work as intended.

```markdown
## API Endpoints

### Post Student
- **Endpoint**: `/students`
- **Body**: 
  ```json
  {
    "name": "string",
    "email": "string"
  }
  ```

### Get Student
- **Endpoint**: `/students/{id}`
```
- [ ] Update Documentation in README.md

---

### Task 9: Perform Integration Testing
- **File Path**: `tests/integration/test_student_integration.py`
- **Description**: Conduct integration tests to validate the entire flow of creating a student and retrieving their information.
- **Dependencies**: All prior tasks
- **Testability**: Ensure that integration tests pass and reflect realistic API interactions.

```python
def test_integration_student_flows(client):
    # Test the flow of creating and retrieving a student
    pass
```
- [ ] Perform Integration Testing

---

These tasks are structured to ensure independent execution and testing, while also adhering to the defined architecture and requirements for the new email functionality in the Student entity.