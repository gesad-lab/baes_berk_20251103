# Project Title

## Overview
This project is a student management application using FastAPI. It allows for management of student data, including creating, retrieving, updating, and deleting student records.

## Setup Instructions
1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/student_app.git
   cd student_app
   ```

2. Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables by creating a `.env` file based on `.env.example`.

## API Endpoints

### 1. Create Student
- **Endpoint**: `/api/v1/students`
- **Method**: `POST`
- **Description**: Creates a new student record.
- **Request Body**:
  ```json
  {
    "name": "string",
    "age": "integer",
    "email": "string"
  }
  ```
- **Response**:
  - **201 Created**: Returns the created student object.
  - **400 Bad Request**: If validation fails.

### 2. Get All Students
- **Endpoint**: `/api/v1/students`
- **Method**: `GET`
- **Description**: Retrieves a list of all students.
- **Response**:
  - **200 OK**: Returns an array of student objects.

### 3. Get Student by ID
- **Endpoint**: `/api/v1/students/{id}`
- **Method**: `GET`
- **Description**: Retrieves a single student by their ID.
- **Response**:
  - **200 OK**: Returns the student object.
  - **404 Not Found**: If the student with the specified ID does not exist.

### 4. Update Student
- **Endpoint**: `/api/v1/students/{id}`
- **Method**: `PUT`
- **Description**: Updates an existing student record.
- **Request Body**:
  ```json
  {
    "name": "string",
    "age": "integer",
    "email": "string"
  }
  ```
- **Response**:
  - **200 OK**: Returns the updated student object.
  - **404 Not Found**: If the student with the specified ID does not exist.
  - **400 Bad Request**: If validation fails.

### 5. Delete Student
- **Endpoint**: `/api/v1/students/{id}`
- **Method**: `DELETE`
- **Description**: Deletes a student record.
- **Response**:
  - **204 No Content**: Successfully deleted the student.
  - **404 Not Found**: If the student with the specified ID does not exist.

## Testing
Run the test suite using:
```bash
pytest
```

## License
MIT License. See `LICENSE` for details.