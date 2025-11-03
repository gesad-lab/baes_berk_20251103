# Student Management API

## Overview
The purpose of this web application is to manage Student entities. Each Student entity will have a single required field: `name`. The application exposes an API for creating, retrieving, updating, and deleting Students. This feature can be beneficial for educational institutions or personal study tracking.

## User Scenarios
1. **Creating a Student**: Users can create a new student by sending a POST request with the student's name.
   - **Test**: Validate by sending a POST request with valid student details and checking for a confirmation response that includes the correct student data and status code (201 Created).

2. **Retrieving a Student**: Users can view a student's details by sending a GET request with the student's ID.
   - **Test**: Send a GET request with a valid student ID and verify that the response includes the correct student's name and status code (200 OK).

3. **Updating a Student**: Users can change a student's name by sending a PUT request with the student ID and the new name.
   - **Test**: Send a PUT request with the student's ID and new name, ensuring the response includes the updated information and status code (200 OK).

4. **Deleting a Student**: Users can remove a student from the system by sending a DELETE request with the student's ID.
   - **Test**: Validate by sending a DELETE request with a valid student ID and checking the response status code (204 No Content).

## API Endpoints

### 1. Create a Student
- **HTTP Method**: POST
- **URI**: `/students`
- **Request Body**: 
  ```json
  {
    "name": "string"  // required
  }
  ```
- **Response**: 
  ```json
  {
    "id": "integer",
    "name": "string"
  }
  ```
- **Status Code**: 201 Created

### 2. Retrieve a Student
- **HTTP Method**: GET
- **URI**: `/students/{id}`
- **Response**: 
  ```json
  {
    "id": "integer",
    "name": "string"
  }
  ```
- **Status Code**: 200 OK

### 3. Update a Student
- **HTTP Method**: PUT
- **URI**: `/students/{id}`
- **Request Body**:
  ```json
  {
    "name": "string"  // required
  }
  ```
- **Response**:
  ```json
  {
    "id": "integer",
    "name": "string"
  }
  ```
- **Status Code**: 200 OK

### 4. Delete a Student
- **HTTP Method**: DELETE
- **URI**: `/students/{id}`
- **Status Code**: 204 No Content

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/student-management-api.git
   ```
2. Change into the project directory:
   ```bash
   cd student-management-api
   ```
3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
To run the application, use the following command:
```bash
uvicorn main:app --reload
```
The application will be available at `http://localhost:8000`.

## Dependencies
- FastAPI: For building the API
- SQLAlchemy: For database operations
- Uvicorn: ASGI server to run the application

## Conclusion
This README provides an overview of the Student Management API, how to set up the application, and the available API endpoints.