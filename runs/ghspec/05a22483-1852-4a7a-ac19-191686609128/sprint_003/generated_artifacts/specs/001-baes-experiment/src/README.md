# README.md

# Project Title

Welcome to the Course Management API! This API allows users to manage courses and students seamlessly.

## Features

### Course Management
- **Create a Course**: Allows users to create a new course by providing the course name and level.
- **Retrieve Course Details**: Users can fetch details of a specific course using its unique identifier.

## API Endpoints

### 1. Create Course
- **Endpoint**: `POST /api/v1/courses`
- **Request Body**:
    ```json
    {
      "name": "Course Name",
      "level": "Intermediate"
    }
    ```
- **Response** (success):
    ```json
    {
      "id": 1,
      "name": "Course Name",
      "level": "Intermediate"
    }
    ```
- **Validation Errors**: 
    - If the name or level is missing, a 400 Bad Request will be returned:
    ```json
    {
      "error": {
        "code": "E001",
        "message": "Missing required fields: name, level"
      }
    }
    ```

### 2. Retrieve Course Details
- **Endpoint**: `GET /api/v1/courses/{course_id}`
- **Response** (success):
    ```json
    {
      "id": 1,
      "name": "Course Name",
      "level": "Intermediate"
    }
    ```

## User Scenarios & Testing

1. **Creating a Course**
   - Test Case: Submit a request to create a new course with valid name and level fields and expect a success response with the created course details.

2. **Retrieving Course Details**
   - Test Case: Send a GET request with a specific course ID to ensure the response includes the correct course name and level.

3. **Error Handling for Missing Course Fields**
   - Test Case: Submit a POST request to create a course without the name or level, and expect validation error responses clearly indicating which fields are missing.

4. **Database Schema Update Verification**
   - Test Case: After the application starts, check the database schema to verify that the Course table exists and that existing records, specifically those related to Students, remain intact.

## Database Setup

A migration strategy using Flask-Migrate has been implemented to add the Courses table to the database. Make sure to run the migration scripts to update your schema.

## Success Criteria

- Courses can be created and retrieved without errors.
- Validation responses are user-friendly and trigger appropriate error messages.
- Tests comprehensively validate functionality and error scenarios.
- Documentation accurately reflects all recent updates and changes to the API.

## Installation

To set up the project:

1. Clone the repository.
2. Install the required dependencies.
3. Initialize the database with migrations.
4. Start the application.

For detailed installation instructions, refer to the [Installation Guide](docs/INSTALLATION.md).

## Contributing

Feel free to submit issues or pull requests. We welcome contributions!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.