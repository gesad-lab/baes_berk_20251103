# student-management/README.md

# Student Management System

## Overview & Purpose
The purpose of this project is to develop a simple web application that manages a Student entity, allowing users to create, retrieve, and manage student information through a RESTful API. The application has an intuitive interface for adding student names and ensures data persistence in a SQLite database, which is set up automatically when the application starts. This feature enhances the overall student management capability of the system.

## Project Structure
The project is organized as follows:

```
student-management/
├── api/                  # Contains API endpoint definitions
├── db/                   # Contains database setup and models
├── services/             # Contains business logic and service functions
├── main.py               # The main application entry point
├── requirements.txt      # Python dependencies for the project
└── README.md             # Project documentation
```

## API Endpoints
1. **POST `/students`**: Create a new student.
   - **Request Body**: 
     - `name`: string (required)
   - **Response**: JSON object with a success message and the created student data.

2. **GET `/students`**: Retrieve a list of all students.
   - **Response**: JSON array of student objects, each containing a name.

## Functional Requirements
- The application must automatically create the SQLite database schema on startup with the `Student` table containing:
  - `id`: integer (primary key, auto-increment)
  - `name`: string (required)

- Input validation must ensure that the `name` field is provided when creating a student.

## Dependencies
To install the required dependencies, add the following to your `requirements.txt`:

```
fastapi
uvicorn
sqlalchemy
sqlite
httpx
```

## Getting Started
1. Initialize a Python (3.11+) environment.
2. Install the dependencies listed in `requirements.txt`.
3. Run the application using `uvicorn main:app --reload`.

This README provides the necessary setup details and structure for the Student Management System project.