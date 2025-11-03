# README.md

---
# API Documentation

## Introduction
This README provides details about the API endpoints available for managing courses and their assigned teachers. The API is built using FastAPI and connects to a SQLite database through SQLAlchemy.

## API Endpoints

### 1. Assign a Teacher to a Course

**Endpoint**: `POST /courses/{id}/assign_teacher`

- **Description**: Assign a teacher to a specified course by its ID.
  
- **Parameters**:
  - `id` (path parameter, integer): The unique identifier of the course to which the teacher will be assigned.
  
- **Request Body**:
  ```json
  {
      "teacher_id": 1  // The ID of the teacher to be assigned
  }
  ```

- **Responses**:
  - **201 Created**: Teacher successfully assigned to the course.
    ```json
    {
        "message": "Teacher assigned successfully."
    }
    ```
  - **400 Bad Request**: Invalid data provided (e.g., teacher does not exist).
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Invalid teacher ID."
        }
    }
    ```
  - **404 Not Found**: Course not found with the provided ID.
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Course not found."
        }
    }
    ```

---

### 2. Update Assigned Teacher for a Course

**Endpoint**: `PUT /courses/{id}/update_teacher`

- **Description**: Update the assigned teacher for a specified course by its ID.

- **Parameters**:
  - `id` (path parameter, integer): The unique identifier of the course for which the teacher assignment is being updated.
  
- **Request Body**:
  ```json
  {
      "teacher_id": 2  // The new ID of the teacher to be assigned
  }
  ```

- **Responses**:
  - **200 OK**: Teacher successfully updated for the course.
    ```json
    {
        "message": "Teacher updated successfully."
    }
    ```
  - **400 Bad Request**: Invalid data provided (e.g., teacher does not exist).
    ```json
    {
        "error": {
            "code": "E001",
            "message": "Invalid teacher ID."
        }
    }
    ```
  - **404 Not Found**: Course not found with the provided ID.
    ```json
    {
        "error": {
            "code": "E002",
            "message": "Course not found."
        }
    }
    ```

---

### 3. Retrieve All Courses

**Endpoint**: `GET /courses`

- **Description**: Retrieve a list of all courses, including details about assigned teachers.

- **Responses**:
  - **200 OK**: Successful retrieval of courses.
    ```json
    [
        {
            "id": 1,
            "course_name": "Mathematics",
            "assigned_teacher": {
                "id": 1,
                "name": "John Doe",
                "email": "john.doe@example.com"
            }
        },
        {
            "id": 2,
            "course_name": "Science",
            "assigned_teacher": null  // No teacher assigned
        }
    ]
    ```

---

## Setup and Usage

1. **Installation**:
   - Ensure Python 3.9+ is installed.
   - Install the dependencies using Poetry or pip:
     ```bash
     pip install -r requirements.txt
     ```

2. **Running the Application**:
   - Start the FastAPI server:
     ```bash
     uvicorn src.main:app --reload
     ```

3. **Accessing the API Documentation**:
   - Visit `http://localhost:8000/docs` for interactive API documentation.

## Conclusion

This README provides a comprehensive overview of the API endpoints related to managing courses and teachers. Follow the setup instructions and refer to the parameter descriptions and response formats for successful interactions with the API.