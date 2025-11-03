# API Documentation

## Overview & Purpose
The purpose of this web application is to manage a "Student" entity, where students are represented by a single field: their name. The application allows for the addition of students and returns their details in JSON format, ensuring a user-friendly experience. It aims to provide an efficient and maintainable solution using best practices for building web applications.

## API Endpoints

### 1. Create a Student
- **Endpoint**: `POST /students`
- **Description**: Adds a new student by providing their name.
- **Request Body**:
  ```json
  {
    "name": "string"
  }
  ```
  - **required**: `name` (string)
- **Responses**:
  - **Success** (201 Created):
  ```json
  {
    "id": "integer",
    "name": "string"
  }
  ```
  - **Error** (400 Bad Request):
  ```json
  {
    "error": {
      "code": "E001",
      "message": "Name is required"
    }
  }
  ```

### 2. Retrieve a Student
- **Endpoint**: `GET /students/{id}`
- **Description**: Retrieves the details of a student using their ID.
- **Responses**:
  - **Success** (200 OK):
  ```json
  {
    "id": "integer",
    "name": "string"
  }
  ```
  - **Error** (404 Not Found):
  ```json
  {
    "error": {
      "message": "Student not found"
    }
  }
  ```

## User Scenarios & Testing

1. **Adding a Student**:
   - As a user, I want to add a new student by providing their name to keep track of them.
   - **Test Case**: Send a POST request with a valid name. Verify that the response confirms the student's creation and the corresponding record exists in the database.

2. **Retrieving Student Information**:
   - As a user, I want to retrieve the details of a student using their ID.
   - **Test Case**: Send a GET request for an existing student ID. Verify that the correct student details are returned in JSON format.

3. **Error Handling for Missing Name**:
   - As a user, I want to receive an error message if I attempt to add a student without providing a name.
   - **Test Case**: Send a POST request with an empty name field. Verify that an appropriate error message is returned in the response.

4. **Database Initialization**:
   - As a developer, I want the application to automatically create the database schema on startup without manual intervention.
   - **Test Case**: Start the application and verify that the expected database schema is created correctly.

## Database Schema Creation
- The application utilizes SQLAlchemy to create the database schema upon startup.
- **Implementation**:
  ```python
  from sqlalchemy import create_engine
  from sqlalchemy.orm import sessionmaker

  engine = create_engine('sqlite:///students.db')
  Base.metadata.create_all(engine)  # Create the schema
  Session = sessionmaker(bind=engine)
  ```

This documentation outlines the API structure and provides a clear overview of the application’s functionality, user scenarios, and technical details regarding the database schema.