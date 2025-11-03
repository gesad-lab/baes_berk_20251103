# README.md

# Project Title

## Overview

This project is a FastAPI application that includes a simple API for managing `Student` and `Course` entities. The application allows for creating, retrieving, and managing data related to students and courses.

## Application Structure

```
src/
  ├── main.py                 # Entry point of the FastAPI application
  ├── models/                 # Database models (including the Course model)
  │   └── student.py          # Model for Student
  │   └── course.py           # Model for Course
  ├── schemas/                # Pydantic models for request/response validation
  │   └── student.py          # Schema for Student
  │   └── course.py           # Schema for Course
  ├── routes/                 # API endpoints for handling HTTP requests
  │   └── student.py          # Routes for Student
  │   └── course.py           # Routes for Course
  ├── database/               # Database connection and setup
tests/
  └── test_student_routes.py   # Tests for Student routes
  └── test_student_model.py    # Tests for Student model
  └── test_course_routes.py     # Tests for Course routes
  └── test_course_model.py      # Tests for Course model
README.md                     # Setup and documentation
```

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   Ensure your database is set up appropriately. Configuration details should be provided in a separate configuration file or as environment variables.

5. **Run migrations:**

   If migrations are required for the database schema, ensure you run them:

   ```bash
   alembic upgrade head
   ```

6. **Run the application:**

   Start the FastAPI application:

   ```bash
   uvicorn src.main:app --reload
   ```

7. **Access the API:**

   Open your browser and navigate to `http://localhost:8000/docs` to access the automatically generated API documentation.

## Usage of Course API

### Create a Course

- **Endpoint:** `POST /courses`
- **Request Body:**

  ```json
  {
    "name": "Course Name",
    "level": "beginner" // Options may include "beginner", "intermediate", "advanced"
  }
  ```

- **Responses:**
  - `201 Created` on success
  - `400 Bad Request` if name or level is missing or invalid

### Retrieve a Course

- **Endpoint:** `GET /courses/{id}`
- **Responses:**
  - `200 OK` with course details
  - `404 Not Found` if the course does not exist

## Testing

To run the tests for the application, use the following command:

```bash
pytest
```

This will execute all the tests in the `tests/` directory, including tests for student and course models and routes.

## Contributions

Contributions are welcome! Please submit a pull request for any changes or improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.