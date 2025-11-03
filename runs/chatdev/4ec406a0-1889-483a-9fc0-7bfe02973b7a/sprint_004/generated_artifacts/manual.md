```markdown
# Student Management Application

A FastAPI application designed to manage students and courses, allowing for the creation of relationships between students and their enrolled courses.

## Main Functions

- **Create Students**: Add new students to the database with their name and email.
- **Create Courses**: Add new courses to the database with their name and level.
- **Enroll Students in Courses**: Link students to their respective courses during student creation.
- **Retrieve Students**: Fetch a list of students along with their enrolled courses.
- **Retrieve Courses**: Fetch a list of available courses.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Environment Dependencies

The following dependencies are required for the application:

- **fastapi**: The web framework used to build the API.
- **uvicorn**: The ASGI server for running the FastAPI application.
- **sqlalchemy**: The ORM used for database interactions.
- **pydantic**: Used for data validation and settings management.
- **alembic**: The migration tool for SQLAlchemy, used to manage database schema changes.

Make sure to adjust the version numbers in `requirements.txt` if you want to use specific versions or if there are newer versions available.

## Database Migration

To set up the database schema and add the necessary relationships, run the following command:

```bash
alembic upgrade head
```

This command will apply the latest migrations, including the creation of the `student_courses` association table, which establishes the many-to-many relationship between students and courses.

## How to Use the Application

### Start the Application

To run the application, use the following command:

```bash
uvicorn main:app --reload
```

This will start the FastAPI server, and you can access the API documentation at `http://127.0.0.1:8000/docs`.

### API Endpoints

- **Create a Student**:
  - **Endpoint**: `POST /students/`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com",
      "course_ids": [1, 2]  // Optional: List of course IDs to enroll in
    }
    ```

- **Retrieve Students**:
  - **Endpoint**: `GET /students/`
  - **Response**: List of students with their enrolled courses.

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Beginner"
    }
    ```

- **Retrieve Courses**:
  - **Endpoint**: `GET /courses/`
  - **Response**: List of available courses.

## Conclusion

This application provides a robust framework for managing students and courses, allowing for easy enrollment and retrieval of information. For further information, please refer to the API documentation available at `http://127.0.0.1:8000/docs`.
```