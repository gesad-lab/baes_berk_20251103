# README.md

# My FastAPI Project

This project demonstrates the usage of FastAPI to manage course and student information.

## API Overview

### Course Management API

The Course Management API allows clients to create and retrieve course details. FastAPI's automatic documentation features are utilized to keep the API documentation up to date. The API can be accessed at the `/docs` endpoint, which provides an interactive API documentation interface for testing the endpoints.

### Endpoints

#### Create a Course

- **Endpoint**: `/courses`
- **Method**: `POST`
- **Request Body**: 
    ```json
    {
        "name": "Course Name",
        "level": "Course Level"
    }
    ```
- **Success Response**: 
    - **Code**: 201 Created
    - **Content**: 
    ```json
    {
        "id": 1,
        "name": "Course Name",
        "level": "Course Level"
    }
    ```

#### Retrieve a Course

- **Endpoint**: `/courses/{id}`
- **Method**: `GET`
- **URL Parameters**: 
    - `id` (integer): The ID of the course to retrieve.
- **Success Response**: 
    - **Code**: 200 OK
    - **Content**: 
    ```json
    {
        "id": 1,
        "name": "Course Name",
        "level": "Course Level"
    }
    ```

### Usage

1. Start the FastAPI application using:
   ```
   uvicorn myapp.main:app --reload
   ```

2. Access the API documentation at: [http://localhost:8000/docs](http://localhost:8000/docs)

### Requirements

- FastAPI
- SQLAlchemy
- SQLite

### Development Environment

Ensure that the virtual environment is configured with the required dependencies for the FastAPI project. To set this up, use the following:

```bash
pip install fastapi[all] sqlalchemy sqlite
```

### Database Setup

Follow the guidelines for automating database schema creation/migrations using SQLAlchemy to ensure a smooth setup.

### Testing

Unit and integration tests should be performed using pytest. Ensure that the test coverage meets the necessary criteria as specified in the project plan.

---

## Conclusion

With the utilization of FastAPI's built-in documentation generation, this project provides a comprehensive API experience for course management while ensuring that users have access to current and interactive API documentation through the `/docs` endpoint.