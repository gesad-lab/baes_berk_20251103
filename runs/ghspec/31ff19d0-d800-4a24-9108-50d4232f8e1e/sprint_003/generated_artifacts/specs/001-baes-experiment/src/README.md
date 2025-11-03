# README.md

# Student Management Application

## Overview

The Student Management Application provides a simple RESTful API for managing students and courses. It allows users to create, retrieve, update, and delete records pertaining to students and courses. The application is built using Flask and uses SQLite for data storage.

## Directory Structure

```plaintext
/student_management_app
│
├── src/                         
│   ├── app.py                   # Main application entry point
│   ├── models.py                # Database models (ORM)
│   ├── routes.py                # API endpoint mappings
│   ├── database.py              # Database connection and schema creation
│   ├── migrations.py            # Migration scripts for schema changes
│   └── config.py                # Application configuration
│
├── tests/                       
│   ├── test_routes.py           # Tests for API routes
│   └── test_models.py           # Tests for database models
│
├── requirements.txt             # Python package dependencies
└── README.md                    # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/student_management_app.git
   cd student_management_app
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations**: Before starting the application, ensure the database schema is created. You can run the migrations using the following command:
   ```bash
   python -m src.migrations
   ```

4. Start the application:
   ```bash
   python -m src.app
   ```

## API Documentation

### Course Entity

The `Course` entity represents a course in the student management system. The following endpoints are available for managing courses:

#### Create Course

- **Endpoint**: `POST /courses`
- **Request Body**:
  ```json
  {
    "name": "Introduction to Python",
    "description": "A beginner course on Python programming."
  }
  ```
- **Response**:
  - **Status Code**: `201 Created`
  - **Body**:
    ```json
    {
      "message": "Course created successfully."
    }
    ```

#### Get All Courses

- **Endpoint**: `GET /courses`
- **Response**:
  - **Status Code**: `200 OK`
  - **Body**:
    ```json
    [
      {
        "id": 1,
        "name": "Introduction to Python",
        "description": "A beginner course on Python programming."
      },
      {
        "id": 2,
        "name": "Advanced Flask",
        "description": "An in-depth course on building applications with Flask."
      }
    ]
    ```

#### Update Course

- **Endpoint**: `PUT /courses/<id>`
- **Request Body**:
  ```json
  {
    "name": "Introduction to Python (Updated)",
    "description": "An updated description for the course."
  }
  ```
- **Response**:
  - **Status Code**: `200 OK`
  - **Body**:
    ```json
    {
      "message": "Course updated successfully."
    }
    ```

#### Delete Course

- **Endpoint**: `DELETE /courses/<id>`
- **Response**:
  - **Status Code**: `204 No Content`

## API Usage Examples

To interact with the API, you can use tools such as Postman or curl commands. Here are some examples using curl:

- Create a new course:
  ```bash
  curl -X POST http://localhost:5000/courses -H "Content-Type: application/json" -d '{"name": "Introduction to Python", "description": "A beginner course on Python programming."}'
  ```

- Get all courses:
  ```bash
  curl -X GET http://localhost:5000/courses
  ```

- Update a course:
  ```bash
  curl -X PUT http://localhost:5000/courses/1 -H "Content-Type: application/json" -d '{"name": "Introduction to Python (Updated)", "description": "An updated description for the course."}'
  ```

- Delete a course:
  ```bash
  curl -X DELETE http://localhost:5000/courses/1
  ```

## Conclusion

This documentation provides an overview of the Student Management Application, including setup instructions and API usage. For further details, feel free to explore the code or reach out with questions.