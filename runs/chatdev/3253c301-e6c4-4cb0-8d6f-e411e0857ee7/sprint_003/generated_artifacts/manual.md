```markdown
# Course Management API

A simple API for managing students and courses, built using FastAPI and SQLAlchemy.

## Main Functions

This API provides the following functionalities:

- **Student Management**: Create and retrieve student records.
- **Course Management**: Create and retrieve course records.
- **Database Migration**: Automatically manage database schema changes while preserving existing data.

### Key Features

- Create and manage students with name and email.
- Create and manage courses with name and level.
- All operations are performed through RESTful API endpoints.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   Create a `requirements.txt` file with the following content:
   ```
   fastapi
   uvicorn
   sqlalchemy
   pydantic
   alembic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the API

To start the FastAPI application, run the following command:
```bash
uvicorn main:app --reload
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

- **Get All Students**:
  - **Endpoint**: `GET /students/`
  - **Response**: Returns a list of all students.

#### Course Endpoints

- **Create a Course**:
  - **Endpoint**: `POST /courses/`
  - **Request Body**:
    ```json
    {
      "name": "Introduction to Programming",
      "level": "Beginner"
    }
    ```
  - **Response**: Returns the created course object.

- **Get All Courses**:
  - **Endpoint**: `GET /courses/`
  - **Response**: Returns a list of all courses.

### Database Migration

The application uses Alembic for database migrations. To apply migrations, run:
```bash
alembic upgrade head
```
This will update the database schema to include the new Course table while preserving existing Student data.

## Documentation

For more detailed documentation on FastAPI, SQLAlchemy, and Pydantic, please refer to the following resources:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)

## Support

If you encounter any issues or have questions, please reach out through the support channels provided in the repository.

```
