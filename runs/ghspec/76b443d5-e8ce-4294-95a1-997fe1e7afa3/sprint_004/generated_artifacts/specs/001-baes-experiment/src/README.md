# README.md

# Project Title

## Introduction

This project leverages FastAPI to create a robust API for managing student enrollments and courses. The application uses SQLite as the database and SQLAlchemy for interactions.

## Setup

1. **Clone the Repository**: 
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: 
   This project uses Poetry for dependency management. Install Poetry if you haven't already.

   ```bash
   poetry install
   ```

3. **Run Migrations**: 
   Run the migrations to set up the database schema.

   ```bash
   poetry run alembic upgrade head
   ```

4. **Start the Application**: 
   Launch the FastAPI app.

   ```bash
   poetry run uvicorn src.main:app --reload
   ```

## API Documentation

Automatic API documentation is available at `/docs`. This can be viewed in your web browser while the FastAPI application is running.

### Enrollment Endpoints

The following endpoints are available for managing student enrollments:

1. **Enroll a Student in a Course**
   - **Endpoint**: `POST /students/{studentId}/enroll`
   - **Description**: Enrolls a student in a specified course. The `studentId` is required in the URL.
   - **Request Body**:
     ```json
     {
       "course_id": 1
     }
     ```
   - **Response**:
     - `201 Created`: Enrollment was successful.
     - `404 Not Found`: Student or course does not exist.

2. **Get Courses for a Student**
   - **Endpoint**: `GET /students/{studentId}/courses`
   - **Description**: Retrieves a list of courses a specified student is enrolled in. The `studentId` is required in the URL.
   - **Response**:
     - `200 OK`: A list of courses.
     - `404 Not Found`: Student does not exist.

## Testing

You can run the tests using pytest. Ensure your database is properly set up before running the tests.

```bash
poetry run pytest tests/
```

## Contributing

Feel free to submit issues or pull requests. Ensure your code adheres to the project's coding standards.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or comments, please contact [Your Email].

--- 

This update includes information about the new functionality for enrolling students in courses and retrieving their enrolled courses, ensuring that the README reflects the changes made as specified in the task documentation.