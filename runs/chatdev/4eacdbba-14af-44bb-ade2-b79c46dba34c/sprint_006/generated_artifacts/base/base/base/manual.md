```markdown
# Course Management System

A simple API for managing students and courses using FastAPI and SQLAlchemy.

## Main Functions

This software provides the following functionalities:

- **Student Management**: Create and retrieve student records.
- **Course Management**: Create and retrieve course records.
- **Database Migration**: Migrate the database schema to include the new Course entity while preserving existing Student data.

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

## How to Use

### Running the Application

1. **Start the Server**:
   Run the following command to start the FastAPI server:
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

- **Get Students**:
  - **Endpoint**: `GET /students/`
  - **Query Parameters**: `skip` (int), `limit` (int)
  - **Response**: Returns a list of students.

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

- **Get Courses**:
  - **Endpoint**: `GET /courses/`
  - **Query Parameters**: `skip` (int), `limit` (int)
  - **Response**: Returns a list of courses.

### Database Migration

To apply the database migration that creates the Course table and preserves existing Student data, run the following command:
```bash
alembic upgrade head
```

This will execute the migration script and update the database schema accordingly.

## Documentation

For more detailed documentation on FastAPI and SQLAlchemy, please refer to the following resources:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/14/)

## Conclusion

This Course Management System provides a simple yet effective way to manage students and courses through a RESTful API. Follow the installation and usage instructions to get started with your own instance.
```