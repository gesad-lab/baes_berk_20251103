# README.md

# Student Management System

## Overview

The Student Management System is a FastAPI-based application designed to manage student information and course offerings. The system provides endpoints for managing students and courses, leveraging a well-structured architecture for scalability and maintainability.

## Project Structure

The following is the project structure, outlining the organization of modules and key files:

```
student_management/
│
├── src/
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py         # New routes for courses
│   ├── models/
│   │   ├── __init__.py
│   │   ├── student.py        # Model for Student entity
│   │   └── course.py         # New model for Course entity
│   ├── services/
│   │   ├── __init__.py
│   │   └── course_service.py  # Service logic for Course
│   ├── dal/
│   │   ├── __init__.py
│   │   └── course_dal.py     # Data access methods for Course
│   ├── app.py                # Main application entry point
│   └── config.py             # Configuration settings
│
├── migrations/
│   └── 002_add_courses_table.py # Migration file for Course table
│
├── tests/
│   ├── __init__.py
│   ├── test_student_routes.py  # Tests for Student routes
│   ├── test_student_service.py  # Tests for Student service
│   ├── test_course_routes.py    # New tests for Course endpoints
│   └── test_course_service.py    # New tests for Course business logic
│
├── .env.example                # Example environment variables
├── requirements.txt            # Project dependencies
└── README.md                   # This README file
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd student_management
   ```
   
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Copy `.env.example` to `.env` and update the necessary configurations.

## Running the Application

To start the application, use the command:

```
uvicorn src.app:app --reload
```

This runs the application in development mode with live reloading enabled.

## Endpoints

### Student Endpoints

- **Get all students**
- **Create a new student**
- **Update student details**
- **Delete a student**

### Course Endpoints (New)

- **Get all courses**
- **Create a new course**
- **Update course details**
- **Delete a course**

Please refer to the API documentation for detailed information on request and response formats.

## Migrations

Database migrations are managed using Alembic. To apply migrations, run:

```
alembic upgrade head
```

To create a new migration after making changes to the models, run:

```
alembic revision --autogenerate -m "Description of changes"
```

## Testing

To run the test suite, use:

```
pytest
```

This will execute all unit tests for both students and courses, ensuring the application functions as intended.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.