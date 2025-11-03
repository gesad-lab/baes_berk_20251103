```markdown
# Student Management API

A FastAPI application for managing student records, including the ability to create and retrieve student information.

## Main Functions

- **Create Student**: Add a new student with a name and email address.
- **Get Students**: Retrieve a list of students with pagination support.

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
   pip install fastapi[all] sqlalchemy alembic
   ```

4. **Set up the database**:
   The application uses SQLite for the database. The database will be created automatically when you run the application.

## How to Use

1. **Run the application**:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**:
   - The API will be available at `http://127.0.0.1:8000`.
   - You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

3. **Create a Student**:
   - Send a POST request to `/students/` with the following JSON body:
     ```json
     {
       "name": "John Doe",
       "email": "john.doe@example.com"
     }
     ```

4. **Get Students**:
   - Send a GET request to `/students/` to retrieve a list of students. You can use query parameters `skip` and `limit` for pagination:
     ```
     GET /students/?skip=0&limit=10
     ```

## Database Migration

To add the email field to the Student entity, run the following commands in the terminal:

1. **Create a migration**:
   ```bash
   alembic revision --autogenerate -m "Add email field to Student"
   ```

2. **Apply the migration**:
   ```bash
   alembic upgrade head
   ```

This will update the database schema to include the new email field while preserving existing student data.

## Additional Information

For more detailed documentation and examples, please refer to the FastAPI documentation at [FastAPI Docs](https://fastapi.tiangolo.com/).

If you encounter any issues or have questions, feel free to reach out for support.
```