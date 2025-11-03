# README.md

# Project Title

## Description
This project provides a RESTful API to manage students, including their names and email addresses.

## User Scenarios & Testing

1. **Creating a Student with Email**: A user wants to create a new student. They send a request with the student's name and email address, and receive a confirmation response with the created student's data.
   - **Test**: Send a POST request with valid student details (name and email) and verify the response includes the correct student data and status code (201 Created).

2. **Retrieving a Student with Email**: A user wants to view a student's details, including their email. They send a request with the student's ID and receive the student's information.
   - **Test**: Send a GET request with a valid student ID and verify the response includes the correct student's name, email, and status code (200 OK).

3. **Updating a Student's Email**: A user wants to change a student's email. They send a request with the student ID and the new email address.
   - **Test**: Send a PUT request with the student's ID and new email, and verify the response includes the updated information and status code (200 OK).

4. **Creating a Student with Invalid Email**: A user tries to create a student with an invalid email format. They should receive an error response.
   - **Test**: Send a POST request with invalid email and verify the response status code (400 Bad Request).

## Functional Requirements

1. **Create Student Endpoint**
   - HTTP Method: POST
   - URI: `/students`
   - Request Body: 
     ```json
     {
       "name": "string",  // required
       "email": "string"  // required, must be a valid email format
     }
     ```
   - Response: 
     ```json
     {
       "id": "integer",
       "name": "string",
       "email": "string"
     }
     ```
   - Status Code: 201 Created

2. **Retrieve Student Endpoint**
   - HTTP Method: GET
   - URI: `/students/{id}`
   - Response: 
     ```json
     {
       "id": "integer",
       "name": "string",
       "email": "string"
     }
     ```
   - Status Code: 200 OK

3. **Update Student Endpoint**
   - HTTP Method: PUT
   - URI: `/students/{id}`
   - Request Body:
     ```json
     {
       "name": "string",
       "email": "string"  // required, must be a valid email format
     }
     ```
   - Response:
     ```json
     {
       "id": "integer",
       "name": "string",
       "email": "string"
     }
     ```
   - Status Code: 200 OK

## Configuration

Ensure the following configurations are set for proper functioning of email validation:

- The email field in the student model must conform to the standard email format. Adjust your database schema if necessary to accommodate these changes.

## Testing

All tests for the new email management feature are located in the `tests/api/test_student.py` and `tests/services/test_student_service.py` files. Run the tests to ensure proper functionality. 

## Installation

1. Clone the repository.
2. Install the required dependencies using pip.
3. Run the application using your preferred method.

## Usage

- Send requests to the `/students` endpoint to manage student data, including creating, retrieving, and updating student records.

### Contact

For any issues or inquiries, please contact the project maintainers.