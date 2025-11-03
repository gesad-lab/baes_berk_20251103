# README.md

# Project Title

## Description

This project aims to provide a robust system for managing courses, utilizing a modern tech stack based on Python, FastAPI, and SQLAlchemy.

## Table of Contents
- [Technology Stack](#technology-stack)
- [API Documentation](#api-documentation)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)

## Technology Stack
- **Programming Language**: Python
- **Web Framework**: FastAPI
- **Database**: SQLite
- **ORM**: SQLAlchemy for database interactions
- **Testing Framework**: pytest for unit and integration testing
- **Environment Management**: Poetry for dependency management
- **API Documentation**: OpenAPI provided automatically by FastAPI

## API Documentation

Automatic API documentation is available via FastAPI at `/docs`. This documentation will provide all necessary details regarding the API endpoints, including how to manage and query courses.

### Courses API Endpoints

- **Create a Course**
  - **Endpoint**: `POST /courses`
  - **Request Body**: 
    ```json
    {
      "name": "Course Name",
      "description": "Course Description",
      "credits": 3
    }
    ```
  - **Responses**:
    - **201 Created**: Successfully created a course.
    - **400 Bad Request**: Validation error.

- **Get a Course by ID**
  - **Endpoint**: `GET /courses/{id}`
  - **Responses**:
    - **200 OK**: A course object if found.
    - **404 Not Found**: No course exists with the provided ID.

## Installation

To install this project, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/your_user/project_name.git
   ```
2. Navigate into the cloned directory:
   ```bash
   cd project_name
   ```
3. Install the required dependencies:
   ```bash
   poetry install
   ```

## Usage

To run the application, use the following command:

```bash
poetry run uvicorn src.main:app --reload
```

You can visit `http://127.0.0.1:8000/docs` in your browser to view and test the API documentation.

## Testing

Run the tests with the following command:

```bash
pytest
```

Make sure to replace any placeholder paths with the actual paths of your project files.