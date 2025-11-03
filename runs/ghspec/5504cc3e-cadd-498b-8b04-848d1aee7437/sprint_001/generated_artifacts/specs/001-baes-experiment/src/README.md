# README.md

# Student Entity Management Web Application

This project is a simple Student Entity Management Web Application that allows users to manage student records via a RESTful API. Users can register students, retrieve student information, update student names, and delete student records.

## Table of Contents

- [Setup Instructions](#setup-instructions)
- [API Usage](#api-usage)
  - [User Registration](#user-registration)
  - [Retrieve Student Information](#retrieve-student-information)
  - [Update Student Information](#update-student-information)
  - [Delete Student](#delete-student)
  - [Error Handling](#error-handling)

## Setup Instructions

To set up the application, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/student-entity-management.git
   cd student-entity-management
   ```

2. **Set Up Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create Database Schema**
   Initialize the SQLite database:
   ```bash
   python setup_database.py  # Replace with your database initialization script
   ```

5. **Run the Application**
   Start the Flask server (or the relevant server you are using):
   ```bash
   flask run
   ```

The application will be running on `http://127.0.0.1:5000`.

## API Usage

### User Registration

To register a new student, send a POST request to `/students` with a JSON body including the student's name.

**Request**
```http
POST /students
Content-Type: application/json

{
  "name": "John Doe"
}
```

**Response**
```json
{
  "id": 1,
  "name": "John Doe"
}
```

### Retrieve Student Information

To retrieve a list of all registered students, send a GET request to `/students`.

**Request**
```http
GET /students
```

**Response**
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

### Update Student Information

To update a student's name, send a PUT request to `/students/{id}` with the new name in the JSON body.

**Request**
```http
PUT /students/1
Content-Type: application/json

{
  "name": "Johnathan Doe"
}
```

**Response**
```json
{
  "id": 1,
  "name": "Johnathan Doe"
}
```

### Delete Student

To delete a student, send a DELETE request to `/students/{id}`.

**Request**
```http
DELETE /students/1
```

**Response**
```json
{
  "message": "Student deletion successful."
}
```

### Error Handling

Validation errors for requests with invalid data will result in a clear and actionable JSON error message.

**Example Response for Invalid Request**
```http
POST /students
Content-Type: application/json

{
  "name": ""
}
```

**Response**
```json
{
  "error": {
    "code": "E001",
    "message": "Invalid name provided. Name cannot be empty.",
    "details": {}
  }
}
```

## Conclusion

This README provides an overview of setting up and using the Student Entity Management Web Application. For development and contributions, please refer to the project documentation and follow our contribution guidelines.