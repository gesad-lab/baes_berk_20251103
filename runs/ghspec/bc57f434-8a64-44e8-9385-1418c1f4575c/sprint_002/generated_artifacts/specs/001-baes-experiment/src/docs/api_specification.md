# Update the API Documentation

```
# API Specification

## User Scenarios & Testing

1. **Create a Student with Email**:
   - As a user, I want to create a new student by providing both a name and an email.
   - **Endpoint**: `POST /students`
   - **Request Body**:
     ```json
     {
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```
   - **Response**:
     - **201 Created**: If the student is created successfully. Returns the created student object.
     - **400 Bad Request**: If validation fails (e.g., missing fields).
   - **Test**: Send a POST request with a valid name and email, and verify that a student is created successfully with both fields.

2. **Get a Student**:
   - As a user, I want to retrieve the details of a specific student, including their email.
   - **Endpoint**: `GET /students/{student_id}`
   - **Response**:
     - **200 OK**: Returns the student object with details.
     ```json
     {
       "id": 1,
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```
     - **404 Not Found**: If the student ID does not exist.
   - **Test**: Send a GET request for an existing student ID and verify that the correct student details (name and email) are returned.

3. **Update a Student's Email**:
   - As a user, I want to update the email of an existing student.
   - **Endpoint**: `PUT /students/{student_id}`
   - **Request Body**:
     ```json
     {
       "email": "new.email@example.com"
     }
     ```
   - **Response**:
     - **200 OK**: If the email is updated successfully. Returns the updated student object.
     - **404 Not Found**: If the student ID does not exist.
     - **400 Bad Request**: If the new email format is invalid.
   - **Test**: Send a PUT request with a valid student ID and a new email, then verify that the student's email is updated correctly.

4. **Validation of Email Field**:
   - If I attempt to create a student without an email, I want to receive a clear error message indicating that the email is required.
   - **Endpoint**: `POST /students`
   - **Request Body**:
     ```json
     {
       "name": "Jane Doe"
     }
     ```
   - **Response**:
     - **400 Bad Request**: Returns a validation error indicating the email is required.
     ```json
     {
       "error": {
         "code": "E001",
         "message": "Email is required."
       }
     }
     ```
   - **Test**: Send a POST request without an email and verify that a validation error is returned.

5. **Error Handling for Invalid Email**:
   - If I provide an invalid format for the email, I want to receive a validation error.
   - **Endpoint**: `POST /students`
   - **Request Body**:
     ```json
     {
       "name": "John Doe",
       "email": "invalid-email-format"
     }
     ```
   - **Response**:
     - **400 Bad Request**: Returns a validation error indicating the email format is invalid.
     ```json
     {
       "error": {
         "code": "E002",
         "message": "Invalid email format."
       }
     }
     ```
   - **Test**: Send a POST request with an invalid email format and verify that a validation error is returned.
```