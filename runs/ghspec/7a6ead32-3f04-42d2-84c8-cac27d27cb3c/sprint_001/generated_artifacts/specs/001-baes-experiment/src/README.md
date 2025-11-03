# README.md

# Student Management API

## Overview
The purpose of this feature is to create a simple web application that allows users to manage Student entities. Each Student will have a required name field. The application will use SQLite for data persistence, ensuring that the student data is stored reliably. The web application aims to provide an easy-to-use API that returns JSON responses, facilitating integration with other systems and front-end interfaces.

## User Scenarios
1. **Creating a Student**:
   - A user sends a request to create a new Student with a valid name.
   - The application responds with a confirmation message and the details of the created Student.
   
2. **Retrieving a Student**:
   - A user sends a request to retrieve a Student by their unique identifier.
   - The application responds with the Student details in JSON format.

3. **Updating a Student**:
   - A user sends a request to update the name of an existing Student.
   - The application confirms the update and returns the updated Student details.

4. **Deleting a Student**:
   - A user sends a request to delete a specific Student.
   - The application responds with a confirmation message indicating successful deletion.

## Testing
- Verify that creating, retrieving, updating, and deleting Students return expected JSON responses.
- Ensure appropriate status codes are returned for each API operation (e.g., 200 OK, 201 Created, 404 Not Found).

## Local Development Setup

To facilitate local development, it is recommended to use Docker and Docker Compose. Below is a sample `docker-compose.yml` that defines the configuration for running the application in a containerized environment.

### docker-compose.yml
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    environment:
      DATABASE_URL: sqlite:///./test.db
    depends_on:
      - db

  db:
    image: nouchka/sqlite3
    volumes:
      - db_data:/data

volumes:
  db_data:
```

## Running the Application
1. Ensure you have [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/install/) installed on your machine.
2. Clone the repository and navigate to the project directory.
3. Run the following command to start the application:
   ```bash
   docker-compose up --build
   ```
4. Access the API at `http://localhost:8000/api/v1/students`.

## API Documentation
Detailed API documentation, including endpoints and usage, will be available using OpenAPI standards and accessible once the server is running.