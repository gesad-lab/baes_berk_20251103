```markdown
# Course Management Application

A simple API for managing students and courses, built using FastAPI and SQLAlchemy.

## Main Functions

This application provides the following functionalities:

- **Create Students**: Add new students with their name and email.
- **Create Courses**: Add new courses with a name and level.
- **Retrieve Students**: Fetch a list of students with their details.

## Installation

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
   alembic
   pydantic
   ```
   Then run:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To start the application, use the following command:
```bash
uvicorn main:app --reload
```
This will run the application on `http://127.0.0.1:8000`.

## API Endpoints

### Create a Student

- **Endpoint**: `POST /students/`
- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
  ```

### Create a Course

- **Endpoint**: `POST /courses/`
- **Request Body**:
  ```json
  {
    "name": "Introduction to Programming",
    "level": "Beginner"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "name": "Introduction to Programming",
    "level": "Beginner"
  }
  ```

### Retrieve Students

- **Endpoint**: `GET /students/`
- **Query Parameters**: 
  - `skip`: Number of records to skip (default: 0)
  - `limit`: Number of records to return (default: 10)
- **Response**:
  ```json
  [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
  ]
  ```

## Database Migration

To create the necessary database tables, run the migration scripts using Alembic. Ensure that your database is set up correctly in `database.py`.

### Migration Commands

1. **Create Migration for Courses**:
   ```bash
   alembic revision --autogenerate -m "Create courses table"
   ```

2. **Apply Migrations**:
   ```bash
   alembic upgrade head
   ```

## Conclusion

This application provides a simple interface for managing students and courses. You can extend its functionality by adding more features as needed. For any issues or feature requests, please reach out to the development team.
```