# README.md

# Project Name

## Introduction
This project provides a comprehensive API for managing educational resources, including students and courses. It is built using FastAPI and offers RESTful endpoints to handle various operations.

## Course API Endpoints

The Course API allows users to manage courses through the following endpoints:

### 1. Create Course
- **Endpoint**: `POST /courses`
- **Description**: Allows users to create a new course by providing the course name and level.
- **Required Body**:
  ```json
  {
    "name": "Course Name",
    "level": "Course Level"
  }
  ```
- **Response**:
  - **Success**:
  ```json
  {
    "id": 1,
    "name": "Course Name",
    "level": "Course Level"
  }
  ```
  - **Error**:
  ```json
  {
    "error": {
      "code": "E400",
      "message": "Invalid input. 'name' and 'level' must be non-empty strings."
    }
  }
  ```

### 2. Retrieve Course
- **Endpoint**: `GET /courses/{id}`
- **Description**: Retrieves information about a specific course using its ID.
- **Response**:
  - **Success**:
  ```json
  {
    "id": 1,
    "name": "Introduction to Programming",
    "level": "Beginner"
  }
  ```
  - **Error**:
  ```json
  {
    "error": {
      "code": "E404",
      "message": "Course not found."
    }
  }
  ```
- **HTTP Status Codes**:
  - `200 OK`: Course information retrieved.
  - `404 Not Found`: Course with specified ID does not exist.

### 3. List Courses
- **Endpoint**: `GET /courses`
- **Description**: Returns a list of all available courses along with their names and levels.
- **Response**:
```json
[
  {
    "id": 1,
    "name": "Introduction to Programming",
    "level": "Beginner"
  },
  {
    "id": 2,
    "name": "Advanced Mathematics",
    "level": "Intermediate"
  }
]
```

## Testing

1. **Create Course Scenario Testing**: Validate that a POST request with valid data (name and level) creates a new course record in the database.
2. **Retrieve Course Scenario Testing**: Validate that a GET request for a specific course ID returns the correct course information, including name and level.
3. **List Courses Scenario Testing**: Validate that a GET request retrieves a list of all courses accurately, including names and levels.

## Database Schema

- The `courses` table includes the following fields:
  - **id**: Integer, primary key.
  - **name**: String, required (non-empty).
  - **level**: String, required (non-empty).

## Setup Instructions

1. Clone the repository and navigate into the project directory.
2. Ensure you have Docker and Docker Compose installed to support the application environment.
3. Run the Docker containers using:
   ```bash
   docker-compose up --build
   ```
4. Migrate the database schema changes with:
   ```bash
   alembic upgrade head
   ```
5. Access the API documentation at `http://localhost:8000/docs`.

## Contributing

Feel free to submit pull requests or open issues for discussion. Your contributions are welcome!

---

This update integrates essential documentation for the new Course API, helping users understand how to interact with the course management functionality efficiently.