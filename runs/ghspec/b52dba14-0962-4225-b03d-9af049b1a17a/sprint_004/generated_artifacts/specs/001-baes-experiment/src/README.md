# Project Documentation

# Student Management System

This project is a Student Management System designed to handle courses, students, and enrollments. It provides a structured API that allows the management of the many-to-many relationship between students and courses.

## Table of Contents
- [Module Structure](#module-structure)
- [API Endpoints](#api-endpoints)
  - [Student API](#student-api)
  - [Course API](#course-api)
  - [Enrollment API](#enrollment-api)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)

## Module Structure

The application structure maintains an organized layout with the following directories:

```
student_management/
│
├── src/
│   ├── api/                   # Contains the API routes
│   │   ├── student_routes.py   # Existing student routes
│   │   └── enrollment_routes.py  # New enrollment routes for handling course enrollments
│   ├── models/                # Data models and schemas
│   │   ├── student_model.py     # Existing student model
│   │   ├── course_model.py       # Existing course model
│   │   └── enrollment_model.py    # New enrollment model for linking students and courses
│   ├── services/              # Business logic
│   │   ├── student_service.py    # Existing student services
│   │   ├── course_service.py      # Existing course service for business logic
│   │   └── enrollment_service.py   # New service to manage enrollment logic
│   ├── database/              # Database connection and migrations
│   │   └── migrations/        # Migration files for enrollments
│   ├── config/                # Configuration management
│   └── app.py                 # Main application entry point
│
├── tests/                     # Test cases structured according to the modules
│   ├── test_students.py       # Existing tests for students
│   ├── test_courses.py        # Tests for the course functionality
│   └── test_enrollments.py    # New tests for enrollment functionalities
│
├── requirements.txt           # Updated with any new dependencies, if needed
├── .env.example               # Configuration examples
└── README.md                  # Project documentation update
```

## API Endpoints

### Student API

- **POST `/students`**: Create a new student.
- **GET `/students/<id>`**: Retrieve a student by ID.
- **PUT `/students/<id>`**: Update an existing student.
- **DELETE `/students/<id>`**: Delete a student.

### Course API

- **POST `/courses`**: Create a new course.
- **GET `/courses/<id>`**: Retrieve a course by ID.
- **PUT `/courses/<id>`**: Update an existing course.
- **DELETE `/courses/<id>`**: Delete a course.

### Enrollment API

The Enrollment API handles the relationship between students and courses.

- **POST `/enrollments`**: Enroll a student in a course.
  - **Request Body**:
    ```json
    {
      "student_id": 1,
      "course_id": 2
    }
    ```

- **GET `/enrollments/<id>`**: Retrieve an enrollment record by ID.
  
- **DELETE `/enrollments/<id>`**: Remove a student from a course by enrollment ID.

## Installation

To set up the project, follow these steps:

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required dependencies using the following command:
   ```
   pip install -r requirements.txt
   ```
4. Copy the `.env.example` to `.env` and update the configuration as needed.

## Usage

To start the application, run the following command:
```
python src/app.py
```

The application will be accessible at `http://localhost:5000`.

## Testing

To run the tests, execute:
```
pytest
```

This will run all the tests, including those for the new enrollment functionalities. Ensure you have the test database set up for successful testing.