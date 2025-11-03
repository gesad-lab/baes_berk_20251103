# README.md

# Student Management Application

## Overview & Purpose

The Student Management Application is a simple web application designed for managing Student entities. Each Student has a single required field: name. The purpose of this application is to provide users with an intuitive interface to create and retrieve Student records while ensuring data persistence in a relational database.

## User Scenarios & Testing

1. **Creating a Student**:
   - **Scenario**: A user sends a request to create a new Student with a valid name.
   - **Test**: Verify that the student is created successfully and the correct JSON response is returned.

2. **Retrieving a Student**:
   - **Scenario**: A user requests the data of a specific Student by ID.
   - **Test**: Confirm that the correct Student details are returned in JSON format.

3. **Creating a Student with Missing Name**:
   - **Scenario**: A user attempts to create a Student without providing a name.
   - **Test**: Ensure the application returns a validation error indicating that the name is required.

4. **Retrieving a Non-Existent Student**:
   - **Scenario**: A user tries to retrieve a Student that does not exist.
   - **Test**: Verify that the application responds with a "Not Found" error.

## Functional Requirements

1. **Student Creation**:
   - **Endpoint**: `POST /students`
   - **Request Body**: 
     ```json
     {
       "name": "string" (required)
     }
     ```
   - **Response**: 
     - **Success (201 Created)**: 
       ```json
       {
         "id": "integer",
         "name": "string"
       }
       ```
     - **Error (400 Bad Request)**: 
       ```json
       {
         "error": {
           "code": "E001",
           "message": "Name is required."
         }
       }
       ```

2. **Retrieve Student by ID**:
   - **Endpoint**: `GET /students/{id}`
   - **Response**: 
     - **Success (200 OK)**: 
       ```json
       {
         "id": "integer",
         "name": "string"
       }
       ```
     - **Error (404 Not Found)**: 
       ```json
       {
         "error": {
           "code": "E002",
           "message": "Student not found."
         }
       }
       ```

## Setup Environment

To set up the environment, follow these steps:

1. Create a virtual environment:
   ```bash
   virtualenv venv
   ```

2. Activate the virtual environment:
   - For macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - For Windows:
     ```bash
     venv\Scripts\activate
     ```

3. Install necessary dependencies:
   ```bash
   pip install Flask SQLAlchemy
   ```

## Running the Application

To run the application, execute the following command:

```bash
python src/app.py
```

The application should start successfully without manual intervention.

## API Testing

You can test the API endpoints using Postman or any HTTP client of your choice. Endpoint details are provided in the Functional Requirements section.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

**Note**: Ensure that your database is properly configured before testing the application.

