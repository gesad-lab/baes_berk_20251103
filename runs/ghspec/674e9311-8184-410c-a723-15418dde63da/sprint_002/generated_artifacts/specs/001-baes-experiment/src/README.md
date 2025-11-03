# Updated README.md with API Documentation

# README.md

# Project Title

## Overview

This project is a Flask-based web application that manages student data using SQLAlchemy ORM. It supports basic CRUD operations and includes an API for interacting with student records.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run database migrations**:
   Ensure you have the Alembic environment set up correctly, then run:
   ```bash
   alembic upgrade head
   ```

4. **Run the application**:
   ```bash
   python main.py
   ```

5. **Access the API documentation**:
   After starting the server, you can access the live API docs at `http://localhost:5000/docs`.

## API Endpoints

### Students

#### Create a Student

- **POST /students**
  
  This endpoint creates a new student entry.

  **Request Body**:
  ```json
  {
      "name": "John Doe",
      "age": 21,
      "email": "john.doe@example.com"
  }
  ```

  **Response**:
  - **201 Created**: Returns the created student object.
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "age": 21,
        "email": "john.doe@example.com"
    }
    ```

  - **400 Bad Request**: If the input is invalid (e.g., missing fields, invalid email format).
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Invalid email format",
            "details": {}
        }
    }
    ```

#### Get All Students

- **GET /students**
  
  This endpoint retrieves a list of all students.

  **Response**:
  - **200 OK**: Returns an array of student objects.
    ```json
    [
        {
            "id": 1,
            "name": "John Doe",
            "age": 21,
            "email": "john.doe@example.com"
        }
    ]
    ```

#### Get a Student by ID

- **GET /students/{id}**
  
  This endpoint retrieves a student by their ID.

  **Response**:
  - **200 OK**: Returns the student object if found.
    ```json
    {
        "id": 1,
        "name": "John Doe",
        "age": 21,
        "email": "john.doe@example.com"
    }
    ```

  - **404 Not Found**: If the student with the specified ID does not exist.
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Student not found",
            "details": {}
        }
    }
    ```

### Further Documentation

For more details about the API, including additional endpoints and usage examples, please refer to the full documentation available in the `/docs` directory or reach out to the development team.

## Testing

To run the tests for the application, use the following command:
```bash
pytest
```

Ensure that you have pytest installed in your virtual environment.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

---

### Note
This README has been updated to include information about the new `email` field for the student entity, which is now a required field in the API. Please ensure to validate email formats when creating a new student.