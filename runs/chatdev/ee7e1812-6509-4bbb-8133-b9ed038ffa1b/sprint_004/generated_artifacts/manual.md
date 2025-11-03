```markdown
# Student Course Management Application

A FastAPI application for managing students and their course enrollments.

## Overview

This application allows users to create and manage students and courses. Students can be enrolled in multiple courses, and the application provides a RESTful API for interacting with the data. The application is built using FastAPI, SQLAlchemy, and Pydantic for data validation.

## Main Functions

- **Create Student**: Add a new student to the database and enroll them in specified courses.
- **Retrieve Students**: Get a list of all students in the database.
- **Create Course**: Add a new course to the database.
- **Retrieve Courses**: Get a list of all courses in the database.

## Installation

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Run the migration** to ensure the database schema is up to date:
   ```bash
   python main.py
   ```

2. **Start the FastAPI server**:
   ```bash
   uvicorn routes:router --reload
   ```

3. **Access the API documentation**:
   Open your browser and navigate to `http://127.0.0.1:8000/docs` to view the interactive API documentation provided by FastAPI.

## API Endpoints

### Students

- **Create a Student**
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com",
      "course_ids": [1, 2]  // List of course IDs to enroll in
    }
    ```

- **Retrieve Students**
  - **Endpoint**: `GET /students/`
  - **Query Parameters**: `skip`, `limit` (for pagination)

### Courses

- **Create a Course**
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Retrieve Courses**
  - **Endpoint**: `GET /courses/`
  - **Query Parameters**: `skip`, `limit` (for pagination)

## Database Migration

The application includes a migration script that ensures the database schema is updated without losing existing data. The migration is handled in the `migration.py` file, which is called when the application starts.

## Conclusion

This application provides a simple yet powerful way to manage students and their course enrollments. With the FastAPI framework, it offers a fast and efficient way to interact with the data through a RESTful API. For further customization and enhancements, feel free to explore the codebase and contribute.

For any issues or feature requests, please reach out to the development team.
```