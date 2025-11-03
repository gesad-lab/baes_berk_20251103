# README.md

# Project Title

This project is designed to manage student records, allowing for the storage and retrieval of student names and email addresses.

## API Specifications

### Endpoint: Create Student
- **POST /api/students**
- **Request Body**: 
    ```json
    {
      "name": "string",
      "email": "string"
    }
    ```
- **Validation**: 
    - The `name` field is required.
    - The `email` field must not be empty and must follow standard email format.
  
- **Response**:
  - **Success (201 Created)**:
    ```json
    {
      "message": "Student created successfully",
      "student": {
        "id": "integer",
        "name": "string",
        "email": "string"
      }
    }
    ```
  - **Error (400 Bad Request)**:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Email must not be empty."
      }
    }
    ```

### Frontend Validation
To ensure that the email field is validated appropriately before form submission, integrate the following JavaScript validation snippet:

```javascript
document.getElementById("student-form").addEventListener("submit", function(event) {
    const emailField = document.getElementById("email");
    if (!emailField.value.trim()) {
        event.preventDefault(); // Prevent form submission
        alert("Email must not be empty."); // Notify user
    }
});
```

This script adds an event listener to the form submission event, checks if the email field is empty, prevents the submission if it is, and alerts the user. 

## Database Migration

Ensure a migration script is present to:
- Add the `email` column to the `students` table.
- Confirm that existing student records remain intact after the update.

## Testing Requirements

- Coverage for email field functionalities should reach at least 70%, focusing on both creation and updates.
- Unit tests for the email validation method should be included.

### Future Enhancements
- Consider additional validations beyond this scope as future upgrades.

## Acknowledgments

Thank you for contributing to the student records management system!