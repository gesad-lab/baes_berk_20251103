# README.md

# Project Title

This is the README file for the project. Below are the details of the API endpoints, database schema, and usage information.

## API Documentation

### 1. Create Course
- **Endpoint**: `POST /courses`
- **Request Body**: 
  ```json
  {
    "name": "Course Name",  // The name of the course (string, required)
    "level": "Beginner"      // The level of the course (string, required)
  }
  ```
- **Response**:
  - **Success**: 
    ```json
    {
      "id": 1,               // Unique identifier for the course
      "name": "Course Name", // The name of the course
      "level": "Beginner"    // The level of the course
    }
    ```
  - **Error** (e.g., if required fields are missing):
    ```json
    {
      "error": {
        "code": "E001",
        "message": "The 'name' and 'level' fields are required.",
        "details": {}
      }
    }
    ```

### 2. Retrieve Course
- **Endpoint**: `GET /courses/{id}`
- **Response**:
  - **Success**: 
    ```json
    {
      "id": 1,               // Unique identifier for the course
      "name": "Course Name", // The name of the course
      "level": "Beginner"    // The level of the course
    }
    ```
  - **Error** (if the course is not found):
    ```json
    {
      "error": {
        "code": "E002",
        "message": "Course not found.",
        "details": {}
      }
    }
    ```

### 3. Database Schema
The new `Course` table is structured as follows:
- `id`: Unique identifier for each course (integer).
- `name`: The name of the course (string, required).
- `level`: The level of the course (string, required).

### 4. Database Migration
A migration script has been created to add the `Course` table to the existing database. This migration preserves the existing `Student` data while adding the new course functionality.

## Success Criteria
- The web application successfully creates and retrieves course entries according to the defined API.
- All error handling scenarios, including validation for required fields, are effectively managed with clear and actionable user responses.

## Local Deployment
To run the application locally, ensure that all dependencies are installed. 

1. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

2. Set up the database:
   ```
   flask db upgrade
   ```

3. Run the application:
   ```
   flask run
   ```

Ensure that the application starts without any issues and that you can access the endpoints described above.