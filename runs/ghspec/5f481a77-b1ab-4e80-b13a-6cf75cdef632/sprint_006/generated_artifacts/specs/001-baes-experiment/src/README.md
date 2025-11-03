# Project Documentation

# Student Management System

## Overview
This project is a Student Management System designed to manage students, courses, and teachers. It provides a RESTful API to facilitate the management of these entities, enabling operations such as creating, updating, and retrieving data.

## Application Structure
```
student_management/
├── src/
│   ├── app.py              # Main application entry point
│   ├── models.py           # Database models (Update for Course-Teacher relationship)
│   ├── schemas.py          # Marshmallow schemas for serialization (Update for Course schema)
│   ├── routes.py           # API routes for handling requests (Update for Course and Teacher routes)
│   ├── config.py           # Configuration management
│   └── db.py               # Database initialization and schema handling (for migrations)
├── tests/
│   ├── test_routes.py      # Tests for API routes (Update for API functionality)
│   └── test_validation.py   # Tests for input validation (Update for new validations)
├── .env.example             # Example environment configuration
└── README.md                # Project documentation
```

## API Endpoints

### Courses
- **Create a Course**
  - **Endpoint:** `POST /courses`
  - **Request Body:**
    ```json
    {
      "name": "Introduction to Programming",
      "level": "beginner"
    }
    ```
  - **Response:** Returns the created course object.

- **Get Course Details**
  - **Endpoint:** `GET /courses/{course_id}`
  - **Response:** Returns detailed information about the course, including the associated teacher.

- **Assign a Teacher to a Course**
  - **Endpoint:** `POST /courses/{course_id}/assign-teacher`
  - **Request Body:**
    ```json
    {
      "teacher_id": 1  // ID of the teacher to be assigned
    }
    ```
  - **Response:** Returns the updated course object with the assigned teacher.

## Additional Configurations
Creating a Teacher is also part of the management process; these functionalities are integrated into the course management routes.

## Testing
To ensure that the API works as expected, there are unit tests implemented for route handling and validation checks. Running the tests can be done with `pytest` in the terminal.

### Running Tests
```bash
pytest tests/
```

Make sure to keep the test environment configuration updated in the `.env` file or using the provided `.env.example` as a template.

## Getting Started
To start the application, ensure you have the required Python packages installed. You can install them using:

```bash
pip install -r requirements.txt
```

Then run the application:

```bash
python src/app.py
```

Make sure to set up your database and run the migrations if necessary to keep the schema up-to-date.

## Conclusion
This documentation serves as a guide to navigate the project and utilize its functionalities efficiently. Contributions and improvements to the system are welcome!