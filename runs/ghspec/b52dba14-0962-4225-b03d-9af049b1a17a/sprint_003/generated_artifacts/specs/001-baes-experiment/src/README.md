# README.md

# Student Management System

## Overview

The Student Management System API allows for the management of students and courses. It provides endpoints to create, read, update and delete student and course information.

## API Endpoints

### Students

#### Create Student
- **POST** `/students`
- **Request Body**:
    ```json
    {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    ```
- **Response**:
    - **201 Created**: Student successfully created.
    - **400 Bad Request**: Validation error if input is invalid.

---

#### Get Student
- **GET** `/students/<id>`
- **Response**:
    - **200 OK**: Returns student information.
    - **404 Not Found**: Student not found.

---

#### Update Student
- **PUT** `/students/<id>`
- **Request Body**:
    ```json
    {
        "name": "John Doe",
        "email": "john.doe_new@example.com"
    }
    ```
- **Response**:
    - **200 OK**: Student successfully updated.
    - **400 Bad Request**: Validation error if input is invalid.
    - **404 Not Found**: Student not found.

---

### Courses

#### Create Course
- **POST** `/courses`
- **Request Body**:
    ```json
    {
        "title": "Introduction to Python",
        "description": "A beginner course on Python programming.",
        "duration": "4 weeks"
    }
    ```
- **Response**:
    - **201 Created**: Course successfully created.
    - **400 Bad Request**: Validation error if input is invalid.

---

#### Get Course
- **GET** `/courses/<id>`
- **Response**:
    - **200 OK**: Returns course information.
    - **404 Not Found**: Course not found.

---

#### Update Course
- **PUT** `/courses/<id>`
- **Request Body**:
    ```json
    {
        "title": "Introduction to Python: Updated",
        "description": "Updated course on Python programming.",
        "duration": "5 weeks"
    }
    ```
- **Response**:
    - **200 OK**: Course successfully updated.
    - **400 Bad Request**: Validation error if input is invalid.
    - **404 Not Found**: Course not found.

---

#### Delete Course
- **DELETE** `/courses/<id>`
- **Response**:
    - **204 No Content**: Course successfully deleted.
    - **404 Not Found**: Course not found.

## Error Handling
All endpoints will return appropriate HTTP status codes and error messages in the case of invalid requests or if the resource is not found. 

---

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory and install dependencies:
    ```bash
    cd student_management
    pip install -r requirements.txt
    ```

3. Set up your `.env` file based on `.env.example`.

## Running the Application

Start the Flask server:
```bash
python src/app.py
```

Visit the API documentation to test endpoints.

## Contributing

Please feel free to submit pull requests for any improvements or issues.

## License

This project is licensed under the MIT License. See the LICENSE file for details.