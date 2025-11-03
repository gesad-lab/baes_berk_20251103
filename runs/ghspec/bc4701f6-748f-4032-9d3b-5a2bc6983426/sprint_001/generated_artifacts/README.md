# README.md

# Student Management API

## Description
This application provides an API to manage student records, allowing users to create and retrieve information about students.

## Installation
To get started with this application, clone the repository and install the required dependencies.

```bash
git clone <repository_url>
cd <project_directory>
pip install -r requirements.txt
```

## Running the Application
To start the application, use the following command:

```bash
python app.py
```

The server will start, and the API will be available at `http://localhost:5000`.

## API Documentation

### 1. Creating a Student
- **Method**: POST
- **URL**: `/students`
- **Request Body**:
  ```json
  {
    "name": "John Doe"  // (required)
  }
  ```
- **Response**:
  - **201 Created**
  ```json
  {
    "id": 1,
    "name": "John Doe"
  }
  ```

- **Error Responses**:
  - **400 Bad Request**
  ```json
  {
    "error": {
      "code": "E001",
      "message": "Name is required."
    }
  }
  ```

### 2. Retrieving a Student
- **Method**: GET
- **URL**: `/students/{id}`
- **Response**:
  - **200 OK**
  ```json
  {
    "id": 1,
    "name": "John Doe"
  }
  ```

  - **404 Not Found**
  ```json
  {
    "error": {
      "code": "E002",
      "message": "Student not found."
    }
  }
  ```

### 3. Automatic Database Initialization
Upon application startup, the SQLite database schema for the Student entity is automatically created. This setup ensures that the API is ready to handle requests without additional database setup.

## Error Handling
- The application handles various error scenarios and returns appropriate error messages with status codes for invalid requests, ensuring that the API usage is intuitive and actionable for users.