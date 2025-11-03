# README.md

# Student Management API

## Overview

The Student Management API allows users to perform CRUD operations on student records. Users can create, retrieve, update, and delete student details, as well as list all students. This API is designed for ease of use and provides a straightforward way to manage student records.

## User Scenarios

1. **Create a Student**: A user can send a request to add a new Student with a name. The system should respond with the created Student's details.
2. **Get a Student**: A user can retrieve the details of a specific Student by their unique identifier.
3. **Update a Student**: A user can modify the name of an existing Student using their unique identifier.
4. **Delete a Student**: A user can remove a Student from the records using their unique identifier.
5. **List All Students**: A user can retrieve a list of all Students along with their details.

## Functional Requirements

### API Endpoints

- **Create Student**: 
  - **Method**: POST
  - **Endpoint**: `/students`
  - **Request**: JSON object with `name` (string, required)
  - **Response**: JSON object of the created Student with an identifier.

- **Get Student**:
  - **Method**: GET
  - **Endpoint**: `/students/{id}`
  - **Response**: JSON object of the requested Student.

- **Update Student**:
  - **Method**: PUT
  - **Endpoint**: `/students/{id}`
  - **Request**: JSON object with updated `name` (string, required)
  - **Response**: JSON object of the updated Student.

- **Delete Student**:
  - **Method**: DELETE
  - **Endpoint**: `/students/{id}`
  - **Response**: Message confirming the deletion.

- **List Students**:
  - **Method**: GET
  - **Endpoint**: `/students`
  - **Response**: JSON array of all Students.

### Database Initialization

- Automatically create the database schema on application startup based on defined entities.

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/student-management-api.git
   cd student-management-api
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   Create a `.env` file based on the provided `.env.example` to configure database connection and application settings.

4. Run the application:
   ```bash
   python app.py
   ```

## Usage

- The API can be accessed through the specified endpoints. Use an API client like Postman or Curl to test the endpoints.
- Make sure to include the necessary headers (like `Content-Type: application/json`) in your requests.

## Contributing

Contributions are welcome! Please adhere to the coding standards and guidelines specified in the project constitution.

## License

This project is licensed under the MIT License - see the LICENSE file for details.