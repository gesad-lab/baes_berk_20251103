# README.md

## Overview & Purpose
The purpose of adding an email field to the existing Student entity is to improve the management capabilities of student records within the Student Management Web Application. By including a required email attribute, we enable better communication and record-keeping functionalities.

## Error Handling and Validation Updates

### Input Validation
- **Name**: The `name` field is required. If not provided, the user will receive an error message: 
  - `{"error": {"code": "E001", "message": "The name field is required."}}`

- **Email**: The `email` field is also required and must follow a valid email format. The system will return specific error messages based on the validation outcome:
  - If the email is missing, the error message will be: 
    - `{"error": {"code": "E002", "message": "The email field is required."}}`
  - If the email format is invalid, the error message will indicate the issue:
    - `{"error": {"code": "E003", "message": "Invalid email format."}}`

### API Responses
All responses from the API will be formatted in JSON to maintain consistency across different endpoints. For error situations, the error responses will follow the structure:
```json
{
  "error": {
    "code": "Exxx",
    "message": "Error message here."
  }
}
```

### User Scenarios & Testing
1. **Create Student Record with Email**: 
   - A user should be able to send a request to create a new student and include an email address.
   - When a valid name and email are provided, a new student record will be created successfully.

2. **Retrieve Student Record with Email**: 
   - A user should be able to fetch a student record and see the email address associated with the student.

3. **Invalid Student Record Creation Without Email**: 
   - Attempts to create a student record without an email address will result in an error response indicating the email field is required.

4. **Retrieve Invalid Email Format**: 
   - If a user attempts to create a student record with an incorrectly formatted email, the response will indicate the format is invalid.

### Technical Plan Updates
- Implement input validation for both `name` and `email` fields to ensure they are mandatory.
- Return meaningful error messages for any validation issues encountered in user requests, including both missing fields and incorrectly formatted emails.

By adhering to the updated error handling and validation procedures, we ensure a clearer and more user-friendly interaction with the Student Management Web Application.