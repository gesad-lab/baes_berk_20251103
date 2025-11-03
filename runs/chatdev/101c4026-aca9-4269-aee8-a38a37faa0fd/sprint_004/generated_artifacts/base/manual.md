```markdown
# Course Management API

A FastAPI application for managing students and courses, allowing for CRUD operations on both entities.

## Main Functions

This software provides the following functionalities:

- **Student Management**: Create, read, update, and delete student records.
- **Course Management**: Create, read, update, and delete course records.
- **Database Migration**: Automatically updates the database schema to include the Course table while preserving existing Student data.

## Quick Install

To set up the environment and install the necessary dependencies, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
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

## How to Use the API

### Running the Application

1. **Start the FastAPI Application**:
   Run the following command to start the server:
   ```bash
   uvicorn main:app --reload
   ```
   The application will be available at `http://127.0.0.1:8000`.

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

- **Get All Students**:
  - **Endpoint**: `GET /students/`

- **Get a Student by ID**:
  - **Endpoint**: `GET /students/{student_id}`

- **Update a Student**:
  - **Endpoint**: `PUT /students/{student_id}`
  - **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **Delete a Student**:
  - **Endpoint**: `DELETE /students/{student_id}`

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

- **Get All Courses**:
  - **Endpoint**: `GET /courses/`

- **Get a Course by ID**:
  - **Endpoint**: `GET /courses/{course_id}`

- **Update a Course**:
  - **Endpoint**: `PUT /courses/{course_id}`
  - **Request Body**:
    ```json
    {
      "name": "Mathematics",
      "level": "Intermediate"
    }
    ```

- **Delete a Course**:
  - **Endpoint**: `DELETE /courses/{course_id}`

### Database Migration

To apply the database migration that adds the Course table while preserving existing Student data, run the following command:
```bash
alembic upgrade head
```

## Documentation

For more detailed documentation on FastAPI, SQLAlchemy, and Pydantic, please refer to the following resources:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)

## Conclusion

This Course Management API provides a robust solution for managing students and courses with a simple and intuitive interface. Feel free to explore the API and integrate it into your applications!
```