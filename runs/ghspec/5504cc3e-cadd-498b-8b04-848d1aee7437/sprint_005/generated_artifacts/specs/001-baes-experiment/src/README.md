# README.md

# Project Title

## Overview

This project is designed to manage an educational institution's data, aligning with the principles of simplicity and modularity. The codebase supports the management of students, courses, and now teachers.

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/your-repo/project.git
   cd project
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up the database:
   - Make sure you have Alembic installed.
   - Run migrations to create the necessary tables:
     ```
     alembic upgrade head
     ```

4. Configure environment variables:
   - Create a `.env` file in the root directory with the necessary database configurations.

## API Endpoints

### Teacher Endpoints

- **Add a Teacher** 
  - **Endpoint**: `POST /api/v1/teachers`
  - **Payload**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **Description**: This endpoint creates a new teacher record in the database.

- **Get Teachers**
  - **Endpoint**: `GET /api/v1/teachers`
  - **Description**: This endpoint retrieves a list of all teachers.

### Other Endpoints

- **Enroll a Student**
  - **Endpoint**: `POST /api/v1/students/enroll`
  - **Payload**:
    ```json
    {
      "student_id": "123",
      "course_id": "456"
    }
    ```

- **Get Courses for a Student**
  - **Endpoint**: `GET /api/v1/students/{student_id}/courses`

## Development Steps

1. **Database Migration**: 
   - Create a migration script using Alembic to introduce the `teachers` table, ensuring it does not interfere with existing `students` and `courses` data.
   
2. **Update the Existing Models**: 
   - Create a new `teacher.py` file in the `src/models` directory for the Teacher model.
   
3. **Enhance API Endpoints**: 
   - Implement the POST and GET endpoints in the `src/api` directory.
   
4. **Develop Service Logic**: 
   - Create a new service file, `teacher_service.py`, to contain business logic for creating and retrieving Teacher records.
   
5. **Input Validation**: 
   - Implement input validation within the API endpoints to ensure that name and email fields are checked for validity and required presence.
   
6. **Testing**: 
   - Write unit tests for the Service functions as well as integration tests for API calls to ensure defects are caught before deployment.
   
7. **Documentation**: 
   - Update this README.md to include instructions for using the new endpoints, alongside relevant payload examples.

## Testing

- Ensure test coverage is adequate by running:
  ```
  pytest
  ```

- Focus on both unit tests for the service logic and integration tests for the API to ensure all functionalities work as expected.