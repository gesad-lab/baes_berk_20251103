# README.md

# Student Management Application

## Overview

The Student Management Application is a simple web application designed to manage student records efficiently. This application allows users to create, read, and retrieve student information, focusing primarily on the student's name. It is suitable for educational institutions and administrators to maintain a database of students.

## Features

- Create a new student record and receive confirmation with the created student information in JSON format.
- Fetch existing student records by valid student ID.
- Retrieve a list of all student records in JSON format.
- Automatic database schema creation upon the first startup.

## Technical Details

### Architecture

The application follows a monolithic architecture, consisting of the following components:

1. **API Layer**: Handles HTTP requests and defines the endpoints.
2. **Service Layer**: Contains the business logic for managing student records.
3. **Data Access Layer**: Interacts with the database using SQLAlchemy ORM.
4. **Database**: Utilizes SQLite for data storage and automatically creates the schema on startup.

### Endpoints

- `POST /api/v1/students`: Create a new student record.
  - **Request Body**: 
    ```json
    {
      "name": "John Doe"
    }
    ```
  - **Response**: 
    ```json
    {
      "id": 1,
      "name": "John Doe"
    }
    ```
  
- `GET /api/v1/students/<id>`: Retrieve a student by ID.
  - **Response**: 
    ```json
    {
      "id": 1,
      "name": "John Doe"
    }
    ```

- `GET /api/v1/students`: List all student records.
  - **Response**: 
    ```json
    [
      {
        "id": 1,
        "name": "John Doe"
      },
      {
        "id": 2,
        "name": "Jane Smith"
      }
    ]
    ```

## Setup Instructions

### Prerequisites

- Python 3.6 or higher
- pip for installing packages

### Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_dir>
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install Flask Flask-SQLAlchemy Marshmallow
   ```

### Running the Application

1. Start the application:
   ```bash
   python api.py
   ```

2. The API will be available at `http://localhost:5000/api/v1/students`.

## Usage Examples

1. **Create a New Student Record**:
   - Use a tool like Postman or cURL to send a `POST` request:
     ```bash
     curl -X POST http://localhost:5000/api/v1/students -H "Content-Type: application/json" -d '{"name": "John Doe"}'
     ```

2. **Retrieve a Student Record by ID**:
   - Send a `GET` request:
     ```bash
     curl http://localhost:5000/api/v1/students/1
     ```

3. **List All Student Records**:
   - Send a `GET` request:
     ```bash
     curl http://localhost:5000/api/v1/students
     ```

## Testing

The application is equipped with unit tests to ensure proper functionality. Tests can be run using pytest:
```bash
pytest tests/
```

## Conclusion

The Student Management Application provides an efficient way to manage student records, ensuring ease of use and quick access to student information. For any issues or feature requests, please submit an issue in the repository.