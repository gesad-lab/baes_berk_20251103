# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- `src/models/student.py`
- `src/api/student_routes.py`
- `migrations/versions/`

## Task Breakdown

### **Database Updates**
- [ ] **Task 1**: Add email column to the Student table schema  
  **File**: `migrations/versions/2023_add_email_column_to_students.py`  
  *Create a new migration script to add a non-nullable email field to the students table using Alembic.*

- [ ] **Task 2**: Run the database migration  
  **File**: `migrations/`  
  *Execute the migration script to update the database schema without losing existing student data.*

### **Model Module Updates**
- [ ] **Task 3**: Update the Student model to include email field  
  **File**: `src/models/student.py`  
  *Modify the SQLAlchemy Student class to include the email column, ensuring it's marked as required and is validated.*

- [ ] **Task 4**: Implement email validation method in the Student model  
  **File**: `src/models/student.py`  
  *Add a class method `validate_email` to the Student model to check for valid email formats using regex.*

### **API Module Updates**
- [ ] **Task 5**: Update the API endpoint for creating a Student  
  **File**: `src/api/student_routes.py`  
  *Modify the POST route to accept and handle the email field in the request body, and ensure it returns the email in the response.*

- [ ] **Task 6**: Update the API endpoint for retrieving a Student  
  **File**: `src/api/student_routes.py`  
  *Ensure the GET route returns the email field when responding with a Student's details.*

- [ ] **Task 7**: Update the API endpoint for updating a Student  
  **File**: `src/api/student_routes.py`  
  *Modify the PUT route to accept an email field in the request body and confirm that the email is updated in the response.*

### **Validation Module Updates**
- [ ] **Task 8**: Implement email validation for API requests  
  **File**: `src/validation/student_validation.py`  
  *Create or update validation logic to ensure incoming requests for creating or updating a Student include a valid email format.*

### **Testing**
- [ ] **Task 9**: Implement unit tests for Student model email validation  
  **File**: `tests/models/test_student.py`  
  *Add tests to validate email formats using the Student model's validation method.*

- [ ] **Task 10**: Implement integration tests for API endpoints  
  **File**: `tests/api/test_routes.py`  
  *Add tests that cover creating, retrieving, and updating Students with the email field, ensuring expected JSON responses and status codes are returned.*

- [ ] **Task 11**: Test for invalid email format responses  
  **File**: `tests/api/test_routes.py`  
  *Create tests for scenarios where invalid email formats are submitted to the API, ensuring 400 Bad Request responses are received.*

### **Documentation Updates**
- [ ] **Task 12**: Update API documentation to include email field  
  **File**: `docs/api_reference.md`  
  *Revise the documentation to include details on the new email field for Student entities, including requirements and expected JSON formats.*

- [ ] **Task 13**: Document migration instructions in README  
  **File**: `README.md`  
  *Add a section on migration instructions for updating the database schema.*

## Conclusion
These tasks provide a structured approach to implementing the new email field in the Student entity while ensuring all necessary components are updated, covered by tests, and documented accordingly. Each task is designed to be independently testable and aligns with the specified requirements.