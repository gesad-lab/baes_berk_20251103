# student_management/README.md

# Student Management API

## Overview

The Student Management API allows you to manage student records in a basic SQLite database. You can create, retrieve, update, and delete student records through RESTful API endpoints.

## Project Structure

```
student_management/
├── src/
│   ├── app.py           # Entry point for the Flask application
│   ├── services/
│   │   └── student.py    # Business logic for student operations
│   ├── models/
│   │   └── student.py    # Data model for the Student entity
│   ├── db/
│   │   └── database.py    # Database initialization
│   └── utils/
│       └── validators.py  # Input validation functions
├── tests/
│   ├── test_student.py    # Unit tests for student operations
└── requirements.txt        # Dependencies for the project
```

## Setup

1. **Clone the Repository**:
   ```
   git clone <repository-url>
   cd student_management
   ```

2. **Install Dependencies**:
   Make sure you have Python 3.x installed. Then, install the required packages using pip:
   ```
   pip install -r requirements.txt
   ```

3. **Database Initialization**:
   The SQLite database will be auto-generated when the application starts. There is a "students" table created with the following structure:
   - **id**: Integer, auto-increment as primary key
   - **name**: String, required

## API Endpoints

### 1. Create Student
- **Endpoint**: `POST /students`
- **Request Body**: 
  ```json
  {
      "name": "John Doe"
  }
  ```
- **Response**:
  - Status: `201 Created`
  - Body:
  ```json
  {
      "id": 1,
      "name": "John Doe"
  }
  ```

### 2. Retrieve Student
- **Endpoint**: `GET /students/{id}`
- **Response**:
  - Status: `200 OK`
  - Body:
  ```json
  {
      "id": 1,
      "name": "John Doe"
  }
  ```
  - If the student ID does not exist, returns `404 Not Found`.

### 3. Update Student
- **Endpoint**: `PUT /students/{id}`
- **Request Body**: 
  ```json
  {
      "name": "Jane Doe"
  }
  ```
- **Response**:
  - Status: `200 OK`
  - Body:
  ```json
  {
      "id": 1,
      "name": "Jane Doe"
  }
  ```
  - If the student ID does not exist, returns `404 Not Found`.

### 4. Delete Student
- **Endpoint**: `DELETE /students/{id}`
- **Response**:
  - Status: `204 No Content`
  - If the student ID does not exist, returns `404 Not Found`.

## Running the Application

To start the application, run the following command:
```
python src/app.py
```
The server will start and listen for incoming requests.

## Testing

You can run the tests using the following command:
```
pytest tests/test_student.py
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.