# README.md

# Project Title

## Overview & Purpose
The purpose of this feature is to create a new `Course` entity within the existing student management system. This is aimed at enhancing the educational capabilities of the application by allowing users to manage courses effectively.

## API Endpoints

### 1. Creating a Course
- **Endpoint**: `POST /courses`
- **Input**: JSON object containing the required fields:
  - `name` (string): The name of the course.
  - `level` (string): The difficulty level of the course.
  
- **Output**: JSON object containing the details of the created course:
  ```json
  {
    "id": 1,
    "name": "Introduction to Programming",
    "level": "Beginner"
  }
  ```

- **User Scenarios**:
  - **Success**: A user sends a request to create a Course with valid `name` and `level` fields. The API returns a success response with the created course data.
  - **Error**: A user sends a request to create a Course with either the `name` or `level` field missing. The API returns an error response indicating that both fields are required.

### 2. Retrieving a Course
- **Endpoint**: `GET /courses/{id}`
  
- **Output**: JSON object containing the details of the retrieved course:
  ```json
  {
    "id": 1,
    "name": "Introduction to Programming",
    "level": "Beginner"
  }
  ```
  
- **User Scenarios**: A user retrieves the details of an existing Course by its ID. The API returns the course's name and level along with the ID in JSON format.

## Database Migration
The existing database schema has been updated to include a new `Course` table without losing existing Student data. The `Course` table includes the following columns:
- `id`: Integer, primary key, auto-incremented.
- `name`: String, required field.
- `level`: String, required field.

The database migration has been tested to ensure that existing Student records remain intact.

## Documentation and References
- **Code Documentation**: Each module, class, and function will have docstrings explaining their purpose and usage.
- **README.md**: Updated to reflect new requirements for creating and managing courses.

## Implementation Timeline
- **Week 1**: Setup environment and design course model and database migrations.
- **Week 2**: Implement `POST /courses` and `GET /courses/{id}` endpoints with necessary business logic.
- **Week 3**: Complete error handling and validation and write unit tests for new features.
- **Week 4**: Conduct thorough testing, update documentation, and prepare for deployment.

## Architecture Overview
The application architecture follows a microservices pattern using FastAPI and SQLAlchemy. This update will introduce API endpoints for creating and retrieving `Course` entities, as well as a corresponding database schema to maintain the necessary data.