# Tasks: Add Email Field to Student Entity

---
INCREMENTAL DEVELOPMENT CONTEXT

Existing Code to Build Upon:
- Current implementation of Student entity and associated APIs without email field.

Instructions for Task Breakdown:
1. Identify which existing files need modifications.
2. Create new files for new functionality.
3. Ensure integration tasks are included.
4. Maintain consistency with existing code style and patterns.

---

## Tasks

### **1. Update Database Model**
- **File**: `src/models.py`
  - [ ] Modify the `Student` class to include the `email` attribute.
  ```python
  email = Column(String, nullable=False)  # Add this line
  ```

### **2. Create Migration Script**
- **File**: `migrations/versions/[timestamp]_add_email_to_student.py`  (Create New File)
  - [ ] Implement a migration that adds the `email` column to the students table, ensuring data integrity.

### **3. Update API Endpoints**
- **File**: `src/api.py`
  - [ ] Implement the `POST /students` endpoint to accept the new `email` field.
  - [ ] Implement the `PUT /students/{id}` endpoint to update the email field.

### **4. Update Error Handling**
- **File**: `src/errors.py`
  - [ ] Create centralized error handling to check for missing email and return appropriate error messages.
  
### **5. Write Unit Tests for New Functionality**
- **File**: `tests/test_api.py`
  - [ ] Write unit tests for the `POST /students` endpoint, focusing on the email field (valid and invalid cases).
  - [ ] Write unit tests for the `PUT /students/{id}` endpoint to test email updates.

### **6. Update Frontend Forms**
- **File**: `src/templates/student_form.html`  (or relevant file)
  - [ ] Modify the form to include an input field for the student's email address.
  
### **7. Add Frontend Validation**
- **File**: `src/js/student_form.js`  (or relevant file)
  - [ ] Implement JavaScript validation to ensure that the email field is not empty before submission.

### **8. Update README Documentation**
- **File**: `README.md`
  - [ ] Document the new API schemas, including how to create and update a student with an email.

### **9. Review Existing Tests for Coverage**
- **File**: `tests/conftest.py`  (or appropriate testing configuration file)
  - [ ] Ensure existing test configurations are updated to reflect the new functionality for full test coverage.

### **10. Run and Verify Migrations**
- **File**: Command Line Interface
  - [ ] Execute migration to ensure the database is updated without data loss.
  - [ ] Verify that the application starts without errors.

--- 

This breakdown creates independent, file-scoped tasks that adhere to the specified guidelines ensuring a methodical development approach for enhancing the Student entity with an email field. Each task is designed to be small, focused, and testable, facilitating an incremental feature addition.