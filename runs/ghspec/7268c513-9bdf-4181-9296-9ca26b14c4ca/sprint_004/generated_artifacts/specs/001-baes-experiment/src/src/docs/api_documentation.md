# src/docs/api_documentation.md

# API Documentation for Student Enrollment API

## Introduction
This document provides an overview of the API that allows for enrolling students into courses. It explains the endpoints available, required request parameters, and expected responses.

## Technology Stack
- **Programming Language**: Python
- **Web Framework**: Flask
- **ORM**: SQLAlchemy for database abstraction
- **Database**: SQLite
- **Testing Framework**: pytest
- **Documentation**: Swagger for API documentation

## Base URL
The base URL for all endpoints is `/api/v1`.

## Endpoints

### Enroll Student into Course

- **Endpoint**: `/enroll`
- **Method**: `POST`
- **Description**: Enroll a student into a specified course.
- **Request Body**:
  ```json
  {
    "student_id": "string",  // ID of the student to enroll
    "course_id": "string"    // ID of the course
  }
  ```
  
- **Responses**:
  - **201 Created**: Enrollment successful
  - **400 Bad Request**: Invalid input data (e.g., missing fields)
  - **404 Not Found**: Given `student_id` or `course_id` does not exist
  - **500 Internal Server Error**: Unexpected error on the server

#### Example Request:
```http
POST /api/v1/enroll HTTP/1.1
Content-Type: application/json

{
  "student_id": "123456",
  "course_id": "course_101"
}
```

#### Example Successful Response:
```json
{
  "message": "Student enrolled successfully.",
  "enrollment_id": "enroll_7890"
}
```

#### Example Error Response:
```json
{
  "error": {
    "code": "E001",
    "message": "Invalid input data. 'student_id' and 'course_id' are required."
  }
}
```

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo.git
   cd your-repo
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   flask db upgrade
   ```

5. Run the application:
   ```bash
   flask run
   ```

## Testing the API
To run tests, ensure your virtual environment is activated and execute:
```bash
pytest
```

## Conclusion
This API document serves as a guide for developers to understand how to interact with the Enrollment API. Team members can refer to this documentation to integrate the API into client applications. For further assistance or issues, please reach out to the development team.