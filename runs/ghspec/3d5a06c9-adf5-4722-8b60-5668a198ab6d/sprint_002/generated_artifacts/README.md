# Project Title

Student Management Application

## Overview

This application provides functionality to manage students, including creating new student records, listing existing students, and updating student information.

## API Endpoints

### 1. Create a Student
- **Endpoint**: `POST /students`
- **Description**: Creates a new student record with the provided name and email.
- **Request Body**: 
  ```json
  {
    "name": "string",
    "email": "string"
  }
  ```
- **Response**: 
  ```json
  {
    "id": "integer",
    "name": "string",
    "email": "string"
  }
  ```

### 2. List Students
- **Endpoint**: `GET /students`
- **Description**: Retrieves a list of all students.
- **Response**: 
  ```json
  [
    {
      "id": "integer",
      "name": "string",
      "email": "string"
    }
  ]
  ```

### 3. Update Student Email
- **Endpoint**: `PUT /students/{id}`
- **Description**: Updates the email address of a specified student.
- **Request Body**: 
  ```json
  {
    "email": "string"
  }
  ```
- **Response**: 
  ```json
  {
    "id": "integer",
    "name": "string",
    "email": "string"
  }
  ```

## Database Schema Update
- The students' database schema has been updated to include an email field (string, required). 
- A migration has been conducted to ensure all existing student data is preserved during the schema update.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd student_management_app
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Copy the `.env.example` to `.env` and set up your environment variables.
5. Run the migrations to update the database schema:
   ```bash
   python -m alembic upgrade head
   ```
6. Start the application:
   ```bash
   python src/main.py
   ```

## Usage Examples
### Create a Student
```bash
curl -X POST http://localhost:8000/students -H "Content-Type: application/json" -d '{
  "name": "John Doe",
  "email": "john.doe@example.com"
}'
```

### List Students
```bash
curl -X GET http://localhost:8000/students
```

### Update Student Email
```bash
curl -X PUT http://localhost:8000/students/1 -H "Content-Type: application/json" -d '{
  "email": "new.email@example.com"
}'
```

## Testing
Unit tests for the new features are located in the `tests/test_student_routes.py` file. To run the tests, you can use:
```bash
pytest
``` 

## License
This project is licensed under the MIT License - see the LICENSE file for details.