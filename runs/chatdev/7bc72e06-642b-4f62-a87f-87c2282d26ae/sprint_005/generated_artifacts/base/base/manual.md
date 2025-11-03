Here's a detailed user manual for the software that includes an introduction to its main functions, installation instructions, and usage guidelines.

```markdown
# Course Management System

A simple API for managing students and courses, allowing users to create and retrieve student and course data.

## Main Functions

The Course Management System provides the following functionalities:

- **Student Management**
  - Create a new student with a name and email.
  - Retrieve a list of all students.

- **Course Management**
  - Create a new course with a name and level.
  - Retrieve a list of all courses.

## Quick Install

To set up the Course Management System, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo/course-management-system.git
   cd course-management-system
   ```

2. **Create a Virtual Environment**
   It is recommended to use a virtual environment to manage dependencies.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   Install the required dependencies using pip:
   ```bash
   pip install fastapi[all] sqlalchemy alembic pydantic
   ```

4. **Run Database Migrations**
   Ensure that the database schema is up to date:
   ```bash
   alembic upgrade head
   ```

5. **Start the Application**
   Run the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```

## How to Use

### API Endpoints

The API provides the following endpoints for managing students and courses:

#### Student Endpoints

- **Create a Student**
  - **Endpoint:** `POST /students/`
  - **Request Body:**
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **Response:**
    ```json
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Get All Students**
  - **Endpoint:** `GET /students/`
  - **Response:**
    ```json
    [
      {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
      }
    ]
    ```

#### Course Endpoints

- **Create a Course**
  - **Endpoint:** `POST /courses/`
  - **Request Body:**
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```
  - **Response:**
    ```json
    {
      "id": 1,
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Get All Courses**
  - **Endpoint:** `GET /courses/`
  - **Response:**
    ```json
    [
      {
        "id": 1,
        "name": "Mathematics",
        "level": "Beginner"
      }
    ]
    ```

## Additional Information

- **Database:** The application uses SQLite as the database. The database file is created automatically when the application runs.
- **Migrations:** The application uses Alembic for database migrations. Ensure to run migrations whenever you change the database schema.
- **Documentation:** For more detailed information on FastAPI, SQLAlchemy, and Pydantic, please refer to their respective documentation.

## Support

If you encounter any issues or have questions, please reach out to our support team via the provided contact methods in the repository.

```

This manual provides a comprehensive overview of the Course Management System, including installation steps, API usage, and additional information for users.