```markdown
# Course Management System

A simple API for managing Students and Courses, built with FastAPI and SQLAlchemy.

## Main Functions

This software provides the following functionalities:

- **Student Management**: Create and retrieve student records.
- **Course Management**: Create and retrieve course records.
- **Database Management**: Automatically handles database migrations to ensure data integrity.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/course-management.git
   cd course-management
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

## Database Setup

The application uses SQLite for database management. The database will be automatically created when you run the application for the first time.

To initialize the database and create the necessary tables, run the following command:
```bash
python main.py
```

## How to Use the API

### Start the Server

To start the FastAPI server, run:
```bash
uvicorn api:router --reload
```
This will start the server at `http://127.0.0.1:8000`.

### API Endpoints

#### Student Endpoints

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  - **Response**: Returns the created student object.

- **Get a Student**:
  - **Endpoint**: `GET /students/{student_id}`
  - **Response**: Returns the student object for the given ID.

#### Course Endpoints

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```
  - **Response**: Returns the created course object.

- **Get a Course**:
  - **Endpoint**: `GET /courses/{course_id}`
  - **Response**: Returns the course object for the given ID.

## Additional Information

### Database Migration

The application includes a migration script that ensures the existing Student data is preserved while adding the new Course entity. This is handled in the `main.py` file.

### Dependencies

The following dependencies are required for the application:

- **fastapi**: The web framework used to create the API.
- **uvicorn**: The ASGI server used to run the FastAPI application.
- **sqlalchemy**: The ORM used for database interactions.
- **pydantic**: The data validation and settings management library used for defining schemas.

Make sure to adjust the version numbers in `requirements.txt` as needed based on your project's requirements or the latest stable releases.

## Conclusion

This Course Management System provides a simple yet effective way to manage students and courses through a RESTful API. For further documentation, please refer to the FastAPI documentation [here](https://fastapi.tiangolo.com/).
```