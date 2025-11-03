# README.md

# Project Title

## API Endpoints

This section documents the API endpoints available in the application for managing student enrollments in courses.

### Student Endpoints

#### Enroll Student in Course

- **Endpoint**: `POST /students/enroll`
- **Description**: Enroll a student in a specified course.
- **Request Body**:
  ```json
  {
    "student_id": "string", // Required: ID of the student to enroll
    "course_id": "string"   // Required: ID of the course to enroll the student in
  }
  ```
- **Responses**:
  - **201 Created**: Successfully enrolled the student.
    ```json
    {
      "message": "Student enrolled successfully."
    }
    ```
  - **400 Bad Request**: Invalid input, check your student or course ID.
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Invalid student or course ID."
      }
    }
    ```

#### Get Student Details

- **Endpoint**: `GET /students/{student_id}`
- **Description**: Retrieve details about a specific student, including their enrolled courses.
- **Path Parameters**:
  - `student_id`: Required; the ID of the student whose details are being fetched.
- **Responses**:
  - **200 OK**: Successfully retrieved student details.
    ```json
    {
      "student_id": "string",
      "name": "string",
      "enrolled_courses": [
        {
          "course_id": "string",
          "course_name": "string"
        }
      ]
    }
    ```
  - **404 Not Found**: Student not found.
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Student not found."
      }
    }
    ```

### Health Check Endpoint

- **Endpoint**: `GET /health`
- **Description**: A simple health check endpoint to verify that the application is operational.
- **Responses**:
  - **200 OK**: Application is healthy.
    ```json
    {
      "status": "healthy"
    }
    ```

## Setup Process

To set up the application, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-url.git
   cd your-repo-directory
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:
   ```bash
   # Run migrations here if applicable
   ```

4. Start the application:
   ```bash
   uvicorn main:app --reload
   ```

## Graceful Shutdown

Ensure that the application handles graceful shut down conditions. The server will finish processing any existing requests before shutting down.