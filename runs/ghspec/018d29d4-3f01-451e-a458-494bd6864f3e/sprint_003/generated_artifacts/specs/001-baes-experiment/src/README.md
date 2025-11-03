# README.md

# Project Title

## Overview & Purpose
The purpose of creating a Course entity is to enhance the existing student management system by tracking courses alongside students. By allowing courses to be defined with a unique name and level, the application can support future features such as student enrollment in courses and better reporting capabilities. This addition is essential for improving the curriculum management aspects of the application and will enable the organization of student data around specific academic programs.

## API Usage Instructions

### Base URL
The base URL for all API endpoints is:
```
http://localhost:8000/api/v1
```

### Endpoints

#### 1. Create New Course
- **URL**: `/courses`
- **Method**: `POST`
- **Description**: Create a new course by providing required attributes.
- **Request Body**:
    ```json
    {
        "name": "Course Name",
        "level": "Course Level"
    }
    ```
- **Response**:
    - **201 Created**: Returns the created course object.
    - **400 Bad Request**: Returns an error message if required fields are missing.
  
- **Example**:
    ```bash
    curl -X POST "http://localhost:8000/api/v1/courses" -H "Content-Type: application/json" -d '{"name": "Mathematics", "level": "Intermediate"}'
    ```

#### 2. Retrieve Course Details
- **URL**: `/courses/{course_id}`
- **Method**: `GET`
- **Description**: Fetch a specific course's details using its ID.
- **Response**:
    - **200 OK**: Returns the course object including name and level.
    - **404 Not Found**: Returns an error message if the course ID does not exist.

- **Example**:
    ```bash
    curl -X GET "http://localhost:8000/api/v1/courses/1"
    ```

### Error Handling
- The system will return JSON formatted error messages for invalid requests, indicating which fields are missing or incorrect. Each error response will contain:
    ```json
    {
        "error": {
            "code": "E001", 
            "message": "Name is required",
            "details": {}
        }
    }
    ```

### Database Migrations
- Ensure migrations are performed to retain existing Student data while integrating the new Course structure. This is handled automatically by the application on startup.

## User Scenarios & Testing
1. **Create New Course**: A user should be able to send a request to create a new course by providing the name and level.
   - Given valid inputs for name and level, when the user submits the creation request, a new course record should be created successfully.

2. **Retrieve Course Details**: A user should be able to fetch a course record and view its details.
   - Given an existing course ID, when the user requests the course, the system should return relevant information including name and level.

3. **Invalid Course Creation Without Required Fields**: A user attempts to create a course record without providing name or level.
   - The system should return a clear error message indicating that both fields are required.

4. **Invalid Course Creation with Missing Level**: A user attempts to create a course without specifying the level.
   - The system should return a clear error message indicating that the level is a required field.

## Deployment Considerations
- Prepare SQLite connection strings and any relevant environment variables inside the `.env` file.