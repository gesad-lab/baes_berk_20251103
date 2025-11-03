# src/docs/api_documentation.md

# API Documentation

## User Scenarios & Testing

1. **Creating a Student with Email**: A user wants to create a new student. They send a request with the student's name and email address, and receive a confirmation response with the created student's data.
   - **Test**: Send a POST request with valid student details (name and email) and verify the response includes the correct student data and status code (201 Created).

   ### Create Student
   - **HTTP Method**: POST
   - **URI**: `/students`
   - **Request Body**: 
     ```json
     {
       "name": "John Doe",  // required
       "email": "john.doe@example.com"  // required, must be a valid email format
     }
     ```
   - **Response**: 
     ```json
     {
       "id": 1,
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```
   - **Status Code**: 201 Created

2. **Retrieving a Student with Email**: A user wants to view a student's details, including their email. They send a request with the student's ID and receive the student's information.
   - **Test**: Send a GET request with a valid student ID and verify the response includes the correct student's name, email, and status code (200 OK).

   ### Retrieve Student
   - **HTTP Method**: GET
   - **URI**: `/students/{id}`
   - **Response**: 
     ```json
     {
       "id": 1,
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```
   - **Status Code**: 200 OK

3. **Updating a Student's Email**: A user wants to change a student's email. They send a request with the student ID and the new email address.
   - **Test**: Send a PUT request with the student's ID and new email, and verify the response includes the updated information and status code (200 OK).

   ### Update Student Email
   - **HTTP Method**: PUT
   - **URI**: `/students/{id}`
   - **Request Body**: 
     ```json
     {
       "email": "john.new.email@example.com"  // required, must be a valid email format
     }
     ```
   - **Response**: 
     ```json
     {
       "id": 1,
       "name": "John Doe",
       "email": "john.new.email@example.com"
     }
     ```
   - **Status Code**: 200 OK

4. **Creating a Student with Invalid Email**: A user tries to create a student with an invalid email format. They should receive an error response.
   - **Test**: Send a POST request with invalid email and verify the response status code (400 Bad Request).

   ### Invalid Email Example
   - **Request Body**: 
     ```json
     {
       "name": "Jane Doe",
       "email": "invalid-email"  // invalid email format
     }
     ```
   - **Expected Response**: 
     ```json
     {
       "error": {
         "code": "E001",
         "message": "Invalid email format"
       }
     }
     ```
   - **Status Code**: 400 Bad Request

---

## Functional Requirements
1. **Update Student Endpoint for Creating a Student**
   - Same as outlined above under the "Creating a Student with Email" section.

2. **Update Student Endpoint for Retrieving a Student**
   - Same as outlined above under the "Retrieving a Student with Email" section.

For further details on implementation, refer to the respective service and model files.